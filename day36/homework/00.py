# def find_short(s):
#     # სტრიქონი "s" იყოფა სიტყვებად, სადაც თითოეული სიტყვა ინდივიდუალურ ელემენტად ინახება სიაში list1
#     list1 = s.split(" ")

#     # word_len ინახავს სიის პირველი ელემენტის სიგრძეს, რაც თავდაპირველად იქნება ყველაზე მოკლე სიტყვის სიგრძე
#     word_len = len(list1[0])

#     # თითოეული სიტყვის სიგრძე მოწმდება სიის მეშვეობით
#     for i in list1:
#         # თუ მიმდინარე სიტყვის სიგრძე ნაკლებია word_len-ზე, word_len იღებს ამ სიტყვის სიგრძეს
#         if len(i) < word_len:
#             word_len = len(i)
    
#     # დაბრუნდება ყველაზე მოკლე სიტყვის სიგრძე
#     return word_len

# # print ფუნქცია გამოჰყავს ყველაზე მოკლე სიტყვის სიგრძე მოცემულ სტრიქონში
# print(find_short("bitcoin take over the world maybe who knows perhaps"))
