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


# Setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))



def get_current_status(index_value):
    orderbook = pyupbit.get_orderbook(ticker=index_value)
    index_value_split = index_value.split("-")[1]
    current_time = orderbook['timestamp']
    balance = 0
    krw_balance = 0
    avg_buy_price = 0
    balances = upbit.get_balances()

    for b in balances:
        if b['currency'] == index_value_split:
            balance = b['balance']
            avg_buy_price = b['avg_buy_price']
        if b['currency'] == "KRW":
            krw_balance = b['balance']

    current_status = {'current_time': current_time, 'orderbook': orderbook, 'balance': balance, 'krw_balance': krw_balance, 'avg_buy_price': avg_buy_price}
    print(current_status)
    return json.dumps(current_status)



def fetch_and_prepare_data():
    
    #############################################################################################
    # XEC
    df_minute30_XEC = pyupbit.get_ohlcv("KRW-XEC", interval="minute30",count=120)
    time.sleep(1)
    # CVC
    df_minute30_CVC = pyupbit.get_ohlcv("KRW-CVC", interval="minute30",count=120)
    time.sleep(1)
    # POLYX
    df_minute30_POLYX = pyupbit.get_ohlcv("KRW-POLYX", interval="minute30",count=120)
    time.sleep(1)
    # T
    df_minute30_T = pyupbit.get_ohlcv("KRW-T", interval="minute30",count=120)
    time.sleep(1)
    # SHIB
    df_minute30_SHIB = pyupbit.get_ohlcv("KRW-SHIB", interval="minute30",count=120)
    time.sleep(1)
    # BTC
    df_minute30_BTC = pyupbit.get_ohlcv("KRW-BTC", interval="minute30",count=120)
    time.sleep(1)
    #XRP
    df_minute30_XRP = pyupbit.get_ohlcv("KRW-XRP", interval="minute30",count=120)
    time.sleep(1)
    # DOGE
    df_minute30_DOGE = pyupbit.get_ohlcv("KRW-DOGE", interval="minute30",count=120)
    time.sleep(1)
    # WAXP
    df_minute30_WAXP = pyupbit.get_ohlcv("KRW-WAXP", interval="minute30",count=120)
    time.sleep(1)
    #CTC
    df_minute30_CTC = pyupbit.get_ohlcv("KRW-CTC", interval="minute30",count=120)
    time.sleep(1)
    #ANKR
    df_minute30_ANKR = pyupbit.get_ohlcv("KRW-ANKR", interval="minute30",count=120)
    time.sleep(1)
    # AERGO
    df_minute30_AERGO = pyupbit.get_ohlcv("KRW-AERGO", interval="minute30",count=120)
    time.sleep(1)
    # HIFI
    df_minute30_HIFI = pyupbit.get_ohlcv("KRW-HIFI", interval="minute30",count=120)
    time.sleep(1)
    # SOL
    df_minute30_SOL = pyupbit.get_ohlcv("KRW-SOL", interval="minute30",count=120)
    time.sleep(1)
    # STMX
    df_minute30_STMX = pyupbit.get_ohlcv("KRW-STMX", interval="minute30",count=120)
    time.sleep(1)
    # ETH
    df_minute30_ETH = pyupbit.get_ohlcv("KRW-ETH", interval="minute30",count=120)
    time.sleep(1)
    # ID
    df_minute30_ID = pyupbit.get_ohlcv("KRW-ID", interval="minute30",count=120)
    time.sleep(1)
    # NEAR
    df_minute30_NEAR = pyupbit.get_ohlcv("KRW-NEAR", interval="minute30",count=120)
    time.sleep(1)
    # SC
    df_minute30_SC = pyupbit.get_ohlcv("KRW-SC", interval="minute30",count=120)
    time.sleep(1)
    # BORA
    df_minute30_BORA = pyupbit.get_ohlcv("KRW-BORA", interval="minute30",count=120)
    time.sleep(1)
    # PYTH
    df_minute30_PYTH = pyupbit.get_ohlcv("KRW-PYTH", interval="minute30",count=120)
    time.sleep(1)
    # LSK
    df_minute30_LSK = pyupbit.get_ohlcv("KRW-LSK", interval="minute30",count=120)
    time.sleep(1)
    # STX
    df_minute30_STX = pyupbit.get_ohlcv("KRW-STX", interval="minute30",count=120)
    time.sleep(1)
    # ETC
    df_minute30_ETC = pyupbit.get_ohlcv("KRW-ETC", interval="minute30",count=120)
    time.sleep(1)
    # APT
    df_minute30_APT = pyupbit.get_ohlcv("KRW-APT", interval="minute30",count=120)
    time.sleep(1)
    # MVL
    df_minute30_MVL = pyupbit.get_ohlcv("KRW-MVL", interval="minute30",count=120)
    time.sleep(1)
    # SXP
    df_minute30_SXP = pyupbit.get_ohlcv("KRW-SXP", interval="minute30",count=120)
    time.sleep(1)
    # AVAX
    df_minute30_AVAX = pyupbit.get_ohlcv("KRW-AVAX", interval="minute30",count=120)
    time.sleep(1)
    # BCH
    df_minute30_BCH = pyupbit.get_ohlcv("KRW-BCH", interval="minute30",count=120)
    time.sleep(1)
    # ICX
    df_minute30_ICX = pyupbit.get_ohlcv("KRW-ICX", interval="minute30",count=120)
    time.sleep(1)
    # SEI
    df_minute30_SEI = pyupbit.get_ohlcv("KRW-SEI", interval="minute30",count=120)
    time.sleep(1)
    # ONG
    df_minute30_ONG = pyupbit.get_ohlcv("KRW-ONG", interval="minute30",count=120)
    time.sleep(1)
    # BTG
    df_minute30_BTG = pyupbit.get_ohlcv("KRW-BTG", interval="minute30",count=120)
    time.sleep(1)
    # ORBS
    df_minute30_ORBS = pyupbit.get_ohlcv("KRW-ORBS", interval="minute30",count=120)
    time.sleep(1)
    # ZRX
    df_minute30_ZRX = pyupbit.get_ohlcv("KRW-ZRX", interval="minute30",count=120)
    time.sleep(1)
    # GMT
    df_minute30_GMT = pyupbit.get_ohlcv("KRW-GMT", interval="minute30",count=120)
    time.sleep(1)
    # HUNT
    df_minute30_HUNT = pyupbit.get_ohlcv("KRW-HUNT", interval="minute30",count=120)
    time.sleep(1)
    # IOTA
    df_minute30_IOTA = pyupbit.get_ohlcv("KRW-IOTA", interval="minute30",count=120)
    time.sleep(1)
    # IQ
    df_minute30_IQ = pyupbit.get_ohlcv("KRW-IQ", interval="minute30",count=120)
    time.sleep(1)
    # STRAX
    df_minute30_STRAX = pyupbit.get_ohlcv("KRW-STRAX", interval="minute30",count=120)
    time.sleep(1)
    # CELO
    df_minute30_CELO = pyupbit.get_ohlcv("KRW-CELO", interval="minute30",count=120)
    time.sleep(1)
    # ARB
    df_minute30_ARB = pyupbit.get_ohlcv("KRW-ARB", interval="minute30",count=120)
    time.sleep(1)
    # BTT
    df_minute30_BTT = pyupbit.get_ohlcv("KRW-BTT", interval="minute30",count=120)
    time.sleep(1)
    # HBAR
    df_minute30_HBAR = pyupbit.get_ohlcv("KRW-HBAR", interval="minute30",count=120)
    time.sleep(1)
    # LINK
    df_minute30_LINK = pyupbit.get_ohlcv("KRW-LINK", interval="minute30",count=120)
    time.sleep(1)
    # SAND
    df_minute30_SAND = pyupbit.get_ohlcv("KRW-SAND", interval="minute30",count=120)
    time.sleep(1)
    # GRT
    df_minute30_GRT = pyupbit.get_ohlcv("KRW-GRT", interval="minute30",count=120)
    time.sleep(1)
    # FLOW
    df_minute30_FLOW = pyupbit.get_ohlcv("KRW-FLOW", interval="minute30",count=120)
    time.sleep(1)
    # ADA
    df_minute30_ADA = pyupbit.get_ohlcv("KRW-ADA", interval="minute30",count=120)
    time.sleep(1)
    # SUI
    df_minute30_SUI = pyupbit.get_ohlcv("KRW-SUI", interval="minute30",count=120)
    time.sleep(1)
    # 
    
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

        return df

    # Add indicators to both dataframes
    
    df_minute30_XEC = add_indicators(df_minute30_XEC)
    df_minute30_CVC = add_indicators(df_minute30_CVC)
    df_minute30_POLYX = add_indicators(df_minute30_POLYX)
    df_minute30_T = add_indicators(df_minute30_T)
    df_minute30_SHIB = add_indicators(df_minute30_SHIB)
    df_minute30_BTC = add_indicators(df_minute30_BTC)
    df_minute30_XRP = add_indicators(df_minute30_XRP)
    df_minute30_DOGE = add_indicators(df_minute30_DOGE)
    df_minute30_WAXP = add_indicators(df_minute30_WAXP)
    df_minute30_CTC = add_indicators(df_minute30_CTC)
    df_minute30_ANKR = add_indicators(df_minute30_ANKR)
    df_minute30_AERGO = add_indicators(df_minute30_AERGO)
    df_minute30_HIFI = add_indicators(df_minute30_HIFI)
    df_minute30_SOL = add_indicators(df_minute30_SOL)
    df_minute30_STMX = add_indicators(df_minute30_STMX)
    df_minute30_ETH = add_indicators(df_minute30_ETH)

    df_minute30_ID = add_indicators(df_minute30_ID)
    df_minute30_NEAR = add_indicators(df_minute30_NEAR)
    df_minute30_SC = add_indicators(df_minute30_SC)
    df_minute30_BORA = add_indicators(df_minute30_BORA)
    df_minute30_PYTH = add_indicators(df_minute30_PYTH)
    df_minute30_LSK = add_indicators(df_minute30_LSK)
    df_minute30_STX = add_indicators(df_minute30_STX)
    df_minute30_ETC = add_indicators(df_minute30_ETC)
    df_minute30_APT = add_indicators(df_minute30_APT)
    df_minute30_MVL = add_indicators(df_minute30_MVL)
    df_minute30_SXP = add_indicators(df_minute30_SXP)
    df_minute30_AVAX = add_indicators(df_minute30_AVAX)
    df_minute30_BCH = add_indicators(df_minute30_BCH)
    df_minute30_ICX = add_indicators(df_minute30_ICX)
    df_minute30_SEI = add_indicators(df_minute30_SEI)
    df_minute30_ONG = add_indicators(df_minute30_ONG)
    df_minute30_BTG = add_indicators(df_minute30_BTG)
    df_minute30_ORBS = add_indicators(df_minute30_ORBS)
    df_minute30_ZRX = add_indicators(df_minute30_ZRX)
    df_minute30_GMT = add_indicators(df_minute30_GMT)
    df_minute30_HUNT = add_indicators(df_minute30_HUNT)
    df_minute30_IOTA = add_indicators(df_minute30_IOTA)
    df_minute30_IQ = add_indicators(df_minute30_IQ)
    df_minute30_STRAX = add_indicators(df_minute30_STRAX)
    df_minute30_CELO = add_indicators(df_minute30_CELO)
    df_minute30_ARB = add_indicators(df_minute30_ARB)
    df_minute30_BTT = add_indicators(df_minute30_BTT)
    df_minute30_HBAR = add_indicators(df_minute30_HBAR)
    df_minute30_LINK = add_indicators(df_minute30_LINK)
    df_minute30_SAND = add_indicators(df_minute30_SAND)
    df_minute30_GRT = add_indicators(df_minute30_GRT)
    df_minute30_FLOW = add_indicators(df_minute30_FLOW)
    df_minute30_ADA = add_indicators(df_minute30_ADA)
    df_minute30_SUI = add_indicators(df_minute30_SUI)




