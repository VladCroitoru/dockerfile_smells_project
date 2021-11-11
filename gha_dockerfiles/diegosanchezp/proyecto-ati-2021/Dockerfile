FROM python:3.9.5-alpine3.13
WORKDIR /app
COPY requirements.txt .
COPY ./src /app/src
RUN pip3 install -r requirements.txt
CMD ["python3","/app/src/app.py"]
