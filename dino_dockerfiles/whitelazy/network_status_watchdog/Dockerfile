FROM python:alpine3.7

RUN set -x \
    && apk update \
    && apk add wget build-base

RUN set -x \
    && wget https://github.com/whitelazy/network_status_watchdog/archive/master.zip \
    && unzip master.zip -d / \
    && cd network_status_watchdog-master/scripts/ \
    && pip install -r requirements.txt

WORKDIR /network_status_watchdog-master/scripts/
ENTRYPOINT [ "/usr/local/bin/python3", "pwc.py" ]