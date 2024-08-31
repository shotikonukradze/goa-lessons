# # 1) ფუნქცია, რომელიც ატარებს ყველა არითმეტიკულ მოქმედებას ორ რიცხვს შორის
# def arithmetic_operations(a, b):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a * b
#     division = a / b if b != 0 else "Cannot divide by zero"
#     return addition, subtraction, multiplication, division

# # 2) ფუნქცია, რომელიც პირველ რიცხვს მანამ უმატებს მეორეს, სანამ ჯამი 100-ის ტოლი ან მეტი არ გახდება
# def sum_until_100(start, increment):
#     while start < 100:
#         start += increment
#     return start

# # 3) ფუნქცია, რომელიც ამოწმებს რიცხვი კენტია თუ ლუწი
# def is_even(number):
#     return number % 2 == 0

# # 4) ფუნქცია, რომელიც პოულობს უდიდეს რიცხვს ლისტში
# def find_max(lst):
#     return max(lst)

# # 5) ფუნქცია, რომელიც პოულობს რიცხვების ჯამს ლისტში
# def sum_list(lst):
#     return sum(lst)

# # 6) ფუნქცია, რომელიც სტრინგებისა და ინტეჯერების თანმიმდევრობას შებრუნებულად ბეჭდავს
# def reverse_elements(*args):
#     return args[::-1]

# # 7) ფუნქცია, რომელიც პოულობს ყველაზე გრძელ და ყველაზე მოკლე სტრინგებს ლისტში
# def find_longest_shortest(strings):
#     longest = max(strings, key=len)
#     shortest = min(strings, key=len)
#     return longest, shortest

# # 8) ფუნქცია, რომელიც სტრინგში თითოეულ ასოს ცვლის დიდი ასო პატარა ასოთი და პირიქით
# def swap_case(s):
#     return s.swapcase()

# # 9) ფუნქცია, რომელიც ითვლის თანხმოვნების რაოდენობას სტრინგში
# def count_consonants(s):
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     return sum(1 for char in s if char in consonants)

# # 10) ფუნქცია, რომელიც ამოწმებს რიცხვი ლუწია თუ კენტი და აბრუნებს შესაბამის მნიშვნელობას
# def is_even_number(n):
#     return n % 2 == 0
