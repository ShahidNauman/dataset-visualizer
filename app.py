from __future__ import annotations

from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


OUTPUT_DIR = Path("outputs")


def load_iris_dataset() -> pd.DataFrame:
    iris_df = sns.load_dataset("iris")
    if iris_df is None or iris_df.empty:
        raise ValueError("Could not load iris dataset.")
    return iris_df


def print_dataset_overview(dataframe: pd.DataFrame) -> None:
    print("Dataset Shape:", dataframe.shape, end="\n\n")

    print("Column Names:", list(dataframe.columns), end="\n\n")

    print(dataframe.head(), end="\n\n")

    info_buffer = StringIO()
    dataframe.info(buf=info_buffer)
    print("Info Summary:")
    print(info_buffer.getvalue(), end="\n\n")

    print("Descriptive statistics:")
    print(dataframe.describe(include="all"), end="\n\n")


def create_scatter_plot(dataframe: pd.DataFrame, output_dir: Path) -> None:
    fig, axis = plt.subplots()
    sns.scatterplot(
        data=dataframe,
        x="sepal_length",
        y="petal_length",
        hue="species",
        ax=axis,
    )
    axis.set_title("Iris: Sepal Length vs Petal Length")
    fig.tight_layout()
    fig.savefig(output_dir / "scatter_plot.png", dpi=300)
    plt.close(fig)


def create_histograms(dataframe: pd.DataFrame, output_dir: Path) -> None:
    numeric_columns = dataframe.select_dtypes(include="number").columns
    fig, axes = plt.subplots(2, 2)
    axes_flat = axes.flatten()

    for index, column_name in enumerate(numeric_columns):
        sns.histplot(data=dataframe, x=column_name, kde=True, ax=axes_flat[index])
        axes_flat[index].set_title(f"Distribution of {column_name}")

    fig.tight_layout()
    fig.savefig(output_dir / "histograms.png", dpi=300)
    plt.close(fig)


def create_box_plots(dataframe: pd.DataFrame, output_dir: Path) -> None:
    numeric_columns = dataframe.select_dtypes(include="number").columns
    melted = dataframe.melt(id_vars="species", value_vars=list(numeric_columns))

    fig, axis = plt.subplots()
    sns.boxplot(data=melted, x="variable", y="value", hue="species", ax=axis)
    axis.set_title("Iris Feature Distributions by Species")
    axis.set_xlabel("Feature")
    axis.set_ylabel("Value")
    axis.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    fig.savefig(output_dir / "box_plots.png", dpi=300)
    plt.close(fig)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    iris_df = load_iris_dataset()
    print_dataset_overview(iris_df)

    create_scatter_plot(iris_df, OUTPUT_DIR)
    create_histograms(iris_df, OUTPUT_DIR)
    create_box_plots(iris_df, OUTPUT_DIR)

    print("Plots saved in:", OUTPUT_DIR.resolve())


if __name__ == "__main__":
    main()
