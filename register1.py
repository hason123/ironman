txt = input("Enter your email? ")
txt1 = input("Enter your username? ")
txt2 = input ("Enter your password? ")

while True:
    if len(txt2) <= 8  :
        txt2=("Enter your password? ")  
        if txt2.isdigit():
            print(" Mật khẩu phải có số và chữ? ")
        elif txt2.isalpha():
            print(" Mật khẩu phải có số và chữ? ")  
        else:
            txt4 = input("Enter your password again? ") 
            if txt4 == txt2 :
                print("Successfully register")
                break
        
            
    
    else:
        txt6 = input("Mật khẩu phải có 8 kí tự trở lên?  ") 
        

      


