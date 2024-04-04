import sqlite3
import json
from datetime import datetime
import pyupbit

def initialize_db(db_path='trading_decisions.sqlite'):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS decisions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                decision TEXT,
                percentage REAL,
                reason TEXT,
                balance REAL,
                krw_balance REAL,
                avg_buy_price REAL,
                krw_price REAL
            );
        ''')
        conn.commit()

def save_decision_to_db(decision, current_status):
    db_path = 'trading_decisions.sqlite'
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
    
        # Parsing current_status from JSON to Python dict
        status_dict = json.loads(current_status)
        #current_price = pyupbit.get_orderbook(ticker="KRW-BTC")['orderbook_units'][0]["ask_price"]
        current_price = status_dict['orderbook']['orderbook_units'][0]["ask_price"]

        # Preparing data for insertion
        data_to_insert = (
            decision.get('decision'),
            decision.get('percentage', 100),  # Defaulting to 100 if not provided
            decision.get('reason', ''),  # Defaulting to an empty string if not provided
            status_dict.get('balance'),
            status_dict.get('krw_balance'),
            status_dict.get('avg_buy_price'),
            current_price
        )
        
        # Inserting data into the database
        cursor.execute('''
            INSERT INTO decisions (timestamp, decision, percentage, reason, balance, krw_balance, avg_buy_price, krw_price)
            VALUES (datetime('now', 'localtime'), ?, ?, ?, ?, ?, ?, ?)
        ''', data_to_insert)
    
        conn.commit()

def fetch_last_decisions(db_path='trading_decisions.sqlite', num_decisions=10):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT timestamp, decision, percentage, reason, balance, krw_balance, avg_buy_price FROM decisions
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (num_decisions,))
        decisions = cursor.fetchall()

        if decisions:
            formatted_decisions = []
            for decision in decisions:
                # Converting timestamp to milliseconds since the Unix epoch
                ts = datetime.strptime(decision[0], "%Y-%m-%d %H:%M:%S")
                ts_millis = int(ts.timestamp() * 1000)
                
                formatted_decision = {
                    "timestamp": ts_millis,
                    "decision": decision[1],
                    "percentage": decision[2],
                    "reason": decision[3],
                    "balance": decision[4],
                    "krw_balance": decision[5],
                    "avg_buy_price": decision[6]
                }
                formatted_decisions.append(str(formatted_decision))
            return "\n".join(formatted_decisions)
        else:
            return "No decisions found."
