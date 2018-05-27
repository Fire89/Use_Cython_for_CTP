# encoding: UTF-8

from tqsdk.api import TqApi
from tqsdk.task import TaskManager
from tqsdk.tools import make_order_until_all_matched
from y_tools import Y_Base

class DemoSpread(Y_Base):
    def __init__(self):
        super(DemoSpread,self).__init__()        
        self.b=0
        self.bf={}      
        self.symbol_a = "SHFE.bu1809"   #"CZCE.MA809" #"SHFE.bu1809"   #
        self.symbol_b = "SHFE.bu1810"        

    def task_main(self):
        print ("start")
        quote_a = self.api.get_quote(self.symbol_a)
        quote_b = self.api.get_quote(self.symbol_b)
        buy_open_spread = 50000
        sell_close_spread = -70000
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
               
        while True:
            if long_volume == 0 and quote_a["ask_price1"] - self.b > 2 :
                print("quote_a['ask_price1'] - self.b :",quote_a['ask_price1'] ,self.b ,  quote_a['ask_price1'] - self.b )
            wait_result = yield {
                "BUY_OPEN": lambda: long_volume == 0 and quote_a["ask_price1"] - self.b > 2,
                "PRINT" : lambda: 1>0,
                "SELL_CLOSE": lambda: long_volume > 0 and 
                (
                      quote_a["ask_price1"] - self.b <= -m
                  or  quote_a["ask_price1"] - self.b >= m
                  or (quote_a["ask_price1"] - self.bf['a1'] >= n and self.bf['a1'] < self.b) #
                ),
            }            
            
                                 
          
            if wait_result["BUY_OPEN"] :                
                print("开仓 ", quote_a["bid_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'])
                task_a = self.On_BUY("SELL",self.symbol_a,max_volume)
                long_volume = max_volume
                self.bf['a1'] = self.b =quote_a["bid_price1"] 
                print("开仓@", quote_a["bid_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'])
                
            if wait_result["SELL_CLOSE"]:
                print("平仓 ", quote_a["ask_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'] )
                task_a = self.On_CLOSE("BUY",self.symbol_a,max_volume)                
                long_volume = 0           
                #self.bf['a1'] = quote_a["ask_price1"]         #下跌行情实盘用这条语句
                self.bf['a1'] = self.b =quote_a["ask_price1"]  #测试时用这条 
                print("平仓@", quote_a["ask_price1"] , " self.b:",self.b," self.bf['a1']:",self.bf['a1'] )
                print("----" * 4)
                
                
                
            if wait_result["PRINT"]:             
                if self.bf['a1'] !=quote_a["ask_price1"] and long_volume != 0:
                    if self.bf['a1'] - n == quote_a["ask_price1"] :
                        print('@  a1:',  quote_a["ask_price1"] ," self.bf:", self.bf['a1'])
                        self.bf['a1'] = quote_a["ask_price1"]
                        print('@3 a1:',  quote_a["ask_price1"] ," self.bf:", self.bf['a1'])              
            
                    
           # wait_subtask_finish = yield {
            #    "ANY_TASK_ERROR": lambda: self.tm.get_error(task_a) or self.tm.get_error(task_a),
             #   "BOTH_TASK_FINSISH": lambda: self.tm.is_finish(task_a) and self.tm.is_finish(task_a),
              #}
            #if wait_subtask_finish["ANY_TASK_ERROR"]:
             #   break            
                  
        print ("finish")
  

if __name__ == "__main__":
    d = DemoSpread()
    d.run()

"""
    移动止盈 测试
    
    运行后开仓 多单1手，成交后判断平仓条件:
        条件 1. 最新价 低于持仓价10个价位 或 最新价大于10个价位  平仓1手
        条件 2. 最新价 大于持仓价6个价位，将持仓价提高6（即 持仓价 + 6）作为新的持仓价，为了理解方便设：x
                之后分2种情况:
                             1.在X价位为基准，继续涨4个价位达到持仓价 大于8，触发条件1 平仓
                             2.在X价位为基准，价格回落4个价位 平仓
                             
        平仓后持仓为0， 开仓条件是 低于上次平仓价2个价位开委托单
        实盘中 使用前一次开仓价位-2 作为开仓条件 
                             
                             
                             
"""
                