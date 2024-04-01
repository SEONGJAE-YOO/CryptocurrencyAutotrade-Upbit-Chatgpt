import pandas_ta as ta

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
    
    # various MA
    df['tema_10'] = ta.tema(df['close'], length=10)
    df['tema_20'] = ta.tema(df['close'], length=20)

    df['dema_10']= ta.dema(df['close'], length=10)
    df['dema_20']= ta.dema(df['close'], length=20)

    df['hma_10']= ta.hma(df['close'], length=10)
    df['hma_20']= ta.hma(df['close'], length=20) 

    df['wma_10']= ta.wma(df['close'], length=10) 
    df['wma_20']= ta.wma(df['close'], length=20) 
    
    #fwma
    df['fwma_10']= ta.fwma(df['close'], length=10)
    df['fwma_20']= ta.fwma(df['close'], length=20)
    
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

    ###############################################################################
    df["cmf"] = ta.cmf(df["high"],df["low"],df["close"],df["volume"],df["open"],length=20)
    
    result_df = ta.squeeze_pro(df["high"], df["low"], df["close"])
    for column in result_df.columns:
        df[column] = result_df[column]

    return df

#####################################################################################
# autotrade_version7.py 에서 사용됨

def add_indicators_version2(df):
    df = add_indicators(df)
    FISHT = ta.fisher(df["high"],df["low"]) 
    df = df.join(FISHT)
    ADX = ta.adx(df["high"],df["low"],df["close"])
    df = df.join(ADX)
    AMAT_df = ta.amat(df["close"])
    for column in AMAT_df.columns:
        if "AMATe_SR_8_21_2" in column:
            df = df.join(AMAT_df[column])

    return df
