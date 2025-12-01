import argparse
import os
import numpy as np
import pyvista as pv


def create_contour_plot(filename, field="E-field", isosurfaces=10, cmap="viridis"):
    """
    Creates a contour plot from a .vti file.

    Args:
        filename (str): The path to the .vti file.
        field (str): The field to plot ('E-field' or 'H-field').
        isosurfaces (int): The number of contour levels.
        cmap (str): The matplotlib colormap to use.
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        print(
            "Please make sure you have run the gprMax simulation and the file exists."
        )
        return

    # Load the .vti file
    grid = pv.read(filename)

    # Convert cell data to point data if necessary
    if field in grid.cell_data:
        print(f"Converting '{field}' from cell data to point data...")
        grid = grid.cell_data_to_point_data()

    if field not in grid.point_data:
        print(f"Error: Field '{field}' not found in point data after loading/conversion.")
        print(f"Available point data: {grid.point_data.keys()}")
        return

    # Check if the field is a vector and compute magnitude if so
    data = grid[field]
    scalar_field = field
    if data.ndim > 1 and data.shape[1] > 1:
        print(f"Field '{field}' is a vector with shape {data.shape}. Computing magnitude for contour plotting.")
        scalar_field = f"{field}_magnitude"
        grid[scalar_field] = np.linalg.norm(data, axis=1)

    # Create a contour plot using the specified field (or its magnitude)
    print(f"Generating contours for {scalar_field} with {isosurfaces} isosurfaces...")
    contours = grid.contour(isosurfaces=isosurfaces, scalars=scalar_field)

    # Create a plotter object and add the contours
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(contours, cmap=cmap)
    plotter.add_mesh(grid.outline(), color="k")
    plotter.show_grid()

    print(f"Saving contour plot for {scalar_field} to contour_plot.png")
    plotter.screenshot("contour_plot.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create contour plots from gprMax .vti files."
    )
    parser.add_argument("filename", help="The path to the .vti file.")
    parser.add_argument(
        "--field",
        choices=["E-field", "H-field"],
        default="E-field",
        help="The field to plot (default: 'E-field').",
    )
    parser.add_argument(
        "--isosurfaces",
        type=int,
        default=10,
        help="The number of contour levels (default: 10).",
    )
    parser.add_argument(
        "--cmap",
        default="viridis",
        help="The matplotlib colormap to use (default: 'viridis').",
    )

    args = parser.parse_args()

    create_contour_plot(args.filename, args.field, args.isosurfaces, args.cmap)
