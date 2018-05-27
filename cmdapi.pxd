#distutils: language = c++
from libcpp cimport bool
from datatype cimport *
cdef extern from "ThostFtdcUserApiStruct.h" nogil:
     struct CThostFtdcFensUserInfoField:
         pass
     struct CThostFtdcReqUserLoginField:
         TThostFtdcDateType	    TradingDay        
         TThostFtdcBrokerIDType	    BrokerID        
         TThostFtdcUserIDType	    UserID        
         TThostFtdcPasswordType	    Password        
         TThostFtdcProductInfoType  UserProductInfo        
         TThostFtdcProductInfoType  InterfaceProductInfo        
         TThostFtdcProtocolInfoType ProtocolInfo        
         TThostFtdcMacAddressType   MacAddress        
         TThostFtdcPasswordType	    OneTimePassword 
         TThostFtdcIPAddressType    ClientIPAddress 
         TThostFtdcLoginRemarkType  LoginRemark 
         
     struct CThostFtdcUserLogoutField:
         pass
     struct CThostFtdcRspUserLoginField:
         pass
     struct CThostFtdcRspInfoField:
         pass
     struct aa:
         int a

cdef extern from "ThostFtdcMdApi.h" nogil:
    cdef cppclass CThostFtdcMdSpi:
         OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
        
    cdef cppclass CThostFtdcMdApi:
         @staticmethod
         CThostFtdcMdApi *CreateFtdcMdApi(char *pszFlowPath , bool bIsUsingUdp , bool bIsMulticast)
         #编译时要出错，不能这么写缺省值，
         #需要解决：CThostFtdcMdApi *CreateFtdcMdApi(char *pszFlowPath = "", bint bIsUsingUdp = false , bint bIsMulticast = False) 
      
         #@staticmethod
         #CThostFtdcMdApi *CreateFtdcMdApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false)       
         @staticmethod
         const char *GetApiVersion()        
         void Release() 
         void Init()         
         int Join() 
         const char *GetTradingDay() 
         void RegisterFront(char *pszFrontAddress) 
         void RegisterNameServer(char *pszNsAddress) 
         void RegisterFensUserInfo(CThostFtdcFensUserInfoField * pFensUserInfo) 
         void RegisterSpi(CThostFtdcMdSpi *pSpi) 
         int SubscribeMarketData(char *ppInstrumentID[], int nCount) 
         int UnSubscribeMarketData(char *ppInstrumentID[], int nCount) 
         int SubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) 
         int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) 
         int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) 
         int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) 

        
