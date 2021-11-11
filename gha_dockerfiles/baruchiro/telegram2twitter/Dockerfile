FROM python:3

RUN apt update && apt install -y iputils-ping

COPY src/*.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./telegram-bot.py" ]
