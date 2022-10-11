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

# # Initial Setup
#
# I often prefer to run my notebooks outside of Kaggle.
# As a result, I specify at the top whether I am running the notebook locally or on Kaggle

# + vscode={"languageId": "python"}
localEnv = True

# + vscode={"languageId": "python"}
# imports and whatnot
import pandas as pd

# + vscode={"languageId": "python"}
# Verify we can read dataset
kaggleDataDir = '/kaggle/input' if localEnv == False else './kaggle-data'
df = pd.read_csv(f'{kaggleDataDir}/COVID_19_Nursing_Home_Data_09_25_2022.csv')
df
