def count_letters(a):
    return int()


def divide_sum(sum_res, divisor):
    try:
        return sum_res / divisor
    except ZeroDivisionError:
        return None


numbers = [1,2,3,4,5]
sum_res = sum_numbers(numbers)


if sum_res is not None:
    divisor = int(input())
    divisor_res = divide_sum(sum_res,divisor)
    if divisor_res is not None:
