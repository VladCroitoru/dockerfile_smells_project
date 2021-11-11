FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip3 install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src