# Import all the libraries needed

import yfinance as yf
import sys
import os
import pandas as pd

class dataScraper:
    
    def __init__(self,country_name:str = None):
        self.country_name = None or country_name
        return
    
    def download_data(self,company_name:str, country_name:str = "IND",start_date:str = "2000-01-01",end_date:str = "2024-12-31") -> str:
        stock = yf.Ticker(company_name)
        data = stock.history(start = start_date, end = end_date)
        
        if(data.empty):
            return f"No data found for {company_name}"
        
        data.to_csv(f"data/scrapedData/{country_name}/{company_name}.csv")
        del data,stock
        return f"Downloaded data for {company_name}" 
        
        
    def bulk_download_data(self,country_name:str = None,tickerlist_path:str = None,required_number:int = None,start_date:str = "2000-01-01",end_date:str = "2024-12-31") -> str:
        if(country_name == None):
            return f"Please give country code\n"
        elif(tickerlist_path == None):
            return f"Please give a path to ticker list\n"
        elif not os.path.exists(tickerlist_path):
            return f"File does not exist at {tickerlist_path}\n"
        
        ticker_symbols = pd.read_csv(tickerlist_path)
        
        if(required_number == None):
            ticker_symbols = ticker_symbols.head(5)
        else:
            ticker_symbols = ticker_symbols.head(required_number)
        
        for ticker in ticker_symbols['Ticker']:
            stock = yf.Ticker(ticker)
            data = stock.history(start = start_date, end = end_date)
            
            if(data.empty):
                return f"No data found for {ticker}"
            
            data.to_csv(f"data/scrapedData/{country_name}/{ticker}.csv")
            del data,stock
            return f"Downloaded data for {ticker}"
        

def main():
    downloader = dataScraper()
    downloader.download_data("NVDA","US")
    #downloader.bulk_download_data(country_name = "IND",tickerlist_path = "data/tickerList/indian_companies.csv")
    
main()