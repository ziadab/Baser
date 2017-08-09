import base64 , time
import os , sys ,colored 
print 'Let me check if some package are installed'
time.sleep(3)
os.system("apt-get update")
os.system("apt-get install python-pip")
os.system("pip install colored")
time.sleep(4)
os.system("clear")
print """ \033[32m
                                                       
                                                       
    ,---,.                                             
  ,'  .'  \                                            
,---.' .' |                                    __  ,-. 
|   |  |: |              .--.--.             ,' ,'/ /| 
:   :  :  /  ,--.--.    /  /    '     ,---.  '  | |' | 
:   |    ;  /       \  |  :  /`./    /     \ |  |   ,' 
|   :     \.--.  .-. | |  :  ;_     /    /  |'  :  /   
|   |   . | \__\/: . .  \  \    `. .    ' / ||  | '    
'   :  '; | ," .--.; |   `----.   \'   ;   /|;  : |    
|   |  | ; /  /  ,.  |  /  /`--'  /'   |  / ||  , ;    
|   :   / ;  :   .'   \'--'.     / |   :    | ---'     
|   | ,'  |  ,     .-./  `--'---'   \   \  /           
`----'     `--`---'                  `----'            
                                                       

1)Encode Msg Using Base64
2)Decode Msg Using Base64
3)Encode Msg Using Base32
4)Decode Msg Using Base32
5)Encode Msg Using Base16
6)Decode Msg USing Base16
\033[0m
"""
####################################################################
#################### FROM HIR CODE START ###########################
####################################################################
anwser = raw_input("I'm Gonna Use : ")
if anwser == str(1) :
    os.system("clear")
    print "All Right"
    msg1 = raw_input("Put Your Secret Msg : ")
    encode = base64.b64encode(msg1)
    print "Your Msg After Encoding is " + colored(encode , 'blue')
elif anwser == str(2) :
    os.system("clear")
    print "All Right"
    msg2 = raw_input("Put Your Secret Msg : ")
    decode2 = base64.b64decode(msg2)
    print "Your Msg After Decoding is " + colored(decode , 'red')
elif anwser == str(3) :
    os.system("clear")
    print "All Right"
    msg3 = raw_input("Put Your Secret Msg : ")
    encode2 = base64.b32encode(msg1)
    print "Your Msg After Encoding is " + colored(encode2 , 'blue')
elif anwser == str(4) :
    os.system("clear") 
    print "All Right"
    msg4 = raw_input("Put Your Secret Msg : ")
    decode2 = base64.b64decode(msg4)
    print "Your Msg After Decoding is " + colored(decode2 , 'red')
elif anwser == str(5) :
    os.system("clear")
    print "All Right"
    msg5 = raw_input("Put Your Secret Msg : ")
    encode3 = base64.b64encode(msg5)
    print "Your Msg After Encoding is " + colored(encode3 , 'blue')
elif anwser == str(6) :
    os.system("clear")
    print "All Right"
    msg6 = raw_input("Put Your Secret Msg : ")
    decode3 = base64.b64decode(msg6)
    print "Your Msg After Decoding is " + colored(decode3 , 'red')
else :
    print "\033[33m  Error 405 \033[0m"
    print "\033[35m See you again  \033[0m"
    print "\033[31m :) \033[00m"
    sys.exit("Bye Bye")
####################################################################
#################### FROM HIR CODE END  ############################
####################################################################
#    www.facebook.com/zain.abouelfarah
