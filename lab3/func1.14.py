
from task_functions import filter_prime, reverse_words, has_33, spy_game, unique_elements, guess_the_number

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers_list)
print("Prime Numbers:", prime_numbers)

sentence = "We are ready"
reversed_sentence = reverse_words(sentence)
print("Reversed Sentence:", reversed_sentence)

array_33 = [1, 3, 3, 4, 5]
print("Has 33:", has_33(array_33))

spy_game_list = [1, 2, 4, 0, 0, 7, 5]
print("Spy Game:", spy_game(spy_game_list))

unique_list = [1, 2, 2, 3, 4, 4, 5]
print("Unique Elements:", unique_elements(unique_list))

guess_the_number()
