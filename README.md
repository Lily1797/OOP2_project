# OOP2_project
A custom function to create an interactive UMAP plot

## Installation
Clone the repository:
```
git clone https://github.com/Lily1797/OOP2_project/
```
Copy the interactive_umap.py file to your path:
```
cd OOP2_project
cp interactive_umap.py Path_to_your_project_directory
```
The code in the interactive_umap.py file defines a new plotting function called plot_interactive_umap. The function takes an AnnData object as input and returns a Bokeh plot with an interactive UMAP plot.


## Usage
Within your main Python script or Jupyter notebook, you can import the function from interactive_umap.py and use it like this:
```
from interactive_umap import plot_interactive_umap  # Assuming interactive_umap.py is in your path

# Load your data
adata = sc.datasets.pbmc68k_reduced()

# Call the function
plot_interactive_umap(adata, color_by="bulk_labels")  # Or color_by="louvain"
```
color_by="bulk_labels"
![color_by="bulk_labels"](https://github.com/Lily1797/OOP2_project/blob/main/bulk_labels.png)
color_by="louvain"
![color_by="louvain"](https://github.com/Lily1797/OOP2_project/blob/main/louvain.png)

This custom function provides flexibility by allowing users to choose the coloring scheme (louvain or bulk_labels) through the color_by argument. It keeps your custom functionality separate from the core plotting scanpy codebase, promoting modularity and easier maintenance. You can extend this further by adding more functionalities to interactive_umap.py without affecting existing scanpy plotting logic.

### Additional styling options
You can further customize your interactive UMAP plot by adding optional arguments for hover tool tooltips or additional styling options as described in the tutorial notebook.
