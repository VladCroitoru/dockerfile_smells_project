FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE $PORT

CMD python3 app.py $PORT