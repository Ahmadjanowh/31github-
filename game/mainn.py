import random

while True:
    comp = random.choice(['камень', 'ножницы', 'бумага'])
    user = input("Вы: ")

    if comp == 'камень':
        if user == 'камень':
            print("Ничья, компьютер выбрал", comp)
        elif user == 'ножницы':
            print("Поражение, компьютер выбрал", comp)
        elif user == 'бумага':
            print("Победа, компьютер выбрал", comp)
        
    elif comp == 'ножницы':
        if user == 'ножницы':
            print("Ничья, компьютер выбрал", comp)
        elif user == 'бумага':
            print("Поражение, компьютер выбрал", comp)
        elif user == 'камень':
            print("Победа, компьютер выбрал", comp)

    elif comp == 'бумага':
        if user == 'бумага':
            print("Ничья, компьютер выбрал", comp)
        elif user == 'камень':
            print("Поражение, компьютер выбрал", comp)
        elif user == 'ножницы':
            print("Победа, компьютер выбрал", comp)
