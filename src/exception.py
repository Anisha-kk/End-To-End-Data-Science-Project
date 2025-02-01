import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()#Give details about the file and line
    #where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occurred in Python script name [{0}] in line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

#Creating a child class of Exception class to handle custom exceptions
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message