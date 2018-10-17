import datetime
def file_create():
    output=open("GUI_OUTPUT_RESULT.txt",'a')
    now=datetime.datetime.now()
    output.write("\n****************NEW RESULT STARTS HERE*************************")
    output.write("\n"*4)
    output.write(now.strftime("\nDATE AND TIME:"+" "+"%H:%M:%S---%d/%b/%Y"))
    return output    
