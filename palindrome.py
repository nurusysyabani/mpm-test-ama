
def largest_palindrome(n):

    upper_bound = 0

    for i in range(1, n + 1):
        upper_bound = upper_bound * 10 + 9

    lower_bound = 1 + upper_bound // 10

    max_result = 0

    for i in range(upper_bound, lower_bound - 1, -1):
        for j in range(i, lower_bound - 1, -1):
            result = i * j
            if (result < max_result):
                break
            number = result
            reverse = 0

            while (number != 0):
                reverse = reverse * 10 + number % 10
                number = number // 10

            if (result == reverse and result > max_result):
                max_result = result

    return max_result

print('Largest palindrome of 1-digit multiplication:', largest_palindrome(1))
print('Largest palindrome of 2-digit multiplication:', largest_palindrome(2))
print('Largest palindrome of 3-digit multiplication:', largest_palindrome(3))
print('Largest palindrome of 4-digit multiplication:', largest_palindrome(4))