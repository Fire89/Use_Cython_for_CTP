from cmdapi cimport CThostFtdcMdApi, CThostFtdcMdSpi, CThostFtdcFensUserInfoField, CThostFtdcReqUserLoginField, CThostFtdcUserLogoutField, aa
from libc.stdlib cimport malloc, free

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
           
        