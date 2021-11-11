FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -e .

RUN chgrp -R 0 /app \
  && chmod -R g+rwX /app
