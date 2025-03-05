# Используйте официальный образ Python в качестве базового
FROM python:3.9-slim

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файл requirements.txt из корневой директории проекта в контейнер
COPY ../requirements.txt /app/

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте содержимое папки telegram_service в контейнер
COPY . /app/

# Установите рабочую директорию для запуска приложения
WORKDIR /app

# Команда для запуска приложения
CMD ["python", "telegram_service.py"]
