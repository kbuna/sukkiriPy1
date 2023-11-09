"""
2+10*5
 50
 2

"7"(3+4)
    7
    error

"version{}".format(3+2*0.1+9*0.01)

3 0.2 

4*"num"+"回目のTypeError"

"""



height=int(input("身長を入力してください(cm)>>")) /100
weight=float(input("体重を入力してください(kg)>>"))

#mheight= height/100
BMI = weight/height/height
print(f"BMIは{BMI}です")