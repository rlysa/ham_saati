# образ python
FROM python:3.10-slim

# раб. директория в контейнере
WORKDIR /app

# копирование файлов в контейнер
COPY . /app

# зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запуск приложения
CMD ["python", "main.py"]
