import pandas_datareader.data as web # To import financial data directly into python
import matplotlib.pyplot as plt
import scipy
import openpyxl  # To save file to the excel

start = "2015-01-01"
end = "2020-10-07"


SP500_ETF = ["VOO", "VV", "MGC", "IVV", "SCHX", "SPY", "SPLG"]

# Save the data in etf
etfs = web.DataReader(SP500_ETF, 'yahoo', start, end)

# The Adjusted Closing Price that shows the ETF's value after posting a dividend will be used
etfs = etfs["Adj Close"]
plt.figure()
etfs.plot(ylabel="Daily Price")
# It is hard to visually compare different graphs. Your eyes can see trends that do not exist.

# It is better to look at a percentage change in a stock/ETF price than to look at how much it changed in price in
# dollars per share. That is because it is easier to compare them to alternatives.
etfs_pct = etfs.pct_change()[1:]
print(etfs_pct.head())
plt.figure()
etfs_pct.plot(ylabel="Daily % Change")
plt.show()

# # ANOVA
# # Check assumptions:
# 1) Residuals (experimental error) are normally distributed (Shapiro-Wilks Test)
# 2) Homogeneity of variances (variances are equal between treatment groups) (Levene or Bartlett Test)
# 3) Data are independent.
# Shapiro-Wilks Test test the null hypo that the data was drawn from a normal distribution.

shapiro_test_voo = scipy.stats.shapiro(etfs_pct['VOO'])
shapiro_test_ivv = scipy.stats.shapiro(etfs_pct['IVV'])

print(shapiro_test_voo.pvalue) # 2.9823333551374853e-38
print(shapiro_test_ivv.pvalue) # 4.044263956073654e-38

# Since p-values is less than 0.05, we reject the null hypothesis that the data was drawn from normal distribution.
# Thus, we violates a normality assumption of the Anova distribution, and we won't use ANOVA.
# Since the data does not have a normal distribution, use Kruskal–Wallis one-way analysis of variance
kruskalWallis = (scipy.stats.kruskal(etfs_pct["VOO"],etfs_pct["VV"],etfs_pct["MGC"],etfs_pct["IVV"],etfs_pct["SCHX"],
                                      etfs_pct["SPY"],etfs_pct["SPLG"]))
print(kruskalWallis.pvalue)
# The p-value is 0.9999952, so we fail to reject the null hypothesis 
# that assumes that the samples (groups) are from identical populations.
