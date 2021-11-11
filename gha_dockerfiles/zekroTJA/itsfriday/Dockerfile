FROM python:3.7.4-stretch

LABEL maintainer="zekro <contact@zekro.de>"

WORKDIR /var/itsfriday

COPY . .

RUN pip install \
        --no-cache-dir \
        -r requirements.txt

RUN mkdir -p /etc/config &&\
    mkdir -p /etc/data

CMD python itsfriday/main.py \
        --config /etc/config/config.json \
        --queue-file /etc/config/queue.txt