import os
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import pyupbit
import pandas as pd  
import pandas_ta as ta
import json
from openai import OpenAI
import schedule
import time
from technical_analysis import add_indicators_version3
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
    df_minute240_XEC = pyupbit.get_ohlcv("KRW-XEC", interval="minute240",count=120)
    time.sleep(1)
    # CVC
    df_minute240_CVC = pyupbit.get_ohlcv("KRW-CVC", interval="minute240",count=120)
    time.sleep(1)
    # POLYX
    df_minute240_POLYX = pyupbit.get_ohlcv("KRW-POLYX", interval="minute240",count=120)
    time.sleep(1)
    # T
    df_minute240_T = pyupbit.get_ohlcv("KRW-T", interval="minute240",count=120)
    time.sleep(1)
    # SHIB
    df_minute240_SHIB = pyupbit.get_ohlcv("KRW-SHIB", interval="minute240",count=120)
    time.sleep(1)
    # BTC
    df_minute240_BTC = pyupbit.get_ohlcv("KRW-BTC", interval="minute240",count=120)
    time.sleep(1)
    #XRP
    df_minute240_XRP = pyupbit.get_ohlcv("KRW-XRP", interval="minute240",count=120)
    time.sleep(1)
    # DOGE
    df_minute240_DOGE = pyupbit.get_ohlcv("KRW-DOGE", interval="minute240",count=120)
    time.sleep(1)
    # WAXP
    df_minute240_WAXP = pyupbit.get_ohlcv("KRW-WAXP", interval="minute240",count=120)
    time.sleep(1)
    #CTC
    df_minute240_CTC = pyupbit.get_ohlcv("KRW-CTC", interval="minute240",count=120)
    time.sleep(1)
    #ANKR
    df_minute240_ANKR = pyupbit.get_ohlcv("KRW-ANKR", interval="minute240",count=120)
    time.sleep(1)
    # AERGO
    df_minute240_AERGO = pyupbit.get_ohlcv("KRW-AERGO", interval="minute240",count=120)
    time.sleep(1)
    # HIFI
    df_minute240_HIFI = pyupbit.get_ohlcv("KRW-HIFI", interval="minute240",count=120)
    time.sleep(1)
    # SOL
    df_minute240_SOL = pyupbit.get_ohlcv("KRW-SOL", interval="minute240",count=120)
    time.sleep(1)
    # STMX
    df_minute240_STMX = pyupbit.get_ohlcv("KRW-STMX", interval="minute240",count=120)
    time.sleep(1)
    # ETH
    df_minute240_ETH = pyupbit.get_ohlcv("KRW-ETH", interval="minute240",count=120)
    time.sleep(1)
    # ID
    df_minute240_ID = pyupbit.get_ohlcv("KRW-ID", interval="minute240",count=120)
    time.sleep(1)
    # NEAR
    df_minute240_NEAR = pyupbit.get_ohlcv("KRW-NEAR", interval="minute240",count=120)
    time.sleep(1)
    # SC
    df_minute240_SC = pyupbit.get_ohlcv("KRW-SC", interval="minute240",count=120)
    time.sleep(1)
    # BORA
    df_minute240_BORA = pyupbit.get_ohlcv("KRW-BORA", interval="minute240",count=120)
    time.sleep(1)
    # PYTH
    df_minute240_PYTH = pyupbit.get_ohlcv("KRW-PYTH", interval="minute240",count=120)
    time.sleep(1)
    # LSK
    df_minute240_LSK = pyupbit.get_ohlcv("KRW-LSK", interval="minute240",count=120)
    time.sleep(1)
    # STX
    df_minute240_STX = pyupbit.get_ohlcv("KRW-STX", interval="minute240",count=120)
    time.sleep(1)
    # ETC
    df_minute240_ETC = pyupbit.get_ohlcv("KRW-ETC", interval="minute240",count=120)
    time.sleep(1)
    # APT
    df_minute240_APT = pyupbit.get_ohlcv("KRW-APT", interval="minute240",count=120)
    time.sleep(1)
    # MVL
    df_minute240_MVL = pyupbit.get_ohlcv("KRW-MVL", interval="minute240",count=120)
    time.sleep(1)
    # SXP
    df_minute240_SXP = pyupbit.get_ohlcv("KRW-SXP", interval="minute240",count=120)
    time.sleep(1)
    # AVAX
    df_minute240_AVAX = pyupbit.get_ohlcv("KRW-AVAX", interval="minute240",count=120)
    time.sleep(1)
    # BCH
    df_minute240_BCH = pyupbit.get_ohlcv("KRW-BCH", interval="minute240",count=120)
    time.sleep(1)
    # ICX
    df_minute240_ICX = pyupbit.get_ohlcv("KRW-ICX", interval="minute240",count=120)
    time.sleep(1)
    # SEI
    df_minute240_SEI = pyupbit.get_ohlcv("KRW-SEI", interval="minute240",count=120)
    time.sleep(1)
    # ONG
    df_minute240_ONG = pyupbit.get_ohlcv("KRW-ONG", interval="minute240",count=120)
    time.sleep(1)
    # BTG
    df_minute240_BTG = pyupbit.get_ohlcv("KRW-BTG", interval="minute240",count=120)
    time.sleep(1)
    # ORBS
    df_minute240_ORBS = pyupbit.get_ohlcv("KRW-ORBS", interval="minute240",count=120)
    time.sleep(1)
    # ZRX
    df_minute240_ZRX = pyupbit.get_ohlcv("KRW-ZRX", interval="minute240",count=120)
    time.sleep(1)
    # GMT
    df_minute240_GMT = pyupbit.get_ohlcv("KRW-GMT", interval="minute240",count=120)
    time.sleep(1)
    # HUNT
    df_minute240_HUNT = pyupbit.get_ohlcv("KRW-HUNT", interval="minute240",count=120)
    time.sleep(1)
    # IOTA
    df_minute240_IOTA = pyupbit.get_ohlcv("KRW-IOTA", interval="minute240",count=120)
    time.sleep(1)
    # IQ
    df_minute240_IQ = pyupbit.get_ohlcv("KRW-IQ", interval="minute240",count=120)
    time.sleep(1)
    # STRAX
    df_minute240_STRAX = pyupbit.get_ohlcv("KRW-STRAX", interval="minute240",count=120)
    time.sleep(1)
    # CELO
    df_minute240_CELO = pyupbit.get_ohlcv("KRW-CELO", interval="minute240",count=120)
    time.sleep(1)  
    # ARB
    df_minute240_ARB = pyupbit.get_ohlcv("KRW-ARB", interval="minute240",count=120)
    time.sleep(1)
    # BTT
    df_minute240_BTT = pyupbit.get_ohlcv("KRW-BTT", interval="minute240",count=120)
    time.sleep(1)
    # HBAR
    df_minute240_HBAR = pyupbit.get_ohlcv("KRW-HBAR", interval="minute240",count=120)
    time.sleep(1)
    # LINK
    df_minute240_LINK = pyupbit.get_ohlcv("KRW-LINK", interval="minute240",count=120)
    time.sleep(1)
    # SAND
    df_minute240_SAND = pyupbit.get_ohlcv("KRW-SAND", interval="minute240",count=120)
    time.sleep(1)
    # GRT
    df_minute240_GRT = pyupbit.get_ohlcv("KRW-GRT", interval="minute240",count=120)
    time.sleep(1)
    # FLOW
    df_minute240_FLOW = pyupbit.get_ohlcv("KRW-FLOW", interval="minute240",count=120)
    time.sleep(1)
    # ADA
    df_minute240_ADA = pyupbit.get_ohlcv("KRW-ADA", interval="minute240",count=120)
    time.sleep(1)
    # SUI
    df_minute240_SUI = pyupbit.get_ohlcv("KRW-SUI", interval="minute240",count=120)
    time.sleep(1)
    # AQT
    df_minute240_AQT = pyupbit.get_ohlcv("KRW-AQT", interval="minute240",count=120)
    time.sleep(1)
    # CBK
    df_minute240_CBK = pyupbit.get_ohlcv("KRW-CBK", interval="minute240",count=120)
    time.sleep(1)
    # FCT2
    df_minute240_FCT2 = pyupbit.get_ohlcv("KRW-FCT2", interval="minute240",count=120)
    time.sleep(1)
    # JST
    df_minute240_JST = pyupbit.get_ohlcv("KRW-JST", interval="minute240",count=120)
    time.sleep(1)
    # UPP
    df_minute240_UPP = pyupbit.get_ohlcv("KRW-UPP", interval="minute240",count=120)
    time.sleep(1)
    # STRIKE
    df_minute240_STRIKE = pyupbit.get_ohlcv("KRW-STRIKE", interval="minute240",count=120)
    time.sleep(1)
    # MOC
    df_minute240_MOC = pyupbit.get_ohlcv("KRW-MOC", interval="minute240",count=120)
    time.sleep(1)
    # TFUEL
    df_minute240_TFUEL = pyupbit.get_ohlcv("KRW-TFUEL", interval="minute240",count=120)
    time.sleep(1)
    # TT
    df_minute240_TT = pyupbit.get_ohlcv("KRW-TT", interval="minute240",count=120)
    time.sleep(1)
    # KNC
    df_minute240_KNC = pyupbit.get_ohlcv("KRW-KNC", interval="minute240",count=120)
    time.sleep(1)
    # CRO
    df_minute240_CRO = pyupbit.get_ohlcv("KRW-CRO", interval="minute240",count=120)
    time.sleep(1)
    # META
    df_minute240_META = pyupbit.get_ohlcv("KRW-META", interval="minute240",count=120)
    time.sleep(1)
    # ELF
    df_minute240_ELF = pyupbit.get_ohlcv("KRW-ELF", interval="minute240",count=120)
    time.sleep(1)
    # AHT
    df_minute240_AHT = pyupbit.get_ohlcv("KRW-AHT", interval="minute240",count=120)
    time.sleep(1)
    # BAT
    df_minute240_BAT = pyupbit.get_ohlcv("KRW-BAT", interval="minute240",count=120)
    time.sleep(1)
    # SBD
    df_minute240_SBD = pyupbit.get_ohlcv("KRW-SBD", interval="minute240",count=120)
    time.sleep(1)
    # MED
    df_minute240_MED = pyupbit.get_ohlcv("KRW-MED", interval="minute240",count=120)
    time.sleep(1)
    # AAVE
    df_minute240_AAVE = pyupbit.get_ohlcv("KRW-AAVE", interval="minute240",count=120)
    time.sleep(1)
    # XTZ
    df_minute240_XTZ = pyupbit.get_ohlcv("KRW-XTZ", interval="minute240",count=120)
    time.sleep(1)  
    # TON
    df_minute240_TON = pyupbit.get_ohlcv("KRW-TON", interval="minute240",count=120)
    time.sleep(1)
    
    #############################3
    # IMX
    df_minute240_IMX = pyupbit.get_ohlcv("KRW-IMX", interval="minute240",count=120)
    time.sleep(1)
    # HPO
    df_minute240_HPO = pyupbit.get_ohlcv("KRW-HPO", interval="minute240",count=120)
    time.sleep(1)
    # EGLD
    df_minute240_EGLD = pyupbit.get_ohlcv("KRW-EGLD", interval="minute240",count=120)
    time.sleep(1)
    # HIVE
    df_minute240_HIVE = pyupbit.get_ohlcv("KRW-HIVE", interval="minute240",count=120)
    time.sleep(1)
    # GRS
    df_minute240_GRS = pyupbit.get_ohlcv("KRW-GRS", interval="minute240",count=120)
    time.sleep(1)
    # QKC
    df_minute240_QKC = pyupbit.get_ohlcv("KRW-QKC", interval="minute240",count=120)
    time.sleep(1)
    # STPT
    df_minute240_STPT = pyupbit.get_ohlcv("KRW-STPT", interval="minute240",count=120)
    time.sleep(1)
    # XEM
    df_minute240_XEM = pyupbit.get_ohlcv("KRW-XEM", interval="minute240",count=120)
    time.sleep(1)
    # STEEM
    df_minute240_STEEM = pyupbit.get_ohlcv("KRW-STEEM", interval="minute240",count=120)
    time.sleep(1)
    # ATOM
    df_minute240_ATOM = pyupbit.get_ohlcv("KRW-ATOM", interval="minute240",count=120)
    time.sleep(1)
    # LOOM
    df_minute240_LOOM = pyupbit.get_ohlcv("KRW-LOOM", interval="minute240",count=120)
    time.sleep(1)
    # 1INCH
    df_minute240_1INCH = pyupbit.get_ohlcv("KRW-1INCH", interval="minute240",count=120)
    time.sleep(1)
    # ARK
    df_minute240_ARK = pyupbit.get_ohlcv("KRW-ARK", interval="minute240",count=120)
    time.sleep(1)
    # ZIL
    df_minute240_ZIL = pyupbit.get_ohlcv("KRW-ZIL", interval="minute240",count=120)
    time.sleep(1)
    # CRE
    df_minute240_CRE = pyupbit.get_ohlcv("KRW-CRE", interval="minute240",count=120)
    time.sleep(1)
    # MBL
    df_minute240_MBL = pyupbit.get_ohlcv("KRW-MBL", interval="minute240",count=120)
    time.sleep(1)
    # ALGO
    df_minute240_ALGO = pyupbit.get_ohlcv("KRW-ALGO", interval="minute240",count=120)
    time.sleep(1)
    # STORJ
    df_minute240_STORJ = pyupbit.get_ohlcv("KRW-STORJ", interval="minute240",count=120)
    time.sleep(1)
    # DKA
    df_minute240_DKA = pyupbit.get_ohlcv("KRW-DKA", interval="minute240",count=120)
    time.sleep(1)
    # XLM
    df_minute240_XLM = pyupbit.get_ohlcv("KRW-XLM", interval="minute240",count=120)
    time.sleep(1)
    # IOST
    df_minute240_IOST = pyupbit.get_ohlcv("KRW-IOST", interval="minute240",count=120)
    time.sleep(1)
    # ARDR
    df_minute240_ARDR = pyupbit.get_ohlcv("KRW-ARDR", interval="minute240",count=120)
    time.sleep(1)
    # CHZ
    df_minute240_CHZ = pyupbit.get_ohlcv("KRW-CHZ", interval="minute240",count=120)
    time.sleep(1)
    # MINA
    df_minute240_MINA = pyupbit.get_ohlcv("KRW-MINA", interval="minute240",count=120)
    time.sleep(1)
    # MANA
    df_minute240_MANA = pyupbit.get_ohlcv("KRW-MANA", interval="minute240",count=120)
    time.sleep(1)
    # KAVA
    df_minute240_KAVA = pyupbit.get_ohlcv("KRW-KAVA", interval="minute240",count=120)
    time.sleep(1)
    # MASK
    df_minute240_MASK = pyupbit.get_ohlcv("KRW-MASK", interval="minute240",count=120)
    time.sleep(1)
    # BLUR
    df_minute240_BLUR = pyupbit.get_ohlcv("KRW-BLUR", interval="minute240",count=120)
    time.sleep(1)
    # SNT
    df_minute240_SNT = pyupbit.get_ohlcv("KRW-SNT", interval="minute240",count=120)
    time.sleep(1)
    # POWR
    df_minute240_POWR = pyupbit.get_ohlcv("KRW-POWR", interval="minute240",count=120)
    time.sleep(1)
    # AXS
    df_minute240_AXS = pyupbit.get_ohlcv("KRW-AXS", interval="minute240",count=120)
    time.sleep(1)
    # DOT
    df_minute240_DOT = pyupbit.get_ohlcv("KRW-DOT", interval="minute240",count=120)
    time.sleep(1)
    # MTL
    df_minute240_MTL = pyupbit.get_ohlcv("KRW-MTL", interval="minute240",count=120)
    time.sleep(1)
    # ONT
    df_minute240_ONT = pyupbit.get_ohlcv("KRW-ONT", interval="minute240",count=120)
    time.sleep(1)
    # GLM
    df_minute240_GLM = pyupbit.get_ohlcv("KRW-GLM", interval="minute240",count=120)
    time.sleep(1)
    # MATIC
    df_minute240_MATIC = pyupbit.get_ohlcv("KRW-MATIC", interval="minute240",count=120)
    time.sleep(1)
    # BSV
    df_minute240_BSV = pyupbit.get_ohlcv("KRW-BSV", interval="minute240",count=120)
    time.sleep(1)
    # EOS
    df_minute240_EOS = pyupbit.get_ohlcv("KRW-EOS", interval="minute240",count=120)
    time.sleep(1)
    # MLK
    df_minute240_MLK = pyupbit.get_ohlcv("KRW-MLK", interval="minute240",count=120)
    time.sleep(1)
    # THETA
    df_minute240_THETA = pyupbit.get_ohlcv("KRW-THETA", interval="minute240",count=120)
    time.sleep(1)
    # TRX
    df_minute240_TRX = pyupbit.get_ohlcv("KRW-TRX", interval="minute240",count=120)
    time.sleep(1)
    # ASTR
    df_minute240_ASTR = pyupbit.get_ohlcv("KRW-ASTR", interval="minute240",count=120)
    time.sleep(1)
    # GAS
    df_minute240_GAS = pyupbit.get_ohlcv("KRW-GAS", interval="minute240",count=120)
    time.sleep(1)
    # WAVES
    df_minute240_WAVES = pyupbit.get_ohlcv("KRW-WAVES", interval="minute240",count=120)
    time.sleep(1)
    # MNT
    df_minute240_MNT = pyupbit.get_ohlcv("KRW-MNT", interval="minute240",count=120)
    time.sleep(1)
    # VET
    df_minute240_VET = pyupbit.get_ohlcv("KRW-VET", interval="minute240",count=120)
    time.sleep(1)
    # QTUM
    df_minute240_QTUM = pyupbit.get_ohlcv("KRW-QTUM", interval="minute240",count=120)
    time.sleep(1)
    # PUNDIX
    df_minute240_PUNDIX = pyupbit.get_ohlcv("KRW-PUNDIX", interval="minute240",count=120)
    time.sleep(1)
    # NEO
    df_minute240_NEO = pyupbit.get_ohlcv("KRW-NEO", interval="minute240",count=120)
    time.sleep(1)
    # 
    
    
    

    # Add indicators to both dataframes    
    
    df_minute240_XEC = add_indicators_version3(df_minute240_XEC)
    df_minute240_CVC = add_indicators_version3(df_minute240_CVC)
    df_minute240_POLYX = add_indicators_version3(df_minute240_POLYX)
    df_minute240_T = add_indicators_version3(df_minute240_T)
    df_minute240_SHIB = add_indicators_version3(df_minute240_SHIB)
    df_minute240_BTC = add_indicators_version3(df_minute240_BTC)
    df_minute240_XRP = add_indicators_version3(df_minute240_XRP)
    df_minute240_DOGE = add_indicators_version3(df_minute240_DOGE)
    df_minute240_WAXP = add_indicators_version3(df_minute240_WAXP)
    df_minute240_CTC = add_indicators_version3(df_minute240_CTC)
    df_minute240_ANKR = add_indicators_version3(df_minute240_ANKR)
    df_minute240_AERGO = add_indicators_version3(df_minute240_AERGO)
    df_minute240_HIFI = add_indicators_version3(df_minute240_HIFI)
    df_minute240_SOL = add_indicators_version3(df_minute240_SOL)
    df_minute240_STMX = add_indicators_version3(df_minute240_STMX)
    df_minute240_ETH = add_indicators_version3(df_minute240_ETH)
    df_minute240_ID = add_indicators_version3(df_minute240_ID)
    df_minute240_NEAR = add_indicators_version3(df_minute240_NEAR)
    df_minute240_SC = add_indicators_version3(df_minute240_SC)
    df_minute240_BORA = add_indicators_version3(df_minute240_BORA)
    df_minute240_PYTH = add_indicators_version3(df_minute240_PYTH)
    df_minute240_LSK = add_indicators_version3(df_minute240_LSK)
    df_minute240_STX = add_indicators_version3(df_minute240_STX)
    df_minute240_ETC = add_indicators_version3(df_minute240_ETC)
    df_minute240_APT = add_indicators_version3(df_minute240_APT)
    df_minute240_MVL = add_indicators_version3(df_minute240_MVL)
    df_minute240_SXP = add_indicators_version3(df_minute240_SXP)
    df_minute240_AVAX = add_indicators_version3(df_minute240_AVAX) 
    df_minute240_BCH = add_indicators_version3(df_minute240_BCH)
    df_minute240_ICX = add_indicators_version3(df_minute240_ICX)
    df_minute240_SEI = add_indicators_version3(df_minute240_SEI)
    df_minute240_ONG = add_indicators_version3(df_minute240_ONG)
    df_minute240_BTG = add_indicators_version3(df_minute240_BTG)
    df_minute240_ORBS = add_indicators_version3(df_minute240_ORBS)
    df_minute240_ZRX = add_indicators_version3(df_minute240_ZRX)
    df_minute240_GMT = add_indicators_version3(df_minute240_GMT)
    df_minute240_HUNT = add_indicators_version3(df_minute240_HUNT)
    df_minute240_IOTA = add_indicators_version3(df_minute240_IOTA)
    df_minute240_IQ = add_indicators_version3(df_minute240_IQ)
    df_minute240_STRAX = add_indicators_version3(df_minute240_STRAX)
    df_minute240_CELO = add_indicators_version3(df_minute240_CELO)
    df_minute240_ARB = add_indicators_version3(df_minute240_ARB)
    df_minute240_BTT = add_indicators_version3(df_minute240_BTT)
    df_minute240_HBAR = add_indicators_version3(df_minute240_HBAR)
    df_minute240_LINK = add_indicators_version3(df_minute240_LINK)
    df_minute240_SAND = add_indicators_version3(df_minute240_SAND)
    df_minute240_GRT = add_indicators_version3(df_minute240_GRT)
    df_minute240_FLOW = add_indicators_version3(df_minute240_FLOW)
    df_minute240_ADA = add_indicators_version3(df_minute240_ADA)
    df_minute240_SUI = add_indicators_version3(df_minute240_SUI)

    ################################################################
    df_minute240_AQT = add_indicators_version3(df_minute240_AQT)
    df_minute240_CBK = add_indicators_version3(df_minute240_CBK)
    df_minute240_FCT2 = add_indicators_version3(df_minute240_FCT2)
    df_minute240_JST = add_indicators_version3(df_minute240_JST)
    df_minute240_UPP = add_indicators_version3(df_minute240_UPP)
    df_minute240_STRIKE = add_indicators_version3(df_minute240_STRIKE)
    df_minute240_MOC = add_indicators_version3(df_minute240_MOC)
    df_minute240_TFUEL = add_indicators_version3(df_minute240_TFUEL)
    df_minute240_TT = add_indicators_version3(df_minute240_TT)
    df_minute240_KNC = add_indicators_version3(df_minute240_KNC)
    df_minute240_CRO = add_indicators_version3(df_minute240_CRO)
    df_minute240_META = add_indicators_version3(df_minute240_META)
    df_minute240_ELF = add_indicators_version3(df_minute240_ELF)
    df_minute240_AHT = add_indicators_version3(df_minute240_AHT)
    df_minute240_BAT = add_indicators_version3(df_minute240_BAT)
    df_minute240_SBD = add_indicators_version3(df_minute240_SBD)
    df_minute240_MED = add_indicators_version3(df_minute240_MED)
    df_minute240_AAVE = add_indicators_version3(df_minute240_AAVE)
    df_minute240_XTZ = add_indicators_version3(df_minute240_XTZ)
    df_minute240_TON = add_indicators_version3(df_minute240_TON)

    ####################################################################33
    df_minute240_IMX = add_indicators_version3(df_minute240_IMX)
    df_minute240_HPO = add_indicators_version3(df_minute240_HPO)
    df_minute240_EGLD = add_indicators_version3(df_minute240_EGLD)
    df_minute240_HIVE = add_indicators_version3(df_minute240_HIVE)
    df_minute240_GRS = add_indicators_version3(df_minute240_GRS)
    df_minute240_QKC = add_indicators_version3(df_minute240_QKC)
    df_minute240_STPT = add_indicators_version3(df_minute240_STPT)
    df_minute240_XEM = add_indicators_version3(df_minute240_XEM)
    df_minute240_STEEM = add_indicators_version3(df_minute240_STEEM)
    df_minute240_ATOM = add_indicators_version3(df_minute240_ATOM)
    df_minute240_LOOM = add_indicators_version3(df_minute240_LOOM)
    df_minute240_1INCH = add_indicators_version3(df_minute240_1INCH)
    df_minute240_ARK = add_indicators_version3(df_minute240_ARK)
    df_minute240_ZIL = add_indicators_version3(df_minute240_ZIL)
    df_minute240_CRE = add_indicators_version3(df_minute240_CRE)
    df_minute240_MBL = add_indicators_version3(df_minute240_MBL)
    df_minute240_ALGO = add_indicators_version3(df_minute240_ALGO)
    df_minute240_STORJ = add_indicators_version3(df_minute240_STORJ)
    df_minute240_DKA = add_indicators_version3(df_minute240_DKA)
    df_minute240_XLM = add_indicators_version3(df_minute240_XLM)
    df_minute240_IOST = add_indicators_version3(df_minute240_IOST)
    df_minute240_ARDR = add_indicators_version3(df_minute240_ARDR)
    df_minute240_CHZ = add_indicators_version3(df_minute240_CHZ)
    df_minute240_MINA = add_indicators_version3(df_minute240_MINA)
    df_minute240_MANA = add_indicators_version3(df_minute240_MANA)
    df_minute240_KAVA = add_indicators_version3(df_minute240_KAVA)
    df_minute240_MASK = add_indicators_version3(df_minute240_MASK)
    df_minute240_BLUR = add_indicators_version3(df_minute240_BLUR)
    df_minute240_SNT = add_indicators_version3(df_minute240_SNT)
    df_minute240_POWR = add_indicators_version3(df_minute240_POWR)
    df_minute240_AXS = add_indicators_version3(df_minute240_AXS)
    df_minute240_DOT = add_indicators_version3(df_minute240_DOT)
    df_minute240_MTL = add_indicators_version3(df_minute240_MTL)
    df_minute240_ONT = add_indicators_version3(df_minute240_ONT)
    df_minute240_GLM = add_indicators_version3(df_minute240_GLM)
    df_minute240_MATIC = add_indicators_version3(df_minute240_MATIC)
    df_minute240_BSV = add_indicators_version3(df_minute240_BSV)
    df_minute240_EOS = add_indicators_version3(df_minute240_EOS)
    df_minute240_MLK = add_indicators_version3(df_minute240_MLK)
    df_minute240_THETA = add_indicators_version3(df_minute240_THETA)
    df_minute240_TRX = add_indicators_version3(df_minute240_TRX)
    df_minute240_ASTR = add_indicators_version3(df_minute240_ASTR)
    df_minute240_GAS = add_indicators_version3(df_minute240_GAS)
    df_minute240_WAVES = add_indicators_version3(df_minute240_WAVES)
    df_minute240_MNT = add_indicators_version3(df_minute240_MNT)
    df_minute240_VET = add_indicators_version3(df_minute240_VET)
    df_minute240_QTUM = add_indicators_version3(df_minute240_QTUM)
    df_minute240_PUNDIX = add_indicators_version3(df_minute240_PUNDIX)
    df_minute240_NEO = add_indicators_version3(df_minute240_NEO)
    



