FROM python:3.7

WORKDIR /app

COPY src/ /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "src/main.py"]
