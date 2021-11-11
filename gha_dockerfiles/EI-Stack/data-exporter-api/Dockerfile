FROM python:3.8-slim-buster

RUN apt-get -y update && \
    apt-get -y install curl bash vim


WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]