#############################################################################################################################
    df_minute30_XEC_tail = df_minute30_XEC.tail(n=1)
    df_minute30_CVC_tail = df_minute30_CVC.tail(n=1)
    df_minute30_POLYX_tail = df_minute30_POLYX.tail(n=1)
    df_minute30_T_tail = df_minute30_T.tail(n=1)
    df_minute30_SHIB_tail = df_minute30_SHIB.tail(n=1)
    df_minute30_BTC_tail = df_minute30_BTC.tail(n=1)
    df_minute30_XRP_tail = df_minute30_XRP.tail(n=1)
    df_minute30_DOGE_tail = df_minute30_DOGE.tail(n=1)
    df_minute30_WAXP_tail = df_minute30_WAXP.tail(n=1)
    df_minute30_CTC_tail = df_minute30_CTC.tail(n=1)
    df_minute30_ANKR_tail = df_minute30_ANKR.tail(n=1)
    df_minute30_AERGO_tail = df_minute30_AERGO.tail(n=1)
    df_minute30_HIFI_tail = df_minute30_HIFI.tail(n=1)
    df_minute30_SOL_tail = df_minute30_SOL.tail(n=1)
    df_minute30_STMX_tail = df_minute30_STMX.tail(n=1)
    df_minute30_ETH_tail = df_minute30_ETH.tail(n=1)
    df_minute30_ID_tail = df_minute30_ID.tail(n=1)
    df_minute30_NEAR_tail = df_minute30_NEAR.tail(n=1)
    df_minute30_SC_tail = df_minute30_SC.tail(n=1)
    df_minute30_BORA_tail = df_minute30_BORA.tail(n=1)
    df_minute30_PYTH_tail = df_minute30_PYTH.tail(n=1)
    df_minute30_LSK_tail = df_minute30_LSK.tail(n=1)
    df_minute30_STX_tail = df_minute30_STX.tail(n=1)
    df_minute30_ETC_tail = df_minute30_ETC.tail(n=1)
    df_minute30_APT_tail = df_minute30_APT.tail(n=1)
    df_minute30_MVL_tail = df_minute30_MVL.tail(n=1)
    df_minute30_SXP_tail = df_minute30_SXP.tail(n=1)
    df_minute30_AVAX_tail = df_minute30_AVAX.tail(n=1)
    df_minute30_BCH_tail = df_minute30_BCH.tail(n=1)
    df_minute30_ICX_tail = df_minute30_ICX.tail(n=1)
    df_minute30_SEI_tail = df_minute30_SEI.tail(n=1)
    df_minute30_ONG_tail = df_minute30_ONG.tail(n=1)
    df_minute30_BTG_tail = df_minute30_BTG.tail(n=1)
    df_minute30_ORBS_tail = df_minute30_ORBS.tail(n=1)
    df_minute30_ZRX_tail = df_minute30_ZRX.tail(n=1)
    df_minute30_GMT_tail = df_minute30_GMT.tail(n=1)
    df_minute30_HUNT_tail = df_minute30_HUNT.tail(n=1)
    df_minute30_IOTA_tail = df_minute30_IOTA.tail(n=1)
    df_minute30_IQ_tail = df_minute30_IQ.tail(n=1)
    df_minute30_STRAX_tail = df_minute30_STRAX.tail(n=1)
    df_minute30_CELO_tail = df_minute30_CELO.tail(n=1)
    df_minute30_ARB_tail = df_minute30_ARB.tail(n=1)
    df_minute30_BTT_tail = df_minute30_BTT.tail(n=1)
    df_minute30_HBAR_tail = df_minute30_HBAR.tail(n=1)
    df_minute30_LINK_tail = df_minute30_LINK.tail(n=1)
    df_minute30_SAND_tail = df_minute30_SAND.tail(n=1)
    df_minute30_GRT_tail = df_minute30_GRT.tail(n=1)
    df_minute30_FLOW_tail = df_minute30_FLOW.tail(n=1)
    df_minute30_ADA_tail = df_minute30_ADA.tail(n=1)
    df_minute30_SUI_tail = df_minute30_SUI.tail(n=1)

    

