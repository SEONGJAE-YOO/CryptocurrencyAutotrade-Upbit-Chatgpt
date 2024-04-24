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
from technical_analysis import add_indicators_version4, trix_buy_signal
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
    df_minute60_XEC = pyupbit.get_ohlcv("KRW-XEC", interval="minute60",count=120)
    time.sleep(1)
    # CVC
    df_minute60_CVC = pyupbit.get_ohlcv("KRW-CVC", interval="minute60",count=120)
    time.sleep(1)
    # POLYX
    df_minute60_POLYX = pyupbit.get_ohlcv("KRW-POLYX", interval="minute60",count=120)
    time.sleep(1)
    # T
    df_minute60_T = pyupbit.get_ohlcv("KRW-T", interval="minute60",count=120)
    time.sleep(1)
    # SHIB
    df_minute60_SHIB = pyupbit.get_ohlcv("KRW-SHIB", interval="minute60",count=120)
    time.sleep(1)
    # BTC
    df_minute60_BTC = pyupbit.get_ohlcv("KRW-BTC", interval="minute60",count=120)
    time.sleep(1)
    #XRP
    df_minute60_XRP = pyupbit.get_ohlcv("KRW-XRP", interval="minute60",count=120)
    time.sleep(1)
    # DOGE
    df_minute60_DOGE = pyupbit.get_ohlcv("KRW-DOGE", interval="minute60",count=120)
    time.sleep(1)
    # WAXP
    df_minute60_WAXP = pyupbit.get_ohlcv("KRW-WAXP", interval="minute60",count=120)
    time.sleep(1)
    #CTC
    df_minute60_CTC = pyupbit.get_ohlcv("KRW-CTC", interval="minute60",count=120)
    time.sleep(1)
    #ANKR
    df_minute60_ANKR = pyupbit.get_ohlcv("KRW-ANKR", interval="minute60",count=120)
    time.sleep(1)
    # AERGO
    df_minute60_AERGO = pyupbit.get_ohlcv("KRW-AERGO", interval="minute60",count=120)
    time.sleep(1)
    # HIFI
    df_minute60_HIFI = pyupbit.get_ohlcv("KRW-HIFI", interval="minute60",count=120)
    time.sleep(1)
    # SOL
    df_minute60_SOL = pyupbit.get_ohlcv("KRW-SOL", interval="minute60",count=120)
    time.sleep(1)
    # STMX
    df_minute60_STMX = pyupbit.get_ohlcv("KRW-STMX", interval="minute60",count=120)
    time.sleep(1)
    # ETH
    df_minute60_ETH = pyupbit.get_ohlcv("KRW-ETH", interval="minute60",count=120)
    time.sleep(1)
    # ID
    df_minute60_ID = pyupbit.get_ohlcv("KRW-ID", interval="minute60",count=120)
    time.sleep(1)
    # NEAR
    df_minute60_NEAR = pyupbit.get_ohlcv("KRW-NEAR", interval="minute60",count=120)
    time.sleep(1)
    # SC
    df_minute60_SC = pyupbit.get_ohlcv("KRW-SC", interval="minute60",count=120)
    time.sleep(1)
    # BORA
    df_minute60_BORA = pyupbit.get_ohlcv("KRW-BORA", interval="minute60",count=120)
    time.sleep(1)
    # PYTH
    df_minute60_PYTH = pyupbit.get_ohlcv("KRW-PYTH", interval="minute60",count=120)
    time.sleep(1)
    # LSK
    df_minute60_LSK = pyupbit.get_ohlcv("KRW-LSK", interval="minute60",count=120)
    time.sleep(1)
    # STX
    df_minute60_STX = pyupbit.get_ohlcv("KRW-STX", interval="minute60",count=120)
    time.sleep(1)
    # ETC
    df_minute60_ETC = pyupbit.get_ohlcv("KRW-ETC", interval="minute60",count=120)
    time.sleep(1)
    # APT
    df_minute60_APT = pyupbit.get_ohlcv("KRW-APT", interval="minute60",count=120)
    time.sleep(1)
    # MVL
    df_minute60_MVL = pyupbit.get_ohlcv("KRW-MVL", interval="minute60",count=120)
    time.sleep(1)
    # SXP
    df_minute60_SXP = pyupbit.get_ohlcv("KRW-SXP", interval="minute60",count=120)
    time.sleep(1)
    # AVAX
    df_minute60_AVAX = pyupbit.get_ohlcv("KRW-AVAX", interval="minute60",count=120)
    time.sleep(1)
    # BCH
    df_minute60_BCH = pyupbit.get_ohlcv("KRW-BCH", interval="minute60",count=120)
    time.sleep(1)
    # ICX
    df_minute60_ICX = pyupbit.get_ohlcv("KRW-ICX", interval="minute60",count=120)
    time.sleep(1)
    # SEI
    df_minute60_SEI = pyupbit.get_ohlcv("KRW-SEI", interval="minute60",count=120)
    time.sleep(1)
    # ONG
    df_minute60_ONG = pyupbit.get_ohlcv("KRW-ONG", interval="minute60",count=120)
    time.sleep(1)
    # BTG
    df_minute60_BTG = pyupbit.get_ohlcv("KRW-BTG", interval="minute60",count=120)
    time.sleep(1)
    # ORBS
    df_minute60_ORBS = pyupbit.get_ohlcv("KRW-ORBS", interval="minute60",count=120)
    time.sleep(1)
    # ZRX
    df_minute60_ZRX = pyupbit.get_ohlcv("KRW-ZRX", interval="minute60",count=120)
    time.sleep(1)
    # GMT
    df_minute60_GMT = pyupbit.get_ohlcv("KRW-GMT", interval="minute60",count=120)
    time.sleep(1)
    # HUNT
    df_minute60_HUNT = pyupbit.get_ohlcv("KRW-HUNT", interval="minute60",count=120)
    time.sleep(1)
    # IOTA
    df_minute60_IOTA = pyupbit.get_ohlcv("KRW-IOTA", interval="minute60",count=120)
    time.sleep(1)
    # IQ
    df_minute60_IQ = pyupbit.get_ohlcv("KRW-IQ", interval="minute60",count=120)
    time.sleep(1)
    # STRAX
    df_minute60_STRAX = pyupbit.get_ohlcv("KRW-STRAX", interval="minute60",count=120)
    time.sleep(1)
    # CELO
    df_minute60_CELO = pyupbit.get_ohlcv("KRW-CELO", interval="minute60",count=120)
    time.sleep(1)  
    # ARB
    df_minute60_ARB = pyupbit.get_ohlcv("KRW-ARB", interval="minute60",count=120)
    time.sleep(1)
    # BTT
    df_minute60_BTT = pyupbit.get_ohlcv("KRW-BTT", interval="minute60",count=120)
    time.sleep(1)
    # HBAR
    df_minute60_HBAR = pyupbit.get_ohlcv("KRW-HBAR", interval="minute60",count=120)
    time.sleep(1)
    # LINK
    df_minute60_LINK = pyupbit.get_ohlcv("KRW-LINK", interval="minute60",count=120)
    time.sleep(1)
    # SAND
    df_minute60_SAND = pyupbit.get_ohlcv("KRW-SAND", interval="minute60",count=120)
    time.sleep(1)
    # GRT
    df_minute60_GRT = pyupbit.get_ohlcv("KRW-GRT", interval="minute60",count=120)
    time.sleep(1)
    # FLOW
    df_minute60_FLOW = pyupbit.get_ohlcv("KRW-FLOW", interval="minute60",count=120)
    time.sleep(1)
    # ADA
    df_minute60_ADA = pyupbit.get_ohlcv("KRW-ADA", interval="minute60",count=120)
    time.sleep(1)
    # SUI
    df_minute60_SUI = pyupbit.get_ohlcv("KRW-SUI", interval="minute60",count=120)
    time.sleep(1)
    # AQT
    df_minute60_AQT = pyupbit.get_ohlcv("KRW-AQT", interval="minute60",count=120)
    time.sleep(1)
    # CBK
    df_minute60_CBK = pyupbit.get_ohlcv("KRW-CBK", interval="minute60",count=120)
    time.sleep(1)
    # FCT2
    df_minute60_FCT2 = pyupbit.get_ohlcv("KRW-FCT2", interval="minute60",count=120)
    time.sleep(1)
    # JST
    df_minute60_JST = pyupbit.get_ohlcv("KRW-JST", interval="minute60",count=120)
    time.sleep(1)
    # UPP
    df_minute60_UPP = pyupbit.get_ohlcv("KRW-UPP", interval="minute60",count=120)
    time.sleep(1)
    # STRIKE
    df_minute60_STRIKE = pyupbit.get_ohlcv("KRW-STRIKE", interval="minute60",count=120)
    time.sleep(1)
    # MOC
    df_minute60_MOC = pyupbit.get_ohlcv("KRW-MOC", interval="minute60",count=120)
    time.sleep(1)
    # TFUEL
    df_minute60_TFUEL = pyupbit.get_ohlcv("KRW-TFUEL", interval="minute60",count=120)
    time.sleep(1)
    # TT
    df_minute60_TT = pyupbit.get_ohlcv("KRW-TT", interval="minute60",count=120)
    time.sleep(1)
    # KNC
    df_minute60_KNC = pyupbit.get_ohlcv("KRW-KNC", interval="minute60",count=120)
    time.sleep(1)
    # CRO
    df_minute60_CRO = pyupbit.get_ohlcv("KRW-CRO", interval="minute60",count=120)
    time.sleep(1)
    # META
    df_minute60_META = pyupbit.get_ohlcv("KRW-META", interval="minute60",count=120)
    time.sleep(1)
    # ELF
    df_minute60_ELF = pyupbit.get_ohlcv("KRW-ELF", interval="minute60",count=120)
    time.sleep(1)
    # AHT
    df_minute60_AHT = pyupbit.get_ohlcv("KRW-AHT", interval="minute60",count=120)
    time.sleep(1)
    # BAT
    df_minute60_BAT = pyupbit.get_ohlcv("KRW-BAT", interval="minute60",count=120)
    time.sleep(1)
    # SBD
    df_minute60_SBD = pyupbit.get_ohlcv("KRW-SBD", interval="minute60",count=120)
    time.sleep(1)
    # MED
    df_minute60_MED = pyupbit.get_ohlcv("KRW-MED", interval="minute60",count=120)
    time.sleep(1)
    # AAVE
    df_minute60_AAVE = pyupbit.get_ohlcv("KRW-AAVE", interval="minute60",count=120)
    time.sleep(1)
    # XTZ
    df_minute60_XTZ = pyupbit.get_ohlcv("KRW-XTZ", interval="minute60",count=120)
    time.sleep(1)  
    # TON
    df_minute60_TON = pyupbit.get_ohlcv("KRW-TON", interval="minute60",count=120)
    time.sleep(1)
    
    #############################3
    # IMX
    df_minute60_IMX = pyupbit.get_ohlcv("KRW-IMX", interval="minute60",count=120)
    time.sleep(1)
    # HPO
    df_minute60_HPO = pyupbit.get_ohlcv("KRW-HPO", interval="minute60",count=120)
    time.sleep(1)
    # EGLD
    df_minute60_EGLD = pyupbit.get_ohlcv("KRW-EGLD", interval="minute60",count=120)
    time.sleep(1)
    # HIVE
    df_minute60_HIVE = pyupbit.get_ohlcv("KRW-HIVE", interval="minute60",count=120)
    time.sleep(1)
    # GRS
    df_minute60_GRS = pyupbit.get_ohlcv("KRW-GRS", interval="minute60",count=120)
    time.sleep(1)
    # QKC
    df_minute60_QKC = pyupbit.get_ohlcv("KRW-QKC", interval="minute60",count=120)
    time.sleep(1)
    # STPT
    df_minute60_STPT = pyupbit.get_ohlcv("KRW-STPT", interval="minute60",count=120)
    time.sleep(1)
    # XEM
    df_minute60_XEM = pyupbit.get_ohlcv("KRW-XEM", interval="minute60",count=120)
    time.sleep(1)
    # STEEM
    df_minute60_STEEM = pyupbit.get_ohlcv("KRW-STEEM", interval="minute60",count=120)
    time.sleep(1)
    # ATOM
    df_minute60_ATOM = pyupbit.get_ohlcv("KRW-ATOM", interval="minute60",count=120)
    time.sleep(1)
    # LOOM
    df_minute60_LOOM = pyupbit.get_ohlcv("KRW-LOOM", interval="minute60",count=120)
    time.sleep(1)
    # 1INCH
    df_minute60_1INCH = pyupbit.get_ohlcv("KRW-1INCH", interval="minute60",count=120)
    time.sleep(1)
    # ARK
    df_minute60_ARK = pyupbit.get_ohlcv("KRW-ARK", interval="minute60",count=120)
    time.sleep(1)
    # ZIL
    df_minute60_ZIL = pyupbit.get_ohlcv("KRW-ZIL", interval="minute60",count=120)
    time.sleep(1)
    # CRE
    df_minute60_CRE = pyupbit.get_ohlcv("KRW-CRE", interval="minute60",count=120)
    time.sleep(1)
    # MBL
    df_minute60_MBL = pyupbit.get_ohlcv("KRW-MBL", interval="minute60",count=120)
    time.sleep(1)
    # ALGO
    df_minute60_ALGO = pyupbit.get_ohlcv("KRW-ALGO", interval="minute60",count=120)
    time.sleep(1)
    # STORJ
    df_minute60_STORJ = pyupbit.get_ohlcv("KRW-STORJ", interval="minute60",count=120)
    time.sleep(1)
    # DKA
    df_minute60_DKA = pyupbit.get_ohlcv("KRW-DKA", interval="minute60",count=120)
    time.sleep(1)
    # XLM
    df_minute60_XLM = pyupbit.get_ohlcv("KRW-XLM", interval="minute60",count=120)
    time.sleep(1)
    # IOST
    df_minute60_IOST = pyupbit.get_ohlcv("KRW-IOST", interval="minute60",count=120)
    time.sleep(1)
    # ARDR
    df_minute60_ARDR = pyupbit.get_ohlcv("KRW-ARDR", interval="minute60",count=120)
    time.sleep(1)
    # CHZ
    df_minute60_CHZ = pyupbit.get_ohlcv("KRW-CHZ", interval="minute60",count=120)
    time.sleep(1)
    # MINA
    df_minute60_MINA = pyupbit.get_ohlcv("KRW-MINA", interval="minute60",count=120)
    time.sleep(1)
    # MANA
    df_minute60_MANA = pyupbit.get_ohlcv("KRW-MANA", interval="minute60",count=120)
    time.sleep(1)
    # KAVA
    df_minute60_KAVA = pyupbit.get_ohlcv("KRW-KAVA", interval="minute60",count=120)
    time.sleep(1)
    # MASK
    df_minute60_MASK = pyupbit.get_ohlcv("KRW-MASK", interval="minute60",count=120)
    time.sleep(1)
    # BLUR
    df_minute60_BLUR = pyupbit.get_ohlcv("KRW-BLUR", interval="minute60",count=120)
    time.sleep(1)
    # SNT
    df_minute60_SNT = pyupbit.get_ohlcv("KRW-SNT", interval="minute60",count=120)
    time.sleep(1)
    # POWR
    df_minute60_POWR = pyupbit.get_ohlcv("KRW-POWR", interval="minute60",count=120)
    time.sleep(1)
    # AXS
    df_minute60_AXS = pyupbit.get_ohlcv("KRW-AXS", interval="minute60",count=120)
    time.sleep(1)
    # DOT
    df_minute60_DOT = pyupbit.get_ohlcv("KRW-DOT", interval="minute60",count=120)
    time.sleep(1)
    # MTL
    df_minute60_MTL = pyupbit.get_ohlcv("KRW-MTL", interval="minute60",count=120)
    time.sleep(1)
    # ONT
    df_minute60_ONT = pyupbit.get_ohlcv("KRW-ONT", interval="minute60",count=120)
    time.sleep(1)
    # GLM
    df_minute60_GLM = pyupbit.get_ohlcv("KRW-GLM", interval="minute60",count=120)
    time.sleep(1)
    # MATIC
    df_minute60_MATIC = pyupbit.get_ohlcv("KRW-MATIC", interval="minute60",count=120)
    time.sleep(1)
    # BSV
    df_minute60_BSV = pyupbit.get_ohlcv("KRW-BSV", interval="minute60",count=120)
    time.sleep(1)
    # EOS
    df_minute60_EOS = pyupbit.get_ohlcv("KRW-EOS", interval="minute60",count=120)
    time.sleep(1)
    # MLK
    df_minute60_MLK = pyupbit.get_ohlcv("KRW-MLK", interval="minute60",count=120)
    time.sleep(1)
    # THETA
    df_minute60_THETA = pyupbit.get_ohlcv("KRW-THETA", interval="minute60",count=120)
    time.sleep(1)
    # TRX
    df_minute60_TRX = pyupbit.get_ohlcv("KRW-TRX", interval="minute60",count=120)
    time.sleep(1)
    # ASTR
    df_minute60_ASTR = pyupbit.get_ohlcv("KRW-ASTR", interval="minute60",count=120)
    time.sleep(1)
    # GAS
    df_minute60_GAS = pyupbit.get_ohlcv("KRW-GAS", interval="minute60",count=120)
    time.sleep(1)
    # WAVES
    df_minute60_WAVES = pyupbit.get_ohlcv("KRW-WAVES", interval="minute60",count=120)
    time.sleep(1)
    # MNT
    df_minute60_MNT = pyupbit.get_ohlcv("KRW-MNT", interval="minute60",count=120)
    time.sleep(1)
    # VET
    df_minute60_VET = pyupbit.get_ohlcv("KRW-VET", interval="minute60",count=120)
    time.sleep(1)
    # QTUM
    df_minute60_QTUM = pyupbit.get_ohlcv("KRW-QTUM", interval="minute60",count=120)
    time.sleep(1)
    # PUNDIX
    df_minute60_PUNDIX = pyupbit.get_ohlcv("KRW-PUNDIX", interval="minute60",count=120)
    time.sleep(1)
    # NEO
    df_minute60_NEO = pyupbit.get_ohlcv("KRW-NEO", interval="minute60",count=120)
    time.sleep(1)
    # 
    
    
    

    # Add indicators to both dataframes    
    
    df_minute60_XEC = add_indicators_version4(df_minute60_XEC)
    df_minute60_CVC = add_indicators_version4(df_minute60_CVC)
    df_minute60_POLYX = add_indicators_version4(df_minute60_POLYX)
    df_minute60_T = add_indicators_version4(df_minute60_T)
    df_minute60_SHIB = add_indicators_version4(df_minute60_SHIB)
    df_minute60_BTC = add_indicators_version4(df_minute60_BTC)
    df_minute60_XRP = add_indicators_version4(df_minute60_XRP)
    df_minute60_DOGE = add_indicators_version4(df_minute60_DOGE)
    df_minute60_WAXP = add_indicators_version4(df_minute60_WAXP)
    df_minute60_CTC = add_indicators_version4(df_minute60_CTC)
    df_minute60_ANKR = add_indicators_version4(df_minute60_ANKR)
    df_minute60_AERGO = add_indicators_version4(df_minute60_AERGO)
    df_minute60_HIFI = add_indicators_version4(df_minute60_HIFI)
    df_minute60_SOL = add_indicators_version4(df_minute60_SOL)
    df_minute60_STMX = add_indicators_version4(df_minute60_STMX)
    df_minute60_ETH = add_indicators_version4(df_minute60_ETH)
    df_minute60_ID = add_indicators_version4(df_minute60_ID)
    df_minute60_NEAR = add_indicators_version4(df_minute60_NEAR)
    df_minute60_SC = add_indicators_version4(df_minute60_SC)
    df_minute60_BORA = add_indicators_version4(df_minute60_BORA)
    df_minute60_PYTH = add_indicators_version4(df_minute60_PYTH)
    df_minute60_LSK = add_indicators_version4(df_minute60_LSK)
    df_minute60_STX = add_indicators_version4(df_minute60_STX)
    df_minute60_ETC = add_indicators_version4(df_minute60_ETC)
    df_minute60_APT = add_indicators_version4(df_minute60_APT)
    df_minute60_MVL = add_indicators_version4(df_minute60_MVL)
    df_minute60_SXP = add_indicators_version4(df_minute60_SXP)
    df_minute60_AVAX = add_indicators_version4(df_minute60_AVAX) 
    df_minute60_BCH = add_indicators_version4(df_minute60_BCH)
    df_minute60_ICX = add_indicators_version4(df_minute60_ICX)
    df_minute60_SEI = add_indicators_version4(df_minute60_SEI)
    df_minute60_ONG = add_indicators_version4(df_minute60_ONG)
    df_minute60_BTG = add_indicators_version4(df_minute60_BTG)
    df_minute60_ORBS = add_indicators_version4(df_minute60_ORBS)
    df_minute60_ZRX = add_indicators_version4(df_minute60_ZRX)
    df_minute60_GMT = add_indicators_version4(df_minute60_GMT)
    df_minute60_HUNT = add_indicators_version4(df_minute60_HUNT)
    df_minute60_IOTA = add_indicators_version4(df_minute60_IOTA)
    df_minute60_IQ = add_indicators_version4(df_minute60_IQ)
    df_minute60_STRAX = add_indicators_version4(df_minute60_STRAX)
    df_minute60_CELO = add_indicators_version4(df_minute60_CELO)
    df_minute60_ARB = add_indicators_version4(df_minute60_ARB)
    df_minute60_BTT = add_indicators_version4(df_minute60_BTT)
    df_minute60_HBAR = add_indicators_version4(df_minute60_HBAR)
    df_minute60_LINK = add_indicators_version4(df_minute60_LINK)
    df_minute60_SAND = add_indicators_version4(df_minute60_SAND)
    df_minute60_GRT = add_indicators_version4(df_minute60_GRT)
    df_minute60_FLOW = add_indicators_version4(df_minute60_FLOW)
    df_minute60_ADA = add_indicators_version4(df_minute60_ADA)
    df_minute60_SUI = add_indicators_version4(df_minute60_SUI)

    ################################################################
    df_minute60_AQT = add_indicators_version4(df_minute60_AQT)
    df_minute60_CBK = add_indicators_version4(df_minute60_CBK)
    df_minute60_FCT2 = add_indicators_version4(df_minute60_FCT2)
    df_minute60_JST = add_indicators_version4(df_minute60_JST)
    df_minute60_UPP = add_indicators_version4(df_minute60_UPP)
    df_minute60_STRIKE = add_indicators_version4(df_minute60_STRIKE)
    df_minute60_MOC = add_indicators_version4(df_minute60_MOC)
    df_minute60_TFUEL = add_indicators_version4(df_minute60_TFUEL)
    df_minute60_TT = add_indicators_version4(df_minute60_TT)
    df_minute60_KNC = add_indicators_version4(df_minute60_KNC)
    df_minute60_CRO = add_indicators_version4(df_minute60_CRO)
    df_minute60_META = add_indicators_version4(df_minute60_META)
    df_minute60_ELF = add_indicators_version4(df_minute60_ELF)
    df_minute60_AHT = add_indicators_version4(df_minute60_AHT)
    df_minute60_BAT = add_indicators_version4(df_minute60_BAT)
    df_minute60_SBD = add_indicators_version4(df_minute60_SBD)
    df_minute60_MED = add_indicators_version4(df_minute60_MED)
    df_minute60_AAVE = add_indicators_version4(df_minute60_AAVE)
    df_minute60_XTZ = add_indicators_version4(df_minute60_XTZ)
    df_minute60_TON = add_indicators_version4(df_minute60_TON)

    ####################################################################33
    df_minute60_IMX = add_indicators_version4(df_minute60_IMX)
    df_minute60_HPO = add_indicators_version4(df_minute60_HPO)
    df_minute60_EGLD = add_indicators_version4(df_minute60_EGLD)
    df_minute60_HIVE = add_indicators_version4(df_minute60_HIVE)
    df_minute60_GRS = add_indicators_version4(df_minute60_GRS)
    df_minute60_QKC = add_indicators_version4(df_minute60_QKC)
    df_minute60_STPT = add_indicators_version4(df_minute60_STPT)
    df_minute60_XEM = add_indicators_version4(df_minute60_XEM)
    df_minute60_STEEM = add_indicators_version4(df_minute60_STEEM)
    df_minute60_ATOM = add_indicators_version4(df_minute60_ATOM)
    df_minute60_LOOM = add_indicators_version4(df_minute60_LOOM)
    df_minute60_1INCH = add_indicators_version4(df_minute60_1INCH)
    df_minute60_ARK = add_indicators_version4(df_minute60_ARK)
    df_minute60_ZIL = add_indicators_version4(df_minute60_ZIL)
    df_minute60_CRE = add_indicators_version4(df_minute60_CRE)
    df_minute60_MBL = add_indicators_version4(df_minute60_MBL)
    df_minute60_ALGO = add_indicators_version4(df_minute60_ALGO)
    df_minute60_STORJ = add_indicators_version4(df_minute60_STORJ)
    df_minute60_DKA = add_indicators_version4(df_minute60_DKA)
    df_minute60_XLM = add_indicators_version4(df_minute60_XLM)
    df_minute60_IOST = add_indicators_version4(df_minute60_IOST)
    df_minute60_ARDR = add_indicators_version4(df_minute60_ARDR)
    df_minute60_CHZ = add_indicators_version4(df_minute60_CHZ)
    df_minute60_MINA = add_indicators_version4(df_minute60_MINA)
    df_minute60_MANA = add_indicators_version4(df_minute60_MANA)
    df_minute60_KAVA = add_indicators_version4(df_minute60_KAVA)
    df_minute60_MASK = add_indicators_version4(df_minute60_MASK)
    df_minute60_BLUR = add_indicators_version4(df_minute60_BLUR)
    df_minute60_SNT = add_indicators_version4(df_minute60_SNT)
    df_minute60_POWR = add_indicators_version4(df_minute60_POWR)
    df_minute60_AXS = add_indicators_version4(df_minute60_AXS)
    df_minute60_DOT = add_indicators_version4(df_minute60_DOT)
    df_minute60_MTL = add_indicators_version4(df_minute60_MTL)
    df_minute60_ONT = add_indicators_version4(df_minute60_ONT)
    df_minute60_GLM = add_indicators_version4(df_minute60_GLM)
    df_minute60_MATIC = add_indicators_version4(df_minute60_MATIC)
    df_minute60_BSV = add_indicators_version4(df_minute60_BSV)
    df_minute60_EOS = add_indicators_version4(df_minute60_EOS)
    df_minute60_MLK = add_indicators_version4(df_minute60_MLK)
    df_minute60_THETA = add_indicators_version4(df_minute60_THETA)
    df_minute60_TRX = add_indicators_version4(df_minute60_TRX)
    df_minute60_ASTR = add_indicators_version4(df_minute60_ASTR)
    df_minute60_GAS = add_indicators_version4(df_minute60_GAS)
    df_minute60_WAVES = add_indicators_version4(df_minute60_WAVES)
    df_minute60_MNT = add_indicators_version4(df_minute60_MNT)
    df_minute60_VET = add_indicators_version4(df_minute60_VET)
    df_minute60_QTUM = add_indicators_version4(df_minute60_QTUM)
    df_minute60_PUNDIX = add_indicators_version4(df_minute60_PUNDIX)
    df_minute60_NEO = add_indicators_version4(df_minute60_NEO)
    
    


