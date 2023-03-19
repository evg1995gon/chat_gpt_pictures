FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt/ .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "chatGPT.wsgi:application", "--bind", "0:8000"]