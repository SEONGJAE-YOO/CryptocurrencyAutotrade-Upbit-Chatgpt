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
    
    df_daily = pyupbit.get_ohlcv("KRW-XEC", "day", count=200)  ## 기본 요청시 200일 (최대)

    # 1분봉 (최대 200개 요청가능)
    df_minute1 = pyupbit.get_ohlcv("KRW-XEC", interval="minute1")
    # 3분봉 (최대 200개 요청가능)
    df_minute3 = pyupbit.get_ohlcv("KRW-XEC", interval="minute3")
    # 5분봉 (최대 200개 요청가능)
    df_minute5 = pyupbit.get_ohlcv("KRW-XEC", interval="minute5")
    # 10분봉 (최대 200개 요청가능)
    df_minute10 = pyupbit.get_ohlcv("KRW-XEC", interval="minute10")
    # 15분봉
    df_XEC_15= pyupbit.get_ohlcv("KRW-XEC", interval="minute15", count=120)

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




    # ID
    # NEAR
    # SC
    # BORA
    # PYTH
    # LSK
    # STX
    # ETC
    # APT
    # MVL
    # SXP
    # AVAX
    # BCH
    # ICX
    # SEI
    # ONG
    # BTG
    # ORBS
    # ZRX
    # GMT
    # HUNT
    # IOTA
    # IQ
    # STRAX
    # CELO
    # ARB
    # BTT
    # HBAR
    # LINK
    # SAND
    # GRT
    # FLOW
    # ADA
    # SUI
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

    
    combined_df = pd.concat([df_minute30_XEC_tail, df_minute30_CVC_tail,df_minute30_POLYX_tail,df_minute30_T_tail,
                             df_minute30_SHIB_tail,df_minute30_BTC_tail,df_minute30_XRP_tail, df_minute30_DOGE_tail,
                             df_minute30_WAXP_tail,df_minute30_CTC_tail,df_minute30_ANKR_tail,df_minute30_AERGO_tail,
                             df_minute30_HIFI_tail,df_minute30_SOL_tail, df_minute30_STMX_tail,df_minute30_ETH_tail
                            ], 
                        keys=['KRW-XEC', 'KRW-CVC','KRW-POLYX','KRW-T',
                            'KRW-SHIB','KRW-BTC','KRW-XRP','KRW-DOGE',
                            'KRW-WAXP','KRW-CTC','KRW-ANKR','KRW-AERGO',
                            'KRW-HIFI','KRW-SOL','KRW-STMX','KRW-ETH'
                            ])
    

    sorted_df = combined_df.sort_values(by='volume', ascending=True)
    result = sorted_df.tail(n=1)
    combined_data = result.to_json(orient='split')
    print(combined_data)
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
    instructions_path = "20240327.md"
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

    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")

if __name__ == "__main__":
    make_decision_and_execute()
    #schedule.every().hour.at(":01").do(make_decision_and_execute)
    schedule.every(30).minutes.do(make_decision_and_execute)

    while True:
        schedule.run_pending()
        time.sleep(1)


# #1초마다 make_decision_and_execute을 동작시키다가 "22:21"이 되면 프로그램 종료
# schedule.every(1).seconds.do(make_decision_and_execute)
# schedule.every().day.at("22:21").do(exit)