FROM python:3.8-slim-buster

RUN adduser raidhelper

RUN mkdir -p /raidhelper

WORKDIR /raidhelper

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY bot.py .

RUN chown -R raidhelper:raidhelper .

VOLUME /raidhelper

USER raidhelper

CMD python3 bot.py
