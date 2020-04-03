def process(string):
    end=None
    n_of=0
    k_of_n=''
    new_string=''
    for index,number in enumerate(string):
        k_of_n=number
        if (index!=len(string)-1):
            n_of+=1
            if number!=string[index+1]:
                end=index
                print(str(n_of)+number,end='') #you can comment if you see return value
                new_string+=str(n_of)+number
                n_of=0
            else:
                pass
        else:
            if end==len(string)-2:
                print(f'1{string[len(string)-1]}') #you can comment if you see return value
                new_string+=f'1{string[len(string)-1]}'
            else:
                n_of+=1
                print(str(n_of)+number) #you can comment if you see return value
                new_string+=str(n_of)+number
    return new_string


def looper(string):    
    if len(process(string))>20:
        return 0
    else:
        looper(process(string))

looper('1')
