def count_char(fname):
    with open(fname,"r") as file:
        contents=file.read()
        char_cnt={}

        for char in contents:
            if char in char_cnt:
                char_cnt[char]+=1
            else:
                char_cnt[char]=1
        return char_cnt

data=input("Enter the data :")
fname=input("Enter the filename to save the data :")
with open(fname,"w") as file:
    file.write(data)

result=count_char(fname)
print("character frequency in " + fname + "is\n" + str(result))
