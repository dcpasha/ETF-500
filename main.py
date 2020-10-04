import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import openpyxl  # To save file to the excel

# TODO
# 1) Make Sure that data is the same. YES, it is the same.
# 2) Make a list of ETFs and import data in a good format
# 3) Compare them during different time interval

# Package to import financial data directly into python
import pandas_datareader.data as web

start = "2020-01-01"
end = "2020-10-04"

SP500_ETF = ["VOO", "VV", "MGC", "IVV", "SCHX", "SPY", "SPLG"]

etfs = web.DataReader(SP500_ETF, 'yahoo', start, end)
# df.to_excel("/Users/pavelpotapov/Data/SP500/My_findings.xlsx") # To save file to the excel

# print(etfs.info())
# print(etfs["Adj Close"].head())
etfs = etfs["Adj Close"]
# print(etfs.head())
transformed_etf = etfs.pct_change()[1:]
# print(transformed_etf.head())

# voo_data = pd.read_csv("/Users/pavelpotapov/Data/SP500/VOO.csv")  # it is a dataframe
# ivv_data = pd.read_csv("/Users/pavelpotapov/Data/SP500/IVV.csv")  # it is a dataframe
#
#
# # Creating index of a dataframe
# # print(voo_data.head())  # "Date" was just a column
# voo_data = voo_data.set_index("Date")
# ivv_data = ivv_data.set_index("Date")
#
#
# # # Selecting certain rows of a dataframe based on index
# # voo_data = voo_data[voo_data.index > "2018-01-01"]
#
# # print("Creating a Series")
# voo_series = pd.Series(voo_data["Close"], name="VOO")
# ivv_series = pd.Series(ivv_data["Close"], name="VOO")
#
#
# # # Selecting certain rows of a Series based on index
# voo_series = voo_series[voo_series.index > '2020-01-01']
# ivv_series = ivv_series[ivv_series.index > '2020-01-01']
#
#
# # Take Percentage change
# voo_pct = voo_series.pct_change()[1:]
# ivv_pct = ivv_series.pct_change()[1:]
#

# # ANOVA
# # Check assumptions:
# # 1) Residuals (experimental error) are normally distributed (Shapiro-Wilks Test)
# # 2) Homogeneity of variances (variances are equal between treatment groups) (Levene or Bartlett Test)
# # 3) Data are independent.
#
# # Shapiro-Wilks Test test the null hypo that the data was drawn from a normal distribution.
# shapiro_test = scipy.stats.shapiro(voo_pct)
# # print(shapiro_test.pvalue)  # 1.501246002511003e-11
# # Since p-values is less than 0.05, we reject the null hypothesis that the data was drawn from normal distribution.
# # Thus, we violates a normality assumption of the Anova distribution, and we won't use it.
#
# # Since the data does not have a normal distribution,
# # use Kruskal–Wallis one-way analysis of variance
print(scipy.stats.kruskal(transformed_etf.iloc[:,1],transformed_etf.iloc[:,2],transformed_etf.iloc[:,3],transformed_etf.iloc[:,4]))
# print(transformed_etf.iloc[:,1].head())