########################################################################################################################
    


    
    combined_df = pd.concat([df_minute30_XEC_tail, df_minute30_CVC_tail,df_minute30_POLYX_tail,df_minute30_T_tail,
                             df_minute30_SHIB_tail,df_minute30_BTC_tail,df_minute30_XRP_tail, df_minute30_DOGE_tail,
                             df_minute30_WAXP_tail,df_minute30_CTC_tail,df_minute30_ANKR_tail,df_minute30_AERGO_tail,
                             df_minute30_HIFI_tail,df_minute30_SOL_tail, df_minute30_STMX_tail,df_minute30_ETH_tail,
                             df_minute30_ID_tail, df_minute30_NEAR_tail, df_minute30_SC_tail, df_minute30_BORA_tail,
                             df_minute30_PYTH_tail, df_minute30_LSK_tail, df_minute30_STX_tail, df_minute30_ETC_tail,
                             df_minute30_APT_tail, df_minute30_MVL_tail, df_minute30_SXP_tail, df_minute30_AVAX_tail,
                             df_minute30_BCH_tail, df_minute30_ICX_tail, df_minute30_SEI_tail, df_minute30_ONG_tail,
                             df_minute30_BTG_tail, df_minute30_ORBS_tail, df_minute30_ZRX_tail, df_minute30_GMT_tail,
                             df_minute30_HUNT_tail, df_minute30_IOTA_tail, df_minute30_IQ_tail, df_minute30_STRAX_tail,
                             df_minute30_CELO_tail, df_minute30_ARB_tail, df_minute30_BTT_tail, df_minute30_HBAR_tail,
                             df_minute30_LINK_tail, df_minute30_SAND_tail, df_minute30_GRT_tail, df_minute30_FLOW_tail,
                             df_minute30_ADA_tail, df_minute30_SUI_tail
                            ], 
                        keys=['KRW-XEC', 'KRW-CVC','KRW-POLYX','KRW-T',
                            'KRW-SHIB','KRW-BTC','KRW-XRP','KRW-DOGE',
                            'KRW-WAXP','KRW-CTC','KRW-ANKR','KRW-AERGO',
                            'KRW-HIFI','KRW-SOL','KRW-STMX','KRW-ETH',
                            "KRW-ID", "KRW-NEAR", "KRW-SC", "KRW-BORA",
                            "KRW-PYTH", "KRW-LSK", "KRW-STX", "KRW-ETC",
                            "KRW-APT", "KRW-MVL", "KRW-SXP", "KRW-AVAX",
                            "KRW-BCH", "KRW-ICX", "KRW-SEI", "KRW-ONG",
                            "KRW-BTG", "KRW-ORBS", "KRW-ZRX", "KRW-GMT",
                            "KRW-HUNT", "KRW-IOTA", "KRW-IQ", "KRW-STRAX",
                            "KRW-CELO", "KRW-ARB", "KRW-BTT", "KRW-HBAR",
                            "KRW-LINK", "KRW-SAND", "KRW-GRT", "KRW-FLOW",
                            "KRW-ADA", "KRW-SUI"
                            ])
    #  EMA > SMA
    combined_df_sort = combined_df[(combined_df['EMA_10'] > combined_df['SMA_10'])]
    combined_df_sort_v2 = combined_df_sort[(combined_df_sort['EMA_5'] > combined_df_sort['SMA_5'])]

    #print(combined_df_sort_v2)
    #sorted_df = combined_df.sort_values(by='volume', ascending=True)
    
    sorted_value_df = combined_df_sort_v2.sort_values(by='value', ascending=True)
    result = sorted_value_df.tail(n=1)
    combined_data = result.to_json(orient='split')
    #print(combined_data)
    # JSON 문자열을 파이썬 딕셔너리로 변환
    data_json = json.loads(combined_data)
    # 'index' 키에 해당하는 값을 추출
    index_value = data_json["index"][0][0]

    return combined_data, index_value

