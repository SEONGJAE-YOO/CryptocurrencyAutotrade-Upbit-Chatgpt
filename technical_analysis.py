import numpy as np
import pandas as pd
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
# autotrade_version8.py 에서 사용됨

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

# autotrade_version9.py 에서 사용되는 기술적 분석 기능  
def add_indicators_version3(df):
    df = add_indicators_version2(df)
    donchian = ta.donchian(df["high"],df["low"], lower_length = 20, upper_length = 20, offset = 0)
    df = df.join(donchian)
    zscore = ta.zscore(close= df["close"],length = 30, std = 1 ,offset = 0)
    df = df.join(zscore)
    tos_stdevall = ta.tos_stdevall(close= df["close"], length = 30, stds = [1,2,3], ddof = 1, offset = 0)
    df = df.join(tos_stdevall)
    # Aroon
    aroon = ta.aroon(df["high"], df["low"])
    df = df.join(aroon)
    
    # Aroon Up이 Down을 상향 돌파하면 주가의 고점이 저점보다 가까이 위치한 상태가 된 것이다. 따라서 주가가 상승 추세에 있는 것으로 해석할 수 있다. 
    # 반대로 Aroon Down이 Up을 상향 돌파하면 주가의 저점이 고점보다 가까이 위치한 것으로 주가가 하락 추세에 있는 것으로 해석할 수 있다. 
    #그러므로 Aroon Up이 Down을 상향 돌파하면 주가가 상승 추세로 전환될 것으로 예상해 매수하고 
    # Aroon Down이 Up을 상향 돌파하면 주가가 하락 추세로 전환될 것으로 예상해 매도하는 전략을 사용할 수 있다.
    # A common buying condition using the Aroon indicator is when Aroon Up crosses above Aroon Down
    #  Assuming 'aroon_up' and 'aroon_down' are the Aroon Up and Aroon Down indicators respectively
    #df['aroon_cross'] = np.where(df['AROONU_14'] > df['AROOND_14'], 1, 0)


    # Chande Momentum Oscillator (CMO)
    cmo = ta.cmo(df["close"])
    df = df.join(cmo)

    # Rate of Change (ROC) , ROC 값이 음수에서 양수로 변하는 시점을 매수 시점으로 고려하겠습니다.
    roc = ta.roc(df["close"],length=10)
    df = df.join(roc)

    # William's %R
    willr = ta.willr(df["high"], df["low"], df["close"])
    df = df.join(willr)
    return df


def add_indicators_version4(df):
    df = add_indicators_version3(df)
    # Trend indicators
    # Ichimoku Cloud
    # raise ValueError(f"Indexes have overlapping values: {overlap}") ValueError: Indexes have overlapping values: Index(['ISA_9', 'ISB_26'], dtype='object')
    #ichimoku = ta.ichimoku(df["high"], df["low"],df["close"])
    #df = df.join(ichimoku)


    # On-Balance Volume
    obv = ta.obv(df["close"], df["volume"])
    df = df.join(obv)


    # Volatility indicators
    # Average True Range (ATR)
    atr = ta.atr(df["high"], df["low"], df["close"])
    df = df.join(atr)

    # Keltner Channel
    keltner = ta.kc(df["high"], df["low"], df["close"])
    df = df.join(keltner)

    # 다른 기술적 분석 지표 추가
    # TRIX
    trix = ta.trix(df["close"])
    df = df.join(trix)
    df["trix_buy_signal"] = trix_buy_signal(df["TRIXs_30_9"], threshold=0)

    #Vortex Indicator
    vortex = ta.vortex(df["high"], df["low"], df["close"])
    for column in vortex.columns:
        df[column] = vortex[column]
    df["vortex_buy_signal"] = vortex_buy_signal(df['VTXP_14'], df['VTXM_14'])
    
    # ADI
    supertrend = ta.supertrend(df["high"], df["low"],df["close"])
    for column in supertrend.columns:
        if "SUPERT_7_3.0" in column:
            df = df.join(supertrend[column])
    df["supertrend_buy_signal"] = supertrend_buy_signal(df['close'], df['SUPERT_7_3.0'])

    
        
    return df

# def add_indicators_version5(df):
#     df = add_indicators_version4(df)
#     #Vortex Indicator
#     vortex = ta.vortex(df["high"], df["low"], df["close"])
#     for column in vortex.columns:
#         df[column] = vortex[column]
#     return df

