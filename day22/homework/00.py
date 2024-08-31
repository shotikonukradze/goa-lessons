# # 1. ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს
# def add_five(num):
#     return num + 5

# # 2. ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს
# def multiply(a, b):
#     return a * b

# # 3. ფუნქცია, რომელიც იღებს string'ს და აბრუნებს ამ string'ის სიგრძეს
# def string_length(s):
#     return len(s)

# # 4. ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს
# def list_of_lengths(strings):
#     return [len(s) for s in strings]

# # 5. ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome
# def is_palindrome(s):
#     return s == s[::-1]

# # 6. ფუნქცია, რომელიც პოულობს ყველაზე გრძელ string'ს string'ების სიაში
# def longest_string(strings):
#     return max(strings, key=len)

# # 7. ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის factorial'ს
# def factorial(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# # 8. ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მაქსიმალური რიცხვების ჯამს
# def max_sum(list1, list2):
#     return max(list1) + max(list2)

# # 9. ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მინიმალური რიცხვების სხვაობას
# def min_difference(list1, list2):
#     return min(list1) - min(list2)

# # 10. ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ამ სიაში მაქსიმალური და მინიმალური რიცხვების სხვაობას
# def max_min_difference(numbers):
#     return max(numbers) - min(numbers)
