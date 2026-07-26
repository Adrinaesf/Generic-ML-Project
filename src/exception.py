import sys

'''
This function will return the error messaged and the inforamtion regarding the error. 
error_message_detail: Exception, sys -> String
Example: ZeroDivisionError, error:detail -> "Error occured in ..."

helper functions: 
    - sys.exc_info() -> (type, error_message, traceback)
    - Ex: (ZeroDivisionError, "division by zero", traceback object)
'''

def error_message_detail(error: Exception, error_detail:sys):
    # save the traceback (error’s path and location history)
    _,_,exc_tb = error_detail.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename

    erorr_message = (
        f"Error occured in python script name: {file_name} \n"
        f"file number: {exc_tb.tb_lineno} \n"
        f"error message: {str(error)}"
    )

    return erorr_message


class CustomeException(Exception): # Same as class CustomException extends Exception

    # Constructor: Same as public MyClass(....) # initilize the parameters
    def __init__(self, error_message: Exception, error_detail:sys):
        # let the parent(Exception) store what it already knows how to store using super()
       super().__init__(error_message)

        # Now add your own extra information
       self.error_message = error_message_detail(
           error_message,
           error_detail
        )

    def __str__(self):
        return self.error_message