"""
TRIX가 양수에서 음수로 변할 때, 이는 상승 추세에서 하락 추세로의 전환을 나타낼 수 있습니다. 
반대로 음수에서 양수로 변할 때는 하락 추세에서 상승 추세로의 전환을 나타낼 수 있습니다.
• 상향 이동(VM+)은 현재 고점에서 이전 저점을 뺀 값으로 계산됩니다.
• 하향 이동(VM-)은 현재 저점에서 이전 고점을 뺀 값으로 계산됩니다.
"""

def trix_buy_signal(trix_signal, threshold=0):
    """
    Generates a buy signal when trix_signal crosses above a threshold.

    Args:
        trix_signal (pd.Series): The TRIX signal line.
        threshold (float): The threshold value for generating buy signals.

    Returns:
        pd.Series: A binary series indicating buy signals (1) and no buy signals (0).
    """
    # Generate buy signals where trix_signal crosses above the threshold
    buy_signal = (trix_signal > threshold) & (trix_signal.shift(1) < threshold)
    
    return buy_signal.astype(int)


"""
소용돌이 표시기는 +DI와 -DI의 차이를 +DI와 -DI의 합으로 나누어 계산합니다. 
그런 다음 결과에 100을 곱하여 백분율 값을 제공합니다. 소용돌이 표시기는 차트에 선으로 표시됩니다.

2. 소용돌이 표시기 사용 방법
소용돌이 표시기는 추세 반전을 식별하는 데 사용됩니다. 
소용돌이 표시기가 40 레벨을 넘으면 새로운 상승 추세가 시작된다는 신호입니다. 
소용돌이 표시기가 60 레벨 아래로 교차하면 새로운 하락 추세가 시작된다는 신호입니다. 

 +DI 라인은 상승 추세의 강도를 측정하고 -DI 라인은 하락 추세의 강도를 측정합니다.
 그런 다음 두 선을 결합하여 소용돌이 표시기 선을 만듭니다. 
 소용돌이 표시선이 중앙선 위로 교차하면 강세 신호이고, 중앙선 아래로 교차하면 약세 신호입니다.

VI+가 VI-를 위로 교차하면 강세 추세를 나타내고, VI-가 VI+를 위로 교차하면 약세 추세를 나타냅니다.
"""

def vortex_buy_signal(VTXP_14, VTXM_14):
    """
    Generates a buy signal when the Vortex Positive (VIP) line crosses above the Vortex Negative (VIM) line.

    Args:
        vtxdf (pd.DataFrame): DataFrame containing Vortex Positive (VIP) and Vortex Negative (VIM) values.

    Returns:
        pd.Series: A binary series indicating buy signals (1) and no buy signals (0).
    """
    # Generate buy signals where VIP crosses above VIM
    buy_signal = (VTXP_14 > VTXM_14) & (VTXP_14.shift(1) <= VTXM_14.shift(1))
    
    return buy_signal.astype(int)


def supertrend_buy_signal(close, SUPERT_7_3):
    """
    Generates a buy signal when the price closes above the Supertrend line.  

    Args:
        df (pd.DataFrame): DataFrame containing 'close' prices and Supertrend values.

    Returns:
        pd.Series: A binary series indicating buy signals (1) and no buy signals (0).
    """
    # Generate buy signals where close price crosses above the Supertrend line
    buy_signal = (close > SUPERT_7_3) & (close.shift(1) <= SUPERT_7_3.shift(1))
    
    return buy_signal.astype(int)

# Elliott Wave Theory

def find_peaks(df):
    # Find local maxima and minima
    local_max = df['high'][((df['high'].shift(1) < df['high']) & (df['high'].shift(-1) < df['high']))]
    local_min = df['low'][((df['low'].shift(1) > df['low']) & (df['low'].shift(-1) > df['low']))]

    # Combine local maxima and minima
    peaks = pd.concat([local_max, local_min]).sort_index()

    return peaks

def detect_elliott_wave(df):
    # Find peaks in the price data
    peaks = find_peaks(df)

    # Initialize wave count
    wave_count = 0

    # Initialize previous peak
    prev_peak = None

    # Initialize Elliott wave pattern
    elliott_wave = []

    # Iterate over peaks
    for time, peak in peaks.iteritems():
        # If this is the first peak, just save it as the previous peak
        if prev_peak is None:
            prev_peak = peak
            continue

        # Calculate the size of the wave
        wave_size = abs(peak - prev_peak)

        # If the wave size is larger than a threshold, start a new wave
        if wave_size > THRESHOLD:
            wave_count += 1
            elliott_wave.append((time, wave_count))

        # Update the previous peak
        prev_peak = peak

    return elliott_wave
