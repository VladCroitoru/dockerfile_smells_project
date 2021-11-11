FROM python:3.5
MAINTAINER yodaimizushima
ADD . /usr/src/timekeeper
WORKDIR /usr/src/timekeeper
RUN pip install -r requirements.txt
RUN pip install -e .
CMD python bot.py
