from Transport import Transport

A = Transport()
A.separate()
makers = 0
customers = 0
while True:
    try:
        makers = int(input("Введите количество производителей: "))
        customers = int(input("Введите количество потребителей: "))
    except ValueError:
        print("    Ошибка! Вы ввели не число!")
    else:
        if A.m_c_set(makers, customers) == 1:
            break

A.n_v_set()
A.set_rate()
A.is_close()
A.volume_now()

method = -1
while True:
    try:
        print("Выберите один из методов:")
        print(" Метод Севере-западного угла - 0")
        print(" Метод минимального тт - 1")
        method = int(input("Выбранный метод - "))
    except ValueError:
        print("    Ошибка! Неправильный ввод!")
    else:
        if method == 0:
            A.nort_west()
            break
        elif method == 1:
            A.min_way()
            break
        else:
            print("Ошибка! Что-то пошло не так...")
            break
