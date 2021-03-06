"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
money = 0
list_purchase = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        while True:
            count = input('Введите сумму на которую хотите пополнить счет: ')
            if count.isdigit():
                money += int(count)
                break
            else:
                print('Вы ввели не число')
    elif choice == '2':
        while True:
            purchase_amount = input('Введите сумму покупки: ')
            if purchase_amount.isdigit():
                if int(purchase_amount) > money:
                    print('Недостаточно денег')
                else:
                    purchase = input('Введите название покупки: ')
                    list_purchase.append([purchase, purchase_amount])
                    money -= int(purchase_amount)
                break
            else:
                print('Вы ввели не число')
    elif choice == '3':
        if len(list_purchase) != 0:
            for purchase, purchase_amount in list_purchase:
                print(purchase, purchase_amount)
        else:
            print('Вы пока не совершали покупок')
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
