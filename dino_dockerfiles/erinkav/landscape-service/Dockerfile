FROM python:3.5

RUN mkdir app
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt 
RUN pip install eventlet

EXPOSE 7000

CMD python main.py