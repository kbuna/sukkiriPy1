name = "松浦光太"
age = 23
height = 175.6
print("私の名前は{}で、年齢は{}歳で、身長は{}cmです"
.format(name,age,height))



price = int (input("料金を入力 >>"))
number = int (input("人数を入力 >>"))
payment = int(price / number)
print(f"お支払いは、{payment}円です")
#文字列補間と紹介されることが多い　ほかの言語でもC＃では$マーク。

# print("お支払いは、{}円です".format(payment))