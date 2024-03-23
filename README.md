# OOP2_project
A custom function to create an interactive UMAP plot

## Instalation
Clone the repository:
```
git clone https://github.com/Lily1797/OOP2_project/
```
Copy the umap_interactive.py file to the scanpy/plotting directory:
```
cd OOP2_project
cp map_interactive.py Path_to_scanpy_plotting_directory
```
The code in the umap_interactive.py file defines a new plotting function called umap_interactive for Scanpy. The function takes an AnnData object as input and returns a Bokeh plot with an interactive UMAP plot.
Import the new function in the scanpy/plotting/__)init__.py file by adding the following line at the bottom of the file:
```
from .umap_interactive import umap_interactive
```

## Usage:

Within your main Python script or Jupyter notebook, you can import the function from umap_interactive.py and use it like this:

```
from scanpy.plotting import umap_interactive  # Assuming umap_interactive.py is in your path

# Load your data
adata = sc.datasets.pbmc68k_reduced()

# Call the function
umap_interactive(adata, color_by="bulk_labels")  # Or color_by="louvain"
```

This approach keeps your custom functionality separate from the core scanpy codebase, promoting modularity and easier maintenance. You can extend this further by adding more functionalities to umap_interactive.py without affecting existing scanpy plotting logic.

