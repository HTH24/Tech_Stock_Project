
"""
Spyder Editor

This is a temporary script file.
"""

from datetime import datetime
import pandas_datareader as web
from matplotlib import pyplot as plt

symbols = ['MSFT', 'AMZN', 'AAPL', 'GOOG', 'FB']
start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 7, 1)
stock_data = web.get_data_yahoo(symbols, start_date, end_date)
print(stock_data)
# print(type(stock_data))
print(stock_data['Adj Close'])


#Plot the adjusted closing prices against time
stock_data['Adj Close'].plot()
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price Over Time')
plt.title('Tech Stocks Adjusted Price')
# plt.show()

daily_returns = stock_data['Adj Close'].pct_change()
daily_returns.plot()

plt.xlabel('Date')
plt.ylabel('Daily Simple Rate of Return')
plt.legend(symbols, loc = 1)
plt.title('Daily Simple Rate of Return')

# Create subplots of daily simple rate of return
plt.figure(figsize=(15, 15))
ax1 = plt.subplot(3, 2, 1)
ax2 = plt.subplot(3, 2, 2)
ax3 = plt.subplot(3, 2, 3)
ax4 = plt.subplot(3, 2, 4)
ax5 = plt.subplot(3, 2, 5)
ax1.plot(stock_data['Adj Close']['AMZN'].pct_change())
ax2.plot(stock_data['Adj Close']['MSFT'].pct_change())
ax3.plot(stock_data['Adj Close']['AAPL'].pct_change())
ax4.plot(stock_data['Adj Close']['GOOG'].pct_change())
ax5.plot(stock_data['Adj Close']['FB'].pct_change())
ax1.set_title('Amazon')
ax2.set_title('Microsoft')
ax3.set_title('Apple')
ax4.set_title('Google')
ax5.set_title('Facebook')
# plt.tight_layout()

# Calculate and plot each tech stock's daily simple rate of return
mean_returns = daily_returns.mean()
print(mean_returns)

plt.figure(figsize=(10, 10))

ax99 = plt.subplot()
ax99.set_xticks(range(len(symbols)))
ax99.set_xticklabels(symbols)
plt.title('Mean Rate of Return')
plt.xlabel('Company Name')
plt.ylabel('Rate of Return')
plt.bar(range(len(symbols)), mean_returns)


# Calculate and plot the variance
stock_variance = daily_returns.var()
print(stock_variance)

plt.figure(figsize=(10, 10))

ax12 = plt.subplot()
ax12.set_xticks(range(len(symbols)))
ax12.set_xticklabels(symbols)

plt.bar(range(len(symbols)), stock_variance)
plt.xlabel('Company Name')
plt.ylabel('Variance')
plt.title('Stock Variances', fontsize = 18)

# Standard deviation
stock_std = daily_returns.std()
print(stock_std)

plt.figure(figsize=(10, 10))

ax20 = plt.subplot()
ax20.set_xticks(range(len(symbols)))
ax20.set_xticklabels(symbols)

plt.bar(range(len(symbols)), stock_std)
plt.xlabel('Company Name')
plt.ylabel('Standard Deviation')
plt.title('Stock Standard Deviations', fontsize = 18)

plt.show()

# Correlations
stock_corr = daily_returns.corr()
print(stock_corr)




