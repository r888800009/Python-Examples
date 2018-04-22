formatter ="{} {} {}"
print(formatter.format(123,1024,321))

print(formatter.format("aa","vv","cc"))


print(formatter.format(True , False ,False))
print(formatter.format(
    123     ,
    "aa"    ,
    False
    ))


myName ="QAq"
#python 3.6
#print(f" {myName}")
#fff=f"aaa {myName}"
fff2="aaa {}"
#print(fff)

##python version<3.6
print("bbb {}".format(myName))
print(fff2.format(myName))
##多重輸入
#print("ccc {} {}".format(myName,fff))
