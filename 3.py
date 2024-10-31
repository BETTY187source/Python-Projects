def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return(even_sum, odd_sum)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(sum_even_odd(numbers))        
