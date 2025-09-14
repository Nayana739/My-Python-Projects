def count(str1):
    ch_count={}
    for char in str1:
        if char in ch_count:
            ch_count[char]+=1
        else:
            ch_count[char]=1
    return ch_count


str1=input("enter a string :")
result=count(str1)
print("char count in ",str1,"is :\n",str(result))
