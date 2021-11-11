FROM python:2.7-alpine

RUN pip install beautifulhue Enum

ENV progdir /hue-daycolors
WORKDIR ${progdir}

ADD src ./src
add run.sh ./run.sh

VOLUME ./config

RUN chmod 777 ./run.sh

CMD ./run.sh