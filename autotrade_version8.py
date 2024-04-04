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
from technical_analysis import add_indicators_version2
from sqlite3_db_function import *
import requests


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
    # AQT
    df_minute30_AQT = pyupbit.get_ohlcv("KRW-AQT", interval="minute30",count=120)
    time.sleep(1)
    # CBK
    df_minute30_CBK = pyupbit.get_ohlcv("KRW-CBK", interval="minute30",count=120)
    time.sleep(1)
    # FCT2
    df_minute30_FCT2 = pyupbit.get_ohlcv("KRW-FCT2", interval="minute30",count=120)
    time.sleep(1)
    # JST
    df_minute30_JST = pyupbit.get_ohlcv("KRW-JST", interval="minute30",count=120)
    time.sleep(1)
    # UPP
    df_minute30_UPP = pyupbit.get_ohlcv("KRW-UPP", interval="minute30",count=120)
    time.sleep(1)
    # STRIKE
    df_minute30_STRIKE = pyupbit.get_ohlcv("KRW-STRIKE", interval="minute30",count=120)
    time.sleep(1)
    # MOC
    df_minute30_MOC = pyupbit.get_ohlcv("KRW-MOC", interval="minute30",count=120)
    time.sleep(1)
    # TFUEL
    df_minute30_TFUEL = pyupbit.get_ohlcv("KRW-TFUEL", interval="minute30",count=120)
    time.sleep(1)
    # TT
    df_minute30_TT = pyupbit.get_ohlcv("KRW-TT", interval="minute30",count=120)
    time.sleep(1)
    # KNC
    df_minute30_KNC = pyupbit.get_ohlcv("KRW-KNC", interval="minute30",count=120)
    time.sleep(1)
    # CRO
    df_minute30_CRO = pyupbit.get_ohlcv("KRW-CRO", interval="minute30",count=120)
    time.sleep(1)
    # META
    df_minute30_META = pyupbit.get_ohlcv("KRW-META", interval="minute30",count=120)
    time.sleep(1)
    # ELF
    df_minute30_ELF = pyupbit.get_ohlcv("KRW-ELF", interval="minute30",count=120)
    time.sleep(1)
    # AHT
    df_minute30_AHT = pyupbit.get_ohlcv("KRW-AHT", interval="minute30",count=120)
    time.sleep(1)
    # BAT
    df_minute30_BAT = pyupbit.get_ohlcv("KRW-BAT", interval="minute30",count=120)
    time.sleep(1)
    # SBD
    df_minute30_SBD = pyupbit.get_ohlcv("KRW-SBD", interval="minute30",count=120)
    time.sleep(1)
    # MED
    df_minute30_MED = pyupbit.get_ohlcv("KRW-MED", interval="minute30",count=120)
    time.sleep(1)
    # AAVE
    df_minute30_AAVE = pyupbit.get_ohlcv("KRW-AAVE", interval="minute30",count=120)
    time.sleep(1)
    # XTZ
    df_minute30_XTZ = pyupbit.get_ohlcv("KRW-XTZ", interval="minute30",count=120)
    time.sleep(1)
    # TON
    df_minute30_TON = pyupbit.get_ohlcv("KRW-TON", interval="minute30",count=120)
    time.sleep(1)
    # 
    
    

    # Add indicators to both dataframes
    
    df_minute30_XEC = add_indicators_version2(df_minute30_XEC)
    df_minute30_CVC = add_indicators_version2(df_minute30_CVC)
    df_minute30_POLYX = add_indicators_version2(df_minute30_POLYX)
    df_minute30_T = add_indicators_version2(df_minute30_T)
    df_minute30_SHIB = add_indicators_version2(df_minute30_SHIB)
    df_minute30_BTC = add_indicators_version2(df_minute30_BTC)
    df_minute30_XRP = add_indicators_version2(df_minute30_XRP)
    df_minute30_DOGE = add_indicators_version2(df_minute30_DOGE)
    df_minute30_WAXP = add_indicators_version2(df_minute30_WAXP)
    df_minute30_CTC = add_indicators_version2(df_minute30_CTC)
    df_minute30_ANKR = add_indicators_version2(df_minute30_ANKR)
    df_minute30_AERGO = add_indicators_version2(df_minute30_AERGO)
    df_minute30_HIFI = add_indicators_version2(df_minute30_HIFI)
    df_minute30_SOL = add_indicators_version2(df_minute30_SOL)
    df_minute30_STMX = add_indicators_version2(df_minute30_STMX)
    df_minute30_ETH = add_indicators_version2(df_minute30_ETH)
    df_minute30_ID = add_indicators_version2(df_minute30_ID)
    df_minute30_NEAR = add_indicators_version2(df_minute30_NEAR)
    df_minute30_SC = add_indicators_version2(df_minute30_SC)
    df_minute30_BORA = add_indicators_version2(df_minute30_BORA)
    df_minute30_PYTH = add_indicators_version2(df_minute30_PYTH)
    df_minute30_LSK = add_indicators_version2(df_minute30_LSK)
    df_minute30_STX = add_indicators_version2(df_minute30_STX)
    df_minute30_ETC = add_indicators_version2(df_minute30_ETC)
    df_minute30_APT = add_indicators_version2(df_minute30_APT)
    df_minute30_MVL = add_indicators_version2(df_minute30_MVL)
    df_minute30_SXP = add_indicators_version2(df_minute30_SXP)
    df_minute30_AVAX = add_indicators_version2(df_minute30_AVAX) 
    df_minute30_BCH = add_indicators_version2(df_minute30_BCH)
    df_minute30_ICX = add_indicators_version2(df_minute30_ICX)
    df_minute30_SEI = add_indicators_version2(df_minute30_SEI)
    df_minute30_ONG = add_indicators_version2(df_minute30_ONG)
    df_minute30_BTG = add_indicators_version2(df_minute30_BTG)
    df_minute30_ORBS = add_indicators_version2(df_minute30_ORBS)
    df_minute30_ZRX = add_indicators_version2(df_minute30_ZRX)
    df_minute30_GMT = add_indicators_version2(df_minute30_GMT)
    df_minute30_HUNT = add_indicators_version2(df_minute30_HUNT)
    df_minute30_IOTA = add_indicators_version2(df_minute30_IOTA)
    df_minute30_IQ = add_indicators_version2(df_minute30_IQ)
    df_minute30_STRAX = add_indicators_version2(df_minute30_STRAX)
    df_minute30_CELO = add_indicators_version2(df_minute30_CELO)
    df_minute30_ARB = add_indicators_version2(df_minute30_ARB)
    df_minute30_BTT = add_indicators_version2(df_minute30_BTT)
    df_minute30_HBAR = add_indicators_version2(df_minute30_HBAR)
    df_minute30_LINK = add_indicators_version2(df_minute30_LINK)
    df_minute30_SAND = add_indicators_version2(df_minute30_SAND)
    df_minute30_GRT = add_indicators_version2(df_minute30_GRT)
    df_minute30_FLOW = add_indicators_version2(df_minute30_FLOW)
    df_minute30_ADA = add_indicators_version2(df_minute30_ADA)
    df_minute30_SUI = add_indicators_version2(df_minute30_SUI)

    ################################################################
    df_minute30_AQT = add_indicators_version2(df_minute30_AQT)
    df_minute30_CBK = add_indicators_version2(df_minute30_CBK)
    df_minute30_FCT2 = add_indicators_version2(df_minute30_FCT2)
    df_minute30_JST = add_indicators_version2(df_minute30_JST)
    df_minute30_UPP = add_indicators_version2(df_minute30_UPP)
    df_minute30_STRIKE = add_indicators_version2(df_minute30_STRIKE)
    df_minute30_MOC = add_indicators_version2(df_minute30_MOC)
    df_minute30_TFUEL = add_indicators_version2(df_minute30_TFUEL)
    df_minute30_TT = add_indicators_version2(df_minute30_TT)
    df_minute30_KNC = add_indicators_version2(df_minute30_KNC)
    df_minute30_CRO = add_indicators_version2(df_minute30_CRO)
    df_minute30_META = add_indicators_version2(df_minute30_META)
    df_minute30_ELF = add_indicators_version2(df_minute30_ELF)
    df_minute30_AHT = add_indicators_version2(df_minute30_AHT)
    df_minute30_BAT = add_indicators_version2(df_minute30_BAT)
    df_minute30_SBD = add_indicators_version2(df_minute30_SBD)
    df_minute30_MED = add_indicators_version2(df_minute30_MED)
    df_minute30_AAVE = add_indicators_version2(df_minute30_AAVE)
    df_minute30_XTZ = add_indicators_version2(df_minute30_XTZ)
    df_minute30_TON = add_indicators_version2(df_minute30_TON)




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

    ####################################################################################
    df_minute30_AQT_tail = df_minute30_AQT.tail(n=1)
    df_minute30_CBK_tail = df_minute30_CBK.tail(n=1)
    df_minute30_FCT2_tail = df_minute30_FCT2.tail(n=1)
    df_minute30_JST_tail = df_minute30_JST.tail(n=1)
    df_minute30_UPP_tail = df_minute30_UPP.tail(n=1)
    df_minute30_STRIKE_tail = df_minute30_STRIKE.tail(n=1)
    df_minute30_MOC_tail = df_minute30_MOC.tail(n=1)
    df_minute30_TFUEL_tail = df_minute30_TFUEL.tail(n=1)
    df_minute30_TT_tail = df_minute30_TT.tail(n=1)
    df_minute30_KNC_tail = df_minute30_KNC.tail(n=1)
    df_minute30_CRO_tail = df_minute30_CRO.tail(n=1)
    df_minute30_META_tail = df_minute30_META.tail(n=1)
    df_minute30_ELF_tail = df_minute30_ELF.tail(n=1)
    df_minute30_AHT_tail = df_minute30_AHT.tail(n=1)
    df_minute30_BAT_tail = df_minute30_BAT.tail(n=1)
    df_minute30_SBD_tail = df_minute30_SBD.tail(n=1)
    df_minute30_MED_tail = df_minute30_MED.tail(n=1)
    df_minute30_AAVE_tail = df_minute30_AAVE.tail(n=1)
    df_minute30_XTZ_tail = df_minute30_XTZ.tail(n=1)
    df_minute30_TON_tail = df_minute30_TON.tail(n=1)


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
                             df_minute30_ADA_tail, df_minute30_SUI_tail, df_minute30_AQT_tail, df_minute30_CBK_tail,
                             df_minute30_FCT2_tail, df_minute30_JST_tail, df_minute30_UPP_tail, df_minute30_STRIKE_tail,
                             df_minute30_MOC_tail, df_minute30_TFUEL_tail, df_minute30_TT_tail, df_minute30_KNC_tail,
                             df_minute30_CRO_tail, df_minute30_META_tail, df_minute30_ELF_tail, df_minute30_AHT_tail,
                             df_minute30_BAT_tail, df_minute30_SBD_tail, df_minute30_MED_tail, df_minute30_AAVE_tail,
                             df_minute30_XTZ_tail, df_minute30_TON_tail
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
                            "KRW-ADA", "KRW-SUI", "KRW-AQT", "KRW-CBK",
                            "KRW-FCT2", "KRW-JST", "KRW-UPP","KRW-STRIKE",
                            "KRW-MOC", "KRW-TFUEL","KRW-TT","KRW-KNC",
                            "KRW-CRO", "KRW-META", "KRW-ELF", "KRW-AHT",
                            "KRW-BAT", "KRW-SBD", "KRW-MED", "KRW-AAVE",
                            "KRW-XTZ", "KRW-TON"
                            ])
    #  EMA > SMA
    # 5일 sma > 20일 sma > (60일 sma & 120일 sma ) -> 골든크로스 전략
    combined_df_sma_5_20 = combined_df[combined_df['SMA_5'] > combined_df['SMA_20']]
    combined_df_sma_5_60 =  combined_df_sma_5_20[combined_df_sma_5_20['SMA_5'] > combined_df_sma_5_20['SMA_60']]
    combined_df_sma_5_120 = combined_df_sma_5_60[combined_df_sma_5_60['SMA_5'] > combined_df_sma_5_60['SMA_120']]
 
    combined_df_sort = combined_df_sma_5_120[(combined_df_sma_5_120['EMA_10'] > combined_df_sma_5_120['SMA_10'])]
    combined_df_sort_v2 = combined_df_sort[(combined_df_sort['EMA_5'] > combined_df_sort['SMA_5'])]
    if len(combined_df_sort_v2) != 0:
        sorted_value_df = combined_df_sort_v2.sort_values(by='value', ascending=True)
    else:
        if len(combined_df_sort) != 0:
            sorted_value_df = combined_df_sort.sort_values(by='value', ascending=True)
        else:
            sorted_value_df = combined_df_sma_5_120.sort_values(by='value', ascending=True)
            if len(combined_df_sma_5_120) != 0:
                sorted_value_df = combined_df_sma_5_120.sort_values(by='value', ascending=True)
            else:
                sorted_value_df = combined_df_sma_5_60.sort_values(by='value', ascending=True)
                if len(combined_df_sma_5_60) != 0:
                    sorted_value_df = combined_df_sma_5_60.sort_values(by='value', ascending=True)
                else:
                    sorted_value_df = combined_df_sma_5_20.sort_values(by='value', ascending=True)
    #print(combined_df_sort_v2)
    #sorted_df = combined_df.sort_values(by='volume', ascending=True)
    
    
    result = sorted_value_df.tail(n=1)
    combined_data = result.to_json(orient='split')
    #combined_data_dumps = json.dumps(combined_data)
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

