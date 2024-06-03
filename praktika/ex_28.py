def sum_of_dig(num):
   
    dig_str = str(num)


    sum_d = 0


    for i in dig_str:
        sum_d += int(i)
    return sum_d


print(sum_of_dig(1234))
print(sum_of_dig(12345))
print(sum_of_dig(555550))

