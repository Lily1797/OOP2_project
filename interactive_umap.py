from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper, ColorBar
from bokeh.palettes import viridis

import scanpy as sc


def plot_interactive_umap(adata, color_by="louvain", size=5, title="Interactive UMAP plot"):
  """
  Creates an interactive UMAP plot using Bokeh. Users can choose to color cells by louvain cluster labels or bulk labels.

  Args:
      adata (AnnData): The AnnData object containing the data.
      color_by (str, optional): Specify "louvain" or "bulk_labels" to color cells by the corresponding attribute. Defaults to "louvain".
      size (int, optional): Size of the circle glyph in the plot. Defaults to 5.
      title (str, optional): Title for the Bokeh plot. Defaults to "Interactive UMAP plot".
  """

  # Get UMAP embeddings
  umap_embeddings = adata.obsm['X_umap']

  # Get color information based on choice
  if color_by == "louvain":
      colors = adata.uns["louvain_colors"]
  elif color_by == "bulk_labels":
      colors = adata.uns["bulk_labels_colors"]
  else:
      raise ValueError(f"Invalid color_by option: {color_by}. Choose 'louvain' or 'bulk_labels'.")

  # Create color mapper
  color_mapper = LinearColorMapper(palette=colors, low=0, high=len(colors) - 1)

  # Get labels for hover tool (if applicable)
  if color_by == "louvain":
      labels = adata.obs["louvain"].tolist()
  elif color_by == "bulk_labels":
      bulk_labels = adata.obs["bulk_labels"].cat.categories.tolist()
      labels = adata.obs['bulk_labels'].cat.codes.tolist()
      label_names = [None]*len(labels)
      for i, code in enumerate(labels):
          label_names[i] = bulk_labels[code]
  else:
      labels = None  # No labels for hover tool if color_by is invalid

  # Create ColumnDataSource
  source = ColumnDataSource(
      data=dict(x=umap_embeddings[:, 0], y=umap_embeddings[:, 1], labels=labels)
  )

  # Create Bokeh figure and customize it
  fig = figure(title=title, x_axis_label="UMAP 1", y_axis_label="UMAP 2")
  fig.circle(
      x="x",
      y="y",
      source=source,
      size=size,
      fill_color={"field": "labels", "transform": color_mapper},
      line_color=None,
  )

  # Add hover tool (if labels are available)
  if labels:
      hover = HoverTool(tooltips=[("(x, y)", "($x, $y)"), ("cluster/label", "@labels")])
      fig.add_tools(hover)

  # Show the plot
  show(fig)