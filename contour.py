import argparse
import os

import pyvista as pv


def create_contour_plot(filename, isosurfaces=10, cmap="viridis"):
    """
    Creates a contour plot from a .vti file.

    Args:
        filename (str): The path to the .vti file.
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

    # Create a contour plot
    contours = grid.contour(isosurfaces=isosurfaces)

    # Create a plotter object and add the contours
    plotter = pv.Plotter()
    plotter.add_mesh(contours, cmap=cmap)
    plotter.add_mesh(grid.outline(), color="k")
    plotter.show_grid()

    # Show the plot
    print("Displaying contour plot. Close the plot window to exit.")
    plotter.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create contour plots from gprMax .vti files."
    )
    parser.add_argument("filename", help="The path to the .vti file.")
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

    create_contour_plot(args.filename, args.isosurfaces, args.cmap)
