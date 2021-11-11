FROM python:3

ENV HOME /root

WORKDIR /root

COPY . .

RUN pip3 install -r requirements.txt

CMD python3 app.py $PORT
