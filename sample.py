import pandas as pd
import matplotlib.pyplot as plt

# Date,Open,High,Low,Close,Volume,Adj Close

def stocks(symbol):

	df = pd.read_csv(f'data/{symbol}.csv')
	return df['Close'].max()

def plot_stock_single_col(symbol,col):

	df = pd.read_csv(f"data/{symbol}.csv")
	df[col].plot()
	plt.show()

def plot_stock_multi_col(symbol,col_list):
	df = pd.read_csv(f"data/{symbol}.csv")
	df[col_list].plot()
	plt.show()



def stock_mean_volume(symbol):

	df = pd.read_csv(f'data/{symbol}.csv')
	return df['Volume'].mean()


def main():
	for symbol in ['AAPL','GOOG']:
		print("Mean Volume ")
		print(symbol,stock_mean_volume(symbol))

if __name__ == '__main__':
	# for plotting Adj Close
	# plot_stock_single_col('AAPL','Adj Close')
	# plot_stock_single_col('AAPL','High')
	plot_stock_multi_col('AAPL',['Close','Adj Close'])