#############################################################################################################################
    df_minute60_XEC_tail = df_minute60_XEC.tail(n=1)
    df_minute60_CVC_tail = df_minute60_CVC.tail(n=1)
    df_minute60_POLYX_tail = df_minute60_POLYX.tail(n=1)
    df_minute60_T_tail = df_minute60_T.tail(n=1)
    df_minute60_SHIB_tail = df_minute60_SHIB.tail(n=1)
    df_minute60_BTC_tail = df_minute60_BTC.tail(n=1)
    df_minute60_XRP_tail = df_minute60_XRP.tail(n=1)
    df_minute60_DOGE_tail = df_minute60_DOGE.tail(n=1)
    df_minute60_WAXP_tail = df_minute60_WAXP.tail(n=1)
    df_minute60_CTC_tail = df_minute60_CTC.tail(n=1)
    df_minute60_ANKR_tail = df_minute60_ANKR.tail(n=1)
    df_minute60_AERGO_tail = df_minute60_AERGO.tail(n=1)
    df_minute60_HIFI_tail = df_minute60_HIFI.tail(n=1)
    df_minute60_SOL_tail = df_minute60_SOL.tail(n=1)
    df_minute60_STMX_tail = df_minute60_STMX.tail(n=1)
    df_minute60_ETH_tail = df_minute60_ETH.tail(n=1)
    df_minute60_ID_tail = df_minute60_ID.tail(n=1)
    df_minute60_NEAR_tail = df_minute60_NEAR.tail(n=1)
    df_minute60_SC_tail = df_minute60_SC.tail(n=1)
    df_minute60_BORA_tail = df_minute60_BORA.tail(n=1)
    df_minute60_PYTH_tail = df_minute60_PYTH.tail(n=1)
    df_minute60_LSK_tail = df_minute60_LSK.tail(n=1)
    df_minute60_STX_tail = df_minute60_STX.tail(n=1)
    df_minute60_ETC_tail = df_minute60_ETC.tail(n=1)
    df_minute60_APT_tail = df_minute60_APT.tail(n=1)
    df_minute60_MVL_tail = df_minute60_MVL.tail(n=1)
    df_minute60_SXP_tail = df_minute60_SXP.tail(n=1)
    df_minute60_AVAX_tail = df_minute60_AVAX.tail(n=1)
    df_minute60_BCH_tail = df_minute60_BCH.tail(n=1)
    df_minute60_ICX_tail = df_minute60_ICX.tail(n=1)
    df_minute60_SEI_tail = df_minute60_SEI.tail(n=1)
    df_minute60_ONG_tail = df_minute60_ONG.tail(n=1)
    df_minute60_BTG_tail = df_minute60_BTG.tail(n=1)
    df_minute60_ORBS_tail = df_minute60_ORBS.tail(n=1)
    df_minute60_ZRX_tail = df_minute60_ZRX.tail(n=1)
    df_minute60_GMT_tail = df_minute60_GMT.tail(n=1)
    df_minute60_HUNT_tail = df_minute60_HUNT.tail(n=1)
    df_minute60_IOTA_tail = df_minute60_IOTA.tail(n=1)
    df_minute60_IQ_tail = df_minute60_IQ.tail(n=1)
    df_minute60_STRAX_tail = df_minute60_STRAX.tail(n=1)
    df_minute60_CELO_tail = df_minute60_CELO.tail(n=1)
    df_minute60_ARB_tail = df_minute60_ARB.tail(n=1)
    df_minute60_BTT_tail = df_minute60_BTT.tail(n=1)
    df_minute60_HBAR_tail = df_minute60_HBAR.tail(n=1)
    df_minute60_LINK_tail = df_minute60_LINK.tail(n=1)
    df_minute60_SAND_tail = df_minute60_SAND.tail(n=1)
    df_minute60_GRT_tail = df_minute60_GRT.tail(n=1)
    df_minute60_FLOW_tail = df_minute60_FLOW.tail(n=1)
    df_minute60_ADA_tail = df_minute60_ADA.tail(n=1)
    df_minute60_SUI_tail = df_minute60_SUI.tail(n=1)

    ####################################################################################
    df_minute60_AQT_tail = df_minute60_AQT.tail(n=1)
    df_minute60_CBK_tail = df_minute60_CBK.tail(n=1)
    df_minute60_FCT2_tail = df_minute60_FCT2.tail(n=1)
    df_minute60_JST_tail = df_minute60_JST.tail(n=1)
    df_minute60_UPP_tail = df_minute60_UPP.tail(n=1)
    df_minute60_STRIKE_tail = df_minute60_STRIKE.tail(n=1)
    df_minute60_MOC_tail = df_minute60_MOC.tail(n=1)
    df_minute60_TFUEL_tail = df_minute60_TFUEL.tail(n=1)
    df_minute60_TT_tail = df_minute60_TT.tail(n=1)
    df_minute60_KNC_tail = df_minute60_KNC.tail(n=1)
    df_minute60_CRO_tail = df_minute60_CRO.tail(n=1)
    df_minute60_META_tail = df_minute60_META.tail(n=1)
    df_minute60_ELF_tail = df_minute60_ELF.tail(n=1)
    df_minute60_AHT_tail = df_minute60_AHT.tail(n=1)
    df_minute60_BAT_tail = df_minute60_BAT.tail(n=1)
    df_minute60_SBD_tail = df_minute60_SBD.tail(n=1)
    df_minute60_MED_tail = df_minute60_MED.tail(n=1)
    df_minute60_AAVE_tail = df_minute60_AAVE.tail(n=1)
    df_minute60_XTZ_tail = df_minute60_XTZ.tail(n=1)
    df_minute60_TON_tail = df_minute60_TON.tail(n=1)
    #####################################################333
    df_minute60_IMX_tail = df_minute60_IMX.tail(n=1)
    df_minute60_HPO_tail = df_minute60_HPO.tail(n=1)
    df_minute60_EGLD_tail = df_minute60_EGLD.tail(n=1)
    df_minute60_HIVE_tail = df_minute60_HIVE.tail(n=1)
    df_minute60_GRS_tail = df_minute60_GRS.tail(n=1)
    df_minute60_QKC_tail = df_minute60_QKC.tail(n=1)
    df_minute60_STPT_tail = df_minute60_STPT.tail(n=1)
    df_minute60_XEM_tail = df_minute60_XEM.tail(n=1)
    df_minute60_STEEM_tail = df_minute60_STEEM.tail(n=1)
    df_minute60_ATOM_tail = df_minute60_ATOM.tail(n=1)
    df_minute60_LOOM_tail = df_minute60_LOOM.tail(n=1)
    df_minute60_1INCH_tail = df_minute60_1INCH.tail(n=1)
    df_minute60_ARK_tail = df_minute60_ARK.tail(n=1)
    df_minute60_ZIL_tail = df_minute60_ZIL.tail(n=1)
    df_minute60_CRE_tail = df_minute60_CRE.tail(n=1)
    df_minute60_MBL_tail = df_minute60_MBL.tail(n=1)
    df_minute60_ALGO_tail = df_minute60_ALGO.tail(n=1)
    df_minute60_STORJ_tail = df_minute60_STORJ.tail(n=1)
    df_minute60_DKA_tail = df_minute60_DKA.tail(n=1)
    df_minute60_XLM_tail = df_minute60_XLM.tail(n=1)
    df_minute60_IOST_tail = df_minute60_IOST.tail(n=1)
    df_minute60_ARDR_tail = df_minute60_ARDR.tail(n=1)
    df_minute60_CHZ_tail = df_minute60_CHZ.tail(n=1)
    df_minute60_MINA_tail = df_minute60_MINA.tail(n=1)
    df_minute60_MANA_tail = df_minute60_MANA.tail(n=1)
    df_minute60_KAVA_tail = df_minute60_KAVA.tail(n=1)
    df_minute60_MASK_tail = df_minute60_MASK.tail(n=1)
    df_minute60_BLUR_tail = df_minute60_BLUR.tail(n=1)
    df_minute60_SNT_tail = df_minute60_SNT.tail(n=1)
    df_minute60_POWR_tail = df_minute60_POWR.tail(n=1)
    df_minute60_AXS_tail = df_minute60_AXS.tail(n=1)
    df_minute60_DOT_tail = df_minute60_DOT.tail(n=1)
    df_minute60_MTL_tail = df_minute60_MTL.tail(n=1)
    df_minute60_ONT_tail = df_minute60_ONT.tail(n=1)
    df_minute60_GLM_tail = df_minute60_GLM.tail(n=1)
    df_minute60_MATIC_tail = df_minute60_MATIC.tail(n=1)
    df_minute60_BSV_tail = df_minute60_BSV.tail(n=1)
    df_minute60_EOS_tail = df_minute60_EOS.tail(n=1)
    df_minute60_MLK_tail = df_minute60_MLK.tail(n=1)
    df_minute60_THETA_tail = df_minute60_THETA.tail(n=1)
    df_minute60_TRX_tail = df_minute60_TRX.tail(n=1)
    df_minute60_ASTR_tail = df_minute60_ASTR.tail(n=1)
    df_minute60_GAS_tail = df_minute60_GAS.tail(n=1)
    df_minute60_WAVES_tail = df_minute60_WAVES.tail(n=1)
    df_minute60_MNT_tail = df_minute60_MNT.tail(n=1)
    df_minute60_VET_tail = df_minute60_VET.tail(n=1)
    df_minute60_QTUM_tail = df_minute60_QTUM.tail(n=1)
    df_minute60_PUNDIX_tail = df_minute60_PUNDIX.tail(n=1)
    df_minute60_NEO_tail = df_minute60_NEO.tail(n=1)
    


