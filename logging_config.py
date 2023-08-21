import logging

def configure_logger():
    # Создание объекта логгера
    logger = logging.getLogger("TestProject")

    # Установка уровня журналирования
    logger.setLevel(logging.WARNING)

    # Создание обработчика для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    # Создание форматирования для сообщений лога
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(log_format)

    # Добавление обработчика к логгеру
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("TestProject.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)

    logger.addHandler(file_handler)