from cmdapi import mdspi, PyCThostFtdcMdSpi,PyCThostFtdcMdApi,PyCThostFtdcMdApiBase,PyCThostFtdcFensUserInfoField,PyCThostFtdcReqUserLoginField,PyCThostFtdcUserLogoutField
    
class mdapi(PyCThostFtdcMdApi):
    def RegisterFront(self, address):
        self.ptr.RegisterFront(address)     #错误，python 继承后，对self.ptr不能访问....
    def RegisterSpi(self, mdspi):
        """
        重新实现父类的方法
        """
        print("Regspi")
        #PyCThostFtdcMdApi.RegisterSpi(self, mdspi)
        super(mdapi, self).RegisterSpi(mdspi)

def test():
    a  = PyCThostFtdcMdApi()
    a1 = mdapi()
    
    b  = PyCThostFtdcMdSpi()
    b1 = mdspi()
    
    a.RegisterSpi(b)
    a1.RegisterSpi(b1)
    #a1.RegisterFront(b"tcp://180.168.146.187:10011")
    
#----------------------------------------------#
def test_PyCThostFtdcMdApiBase():
    #char gMdFrontAddr[] = "tcp://180.168.146.187:10011"
    gMdFrontAddr = b"tcp://180.168.146.187:10011"
    a  = PyCThostFtdcMdApiBase()
    b  = mdspi()    
    a.RegisterSpi(b)
    print(a.GetApiVersion())
    #a.Init()
    #a.Join()
    print(a.GetTradingDay())
    a.RegisterFront(gMdFrontAddr)
    a.RegisterNameServer(gMdFrontAddr)
    a.ReqUserLogin(PyCThostFtdcReqUserLoginField(),0)
    
from cmdapi import testaa,Pyaa,pyaaobj,logfieldobj,aaobj   
def testStructaa():
    #from cmdapi import testaa,Pyaa,aaobj,pyaaobj,logfieldobj
    pyt  =Pyaa(a=8)
    aaa = testaa()
    aaa.t(aaobj)    
    print("getptr",pyt.getptr())
    
#test()    
#test_PyCThostFtdcMdApiBase()

#print("begin teststrctaa...func...")
#testStructaa()

pyt  =Pyaa(a=8)
aaa = testaa()
aaa.t(pyt)    
#print("getptr",pyt.getptr())
from cmdapi import return_aa_struct

print(type(return_aa_struct(2))) #Is Dict