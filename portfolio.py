import yfinance as yf
import matplotlib.pyplot as plt
import pandas

tickers = ['AAPL', 'TSLA', 'META', 'AMZN', 'NVDA']
weights = [.2,.2,.2,.2,.2]
initial_amount = 10000

df = yf.download(tickers, start='2020-01-01', end='2024-12-31')['Close']
df.head()

normalized = df/df.iloc[0]
portfolio = (normalized * weights).sum(axis=1) * initial_amount
print(f'Il valore finale del portafoglio è:{portfolio}')

plt.figure(figsize=(18,9))
plt.plot(portfolio, color='blue')
plt.title=("Portfolio historical value")
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show(True)
