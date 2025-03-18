import requests
import pandas as pd
import time
# import numpy
# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime
# from kafka import KafkaProducer

class OptionsScraper:
    def get_tickers(self):
        arr = []
        try:
            with open ("nasdaq_tickers.txt") as f:
                for item in f:
                    try:
                        arr.append(str(item.strip()))
                    except Exception as e:
                        print(e)
                        continue
                dataframe = pd.DataFrame({'Ticker': arr})
        except Exception as e:
            print(f"Unexpected error: {e}")
            dataframe = pd.DataFrame()
        return dataframe
    
    def get_data(self, dataframe: pd):
        data_responses = []
        for ticker in dataframe['Ticker']:
            try:
                # print(str(ticker))
                response = requests.get(f"https://www.webull.com/quote/nasdaq-" + str(ticker) + f"/options")
                # print(response.status_code)
                print(f"https://www.webull.com/quote/nasdaq-" + str(ticker) + f"/options")

                if response.status_code == 200:
                    # data_responses.append({'Ticker': ticker, 'Data': response.json()})
                    try:
                        file = "assets/results_" + str(ticker) + f".txt"
                        with open (file, "w", encoding="utf-8") as f:
                            f.write(response.text)
                            print(f"Wrote" + str(ticker) + f"to file")
                    except Exception as e:
                        print(e)

                elif response.status_code != 200:
                    time.sleep(10)
                    try:
                        file = "assets/results_" + str(ticker) + f".txt"
                        with open (file, "w", encoding="utf-8") as f:
                            f.write(response.text)
                            print(f"Wrote" + str(ticker) + f"to file")
                    except Exception as e:
                        print(e)

            except Exception as e:
                print("Error requesting data for {ticker}: {e}")
x = OptionsScraper()
y = x.get_tickers()
x.get_data(y)
# print(y)
# print(x)



