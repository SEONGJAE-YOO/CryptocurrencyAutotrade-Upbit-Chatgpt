import os
from dotenv import load_dotenv
load_dotenv()
import pyupbit
import pandas as pd
import pandas_ta as ta
import json
from openai import OpenAI
import schedule
import time

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))
# df_daily = pyupbit.get_ohlcv("KRW-BTC", "day", count=30)
# df_hourly = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=24)
# print(df_daily)
# print("\n")   
# print(df_hourly)


# print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
# print(upbit.get_balance("KRW"))         # 보유 현금 조회
#def fetch_and_prepare_data():
df_daily = pyupbit.get_ohlcv("KRW-BTC", "day", count=290)
df_hourly = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=290)

# Define a helper function to add indicators
def add_indicators(df):
    # Moving Averages
    df['SMA_5'] = ta.sma(df['close'], length=5)
    df['EMA_5'] = ta.ema(df['close'], length=5)

    df['SMA_10'] = ta.sma(df['close'], length=10)
    df['EMA_10'] = ta.ema(df['close'], length=10)

    df['SMA_20'] = ta.sma(df['close'], length=20)
    df['EMA_20'] = ta.ema(df['close'], length=20)

    df['SMA_60'] = ta.sma(df['close'], length=60)
    df['EMA_60'] = ta.ema(df['close'], length=60)

    df['SMA_120'] = ta.sma(df['close'], length=120)
    df['EMA_120'] = ta.ema(df['close'], length=120)

    # Calculate short and long-term moving averages
    df['SMA_50'] = ta.sma(df['close'], length=50)
    df['SMA_200'] = ta.sma(df['close'], length=200)
    # Generate buy/sell signals based on the crossover
    df['Signal'] = 0  # Initialize signal column
    
    # When SMA_50 crosses above SMA_200, set signal to 1 (Buy)
    df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1
    
    # When SMA_50 crosses below SMA_200, set signal to -1 (Sell)
    df.loc[df['SMA_50'] < df['SMA_200'], 'Signal'] = -1

    # RSI
    df['RSI_7'] = ta.rsi(df['close'], length=7)
    df['RSI_14'] = ta.rsi(df['close'], length=14)
    df['RSI_21'] = ta.rsi(df['close'], length=21)
    
    # Stochastic Oscillator
    stoch = ta.stoch(df['high'], df['low'], df['close'], k=14, d=3, smooth_k=3)
    df = df.join(stoch)

    # MACD
    ema_fast = df['close'].ewm(span=12, adjust=False).mean()
    ema_slow = df['close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema_fast - ema_slow
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_Histogram'] = df['MACD'] - df['Signal_Line']

    # Bollinger Bands
    df['Middle_Band'] = df['close'].rolling(window=20).mean()
    # Calculate the standard deviation of closing prices over the last 20 days
    std_dev = df['close'].rolling(window=20).std()
    # Calculate the upper band (Middle Band + 2 * Standard Deviation)
    df['Upper_Band'] = df['Middle_Band'] + (std_dev * 2)
    # Calculate the lower band (Middle Band - 2 * Standard Deviation)
    df['Lower_Band'] = df['Middle_Band'] - (std_dev * 2)

    return df

# Add indicators to both dataframes
df_daily = add_indicators(df_daily)
df_hourly = add_indicators(df_hourly)

combined_df = pd.concat([df_daily, df_hourly], keys=['daily', 'hourly'])
result_excel = combined_df.to_csv('daily_hourly.csv', index = True)

#print(combined_df)
# combined_data = combined_df.to_json(orient='split')

# # make combined data as string and print length
# print(len(combined_data))
# result =json.dumps(combined_data)
# print(result)
    #return json.dumps(combined_data)

