from homework import *
from pytest import approx
from pathlib import Path
import urllib.request
import sqlite3
import pandas as pd
import re


def test_python(capsys):
    def make_list(n):
        result = []
        for i in range(n):
            result.append(i)
        return result

    with time_it() as timer:
        make_list(1000)

    out, err = capsys.readouterr()
    assert re.findall(r'\d+', out)


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    customer_df = pd.read_sql_query(sql_query_1, con)
    order_df = pd.read_sql_query(sql_query_2, con)

    assert customer_df.iloc[2, 1] == "Unknown"
    assert customer_df.shape == (10, 2)
    assert customer_df.iloc[4, 1] == "719-724-7869"
    assert order_df.iloc[0, 1] == "Archived"
    assert order_df.iloc[5, 1] == "Last Year"
    assert order_df.iloc[9, 1] == "Active"

    Path('data.db').unlink(missing_ok=True)


def test_model():
    model = train_model()
    testing_data = pd.read_csv('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/spam_test.csv')
    X_test = np.array(testing_data.iloc[:, 0:57])
    y_test = np.ravel(testing_data.iloc[:, -1])
    assert model.score(X_test, y_test) == approx(0.79878313)


def test_regex():
    text = "There is no error in this code. However, an unexpected error occurred during execution."
    assert re.findall(regex_pattern, text) == ["error"]
