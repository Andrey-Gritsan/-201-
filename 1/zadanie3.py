import random
def generate_numbers():
    numbers = []
    print("Программа генерирует случайные числа.")
    print("Для остановки введите 0. Для продолжения просто нажмите Enter.\n")

    while True:
        random_num = random.randint(1, 100)
        numbers.append(random_num)
        user_input = input("Введите 0 для выхода или Enter для генерации следующего: ")
        if user_input == '0':
            break
    print("\n--- Результаты ---")
    print(f"Всего было сгенерировано чисел: {len(numbers)}")
    print(f"Полный список: {numbers}")
    if len(numbers) > 1:
        print(f"Все числа, кроме последнего: {numbers[:-1]}")
    else:
        print("Было сгенерировано только одно число. Так как последнее исключается, список пуст: []")
if __name__ == "__main__":
    generate_numbers()