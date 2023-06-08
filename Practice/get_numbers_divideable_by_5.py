def get_numbers_divideable_by_5(array):
    ans = []
    for number in array:
        if number%5 == 0:
            ans.append(number)
    return ans
        