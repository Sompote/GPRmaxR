# GPRMax Plotting Instructions

This document provides instructions for generating and interpreting various plots from your gprMax simulation output files.

Your simulation for `sand_with_hole` has produced two main types of output files relevant for plotting:

1.  **`.vti` files (e.g., `sand_with_hole_snapshot.vti`):** These are 3D volumetric data files that contain snapshots of the electromagnetic field (like E-field or H-field) in the simulation domain at specific moments in time. These are useful for visualizing wave propagation in 3D.
2.  **`.out` files (e.g., `sand_with_hole.out`):** These files contain the recorded signal (voltage/field strength over time) at receiver locations. This is the "real GPR data" (A-scans or B-scans) that you would typically analyze.

---

## 1. Plotting 3D Field Snapshots (Contour Plots)

The `contour.py` script helps visualize the electromagnetic field within the simulation domain from `.vti` files. The script has been updated to handle vector fields (like E-field) by plotting their magnitude by default.

**Command:**

To generate a contour plot of the E-field magnitude from your snapshot file:

```bash
python contour.py ../user_models/sand_with_hole_snaps/sand_with_hole_snapshot.vti
```

-   The script will open a 3D viewer window showing the contour lines of the E-field magnitude.
-   **Note:** If `contour.py` is located in your main GPRmax directory (one level up from your current `gprMax` working directory), you need to run it as `python ../contour.py ...`.

---

## 2. Plotting GPR Data (A-scans and B-scans)

The `tools/plot_Ascan.py` and `tools/plot_Bscan.py` scripts are used to visualize the raw GPR data (signal traces) from your `.out` files.

### Plotting an A-scan (Single Trace)

An A-scan shows the amplitude of the received signal versus time at a single receiver point.

**Command:**

```bash
python tools/plot_Ascan.py ../user_models/sand_with_hole.out
```

-   This will open a 2D plot window displaying the A-scan. Each receiver in the output file will likely generate a separate plot.
-   You can specify which output component to plot using the `--outputs` argument (e.g., `Ex`, `Hy`).

### Plotting a B-scan (Radargram)

A B-scan (or radargram) is a 2D image created by stacking multiple A-scans collected along a line, showing amplitude versus time/depth for different spatial positions. This is the most common visualization for GPR data.

**Command:**

```bash
python tools/plot_Bscan.py ../user_models/sand_with_hole.out
```

-   This will open a 2D image plot (radargram) if your `sand_with_hole.out` file contains data from multiple receiver positions along a line.
-   Ensure your simulation was set up to produce B-scan data (e.g., by moving the antenna along a survey line).

---

By using these plotting tools, you can analyze both the internal field distributions and the resulting GPR data from your simulations.
