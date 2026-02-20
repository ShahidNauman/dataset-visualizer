# Exploring and Visualizing a Simple Dataset

### Objective:

Learn how to load, inspect, and visualize a dataset to understand data trends and distributions.

### Dataset:

Iris Dataset (CSV format, can be loaded via seaborn or downloaded)

### Instructions:

- [x] Load the dataset using pandas.
- [x] Print the shape, column names, and the first few rows using .head().
- [x] Use .info() and .describe() for summary statistics.
- [x] Visualize the dataset:
  - [x] Create a scatter plot to show relationships between features.
  - [x] Use histograms to show value distributions.
  - [x] Use box plots to identify outliers.
- [x] Use matplotlib and seaborn for plotting.

### Skills:

- Data loading and inspection using pandas
- Descriptive statistics and data exploration
- Basic plotting and visualization with seaborn and matplotlib

## Application

This project includes a runnable Python app: `app.py`.

### What it does

- Loads the Iris dataset with `seaborn`, then works with it as a pandas DataFrame.
- Prints:
  - dataset shape
  - column names
  - first 5 rows (`head()`)
  - `info()` summary
  - `describe()` summary statistics
- Generates visualizations with matplotlib + seaborn:
  - scatter plot (`outputs/scatter_plot.png`)
  - histograms (`outputs/histograms.png`)
  - box plots (`outputs/box_plots.png`)

### Run

```bash
pip install -r requirements.txt
python app.py
```

After running, check the `outputs/` folder for the generated plots.
