
import torch

from temporal_memory import TemporalMemoryApicalTiebreak

real_type = torch.float32
int_type = torch.int64

device = "cuda" if torch.cuda.is_available() else "cpu"


class PairMemoryApicalTiebreak(TemporalMemoryApicalTiebreak):
    """
    pair memory with apical tiebreak, built on temporal memory with apical tiebreak.

    pair memory (the process by which information is learned by "grouping" context
    from basal and apical synapses) is enabled via the following configurations of the
    basic Temporal Memory algorithm:

    1. basal reinforce candidates (list of bits that active cells may reinforce
                                   basal synapses to)
            = basal input

    2. apical reinforce candidates (list of all bits that active cells may reinforce
                                    apical synapses to)
            = apical input

    3. basal growth candidates (list of bits that active cells may grow new basal
                                synapses to)
            = basal input (by default)

    4. apical growth candidates (list of bits that active cells may grow new apical
                                 synapses to)
            = apical input (by default)

    for the original implementation of this class, please refer to:
    https://github.com/numenta/nupic.research/blob/master/packages/columns/
    """

    def compute(
        self,
        active_minicolumns,
        basal_input,
        apical_input=None,
        basal_growth_candidates=None,
        apical_growth_candidates=None,
        learn=True
    ):
        """
        perform one timestep: use the basal and apical input to form a set of
        predictions, then activate the specified columns. then learn.

        `active_minicolumns` (torch.Tensor) contains the active minicolumns.

        `basal_input` (torch.Tensor) contains the list of active input bits
        for the basal dendrite segments.

        `basal_growth_candidates` (torch.Tensor or None) contains the list of bits
        that the active cells may grow new basal synapses to.
        if None, the `basal_input` is assumed to be growth candidates.

        `apical_input` (torch.Tensor) contains the list of active input bits
        for the apical dendrite segments.

        `apical_growth_candidates` (torch.Tensor or None) contains the list of bits
        that the active cells may grow new apical synapses to.
        if None, the `apical_input` is assumed to be growth candidates.

        `learn` (bool) -- whether to grow / reinforce / punish synapses
        """

        active_minicolumns = active_minicolumns.to(int_type).to(device)
        basal_input = basal_input.to(int_type).to(device)

        if apical_input is None:
            apical_input = torch.Tensor([])
        apical_input = apical_input.to(int_type).to(device)

        if basal_growth_candidates is None:
            basal_growth_candidates = basal_input
        basal_growth_candidates = basal_growth_candidates.to(int_type).to(device)

        if apical_growth_candidates is None:
            apical_growth_candidates = apical_input
        apical_growth_candidates = apical_growth_candidates.to(int_type).to(device)

        self.depolarize_cells(
            basal_input=basal_input,
            apical_input=apical_input,
            learn=learn
        )

        self.activate_cells(
            active_minicolumns=active_minicolumns,
            basal_reinforce_candidates=basal_input,
            apical_reinforce_candidates=apical_input,
            basal_growth_candidates=basal_growth_candidates,
            apical_growth_candidates=apical_growth_candidates,
            learn=learn
        )

    def get_active_cells(self):
        """
        return set of new active cells.
        """

        return self.active_cells

    def get_predicted_cells(self):
        """
        return prediction for this timestep.
        """

        return self.predicted_cells

    def get_basal_predicted_cells(self):
        """
        get cells with active basal segments.
        """
        return torch.unique(
            self.map_segments_to_cells("basal", self.active_basal_segments)
        )

    def get_apical_predicted_cells(self):
        """
        get cells with active apical segments.
        """

        return torch.unique(
            self.map_segments_to_cells("apical", self.active_apical_segments)
        )