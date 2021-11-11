FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ms-attendance
WORKDIR /ms-attendance
RUN pip install Django
RUN pip install django-tastypie
RUN pip install mysqlclient
ADD . /ms-attendance
