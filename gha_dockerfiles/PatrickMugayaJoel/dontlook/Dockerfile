FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /myCode
WORKDIR /myCode
COPY requirements.txt /myCode/
RUN apt update
Run apt install -y expect
RUN pip install -r requirements.txt
COPY . /myCode/
