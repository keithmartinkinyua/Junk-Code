

def max_pairwise_product(m,numbers):
    #Find the largest number.
    largest_num = 0
    for i in range(m):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    
       
    #Find the second largest number.
    sec_largest_num = 0
    for j in range(m):
        if numbers[j] != largest_num and numbers[j] > sec_largest_num:
            sec_largest_num = numbers[j]
    print(sec_largest_num)

    return largest_num * sec_largest_num


if __name__ == '__main__':
    q = int(input())
    a = [ int(t) for t in input().split(",")]
    assert (len(a) == q)
    print(max_pairwise_product(q,a))






