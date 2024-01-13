import pandas as pd

tb_branded_products:
type: pandas.JSONDataset
filepath: data / 01
_raw / tb_branded_products.json

tb_categories:
type: pandas.CSVDataset
filepath: data / 01
_raw / tb_categories.csv

tb_product_categories:
type: pandas.CSVDataset
filepath: data / 01
_raw / tb_product_categories.csv

ixone_products:
type: pandas.JSONDataset
filepath: data / 01
_raw / ixone_products.json


def preprocess_tb(tb_branded_products: pd.DataFrame,
                  tb_categories: pd.DataFrame,
                  tb_product_categories: pd.DataFrame
                  ) -> pd.DataFrame:
    """Preprocesses the tb product data, combine with the categories.

    Args:
        df: Raw data.
        df: Raw data.
        df: Raw data.
    Returns:
        Preprocessed data...
    """


def preprocess_ixone_products(ixone_products: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the data, convert field names

    Args:
        ixone_products: Raw data.
    Returns:
        Preprocessed data..
    """


def create_model_input_table(
        shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    """Combines all data to create a model input table.

    Args:
       ....
    Returns:
        Model input table.

    """