def analyze_data_with_gpt4(data_json,last_decisions,fear_and_greed,current_status):
    instructions_path = "autotrade_version8.md"
    try:
        instructions = get_instructions(instructions_path)
        if not instructions:
            print("No instructions found.")
            return None

        #current_status = get_current_status(index_value)
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": data_json},
                {"role": "user", "content": current_status},
                {"role": "user", "content": last_decisions},
                {"role": "user", "content": fear_and_greed}
            ],
            response_format={"type":"json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in analyzing data with GPT-4: {e}")
        return None
    

def execute_buy(index_value_v2,percentage):
    print(f"Attempting to buy {index_value_v2} with a percentage of KRW balance...")
    try:
        krw_balance = upbit.get_balance("KRW")
        amount_to_invest = krw_balance * (percentage / 100)
        if amount_to_invest > 5000:  # Ensure the order is above the minimum threshold
            result = upbit.buy_market_order(index_value_v2, amount_to_invest * 0.9995)  # Adjust for fees
            print("Buy order successful:", result)
    except Exception as e:
        print(f"Failed to execute buy order: {e}")


def execute_sell(index_value,percentage):
    try:
        print(f"Attempting to sell a percentage of {index_value}...")
        index_value_split = index_value.split("-")[1]
        btc_balance = upbit.get_balance(index_value_split)
        amount_to_sell = btc_balance * (percentage / 100)
        current_price = pyupbit.get_orderbook(ticker=index_value)['orderbook_units'][0]["ask_price"]
        if current_price * amount_to_sell > 5000:  # Ensure the order is above the minimum threshold
            result = upbit.sell_market_order(index_value, amount_to_sell)
            print("Sell order successful:", result)
    except Exception as e:
        print(f"Failed to execute sell order: {e}")

