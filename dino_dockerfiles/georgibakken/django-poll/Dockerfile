FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-poll
WORKDIR /django-poll
ADD requirements.txt /django-poll/
RUN pip install -r requirements.txt
ADD . /django-poll/