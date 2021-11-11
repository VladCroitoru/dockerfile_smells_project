
FROM python:alpine

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . ./

CMD exec python3 main.py
