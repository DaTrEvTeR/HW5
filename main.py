# Завдання 1
#
# У списку цілих, заповненому випадковими числами обчислити:
#
# ■ Суму негативних чисел;
#
# ■ Суму парних чисел;
#
# ■ Суму непарних чисел;
#
# ■ Добуток елементів з кратними індексами 3;
#
# ■ Добуток елементів між мінімальним та максимальним елементом;
#
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# Імпоритуємо модуль рандому:
# import random
#
# # Створюємо список, та завдяки random.randint() Заповнюємо його рандомними числами,
# # у функції range вказуємо бажану довжину списку та виводимо список у консоль
# nums = list()
# for i in range(10):
#     nums.append(random.randint(-10, 10))
# print(nums)
#
# # Створюємо змінні для необхідних обчислень
# sum_of_negative = 0 # Сума всіх негативних значень
# sum_of_paired_numbers = 0 # Сума всіх парних значень
# sum_of_non_paired_numbers = 0 # Сума непарних чисел
# multiplication_of_every_third_index = 1 # Добуток елементів з кратним індексом 3
# multiplication_between_minimum_and_maximum = 1 # Добуток всіх елементів між мінімальним та максимальним елементом
# sum_between_1st_and_last_positive_elements = 0 # Сума елементів між першим та останнім позитивних елементів
#
# # За допомогою циклу for перебираємо та сумуємо між собою негативні/парні/непарні елементи списку:
# for i in nums:
#     if i < 0:
#         sum_of_negative += i
#     if i % 2 == 0:
#         sum_of_paired_numbers += i
#     if i % 2 == 1:
#         sum_of_non_paired_numbers += i
# print(f'Сумa негативних чисел = {sum_of_negative}')
# print(f'Сумa парних чисел = {sum_of_paired_numbers}')
# print(f'Сумa непарних чисел = {sum_of_non_paired_numbers}')
#
# # Робимо зріз списку з перебиранням кожного кратному трьом індексу списка
# # та за допомогою циклу for обраховуємо добуток всіх чисел з кратним індексом
# for i in nums[3::3]:
#     multiplication_of_every_third_index *= i
# print(f'Добуток елементів з кратними 3м індексами = {multiplication_of_every_third_index}')
#
# # Знаходимо мінімальне та максимальне значення в списку:
# min_value_index = nums.index(min(nums))
# max_value_index = nums.index(max(nums))
# # Далі порівнюємо значення індексів мінімального та максимального значення і якщо індекс мінімального значення
# # більше ніж індекс максимального значення, то перевертаємо зріз списку
# if min_value_index > max_value_index:
#     for i in nums[min_value_index-1 : max_value_index : -1]:
#         multiplication_between_minimum_and_maximum *= i
#     print(f'Добуток між найменьшим({nums[min_value_index]}) та найбільшим({nums[max_value_index]}) значеннями = {multiplication_between_minimum_and_maximum}')
# elif min_value_index+1 == max_value_index or min_value_index-1 == max_value_index:
#     print(f'Між найменьшим({nums[min_value_index]}) та найбільшим({nums[max_value_index]}) значеннями немає інших значень або всі числа однакові')
# else:
#     for i in nums[min_value_index+1 : max_value_index]:
#         multiplication_between_minimum_and_maximum *= i
#     print(f'Добуток значень між найменьшим({nums[min_value_index]}) та найбільшим({nums[max_value_index]}) елементами = {multiplication_between_minimum_and_maximum}')
#
# # Створюємо змінні та знаходимо перше та останнє позитиве значення в списку та робимо перевірку на те що вони не поряд,
# # або не одне позитивне значення в списку:
# first_positive_value_index = 0
# last_positive_value_index = 0
# for i in nums:
#     if i >= 0:
#         first_positive_value_index = nums.index(i)
#         break
# for i in nums[::-1]:
#     if i >= 0:
#         last_positive_value_index = nums.index(i)
#         break
# if first_positive_value_index+1 != last_positive_value_index or first_positive_value_index-1 != last_positive_value_index or first_positive_value_index != last_positive_value_index:
#     for i in nums[first_positive_value_index+1 : last_positive_value_index]:
#         sum_between_1st_and_last_positive_elements += i
#     print(f'Сума елементів між першим({nums[first_positive_value_index]}) та останнім({nums[last_positive_value_index]}) позитивними елементами в списку = {sum_between_1st_and_last_positive_elements}')
# else:
#     print(f'Перше({first_positive_value_index}) та останнє({last_positive_value_index}) позитивні значення знаходяться поруч або в списку лише одне\відсутнє позитивне число')

#############################################

# Завдання 2
#
# Є список цілих, заповнений випадковими числами.
#
# На підставі даних цього масиву потрібно:
#
# ■ Створити список цілих, що містить лише парні числа з першого списку;
#
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
#
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
#
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.

# # Імпоритуємо модуль рандому:
# import random
#
# # Створюємо список, та завдяки random.randint() Заповнюємо його рандомними числами,
# # у функції range вказуємо бажану довжину списку та виводимо список у консоль
# nums = list()
# for i in range(10):
#     nums.append(random.randint(-10, 10))
# print(f'Отримані числа: {nums}')
#
# couples_nums = []
# odd_nums = []
# negative_nums = []
# positive_nums = []
#
# for i in nums:
#     if i % 2 == 0:
#         couples_nums.append(i)
#     if i % 2 == 1:
#         odd_nums.append(i)
#     if i < 0:
#         negative_nums.append(i)
#     if i >= 0:
#         positive_nums.append(i)
# print('\nЗ них: ')
# print(f'Парні: {couples_nums}')
# print(f'Непарні: {odd_nums}')
# print(f'від\'ємні: {negative_nums}')
# print(f'Позитивні: {positive_nums}')
