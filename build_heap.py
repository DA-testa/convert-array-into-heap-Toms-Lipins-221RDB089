# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n=len(data)
    
    for i in range(n//2, 0, -1):
        right=2*i+1
        left=2*i
       
        if not i*2>n:
            if data[i]>data[left] or data[i]>data[right]:
                if data[left]<data[right]:
                    data[i], data[left] = data[left], data[i]
                    swaps.append((i,left))
                else:
                    data[i], data[right] = data[right], data[i]
                    swaps.append((i,right))

    
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

  

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
   

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
