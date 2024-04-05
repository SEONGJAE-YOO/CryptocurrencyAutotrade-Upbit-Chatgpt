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
from technical_analysis import add_indicators_version2, add_indicators, add_indicators_version3

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))

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
                            df_minute240_XTZ_tail, df_minute240_TON_tail
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
if len(combined_df_sort) != 0:
    combined_df_sort = combined_df_sort_cmf

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

sell_data = result.to_json(orient='split')
print(sell_data)
#combined_df_sorted = combined_df.sort_values(by='Volume')
#sorted_df = combined_df.sort_values(by='volume', ascending=True)
#result = sorted_df.tail(n=1)
#print(result)
result_excel = result.to_csv('add_indicators_version3_0405.csv', index = True)
# combined_data = combined_df.to_json(orient='split')
# print(combined_data)
