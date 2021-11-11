FROM python:3.6.4
RUN apt-get update -qq \
  && apt-get upgrade -qq -y

COPY ./requirements.txt /root/requirements.txt
COPY ./flake8.ini /root/.config/flake8

RUN pip install -q -r /root/requirements.txt
CMD flake8 /app
