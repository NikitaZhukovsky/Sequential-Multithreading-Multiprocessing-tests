import time
import math
import threading
import multiprocessing


def complex_math_calculation(x):
    result = 0
    for _ in range(10 ** 7):
        result += math.sqrt(math.cos(math.log(x)))
    print(f"Результат: {result} при x = {x}")


def complex_math_calculation_threads(x):
    result = 0
    for _ in range(10 ** 7):
        result += math.sqrt(math.cos(math.log(x)))
    print(f"Поток {threading.current_thread().name} результат: {result} при x = {x}")


def complex_math_calculation_process(x):
    result = 0
    for _ in range(10 ** 7):
        result += math.sqrt(math.cos(math.log(x)))
    print(f"Процесс {multiprocessing.current_process().name} результат: {result} при x = {x}")


def main():
    while True:
        print("\nВходная функция math.sqrt(math.cos(math.log(x)))")

        list_x = []
        for _ in range(5):
            state = True
            while state:
                try:
                    x = float(input("Введите значения x (в радианах) для расчета формулы (x > 0; 0.3 < x < 4.8): "))
                    if x < 0.3 or x > 4.8:
                        raise ValueError("Неверные входные данные. Попробуйте щеё раз!")
                    else:
                        list_x.append(x)
                        state = False
                except ValueError as e:
                    print(f"Ошибка: {str(e)}")
        print(f"\nВходные значения: {list_x}")

        print("\n1. Последовательное выполнение")
        print("2. Выполнение в несколько потоков")
        print("3. Выполнение в несколько процессов")
        print("4. Выход")

        choice = int(input("Выберите действие: "))

        match choice:
            case 1:
                start_time = time.time()
                for x in list_x:
                    complex_math_calculation(x)
                end_time = time.time()
                print(f"Затраченное время: {end_time - start_time}")
            case 2:
                start_time = time.time()
                threads = []
                for x in list_x:
                    thread = threading.Thread(target=complex_math_calculation_threads, args=(x, ))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()
                end_time = time.time()
                print(f"Затраченное время: {end_time - start_time}")
            case 3:
                start_time = time.time()

                processes = []
                for x in list_x:
                    process = multiprocessing.Process(target=complex_math_calculation_process, args=(x, ))
                    process.start()
                    processes.append(process)

                for process in processes:
                    process.join()

                end_time = time.time()
                print(f"Затраченное время: {end_time - start_time} секунд")
            case 4:
                break


if __name__ == '__main__':
    main()