def get_instructions(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            instructions = file.read()
        return instructions
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred while reading the file:", e)

def analyze_data_with_gpt4(data_json,index_value):
    instructions_path = "autotrade_version5.md"
    try:
        instructions = get_instructions(instructions_path)
        if not instructions:
            print("No instructions found.")
            return None

        current_status = get_current_status(index_value)
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": data_json},
                {"role": "user", "content": current_status}
            ],
            response_format={"type":"json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in analyzing data with GPT-4: {e}")
        return None
    
def execute_buy(index_value):
    print(f"Attempting to buy {index_value}...")
    try:
        krw = upbit.get_balance("KRW")
        if krw > 5000:
            result = upbit.buy_market_order(index_value, krw*0.9995)
            print("Buy order successful:", result)
    except Exception as e:
        print(f"Failed to execute buy order: {e}")

def execute_sell(index_value):
    print(f"Attempting to sell {index_value}...")
    index_value_split = index_value.split("-")[1]
    
    try:
        index_value_split_value = upbit.get_balance(index_value_split)
        current_price = pyupbit.get_orderbook(ticker=index_value)['orderbook_units'][0]["ask_price"]
        if current_price*index_value_split_value > 5000:
            result = upbit.sell_market_order(index_value, index_value_split_value)
            print("Sell order successful:", result)
    except Exception as e:
        print(f"Failed to execute sell order: {e}")

