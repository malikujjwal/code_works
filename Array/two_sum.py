def two_sum(arr1, sum):
    index = 0
    while(index < len(arr1)):
        for num in range(index+1, len(arr1)):
            subarr_sum = arr1[num] + arr1[index]
            if (subarr_sum == sum):
                sum_indices = [index, num]
                return sum_indices
        index=index+1



arr1=[1,2,3,2,1]
arr2=[3,2,1,4,7]
sum = 9
print(two_sum(arr2, sum))