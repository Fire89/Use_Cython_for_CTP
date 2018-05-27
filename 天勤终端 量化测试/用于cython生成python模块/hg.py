# encoding: UTF-8

from tqsdk.api import TqApi
from tqsdk.task import TaskManager
from tqsdk.tools import make_order_until_all_matched
from y_tools import Y_Base

class DemoSpread(Y_Base):
    """
        海龟交易策略

        类型：日内趋势追踪+反转策略
        
        周期：20天
        
        交易规则：        
        如果向上突破这只代码过去20天的最高价，则按csv配置文件中的金额买入。
        如果向下突破这只代码过去20天的最低价，并且有可卖仓位，则全部卖出。
        
    """
 

    def __init__(self):
        super(DemoSpread,self).__init__()        
        self.b=0
        self.bf={}      
        self.symbol_a ="CZCE.MA809" #"SHFE.bu1809"   #
        
    def task_main(self):
        print ("start")
        quote_a = self.api.get_quote(self.symbol_a)        
        max_volume = 1
        long_volume = 0
        m = 10
        n = 4
        while True:
            w =  yield {'askprice' : lambda: long_volume == 0 and quote_a["ask_price1"]>0 }
            self.b=quote_a["ask_price1"]
            print(quote_a["ask_price1"] ,quote_a["bid_price1"])
            if self.b !=0:
                break
        self.b = 500
        self.bf['a1'] = quote_a["ask_price1"] 
        dictk = self.max_min_ave_ks(self.symbol_a,60 * 60 * 24,20)     
        while True:
            wait_result = yield {
                "BUY_OPEN": lambda: (long_volume == 0 and quote_a["ask_price1"] >= dictk['max']),                           
                  "PRINT" : lambda:  1>0,
              "SELL_CLOSE": lambda: (long_volume > 0  and quote_a["ask_price1"] <= dictk['min']),
                                }
            if wait_result["PRINT"]:
                s = self.max_min_ave_ks(self.symbol_a,60 * 60 * 24,20)
                print(s)
           
            if wait_result["BUY_OPEN"] :                
                print("开仓 ", quote_a["ask_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'])
                task_a = self.On_BUY("BUY",self.symbol_a,max_volume)
                long_volume = max_volume
                self.bf['a1'] = self.b =quote_a["ask_price1"] 
                print("开仓@", quote_a["ask_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'])
                
            if wait_result["SELL_CLOSE"]:
                print("平仓 ", quote_a["bid_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'] )
                task_a = self.On_CLOSE("SELL",self.symbol_a,max_volume)                
                long_volume = 0           
                #self.bf['a1'] = quote_a["ask_price1"]         #下跌行情实盘用这条语句
                self.bf['a1'] = self.b =quote_a["ask_price1"]  #测试时用这条 
                print("平仓@", quote_a["bid_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'] )
                print("----" * 4)
             
                
    

if __name__ == "__main__":
    d = DemoSpread()
    d.run()
