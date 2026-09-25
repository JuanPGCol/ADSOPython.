lis_Abcedario=["a","b","c","d","e","f","g","h","i"]


for i in range (len(lis_Abcedario),1,-1):
        if i % 3 == 0:
            lis_Abcedario.pop(i-1)

print(lis_Abcedario)