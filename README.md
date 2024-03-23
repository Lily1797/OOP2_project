# OOP2_project
A custom function to create an interactive UMAP plot

## Instalation
Clone the repository:
```
git clone https://github.com/Lily1797/OOP2_project/
```
Copy the interactive_umap.py file to the scanpy/plotting directory:
```
cd OOP2_project
cp interactive_umap.py Path_to_scanpy_plotting_directory
```
The code in the interactive_umap.py file defines a new plotting function called umap_interactive for Scanpy. The function takes an AnnData object as input and returns a Bokeh plot with an interactive UMAP plot.
Import the new function in the scanpy/plotting/__)init__.py file by adding the following line at the bottom of the file:
```
from .umap_interactive import interactive_umap
```

## Usage:
Within your main Python script or Jupyter notebook, you can import the function from umap_interactive.py and use it like this:
```
from scanpy.plotting import interactive_umap  # Assuming interactive_umap.py is in your path

# Load your data
adata = sc.datasets.pbmc68k_reduced()

# Call the function
interactive_umap(adata, color_by="bulk_labels")  # Or color_by="louvain"
```
This custom function provides flexibility by allowing users to choose the coloring scheme (louvain or bulk_labels) through the color_by argument. It keeps your custom functionality separate from the core plotting scanpy codebase, promoting modularity and easier maintenance. You can extend this further by adding more functionalities to interactive_umap.py without affecting existing scanpy plotting logic.

### Additional styling options
You can further customize your interactive UMAP plot by adding optional arguments for hover tool tooltips or additional styling options as described in the tutorial notebook.
