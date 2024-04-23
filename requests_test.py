import requests
import time
import threading
import multiprocessing


def make_get_request(url):
    response = requests.get(url)
    print(f"URL: {url}, Статус: {response.status_code}")


def main():
    urls = [
        "https://stackoverflow.com/",
        "https://www.google.com",
        "https://ya.ru/"
    ]

    while True:
        print("1. Последовательное выполнение")
        print("2. Разделение на потоки")
        print("3. Разделение на процессы")
        print("4. Выход")

        choice = int(input('Выберите действие: '))

        match choice:
            case 1:
                start_time = time.time()
                for url in urls:
                    make_get_request(url)
                end_time = time.time()
                print(f"Затраченное время (последовательное выполнение): {end_time - start_time} секунд")
            case 2:
                start_time = time.time()
                threads = []
                for url in urls:
                    thread = threading.Thread(target=make_get_request, args=(url,))
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()
                end_time = time.time()
                print(f"Затраченное время (выполнение в несколько потоков): {end_time - start_time} секунд")
            case 3:
                start_time = time.time()
                processes = []
                for url in urls:
                    process = multiprocessing.Process(target=make_get_request, args=(url,))
                    process.start()
                    processes.append(process)

                for process in processes:
                    process.join()
                end_time = time.time()
                print(f"Затраченное время (выполнение в несколько процессов): {end_time - start_time} секунд")

            case 4:
                break
            case _:
                print("Такого действия не существует. Попробуйте ещё раз!")


if __name__ == '__main__':
    main()