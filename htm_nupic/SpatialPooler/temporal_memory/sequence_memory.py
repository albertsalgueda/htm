import torch

from temporal_memory import TemporalMemoryApicalTiebreak

real_type = torch.float32
int_type = torch.int64

device = "cuda" if torch.cuda.is_available() else "cpu"


class SequenceMemoryApicalTiebreak(TemporalMemoryApicalTiebreak):
    """
    sequence memory with apical tiebreak, built on temporal memory with apical tiebreak.

    sequence memory (the process by which sequences are learned) is enabled
    via the following configurations of the basic Temporal Memory algorithm:

    1. basal reinforce candidates (list of bits that active cells may reinforce
                                   basal synapses to)
            = active cells (all correctly predicted cells + all cells in bursting
                            minicolumns)

    2. apical reinforce candidates (list of all bits that active cells may reinforce
                                    apical synapses to)
            = previous apical input

    3. basal growth candidates (list of bits that active cells may grow new basal
                                synapses to)
            = learning cells (correctly predicted cells + cells with best matching
                              basal segments, which are the cells with the highest
                              active synapses among cells in each bursting minicolumn +
                              cells with new basal segments)

    4. apical growth candidates (list of bits that active cells may grow new apical
                                 synapses to)
            = previous apical growht candidates

    for the original implementation of this class, please refer to:
    https://github.com/numenta/nupic.research/blob/master/packages/columns/
    """

    def __init__(
        self,
        num_minicolumns=2048,
        apical_input_size=0,
        num_cells_per_minicolumn=32,
        activation_threshold=13,
        reduced_basal_threshold=13,
        initial_permanence=0.21,
        connected_permanence=0.50,
        matching_threshold=10,
        sample_size=20,
        permanence_increment=0.1,
        permanence_decrement=0.1,
        basal_segment_incorrect_decrement=0.0,
        apical_segment_incorrect_decrement=0.0,
        max_synapses_per_segment=-1,
        seed=42
    ):

        params = {
            "num_minicolumns" : num_minicolumns,
            "basal_input_size" : num_minicolumns * num_cells_per_minicolumn,
            "apical_input_size" : apical_input_size,
            "num_cells_per_minicolumn" : num_cells_per_minicolumn,
            "activation_threshold" : activation_threshold,
            "reduced_basal_threshold" : reduced_basal_threshold,
            "initial_permanence" : initial_permanence,
            "connected_permanence" : connected_permanence,
            "matching_threshold" : matching_threshold,
            "sample_size" : sample_size,
            "permanence_increment" : permanence_increment,
            "permanence_decrement" : permanence_decrement,
            "basal_segment_incorrect_decrement" : basal_segment_incorrect_decrement,
            "apical_segment_incorrect_decrement" : apical_segment_incorrect_decrement,
            "max_synapses_per_segment" : max_synapses_per_segment,
            "seed" : seed
        }

        super().__init__(**params)

        self.previous_apical_input = torch.empty(0, dtype=int_type).to(device)
        self.previous_apical_growth_candidates = torch.empty(
            0, dtype=int_type
        ).to(device)
        self.previous_predicted_cells = torch.empty(0, dtype=int_type).to(device)

    def reset(self):
        """
        clear all cell and segment activity.
        """

        super().reset()

        self.previous_apical_input = self.previous_apical_input.new_empty((0,))
        self.previous_apical_growth_candidates = \
            self.previous_apical_growth_candidates.new_empty((0,))
        self.previous_predicted_cells = self.previous_predicted_cells.new_empty((0,))

    def compute(
        self,
        active_minicolumns,
        apical_input=None,
        apical_growth_candidates=None,
        learn=True
    ):
        """
        perform one timestep: activate the specified minicolumn using the predictions
        from the previous timestep and then learn. form a new set of predictions
        using the newly active cells and the apical input.

        `active_minicolumns` (torch.Tensor) contains the active minicolumns.

        `apical_input` (torch.Tensor) contains the list of active input bits
        for the apical dendrite segments.

        `apical_growth_candidates` (torch.Tensor or None) contains the list of bits
        that the active cells may grow new apical synapses to.
        if None, the `apical_input` is assumed to be growth candidates.

        `learn` (bool) -- whether to grow / reinforce / punish synapses
        """

        active_minicolumns = active_minicolumns.to(int_type).to(device)

        if apical_input is None:
            apical_input = torch.Tensor([])
        apical_input = apical_input.to(int_type).to(device)

        if apical_growth_candidates is None:
            apical_growth_candidates = apical_input
        apical_growth_candidates = apical_growth_candidates.to(int_type).to(device)

        self.previous_predicted_cells = self.predicted_cells

        self.activate_cells(
            active_minicolumns=active_minicolumns,
            basal_reinforce_candidates=self.active_cells,
            apical_reinforce_candidates=self.previous_apical_input,
            basal_growth_candidates=self.learning_cells,
            apical_growth_candidates=self.previous_apical_growth_candidates,
            learn=learn
        )

        self.depolarize_cells(
            basal_input=self.active_cells,
            apical_input=apical_input,
            learn=learn
        )

        self.previous_apical_input = apical_input.clone()
        self.previous_apical_growth_candidates = apical_growth_candidates.clone()

    def get_active_cells(self):
        """
        return set of new active cells.
        """

        return self.active_cells

    def get_predicted_cells(self):
        """
        return prediction from previous timestep.
        """

        return self.previous_predicted_cells

    def get_learning_cells(self):
        """
        return set of learning cells.
        """

        return self.learning_cells

    def get_next_predicted_cells(self):
        """
        return prediction for next timestep.
        """

        return self.predicted_cells

    def get_next_basal_predicted_cells(self):
        """
        return cells with active basal segments.
        """

        return torch.unique(
            self.map_basal_segments_to_cells(self.active_basal_segments)
        )

    def get_next_apical_predicted_cells(self):
        """
        return cells with active apical segments.
        """

        return torch.unique(
            self.map_apical_segments_to_cells(self.active_apical_segments)
        )

    def get_num_basal_segments(self):
        """
        return total number of basal segments.
        """

        return len(self.basal_segment_to_cell)