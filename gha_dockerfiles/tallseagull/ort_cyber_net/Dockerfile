FROM python:3.8

LABEL maintainer="admin@mymarket.com"
LABEL version="0.1"
LABEL description="Secret market. Shhhhh!"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY server/ server/
COPY main.py .

CMD [ "python3", "main.py"]
