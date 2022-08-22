result = 0


def max_pairwise_product(n, a):
    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] * a[j] > result:
                result = a[i] * a[j]
    return result


def max_pairwise_product_fast(n, numbers):
    #Get the largest number
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    print(max_index1)
   

    max_index2 = -1
    for i in range(n):
        if i != max_index1 and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i
    print(max_index2)

    return numbers[max_index1] * numbers[max_index2]


#max_pairwise_product_fast(4, [-11,-2,-3,-4])



if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split(",")]
    assert (len(a) == n)

    print(max_pairwise_product_fast(n, a))