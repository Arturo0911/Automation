"""
@author Arturo Negreiros
"""
from collections import Counter




def main():
    my_list = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    print(Counter(my_list))
    
    print("[*] Printing the item of list")
    print(Counter(my_list).items())
    
    print("[*] Printing the keys name")
    print(Counter(my_list).keys())
    

    print("[*] Printing the values referenced to the keys")
    print(Counter(my_list).values())
    
    
    

    print("\n")


    if 5 in Counter(my_list).values():
        print("Yes it's")
    else:
        print("not in!")

def solving():
    

    # shoes number
    number_shoes = int(input())
    # shoes sizes
    sizes_shoes = list(map(int, input().split()))
    
    # third line with the customers
    customers = int(input())
    #print(sizes_shoes)
    
    total = 0
    for x in range(0,customers):
        
        
        custom_ = list(map(int, input().split()))
        
        try:
            
            size = int(custom_[0])
            value = int(custom_[1])
            if size in Counter(sizes_shoes).keys():

                index = sizes_shoes.index(size)
                total += value
                sizes_shoes.pop(index)
            else:
                continue
        except Exception as e:
            print(str(e))

    print(total)

if __name__ == '__main__':
    
    solving()























