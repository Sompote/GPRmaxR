import numpy as np
import pyvista as pv

# Create a dummy grid
grid = pv.UniformGrid()
grid.dimensions = (10, 10, 10)
grid.spacing = (1, 1, 1)
grid.origin = (0, 0, 0)

# Create dummy E-field and H-field data
n_cells = grid.n_cells
e_field = np.random.rand(n_cells)
h_field = np.random.rand(n_cells)

# Add the data to the grid as cell data
grid.cell_data["E-field"] = e_field
grid.cell_data["H-field"] = h_field

# Save the dummy data to a .vti file
grid.save("dummy_data.vti")

print("Dummy data file 'dummy_data.vti' created successfully.")
