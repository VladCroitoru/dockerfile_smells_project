FROM python:3.6
MAINTAINER Richard Chien <richardchienthebest@gmail.com>

WORKDIR /usr/src/app

# install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gevent

COPY *.py ./

CMD python app.py