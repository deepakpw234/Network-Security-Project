import os
import sys
from src.logging.logger import logging


def get_error_details(error,error_details:sys):
    _,_,ex_tab = error_details.exc_info()
    filename = ex_tab.tb_frame.f_code.co_filename
    line_num = ex_tab.tb_lineno
    error_message = f"The error occured in the python script [{filename}] in the line [{line_num}] with the error message [{str(error)}]"

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error_message,error_details)


    def __str__(self):
        return self.error_message
    