########################################################################################################################
    combined_df = pd.concat([df_minute60_XEC_tail, df_minute60_CVC_tail,df_minute60_POLYX_tail,df_minute60_T_tail,
                            df_minute60_SHIB_tail,df_minute60_BTC_tail,df_minute60_XRP_tail, df_minute60_DOGE_tail,
                            df_minute60_WAXP_tail,df_minute60_CTC_tail,df_minute60_ANKR_tail,df_minute60_AERGO_tail,
                            df_minute60_HIFI_tail,df_minute60_SOL_tail, df_minute60_STMX_tail,df_minute60_ETH_tail,
                            df_minute60_ID_tail, df_minute60_NEAR_tail, df_minute60_SC_tail, df_minute60_BORA_tail,
                            df_minute60_PYTH_tail, df_minute60_LSK_tail, df_minute60_STX_tail, df_minute60_ETC_tail,
                            df_minute60_APT_tail, df_minute60_MVL_tail, df_minute60_SXP_tail, df_minute60_AVAX_tail,
                            df_minute60_BCH_tail, df_minute60_ICX_tail, df_minute60_SEI_tail, df_minute60_ONG_tail,
                            df_minute60_BTG_tail, df_minute60_ORBS_tail, df_minute60_ZRX_tail, df_minute60_GMT_tail,
                            df_minute60_HUNT_tail, df_minute60_IOTA_tail, df_minute60_IQ_tail, df_minute60_STRAX_tail,
                            df_minute60_CELO_tail, df_minute60_ARB_tail, df_minute60_BTT_tail, df_minute60_HBAR_tail,
                            df_minute60_LINK_tail, df_minute60_SAND_tail, df_minute60_GRT_tail, df_minute60_FLOW_tail,
                            df_minute60_ADA_tail, df_minute60_SUI_tail, df_minute60_AQT_tail, df_minute60_CBK_tail,
                            df_minute60_FCT2_tail, df_minute60_JST_tail, df_minute60_UPP_tail, df_minute60_STRIKE_tail,
                            df_minute60_MOC_tail, df_minute60_TFUEL_tail, df_minute60_TT_tail, df_minute60_KNC_tail,
                            df_minute60_CRO_tail, df_minute60_META_tail, df_minute60_ELF_tail, df_minute60_AHT_tail,
                            df_minute60_BAT_tail, df_minute60_SBD_tail, df_minute60_MED_tail, df_minute60_AAVE_tail,
                            df_minute60_XTZ_tail, df_minute60_TON_tail, df_minute60_IMX_tail, df_minute60_HPO_tail,
                            df_minute60_EGLD_tail, df_minute60_HIVE_tail, df_minute60_GRS_tail, df_minute60_QKC_tail,
                            df_minute60_STPT_tail, df_minute60_XEM_tail, df_minute60_STEEM_tail, df_minute60_ATOM_tail,
                            df_minute60_LOOM_tail, df_minute60_1INCH_tail, df_minute60_ARK_tail, df_minute60_ZIL_tail,
                            df_minute60_CRE_tail, df_minute60_MBL_tail, df_minute60_ALGO_tail, df_minute60_STORJ_tail,
                            df_minute60_DKA_tail, df_minute60_XLM_tail, df_minute60_IOST_tail, df_minute60_ARDR_tail,
                            df_minute60_CHZ_tail, df_minute60_MINA_tail, df_minute60_MANA_tail, df_minute60_KAVA_tail,
                            df_minute60_MASK_tail, df_minute60_BLUR_tail, df_minute60_SNT_tail, df_minute60_POWR_tail,
                            df_minute60_AXS_tail, df_minute60_DOT_tail, df_minute60_MTL_tail, df_minute60_ONT_tail,
                            df_minute60_GLM_tail, df_minute60_MATIC_tail, df_minute60_BSV_tail, df_minute60_EOS_tail,
                            df_minute60_MLK_tail, df_minute60_THETA_tail, df_minute60_TRX_tail, df_minute60_ASTR_tail,
                            df_minute60_GAS_tail, df_minute60_WAVES_tail, df_minute60_MNT_tail, df_minute60_VET_tail,
                            df_minute60_QTUM_tail, df_minute60_PUNDIX_tail, df_minute60_NEO_tail
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

    # Filter the DataFrame for the buying condition
    # combined_df_sort_aroon_cross = combined_df_sort[combined_df_sort['aroon_cross'] == 1]
    # if len(combined_df_sort_aroon_cross) != 0:
    #     combined_df_sort = combined_df_sort_aroon_cross
        
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
        
        
        # MACD 지표를 사용한 매수 조건: MACD line이 signal line을 상향 돌파한 경우
        #  MACD가 시그널을 상향돌파하는 경우, 상승 모멘텀을 받는 것이므로 매수
    buy_condition_MACD = combined_df_sort["MACD"] > combined_df_sort["Signal_Line"]
    buy_condition_MACD_df = combined_df_sort[buy_condition_MACD]
    if len(buy_condition_MACD_df) != 0:
        combined_df_sort = buy_condition_MACD_df

    # 볼린저 밴드를 사용한 매수 조건: 현재 종가가 lower band 아래에 있는 경우
    combined_df_sort_lower_band = combined_df_sort[combined_df_sort['close'] < combined_df_sort['Lower_Band']]
    if len(combined_df_sort_lower_band) != 0:
        combined_df_sort = combined_df_sort_lower_band
        
    # 
    # OBV 지표를 사용한 매수 조건: OBV 값이 0보다 큰 경우
    combined_df_sort_OBV = combined_df_sort[combined_df_sort['OBV'] > 0]
    if len(combined_df_sort_OBV) != 0:
        combined_df_sort = combined_df_sort_OBV
        
    # ATRr_14
    # ATRr_14 값이 0.5 이하인 경우, 주식이 평정 상태에 있으므로 매수 기회로 간주될 수 있습니다
    # ATR 값이 높다면 현재 변동성이 큰 불안정한 타이밍이라는 의미이고, 낮다면 변동성이 낮고 안정적인 타이밍이라는 의미입니다.
    # 조건: ATRr_14 값이 0.5 이하인 경우
    combined_df_sort_ATRr_14 = combined_df_sort[combined_df_sort['ATRr_14'] <= 0.5]
    if len(combined_df_sort_ATRr_14) != 0:
        combined_df_sort = combined_df_sort_ATRr_14
        

    # Keltner Channels을 사용한 매수 조건: close price가 lower band 위에 있는 경우 -> 숏 포지션
    # 
    combined_df_sort_keltner = combined_df_sort[combined_df_sort['close'] > combined_df_sort['KCLe_20_2']]
    if len(combined_df_sort_keltner) != 0:
        combined_df_sort = combined_df_sort_keltner
            
    #df_minute60_NEO["trix_buy_signal"] 
    combined_df_sort_trix = combined_df_sort[combined_df_sort['trix_buy_signal'] == 1]
    if len(combined_df_sort_trix) != 0:
        combined_df_sort = combined_df_sort_trix

    # df["vortex_buy_signal"] 
    combined_df_sort_vortex = combined_df_sort[combined_df_sort['vortex_buy_signal'] == 1]
    if len(combined_df_sort_vortex) != 0:
        combined_df_sort = combined_df_sort_vortex

    # supertrend_buy_signal
    combined_df_sort_super = combined_df_sort[combined_df_sort['supertrend_buy_signal'] == 1]
    if len(combined_df_sort_super) != 0:
        combined_df_sort = combined_df_sort_super

    # Donchian Channels을 사용한 매수 조건: close price가 upper band 위에 있는 경우
    # 상승 추세인 경우: 주가가 돈치안 상하선을 돌파하면 매수! 
    #하락 추세인경우 : 주가가 돈치안 하한선을 돌파하면 매수!
    combined_df_sort_DCU_20_20 = combined_df_sort[combined_df_sort['close'] > combined_df_sort['DCU_20_20']]
    if len(combined_df_sort_DCU_20_20) != 0:
        combined_df_sort = combined_df_sort_DCU_20_20    

    combined_df_sort_v2 = combined_df_sort[(combined_df_sort['EMA_5'] > combined_df_sort['SMA_5'])]

    # when the current close price falls below the lower Donchian Channel (DCL_20_20), 
    combined_df_DCL_20_20 = combined_df_sort_v2[combined_df_sort_v2['close'] > combined_df_sort_v2['DCL_20_20']]

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

def analyze_data_with_gpt4(data_json,current_status):
    instructions_path = "autotrade_version10.md"
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
                #{"role": "user", "content": last_decisions},
                #{"role": "user", "content": fear_and_greed}
            ],
            response_format={"type":"json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in analyzing data with GPT-4: {e}")
        return None
    

def execute_buy(index_value_v2):
    print(f"Attempting to buy {index_value_v2} ...")
    try:
        krw_balance = upbit.get_balance("KRW")
        amount_to_invest = krw_balance
        if amount_to_invest > 5000:  # Ensure the order is above the minimum threshold
            result = upbit.buy_market_order(index_value_v2, amount_to_invest * 0.9995)  # Adjust for fees
            print("Buy order successful:", result)
    except Exception as e:
        print(f"Failed to execute buy order: {e}")


def execute_sell(index_value):
    try:
        print(f"Attempting to sell the {index_value}...")
        index_value_split = index_value.split("-")[1]
        btc_balance = upbit.get_balance(index_value_split)
        amount_to_sell = btc_balance
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

# 밑에 함수 에러 해결해줘! 에러는 다음과 같아: make_decision_and_execute_sell.... Failed to parse the advice as JSON: name 'index_value' is not defined
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
            #last_decisions = fetch_last_decisions()
            #fear_and_greed = fetch_fear_and_greed_index(limit=7)  
            current_status = get_current_status(index_value_v2)
            for attempt in range(max_retries):
                try:
                    advice = analyze_data_with_gpt4(data_json_v2,current_status)
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

            
            if decision.get('decision') == "buy":
                execute_buy(index_value_v2)
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
            df_minute60_index_value = pyupbit.get_ohlcv(index_value, interval="minute60",count=120)
            df_minute60_index_value = add_indicators_version4(df_minute60_index_value)
            df_minute60_index_value_tail = df_minute60_index_value.tail(n=1)
            sell_data = df_minute60_index_value_tail.to_json(orient='split')
            #last_decisions = fetch_last_decisions()
            #fear_and_greed = fetch_fear_and_greed_index(limit=30)
            current_status = get_current_status(index_value)
            advice = analyze_data_with_gpt4(sell_data,current_status)
            
            decision = json.loads(advice)
            print(decision)
            
            if decision.get('decision') == "sell":
                execute_sell(index_value)
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
      
    # 1시간마다 스케줄 설정
    schedule.every().day.at("13:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("14:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("15:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("16:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("17:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("18:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("19:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("20:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("21:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("22:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("23:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("00:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("01:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("02:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("03:01").do(make_decision_and_execute_schedule)
    
    schedule.every().day.at("04:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("05:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("06:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("07:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("08:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("09:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("10:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("11:01").do(make_decision_and_execute_schedule)
    schedule.every().day.at("12:01").do(make_decision_and_execute_schedule)

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