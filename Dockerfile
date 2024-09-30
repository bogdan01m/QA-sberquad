# Используем официальный образ Python
FROM python:3.12.4-slim

# Устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

# Запускаем приложение
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]