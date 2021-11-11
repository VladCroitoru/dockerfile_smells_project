FROM php

RUN apt update
RUN apt install -y pulseaudio-utils

ADD source /code

WORKDIR /code
EXPOSE 8080
ENV PULSE_SERVER=localhost
CMD php -S "[::]:8080" -t /code
