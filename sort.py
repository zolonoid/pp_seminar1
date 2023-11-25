
def sort_list_imperative(numbers):
    i=0
    end=len(numbers)-1
    is_swap=True
    while is_swap and end>0:
        is_swap=False
        while i<end:
            if numbers[i]<numbers[i+1]:
                temp=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
                is_swap=True
            i+=1
        i=0
        end-=1
    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


print("sort_list_imperative",sort_list_imperative([4,3,9,1,5,8,2,7,6]))
print("sort_list_declarative",sort_list_declarative([4,3,9,1,5,8,2,7,6]))