#############################################################################################################################
    df_minute240_XEC_tail = df_minute240_XEC.tail(n=1)
    df_minute240_CVC_tail = df_minute240_CVC.tail(n=1)
    df_minute240_POLYX_tail = df_minute240_POLYX.tail(n=1)
    df_minute240_T_tail = df_minute240_T.tail(n=1)
    df_minute240_SHIB_tail = df_minute240_SHIB.tail(n=1)
    df_minute240_BTC_tail = df_minute240_BTC.tail(n=1)
    df_minute240_XRP_tail = df_minute240_XRP.tail(n=1)
    df_minute240_DOGE_tail = df_minute240_DOGE.tail(n=1)
    df_minute240_WAXP_tail = df_minute240_WAXP.tail(n=1)
    df_minute240_CTC_tail = df_minute240_CTC.tail(n=1)
    df_minute240_ANKR_tail = df_minute240_ANKR.tail(n=1)
    df_minute240_AERGO_tail = df_minute240_AERGO.tail(n=1)
    df_minute240_HIFI_tail = df_minute240_HIFI.tail(n=1)
    df_minute240_SOL_tail = df_minute240_SOL.tail(n=1)
    df_minute240_STMX_tail = df_minute240_STMX.tail(n=1)
    df_minute240_ETH_tail = df_minute240_ETH.tail(n=1)
    df_minute240_ID_tail = df_minute240_ID.tail(n=1)
    df_minute240_NEAR_tail = df_minute240_NEAR.tail(n=1)
    df_minute240_SC_tail = df_minute240_SC.tail(n=1)
    df_minute240_BORA_tail = df_minute240_BORA.tail(n=1)
    df_minute240_PYTH_tail = df_minute240_PYTH.tail(n=1)
    df_minute240_LSK_tail = df_minute240_LSK.tail(n=1)
    df_minute240_STX_tail = df_minute240_STX.tail(n=1)
    df_minute240_ETC_tail = df_minute240_ETC.tail(n=1)
    df_minute240_APT_tail = df_minute240_APT.tail(n=1)
    df_minute240_MVL_tail = df_minute240_MVL.tail(n=1)
    df_minute240_SXP_tail = df_minute240_SXP.tail(n=1)
    df_minute240_AVAX_tail = df_minute240_AVAX.tail(n=1)
    df_minute240_BCH_tail = df_minute240_BCH.tail(n=1)
    df_minute240_ICX_tail = df_minute240_ICX.tail(n=1)
    df_minute240_SEI_tail = df_minute240_SEI.tail(n=1)
    df_minute240_ONG_tail = df_minute240_ONG.tail(n=1)
    df_minute240_BTG_tail = df_minute240_BTG.tail(n=1)
    df_minute240_ORBS_tail = df_minute240_ORBS.tail(n=1)
    df_minute240_ZRX_tail = df_minute240_ZRX.tail(n=1)
    df_minute240_GMT_tail = df_minute240_GMT.tail(n=1)
    df_minute240_HUNT_tail = df_minute240_HUNT.tail(n=1)
    df_minute240_IOTA_tail = df_minute240_IOTA.tail(n=1)
    df_minute240_IQ_tail = df_minute240_IQ.tail(n=1)
    df_minute240_STRAX_tail = df_minute240_STRAX.tail(n=1)
    df_minute240_CELO_tail = df_minute240_CELO.tail(n=1)
    df_minute240_ARB_tail = df_minute240_ARB.tail(n=1)
    df_minute240_BTT_tail = df_minute240_BTT.tail(n=1)
    df_minute240_HBAR_tail = df_minute240_HBAR.tail(n=1)
    df_minute240_LINK_tail = df_minute240_LINK.tail(n=1)
    df_minute240_SAND_tail = df_minute240_SAND.tail(n=1)
    df_minute240_GRT_tail = df_minute240_GRT.tail(n=1)
    df_minute240_FLOW_tail = df_minute240_FLOW.tail(n=1)
    df_minute240_ADA_tail = df_minute240_ADA.tail(n=1)
    df_minute240_SUI_tail = df_minute240_SUI.tail(n=1)

    ####################################################################################
    df_minute240_AQT_tail = df_minute240_AQT.tail(n=1)
    df_minute240_CBK_tail = df_minute240_CBK.tail(n=1)
    df_minute240_FCT2_tail = df_minute240_FCT2.tail(n=1)
    df_minute240_JST_tail = df_minute240_JST.tail(n=1)
    df_minute240_UPP_tail = df_minute240_UPP.tail(n=1)
    df_minute240_STRIKE_tail = df_minute240_STRIKE.tail(n=1)
    df_minute240_MOC_tail = df_minute240_MOC.tail(n=1)
    df_minute240_TFUEL_tail = df_minute240_TFUEL.tail(n=1)
    df_minute240_TT_tail = df_minute240_TT.tail(n=1)
    df_minute240_KNC_tail = df_minute240_KNC.tail(n=1)
    df_minute240_CRO_tail = df_minute240_CRO.tail(n=1)
    df_minute240_META_tail = df_minute240_META.tail(n=1)
    df_minute240_ELF_tail = df_minute240_ELF.tail(n=1)
    df_minute240_AHT_tail = df_minute240_AHT.tail(n=1)
    df_minute240_BAT_tail = df_minute240_BAT.tail(n=1)
    df_minute240_SBD_tail = df_minute240_SBD.tail(n=1)
    df_minute240_MED_tail = df_minute240_MED.tail(n=1)
    df_minute240_AAVE_tail = df_minute240_AAVE.tail(n=1)
    df_minute240_XTZ_tail = df_minute240_XTZ.tail(n=1)
    df_minute240_TON_tail = df_minute240_TON.tail(n=1)
    #####################################################333
    df_minute240_IMX_tail = df_minute240_IMX.tail(n=1)
    df_minute240_HPO_tail = df_minute240_HPO.tail(n=1)
    df_minute240_EGLD_tail = df_minute240_EGLD.tail(n=1)
    df_minute240_HIVE_tail = df_minute240_HIVE.tail(n=1)
    df_minute240_GRS_tail = df_minute240_GRS.tail(n=1)
    df_minute240_QKC_tail = df_minute240_QKC.tail(n=1)
    df_minute240_STPT_tail = df_minute240_STPT.tail(n=1)
    df_minute240_XEM_tail = df_minute240_XEM.tail(n=1)
    df_minute240_STEEM_tail = df_minute240_STEEM.tail(n=1)
    df_minute240_ATOM_tail = df_minute240_ATOM.tail(n=1)
    df_minute240_LOOM_tail = df_minute240_LOOM.tail(n=1)
    df_minute240_1INCH_tail = df_minute240_1INCH.tail(n=1)
    df_minute240_ARK_tail = df_minute240_ARK.tail(n=1)
    df_minute240_ZIL_tail = df_minute240_ZIL.tail(n=1)
    df_minute240_CRE_tail = df_minute240_CRE.tail(n=1)
    df_minute240_MBL_tail = df_minute240_MBL.tail(n=1)
    df_minute240_ALGO_tail = df_minute240_ALGO.tail(n=1)
    df_minute240_STORJ_tail = df_minute240_STORJ.tail(n=1)
    df_minute240_DKA_tail = df_minute240_DKA.tail(n=1)
    df_minute240_XLM_tail = df_minute240_XLM.tail(n=1)
    df_minute240_IOST_tail = df_minute240_IOST.tail(n=1)
    df_minute240_ARDR_tail = df_minute240_ARDR.tail(n=1)
    df_minute240_CHZ_tail = df_minute240_CHZ.tail(n=1)
    df_minute240_MINA_tail = df_minute240_MINA.tail(n=1)
    df_minute240_MANA_tail = df_minute240_MANA.tail(n=1)
    df_minute240_KAVA_tail = df_minute240_KAVA.tail(n=1)
    df_minute240_MASK_tail = df_minute240_MASK.tail(n=1)
    df_minute240_BLUR_tail = df_minute240_BLUR.tail(n=1)
    df_minute240_SNT_tail = df_minute240_SNT.tail(n=1)
    df_minute240_POWR_tail = df_minute240_POWR.tail(n=1)
    df_minute240_AXS_tail = df_minute240_AXS.tail(n=1)
    df_minute240_DOT_tail = df_minute240_DOT.tail(n=1)
    df_minute240_MTL_tail = df_minute240_MTL.tail(n=1)
    df_minute240_ONT_tail = df_minute240_ONT.tail(n=1)
    df_minute240_GLM_tail = df_minute240_GLM.tail(n=1)
    df_minute240_MATIC_tail = df_minute240_MATIC.tail(n=1)
    df_minute240_BSV_tail = df_minute240_BSV.tail(n=1)
    df_minute240_EOS_tail = df_minute240_EOS.tail(n=1)
    df_minute240_MLK_tail = df_minute240_MLK.tail(n=1)
    df_minute240_THETA_tail = df_minute240_THETA.tail(n=1)
    df_minute240_TRX_tail = df_minute240_TRX.tail(n=1)
    df_minute240_ASTR_tail = df_minute240_ASTR.tail(n=1)
    df_minute240_GAS_tail = df_minute240_GAS.tail(n=1)
    df_minute240_WAVES_tail = df_minute240_WAVES.tail(n=1)
    df_minute240_MNT_tail = df_minute240_MNT.tail(n=1)
    df_minute240_VET_tail = df_minute240_VET.tail(n=1)
    df_minute240_QTUM_tail = df_minute240_QTUM.tail(n=1)
    df_minute240_PUNDIX_tail = df_minute240_PUNDIX.tail(n=1)
    df_minute240_NEO_tail = df_minute240_NEO.tail(n=1)
    


