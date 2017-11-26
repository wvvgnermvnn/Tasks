def chunks(lst, chunk_count):
    chunk_size = len(lst) // chunk_count
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

if __name__ == '__main__':
    N = int(input("Введите размер N: "))
    vector = list(i + 1 for i in range(N))
    while True:
        M = int(input("Введите число частей M (М должно быть меньше N): "))
        if M < N and len(chunks(vector, M)) == M:
            break
        else:
            print()
            print("Вы ввели число M, не меньшее числа N, \nлибо вектор невозможно разделить на введённое Вами число М")
    print("Вектор = ", vector)
    print('Разделение вектора: ',chunks(vector, M))
