import time
import colorama
from colorama  import Fore, Back, Style

colorama.init()

print(colorama.Style.BRIGHT + colorama.Fore.BLUE + """


 .S_SSSs     .S_sSSs     .S       S.    .S    S.   
.SS~SSSSS   .SS~YS%%b   .SS       SS.  .SS    SS.  
S%S   SSSS  S%S   `S%b  S%S       S%S  S%S    S%S  
S%S    S%S  S%S    S%S  S%S       S%S  S%S    S%S  
S%S SSSS%P  S%S    d*S  S&S       S&S  S%S SSSS%S  
S&S  SSSY   S&S   .S*S  S&S       S&S  S&S  SSS&S  
S&S    S&S  S&S_sdSSS   S&S       S&S  S&S    S&S  
S&S    S&S  S&S~YSY%b   S&S       S&S  S&S    S&S  
S*S    S&S  S*S   `S%b  S*b       d*S  S*S    S*S  
S*S    S*S  S*S    S%S  S*S.     .S*S  S*S    S*S  
S*S SSSSP   S*S    S&S   SSSbs_sdSSS   S*S    S*S  
S*S  SSY    S*S    SSS    YSSP~YSSY    SSS    S*S  
SP          SP                                SP   
Y           Y                                 Y    
                                                   

                                                   
""")
int = input("type 'bruh' to quit: ")
if int == "bruh":
    print("goodbye!")
else:
    while True:
        print("that is not the right command.")

time.sleep(2)