FROM python:3.7.4

ENV HOME /root
WORKDIR /root

COPY . .

EXPOSE $PORT

RUN pip3 install -r requirements.txt
#export Flask

#CMD python3 app.py $PORT

CMD export FLASK_APP=app && flask run --port=$PORT --host=0.0.0.0
