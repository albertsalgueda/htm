import matplotlib.pyplot as plt
import torch as torch

x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

grid_x, grid_y = torch.meshgrid(x, y, indexing='ij')
grid_x
grid_y

torch.equal(torch.cat(tuple(torch.dstack([grid_x, grid_y]))),
            torch.cartesian_prod(x, y))

xs = torch.linspace(-5, 5, steps=100)
ys = torch.linspace(-5, 5, steps=100)
x, y = torch.meshgrid(xs, ys, indexing='xy')
z = torch.sin(torch.sqrt(x * x + y * y))
ax = plt.axes(projection='3d')
ax.plot_surface(x.numpy(), y.numpy(), z.numpy())
plt.show()