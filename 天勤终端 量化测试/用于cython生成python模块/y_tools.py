# encoding: UTF-8

from tqsdk.api import TqApi
from tqsdk.tools import make_order_until_all_matched
from tqsdk.task import TaskManager

def find_order_status(orders):
    for i in orders:
        try:
            if "status" in orders[i]:
                print(orders[i])
        except Exception as e:
            pass
        

def set_a(api, quote_a, bf, n):
    if bf['a1'] != quote_a["bid_price1"] :
        if bf['a1'] + n == quote_a["bid_price1"] :
            print('@  a1:',  quote_a["bid_price1"] ," b:", bf['a1'])
            bf['a1'] = quote_a["bid_price1"]
            print('@3 a1:',  quote_a["bid_price1"] ," b:", bf['a1'])          
            
 

class Y_Base:
    def __init__(self):
        self.api = TqApi()
        self.tm = TaskManager(self.api)        

    def task_main(self):
        """
        def test():
            max_volume = 1
            while True:
                wait_result = yield {
                    "BUY_OPEN": False,
                    "PRINT" : lambda: 1>0,
                    "SELL_CLOSE": False,
                }             
                
                if wait_result["BUY_OPEN"] :     
                    On_BUY(self, B_or_S, symbol, max_volume)                        
                            
                if wait_result["SELL_CLOSE"]:
                    #bors= "BUY" if self.b > price else "SELLL" 
                    On_CLOSE(self, B_or_S, symbol, max_volume)
                if wait_result["PRINT"]:  
                    pass
                
        """
        pass
            
    """
    def case_all(self, wait_result):
        if wait_result["BUY_OPEN"] :     
            self.On_BUY(B_or_S, symbol, max_volume)                        
                    
        if wait_result["SELL_CLOSE"]:
            #bors= "BUY" if self.b > price else "SELLL" 
            self.On_CLOSE(B_or_S, symbol, max_volume)
        if wait_result["PRINT"]:  
            pass       
    """ 
        
    def On_BUY(self, B_or_S, symbol, max_volume):
        #direction="BUY", offset="OPEN"
        if B_or_S == "BUY":
            task_a = self.tm.start_task(make_order_until_all_matched(self.api, symbol= symbol, direction="BUY", offset="OPEN", volume=max_volume))                                          
            #self.On_Open_Buy()     开多仓 
        else:
            task_b = self.tm.start_task(make_order_until_all_matched(self.api, symbol= symbol, direction="SELL", offset="OPEN", volume=max_volume))                             
            #self.On_Open_Sell()    开空仓 
        return task_a if   B_or_S == "BUY" else task_b 
        
    def On_CLOSE(self, B_or_S, symbol, max_volume): 
        """
        #direction="SELL", offset="CLOSE"
        BorS:
            "SELL"   多单持仓 （卖入平仓）
            "BUY"    空单持仓 （买入平仓） 
        """
        if B_or_S == "SELL":    
            """
                "SELL" 原持仓为多单，平仓   "BUY" 原持仓为空单， 平仓
            """
            task_a = self.tm.start_task(make_order_until_all_matched(self.api, symbol= symbol, direction="SELL", offset="CLOSE", volume=max_volume))                                                 
            #self.On_Close_Buy()                          
        else:
            #self.On_Close_Sell()    
            task_b = self.tm.start_task(make_order_until_all_matched(self.api, symbol= symbol, direction="BUY", offset="CLOSE", volume=max_volume))       
   
        return task_a if B_or_S == "SELL" else task_b 
    
    def max_min_ave_ks(self,symbol, m, n = 20):
        """
        Args:
            symbol (str): 指定合约代码.
                 m (int): K线数据周期，以秒为单位。
        Returns:
            Dict：｛
                    min: n个数据的最小值
                    max: n个数据的最高值
                    ave: n个数据的平均值
                   ｝
                   
                   
        使用：
             def task_main(self):
                 quote_a = self.api.get_quote(self.symbol_a)  
                 dictk = self.max_min_ave_ks(self.symbol_a,60 * 60 * 24,20)     
                 while True:
                     wait_result = yield {
                         "BUY_OPEN": lambda: (long_volume == 0 and quote_a["ask_price1"] >= dictk['max']),                           
                           "PRINT" : lambda:  1>0,
                       "SELL_CLOSE": lambda: (long_volume > 0  and quote_a["ask_price1"] <= dictk['min']),
                                         }
                     if wait_result["PRINT"]:            
                         print(......)
                    
                     if wait_result["BUY_OPEN"] :                
                         print("开仓 ", quote_a["ask_price1"] )
                         task_a = self.On_BUY("BUY",self.symbol_a,max_volume)
                         
                     if wait_result["SELL_CLOSE"]:
                         print("平仓 ", quote_a["bid_price1"])
                         task_a = self.On_CLOSE("SELL",self.symbol_a,max_volume)                
                     ........   
        """
        kline_serial_1ks = self.api.get_kline_serial(self.symbol_a, m)
        return  { 'min' : min(kline_serial_1ks.low[-n:]),
                  'max' : max(kline_serial_1ks.high[-n:]),
                  'ave' : sum(kline_serial_1ks.close[-n:])/n,
                 }
    
    def run(self):                    
        self.tm.start_task(self.task_main())
        self.api.run()    

   
"""
基类 使用方法：
    class DemoSpread(Y_Base):
        def __init__(self):
            super(DemoSpread,self).__init__()
            ..........
        def task_main(self):
            .........
        
    if __name__ == "__main__":
        d = DemoSpread()
        d.run() 
    
"""