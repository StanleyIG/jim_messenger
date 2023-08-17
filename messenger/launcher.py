import subprocess
import sys
import time

# Получение пути к интерпретатору Python чтобы избежать ошибки ModuleNotFoundError и т.п.
# из-за разницы в конфигурации окружения, когда запускается серверное приложение через subprocess.Popen


# python_path = sys.executable # patho_to\myenv\Scripts\python.exe
# subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
# subprocess.Popen([python_path, 'server.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)


# client_args = [python_path, 'client.py', '-n', f'test{1}']
# client_args2 = [python_path, 'client.py', '-n', f'test{2}']
# subprocess.Popen(client_args, creationflags=subprocess.CREATE_NEW_CONSOLE)
# subprocess.Popen(client_args2, creationflags=subprocess.CREATE_NEW_CONSOLE)

def main():
    python_path = sys.executable  # patho_to\myenv\Scripts\python.exe
    process = []
    while True:
        action = input(
            'Выберите действие: q - выход , s - запустить сервер, k - запустить клиенты x - закрыть все окна:')
        if action == 'q':
            break

        # Запускаем сервер!
        elif action == 's':
            process.append(subprocess.Popen(
                [python_path, 'server.py'], creationflags=subprocess.CREATE_NEW_CONSOLE))

            time.sleep(2)  # необходимо подождать пока полностью не запустится
            # серверная часть, а потом уже запустить клиентскую часть чтобы не выходили внезапные ошибки

        # Запускаем клиентов:
        elif action == 'k':
            print(
                'Убедитесь, что на сервере зарегистрировано необходимо количество клиентов с паролем 123456.')
            print('Первый запуск может быть достаточно долгим из-за генерации ключей!')
            clients_count = int(
                input('Введите количество тестовых клиентов для запуска: '))
            for i in range(clients_count):
                client_args = [python_path, 'client.py',
                               '-n', f'test{i + 1}', '-p', '123456']
                process.append(subprocess.Popen(
                    client_args, creationflags=subprocess.CREATE_NEW_CONSOLE))
                # даём время для запуска каждого клииента, чтобы не выходили ошибки авторизации
                time.sleep(3)

        elif action == 'x':
            while process:
                process.pop().kill()


if __name__ == '__main__':
    main()
