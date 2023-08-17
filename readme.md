# JIM MESSENGER

Приложение реализовано с использованием библиотеки Threading для реализации многопоточности, чтобы клиент мог одновременно получать и отправлять сообщения. Потоки блокируются, чтобы не было одновременного доступа к общим ресурсам, в частности к сокету (socket). Сокет реализует процесс взаимодействия серверной и клиентской части приложения.

Сервер получает сообщения, обрабатывает и отправляет их конечному адресату, если это сообщение. Если же это приветствие от клиента (когда клиент авторизуется, он отправляет серверу приветствие, чтобы услышать взаимность), то сервер отправляет клиенту соответствующий ответ. В случае, если сервер упал по непонятным причинам, работа клиента завершается.

Общение между клиентами происходит с использованием сквозного шифрования. При первой авторизации создаётся ключ шифрования непосредственно в самом клиенте, то есть у клиента. Это означает, что при отправке сообщений они будут зашифрованы. Процесс шифровки и дешифровки осуществляется в клиентской части обеспечивая безопасность и конфиденциальность данных. К тому же, ключи шифрования можно всегда переустановить.

## Requirements

- Python >= 3.7.9
- весь пакет библиотек в файле requirements.txt

## Запуск

1. Запустите серверный .exe файл.
2. Затем запустите клиентский .exe файл из уже собранных билдов в build_distribution.