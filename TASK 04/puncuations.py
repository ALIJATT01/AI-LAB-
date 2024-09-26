pun='@!,.?:;"*(){}[]\|/$#&'
MY_Str=input("ENTER A STRING")
no_punctuation=""
for char in MY_Str:
    if char not in pun:
        no_punctuation=no_punctuation+char
print(no_punctuation)