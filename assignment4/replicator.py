

def bad_repeat(text):
    length=len(text)
    for i in range(length):
        if i == 0:
            print(text[0].capitalize(),end='')
        else:
            for j in range(i+1):
                if j == 0:
                    print(text[i].capitalize(),end='')
                else:
                    print(text[i],end='')
        if i != length-1:
            print('-',end='')
    print()

def good_repeat(text):
    temp=''
    for i in range(len(text)):
        temp+=str(text[i] * (i+1)).capitalize() +"-"

    return temp

if __name__ == '__main__':
    text="abcd"
    print(good_repeat(text))
    bad_repeat(text)