def make_decision_and_execute():
    print("Making decision and executing...")
    data_json, index_value = fetch_and_prepare_data()
    print(data_json)
    advice = analyze_data_with_gpt4(data_json,index_value)
    # print(index_value)
    # index_value_split = index_value.split("-")[1]
    # print(index_value_split)
    try:
        decision = json.loads(advice)
        print(decision)
        if decision.get('decision') == "buy":
            execute_buy(index_value)
        elif decision.get('decision') == "sell":
            execute_sell(index_value)
        return data_json, index_value
    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")

def make_decision_and_execute_sell(data_json,index_value):
    print("Making decision and executing...")
    #data_json, index_value = fetch_and_prepare_data()
    print(data_json)
    advice = analyze_data_with_gpt4(data_json,index_value)
    # print(index_value)
    # index_value_split = index_value.split("-")[1]
    # print(index_value_split)
    try:
        decision = json.loads(advice)
        print(decision)
        if decision.get('decision') == "buy":
            execute_buy(index_value)
        elif decision.get('decision') == "sell":
            execute_sell(index_value)

    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")

if __name__ == "__main__":
    data_json, index_value = make_decision_and_execute()
    schedule.every(30).minutes.do(make_decision_and_execute_sell, data_json=data_json, index_value=index_value)
    schedule.every(31).minutes.do(make_decision_and_execute)

    while True:
        schedule.run_pending()
        time.sleep(1)


# #1초마다 make_decision_and_execute을 동작시키다가 "22:21"이 되면 프로그램 종료
# schedule.every(1).seconds.do(make_decision_and_execute)
# schedule.every().day.at("22:21").do(exit)