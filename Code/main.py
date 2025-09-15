from api.oanda_api import OandaApi
from infrastructure.InstrumentCollection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from simulation.ema_macd_mp import run_ema_macd
from dateutil import parser
from infrastructure.collect_data import run_collection

if __name__ == '__main__':
    #api = OandaApi()

    instrumentCollection.LoadInstruments("./data")
    #run_collection(instrumentCollection, api)
    #instrumentCollection.PrintInstruments()

    #run_ma_sim(curr_list=["EUR", "USD", "AUD", "GBP", "JPY", "CAD"])
    #run_ma_sim()
    #run_ema_macd(instrumentCollection)
    run_ema_macd(instrumentCollection)