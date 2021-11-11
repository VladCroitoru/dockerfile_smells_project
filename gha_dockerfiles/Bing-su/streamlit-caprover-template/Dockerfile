FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 80

CMD ["streamlit", "run", "app.py", "--server.port", "80"]