def make_decision_and_execute():
    print("Making decision and executing...")
    data_json, index_value = fetch_and_prepare_data()
    print(data_json)
    advice = analyze_data_with_gpt4(data_json,index_value)

    try:
        decision = json.loads(advice)
        print(decision)
        if decision.get('decision') == "buy":
            execute_buy(index_value)
            return index_value
    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")


def make_decision_and_execute_schedule():
    
    try:
        global index_value
        # index_value = None
        krw = upbit.get_balance("KRW")
        max_retries = 5
        retry_delay_seconds = 5
        decision = None

        if krw > 5000:
            print("Making decision and executing...")
            data_json_v2, index_value_v2 = fetch_and_prepare_data()
            print(data_json_v2)
            last_decisions = fetch_last_decisions()
            fear_and_greed = fetch_fear_and_greed_index(limit=30)
            current_status = get_current_status(index_value_v2)
            for attempt in range(max_retries):
                try:
                    advice = analyze_data_with_gpt4(data_json_v2,last_decisions,fear_and_greed,current_status)
                    decision = json.loads(advice)
                    print(decision)
                    break
                except json.JSONDecodeError as e:
                    print(f"JSON parsing failed: {e}. Retrying in {retry_delay_seconds} seconds...")
                    time.sleep(retry_delay_seconds)
                    print(f"Attempt {attempt + 2} of {max_retries}")
            if not decision:
                print("Failed to make a decision after maximum retries.")
                return

            percentage = decision.get('percentage', 100)
            if decision.get('decision') == "buy":
                execute_buy(index_value_v2,percentage)
                index_value = index_value_v2
                return index_value
            
            save_decision_to_db(decision, current_status)
        else:
            print(f"make_decision_and_execute_sell....")
            make_decision_and_execute_sell(index_value)
    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")    

