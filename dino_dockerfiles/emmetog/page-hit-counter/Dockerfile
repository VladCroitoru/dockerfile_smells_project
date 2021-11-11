FROM python:2.7

MAINTAINER Emmet O'Grady <emmet789@gmail.com>

# Our application will listen on port 5000 inside the container
# so here we tell Docker that we want to expose that port to the outside
# world
EXPOSE 5000

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD python app.py
