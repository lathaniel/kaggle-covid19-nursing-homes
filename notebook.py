# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: kaggle-cms
#     language: python
#     name: kaggle-cms
# ---

# imports and whatnot
import pandas as pd

# Verify we can read dataset
df = pd.read_csv('./kaggle-data/COVID_19_Nursing_Home_Data_09_25_2022.csv')
df