def make_decision_and_execute_sell(index_value):
    
    try:
        if isinstance(index_value, str): 
            print("Making decision and executing...")
            df_minute30_index_value = pyupbit.get_ohlcv(index_value, interval="minute30",count=120)
            df_minute30_index_value = add_indicators_version2(df_minute30_index_value)
            df_minute30_index_value_tail = df_minute30_index_value.tail(n=1)
            sell_data = df_minute30_index_value_tail.to_json(orient='split')
            last_decisions = fetch_last_decisions()
            fear_and_greed = fetch_fear_and_greed_index(limit=30)
            current_status = get_current_status(index_value)
            advice = analyze_data_with_gpt4(sell_data,last_decisions,fear_and_greed,current_status)
            
            decision = json.loads(advice)
            print(decision)
            percentage = decision.get('percentage', 100)
            if decision.get('decision') == "sell":
                execute_sell(index_value,percentage)
                index_value = None
                return index_value
            save_decision_to_db(decision, current_status)
    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")

def fetch_fear_and_greed_index(limit=1, date_format=''):
    """
    Fetches the latest Fear and Greed Index data.
    Parameters:
    - limit (int): Number of results to return. Default is 1.
    - date_format (str): Date format ('us', 'cn', 'kr', 'world'). Default is '' (unixtime).
    Returns:
    - dict or str: The Fear and Greed Index data in the specified format.
    """
    base_url = "https://api.alternative.me/fng/"
    params = {
        'limit': limit,
        'format': 'json',
        'date_format': date_format
    }
    response = requests.get(base_url, params=params)
    myData = response.json()['data']
    resStr = ""
    for data in myData:
        resStr += str(data)
    return resStr

if __name__ == "__main__":
    initialize_db()
    #schedule.every(1).minutes.do(make_decision_and_execute_schedule)
    schedule.every().hour.at(":00").do(make_decision_and_execute_schedule)  
    #schedule.every().hour.at(":30").do(functools.partial(make_decision_and_execute_sell, index_value))

    while True:
        schedule.run_pending()
        time.sleep(1)


# #1초마다 make_decision_and_execute을 동작시키다가 "22:21"이 되면 프로그램 종료
# schedule.every(1).seconds.do(make_decision_and_execute)
# schedule.every().day.at("22:21").do(exit)  
        
"""
What Is the Crypto Fear and Greed Index? 

0-24: Extreme Fear (indicating potential buying opportunities as market participants might be too worried)

25-49: Fear (suggesting caution among investors)

50: Neutral (market sentiment is balanced between fear and greed)

51-74: Greed (implying increasing market confidence and investment risk)

75-100: Extreme Greed (a warning signal that the market may be overvalued and due for a correction)
"""