########################################################################################################################
    


    
    combined_df = pd.concat([df_minute240_XEC_tail, df_minute240_CVC_tail,df_minute240_POLYX_tail,df_minute240_T_tail,
                             df_minute240_SHIB_tail,df_minute240_BTC_tail,df_minute240_XRP_tail, df_minute240_DOGE_tail,
                             df_minute240_WAXP_tail,df_minute240_CTC_tail,df_minute240_ANKR_tail,df_minute240_AERGO_tail,
                             df_minute240_HIFI_tail,df_minute240_SOL_tail, df_minute240_STMX_tail,df_minute240_ETH_tail,
                             df_minute240_ID_tail, df_minute240_NEAR_tail, df_minute240_SC_tail, df_minute240_BORA_tail,
                             df_minute240_PYTH_tail, df_minute240_LSK_tail, df_minute240_STX_tail, df_minute240_ETC_tail,
                             df_minute240_APT_tail, df_minute240_MVL_tail, df_minute240_SXP_tail, df_minute240_AVAX_tail,
                             df_minute240_BCH_tail, df_minute240_ICX_tail, df_minute240_SEI_tail, df_minute240_ONG_tail,
                             df_minute240_BTG_tail, df_minute240_ORBS_tail, df_minute240_ZRX_tail, df_minute240_GMT_tail,
                             df_minute240_HUNT_tail, df_minute240_IOTA_tail, df_minute240_IQ_tail, df_minute240_STRAX_tail,
                             df_minute240_CELO_tail, df_minute240_ARB_tail, df_minute240_BTT_tail, df_minute240_HBAR_tail,
                             df_minute240_LINK_tail, df_minute240_SAND_tail, df_minute240_GRT_tail, df_minute240_FLOW_tail,
                             df_minute240_ADA_tail, df_minute240_SUI_tail, df_minute240_AQT_tail, df_minute240_CBK_tail,
                             df_minute240_FCT2_tail, df_minute240_JST_tail, df_minute240_UPP_tail, df_minute240_STRIKE_tail,
                             df_minute240_MOC_tail, df_minute240_TFUEL_tail, df_minute240_TT_tail, df_minute240_KNC_tail,
                             df_minute240_CRO_tail, df_minute240_META_tail, df_minute240_ELF_tail, df_minute240_AHT_tail,
                             df_minute240_BAT_tail, df_minute240_SBD_tail, df_minute240_MED_tail, df_minute240_AAVE_tail,
                             df_minute240_XTZ_tail, df_minute240_TON_tail, df_minute240_IMX_tail, df_minute240_HPO_tail,
                             df_minute240_EGLD_tail, df_minute240_HIVE_tail, df_minute240_GRS_tail, df_minute240_QKC_tail,
                             df_minute240_STPT_tail, df_minute240_XEM_tail, df_minute240_STEEM_tail, df_minute240_ATOM_tail,
                             df_minute240_LOOM_tail, df_minute240_1INCH_tail, df_minute240_ARK_tail, df_minute240_ZIL_tail,
                             df_minute240_CRE_tail, df_minute240_MBL_tail, df_minute240_ALGO_tail, df_minute240_STORJ_tail,
                             df_minute240_DKA_tail, df_minute240_XLM_tail, df_minute240_IOST_tail, df_minute240_ARDR_tail,
                             df_minute240_CHZ_tail, df_minute240_MINA_tail, df_minute240_MANA_tail, df_minute240_KAVA_tail,
                             df_minute240_MASK_tail, df_minute240_BLUR_tail, df_minute240_SNT_tail, df_minute240_POWR_tail,
                             df_minute240_AXS_tail, df_minute240_DOT_tail, df_minute240_MTL_tail, df_minute240_ONT_tail,
                             df_minute240_GLM_tail, df_minute240_MATIC_tail, df_minute240_BSV_tail, df_minute240_EOS_tail,
                             df_minute240_MLK_tail, df_minute240_THETA_tail, df_minute240_TRX_tail, df_minute240_ASTR_tail,
                             df_minute240_GAS_tail, df_minute240_WAVES_tail, df_minute240_MNT_tail, df_minute240_VET_tail,
                             df_minute240_QTUM_tail, df_minute240_PUNDIX_tail, df_minute240_NEO_tail
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
                            "KRW-XTZ", "KRW-TON", "KRW-IMX", "KRW-HPO",
                            "KRW-EGLD", "KRW-HIVE", "KRW-GRS", "KRW-QKC",
                            "KRW-STPT", "KRW-XEM", "KRW-STEEM", "KRW-ATOM",
                            "KRW-LOOM", "KRW-1INCH", "KRW-ARK", "KRW-ZIL",
                            "KRW-CRE", "KRW-MBL", "KRW-ALGO", "KRW-STORJ",
                            "KRW-DKA", "KRW-XLM", "KRW-IOST", "KRW-ARDR",
                            "KRW-CHZ", "KRW-MINA", "KRW-MANA", "KRW-KAVA",
                            "KRW-MASK", "KRW-BLUR", "KRW-SNT", "KRW-POWR",
                            "KRW-AXS", "KRW-DOT", "KRW-MTL", "KRW-ONT",
                            "KRW-GLM", "KRW-MATIC", "KRW-BSV", "KRW-EOS",
                            "KRW-MLK", "KRW-THETA", "KRW-TRX", "KRW-ASTR",
                            "KRW-GAS", "KRW-WAVES", "KRW-MNT", "KRW-VET",
                            "KRW-QTUM", "KRW-PUNDIX", "KRW-NEO"
                            ])
    #
    combined_df = combined_df.dropna(how='any', axis=0)    
    #  SMA_5 > SMA_20    
    combined_df_sma_5_20 = combined_df[combined_df['SMA_5'] > combined_df['SMA_20']]
    combined_df_sma_5_60 =  combined_df_sma_5_20[combined_df_sma_5_20['SMA_5'] > combined_df_sma_5_20['SMA_60']]
    combined_df_sma_5_120 = combined_df_sma_5_60[combined_df_sma_5_60['SMA_5'] > combined_df_sma_5_60['SMA_120']]
    combined_df_sort = combined_df_sma_5_120[(combined_df_sma_5_120['EMA_10'] > combined_df_sma_5_120['SMA_10'])]
        
    # "The RSI_14 has dropped below 30, suggesting the cryptocurrency pair is currently undervalued and likely to experience a price rebound. This oversold condition presents a favorable buying opportunity, anticipating a corrective rally."})
    combined_df_RSI_7 = combined_df_sort[combined_df_sort['RSI_7'] < 40]
    if len(combined_df_RSI_7) != 0:
        combined_df_sort = combined_df_RSI_7

    combined_df_RSI_14 = combined_df_sort[combined_df_sort['RSI_14'] < 40]
    if len(combined_df_RSI_14) != 0:
        combined_df_sort = combined_df_RSI_14

    combined_df_RSI_21 = combined_df_sort[combined_df_sort['RSI_21'] < 40]
    if len(combined_df_RSI_21) != 0:
        combined_df_sort = combined_df_RSI_21    

    # The Chaikin Money Flow ("cmf") indicator has surged above 0

    combined_df_sort_cmf = combined_df_sort[combined_df_sort['cmf'] > 0]
    if len(combined_df_sort_cmf) != 0:
        combined_df_sort = combined_df_sort_cmf

    #"When the "SQZPRO_20_2.0_20_2_1.5_1" value is positive, it indicates that the Squeeze Pro indicator is positive, signifying a contraction in volatility between the Bollinger Bands and Keltner Channels. This suggests an imminent sharp price movement,
    combined_df_sort_SQZPRO_20_2 = combined_df_sort[combined_df_sort["SQZPRO_20_2.0_20_2_1.5_1"] > 0]
    if len(combined_df_sort_SQZPRO_20_2) != 0:
        combined_df_sort = combined_df_sort_SQZPRO_20_2
        

    #"When "SQZPRO_ON_WIDE" is indicated as 1, it signifies a squeeze occurring within a wide range of Keltner Channels, suggesting a significant change in volatility and typically indicating a moment of rapid price movement. 


    combined_df_sort_SQZPRO_ON_WIDE = combined_df_sort[combined_df_sort["SQZPRO_ON_WIDE"] == 1]
    if len(combined_df_sort_SQZPRO_ON_WIDE) != 0:
        combined_df_sort = combined_df_sort_SQZPRO_ON_WIDE

    #매수 타이밍:

    # Z-Score가 음수인 경우: 해당 자산이 평균보다 낮게 평가되어 있으므로 매수 타이밍일 수 있습니다.
    # 또는 Z-Score가 일정 임계값 이하인 경우에도 매수 타이밍일 수 있습니다. 이는 해당 자산이 과소평가되었을 가능성이 있기 때문입니다.
    combined_df_sort_ZS_30 = combined_df_sort[combined_df_sort["ZS_30"] < 0]
    if len(combined_df_sort_ZS_30) != 0:
        combined_df_sort = combined_df_sort_ZS_30

    # df["close"] > df["TOS_STDEVALL_30_LR"]
    # """
    # 매수 기회 시점:

    # a) 더 공격적인 전략:

    # df["close"] > df["TOS_STDEVALL_30_L_1"] 조건은 하단 밴드에 근접했을 때 매수를 신호할 수 있어 더 공격적인 전략입니다.
    # 하지만, 하락 후 바로 반등하지 않고 변동성이 지속될 수도 있어 위험성 또한 높습니다.
    # b) 더 안전한 전략:

    # df["close"] > df["TOS_STDEVALL_30_LR"] 조건은 LR 선을 넘어섰을 때 매수를 신호할 수 있어 더 안전한 전략입니다.
    # 하지만, 상승 기회를 일부 놓칠 수도 있습니다.
    # 3. 결론:

    # 어떤 조건을 사용할지는 투자 스타일과 위험 수용 태도에 따라 달라집니다.
    # 더 공격적인 투자를 원한다면 df["close"] > df["TOS_STDEVALL_30_L_1"]을 사용할 수 있습니다.
    # 보수적인 투자를 원한다면 df["close"] > df["TOS_STDEVALL_30_LR"]을 사용할 수 있습니다.
    # """
    combined_df_sort_TOS_STDEVALL_30_LR = combined_df_sort[ combined_df_sort["close"] > combined_df_sort["TOS_STDEVALL_30_LR"]]
    if len(combined_df_sort_TOS_STDEVALL_30_LR) != 0:
        combined_df_sort = combined_df_sort_TOS_STDEVALL_30_LR
        
    ###
    # Aroon Up이 Down을 상향 돌파하면 주가의 고점이 저점보다 가까이 위치한 상태가 된 것이다. 따라서 주가가 상승 추세에 있는 것으로 해석할 수 있다. 
    # 반대로 Aroon Down이 Up을 상향 돌파하면 주가의 저점이 고점보다 가까이 위치한 것으로 주가가 하락 추세에 있는 것으로 해석할 수 있다. 
    #그러므로 Aroon Up이 Down을 상향 돌파하면 주가가 상승 추세로 전환될 것으로 예상해 매수하고 
    # Aroon Down이 Up을 상향 돌파하면 주가가 하락 추세로 전환될 것으로 예상해 매도하는 전략을 사용할 수 있다.
    # A common buying condition using the Aroon indicator is when Aroon Up crosses above Aroon Down
    #  Assuming 'aroon_up' and 'aroon_down' are the Aroon Up and Aroon Down indicators respectively
    combined_df_sort['aroon_cross'] = np.where(combined_df_sort['AROONU_14'] > combined_df_sort['AROOND_14'], 1, 0)

    # Filter the DataFrame for the buying condition
    combined_df_sort_aroon_cross = combined_df_sort[combined_df_sort['aroon_cross'] == 1]
    if len(combined_df_sort_aroon_cross) != 0:
        combined_df_sort = combined_df_sort_aroon_cross
        
    ## Chande Momentum Oscillator (CMO)
    #  CMO 값이 -50 이하일 경우, 주식이 과매도 상태에 있으므로 매수 기회로 간주될 수 있습니다
    # 조건: CMO_14 값이 -50 이하인 경우
    buy_condition = combined_df_sort["CMO_14"] <= -50


    buy_condition_CMO = combined_df_sort[buy_condition]
    if len(buy_condition_CMO) != 0:
        combined_df_sort = buy_condition_CMO
        
    # RSO
    combined_df_sort_ROC_10 = combined_df_sort[combined_df_sort['ROC_10'] > 0]
    if len(combined_df_sort_ROC_10) != 0:
        combined_df_sort = combined_df_sort_ROC_10
        
    # WILLR 지표를 사용한 매수 조건: WILLR 값이 -20 이하인 경우 (length=14)
    combined_df_sort_WILLR = combined_df_sort[combined_df_sort['WILLR_14'] <= -20]
    if len(combined_df_sort_WILLR) != 0:
        combined_df_sort = combined_df_sort_WILLR
        
        """
        # MACD 지표를 사용한 매수 조건: MACD line이 signal line을 상향 돌파한 경우
    buy_condition_MACD = combined_df_sort["MACD"] > combined_df_sort["MACD_Signal"]

    buy_condition_MACD_df = combined_df_sort[buy_condition_MACD]
    if len(buy_condition_MACD_df) != 0:
        combined_df_sort = buy_condition_MACD_df

    # 볼린저 밴드를 사용한 매수 조건: 현재 종가가 lower band 아래에 있는 경우
    combined_df_sort_v2 = combined_df_sort[combined_df_sort['close'] < combined_df_sort['Lower_Band']]

        """

    combined_df_sort_v2 = combined_df_sort[(combined_df_sort['EMA_5'] > combined_df_sort['SMA_5'])]
    # when the current close price falls below the lower Donchian Channel (DCL_20_20), 
    combined_df_DCL_20_20 = combined_df_sort_v2[combined_df_sort_v2['close'] < combined_df_sort_v2['DCL_20_20']]

    if len(combined_df_DCL_20_20) != 0:
        sorted_value_df = combined_df_DCL_20_20.sort_values(by='value', ascending=True)
    else:
        if len(combined_df_sort_v2) != 0:
                sorted_value_df = combined_df_sort_v2.sort_values(by='value', ascending=True)
        else:
            if len(combined_df_sort) != 0:
                sorted_value_df = combined_df_sort.sort_values(by='value', ascending=True)
            else:
                if len(combined_df_sma_5_120) != 0:
                    sorted_value_df = combined_df_sma_5_120.sort_values(by='value', ascending=True)
                else:
                    if len(combined_df_sma_5_60) != 0:
                        sorted_value_df = combined_df_sma_5_60.sort_values(by='value', ascending=True)
                    else:
                        sorted_value_df = combined_df_sma_5_20.sort_values(by='value', ascending=True)

    
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
    instructions_path = "autotrade_version9.md"
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
            fear_and_greed = fetch_fear_and_greed_index(limit=7)
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
            df_minute240_index_value = pyupbit.get_ohlcv(index_value, interval="minute240",count=120)
            df_minute240_index_value = add_indicators_version3(df_minute240_index_value)
            df_minute240_index_value_tail = df_minute240_index_value.tail(n=1)
            sell_data = df_minute240_index_value_tail.to_json(orient='split')
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
      
    # 13:00에 실행되는 스케줄 설정
    schedule.every().day.at("13:00").do(make_decision_and_execute_schedule)

    # 17:00에 실행되는 스케줄 설정
    schedule.every().day.at("17:00").do(make_decision_and_execute_schedule)
    schedule.every().day.at("21:00").do(make_decision_and_execute_schedule)
    schedule.every().day.at("01:00").do(make_decision_and_execute_schedule)

    schedule.every().day.at("05:00").do(make_decision_and_execute_schedule)
    schedule.every().day.at("09:00").do(make_decision_and_execute_schedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


# #1초마다 make_decision_and_execute을 동작시키다가 "22:21"이 되면 프로그램 종료
# schedule.every(1).seconds.do(make_decision_and_execute)
# schedule.every().day.at("22:21").do(exit)  
        
"""
What Is the Crypto Fear and Greed Index? 

0-24: Extreme Fear (indicating potential buying opportunities as market participants might be too worried), Extreme Fear can lead to stocks becoming oversold or undervalued, which is a buy indicator.

25-49: Fear (suggesting caution among investors)

50: Neutral (market sentiment is balanced between fear and greed)

51-74: Greed (implying increasing market confidence and investment risk)

75-100: Extreme Greed (a warning signal that the market may be overvalued and due for a correction), Extreme Greed can result in stocks becoming overbought or overvalued, which can trigger mass selling.


"""