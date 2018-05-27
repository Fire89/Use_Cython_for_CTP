#distutils: language = c++

cimport cmdapi
from cmdapi cimport CThostFtdcMdApi,CThostFtdcMdSpi,CThostFtdcReqUserLoginField

cdef class PyCThostFtdcMdApiBase: 
    cdef cmdapi.CThostFtdcMdApi *ptr     
    def __cinit__(self):
        self.ptr = cmdapi.CThostFtdcMdApi.CreateFtdcMdApi("",False,False)       
    def RegisterSpi(self, PyCThostFtdcMdSpi mdspi):
        self.ptr.RegisterSpi(mdspi.ptr)
    def __dealloc__(self):
        self.ptr.Release() 
        
    
    def GetApiVersion(self):
        strVersion = self.ptr.GetApiVersion()
        return strVersion

    def Init(self):
        self.ptr.Init()
    def Join(self):
        self.ptr.Join() 
        
    def GetTradingDay(self):
        strTradingDay = self.ptr.GetTradingDay()
        return strTradingDay
    def RegisterFront(self, pszFrontAddress ) :
        self.ptr.RegisterFront( pszFrontAddress) 
        
    def RegisterNameServer(self, pszNsAddress):
        self.ptr.RegisterNameServer(pszNsAddress) 
    
    """
         void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) 
         
         void RegisterSpi(CThostFtdcMdSpi *pSpi) 
         int SubscribeMarketData(char *ppInstrumentID[], int nCount) 
         int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) 
         int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) 
         int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) 
    """    
    def ReqUserLogin(self, pReqUserLoginField,  nRequestID):
        self.ptr.ReqUserLogin(<CThostFtdcReqUserLoginField *>pReqUserLoginField, nRequestID)
    #     int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) 
    
        

cdef class PyCThostFtdcMdApi: 
    cdef cmdapi.CThostFtdcMdApi *ptr     
    def __cinit__(self):
        self.ptr = cmdapi.CThostFtdcMdApi.CreateFtdcMdApi("",False,False)
        #self.ptr = new cmdapi.CThostFtdcMdApi() 要使用此语句，必须实现抽象类方法
    def RegisterSpi(self, PyCThostFtdcMdSpi mdspi):
        self.ptr.RegisterSpi(mdspi.ptr)

    def __dealloc__(self):
        self.ptr.Release()       
       
cdef class PyCThostFtdcMdSpi:
    cdef cmdapi.CThostFtdcMdSpi *ptr
    def __cinit__(self):
        self.ptr = new cmdapi.CThostFtdcMdSpi()
        
    def __dealloc__(self):
        if self.ptr is not NULL: 
            del self.ptr 
            
class mdspi(PyCThostFtdcMdSpi):
    #OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    def OnRspUserLogin(pRspUserLogin, pRspInfo,  nRequestID, bIsLast):
        pass
"""        
class mdapi(PyCThostFtdcMdApi):
    def RegisterFront(self, address):
        self.ptr.RegisterFront(address)
    def RegisterSpi(self, mdspi):
        print("Regspi")
        #PyCThostFtdcMdApi.RegisterSpi(self, mdspi)
        super(mdapi, self).RegisterSpi(mdspi)
"""


from cmdapi cimport CThostFtdcFensUserInfoField, CThostFtdcReqUserLoginField, CThostFtdcUserLogoutField, aa
from libc.stdlib cimport malloc, free
from cpython cimport *
cdef class PyCThostFtdcFensUserInfoField:            
    cdef CThostFtdcFensUserInfoField *ptr     
    def __cinit__(self):
        self.ptr = <CThostFtdcFensUserInfoField *> malloc(sizeof(CThostFtdcFensUserInfoField))    
    def __del__(self):
        free(self.ptr)

cdef class PyCThostFtdcReqUserLoginField:            
    cdef CThostFtdcReqUserLoginField *ptr     
    def __cinit__(self):
        self.ptr = <CThostFtdcReqUserLoginField *> malloc(sizeof(CThostFtdcReqUserLoginField))    
    def __del__(self):
        free(self.ptr)
    
cdef class PyCThostFtdcUserLogoutField:            
    cdef CThostFtdcUserLogoutField *ptr     
    def __cinit__(self):
        self.ptr = <CThostFtdcUserLogoutField *> malloc(sizeof(CThostFtdcUserLogoutField))    
    def __del__(self):
        free(self.ptr)
        
        

#-----------------------------------------#
"""
    以下测试 cython传递 struct对象 到 .py文件   是否可行验证
"""
cdef class Pyaa:            
    cdef aa *ptr     
    def __cinit__(self,int a):
        self.ptr = <aa *> malloc(sizeof(aa))
        self.ptr.a = a
    #def __init__(self,s):
    #   self.ptr.a = s
    def __del__(self):
        free(self.ptr)
    def seta(self,v):
        self.ptr.a = v
    def geta(self):
        self.ptr.a
    def getptr(self):
        self.ptr
    
cdef extern from "stdio.h":
    extern int printf(const char *format, ...)
aaobj = aa(a=8)
pyaaobj = Pyaa(8)
logfieldobj = CThostFtdcReqUserLoginField(BrokerID=b"xxxxx",UserID=b"xxxxx",Password=b"xxxx")
cdef class testaa:
    def t(self,Pyaa aaa):
        """        
        ('1 Pyaa.getptr %d\n', None)
        ('1 Pyaa.geta(88) %d\n', None)
        ('1 python print ptr.a', 88)
        ('2 python print ptr.a', 9)
        ('2 python print ptr.geta', None)
        1 Pyaa.ptr.a 88
        """
        
        #printf("%d\n", <aa *>aaa)
        aaa.ptr
        aaa.getptr()
        aaa.seta(88)
        print("1 Pyaa.getptr %d\n", aaa.getptr())
        print("1 Pyaa.geta(88) %d\n", aaa.geta())
        printf("1 Pyaa.ptr.a %d\n", aaa.ptr.a)
        print("1 python print ptr.a", aaa.ptr.a)
        aaa.ptr.a = 9
        print("2 python print ptr.a", aaa.ptr.a)
        print("2 python print ptr.geta", aaa.geta())
       
def return_aa_struct(a):
    return aa(a=a)
"""
struct_conversion_extern_header.h

struct my_date_t {
    int year;
    int month;
    int day;
};


cdef extern from "struct_conversion_extern_header.h":
    cdef struct my_date_t:
        int year
        int month
        int day


def test_extern_struct():
    
    #  >>> test_extern_struct()
    #  [('day', 24), ('month', 6), ('year', 2000)]
    
    cdef my_date_t day = my_date_t(year=2000, month=6, day=24)
    cdef object d = day
    assert type(d) is dict
    assert d == day
    return sorted(day.items())

"""
 