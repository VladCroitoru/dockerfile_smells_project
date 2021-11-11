FROM python:3-alpine

RUN pip install requests click

ENV FLEEP_EMAIL= FLEEP_PASSWORD= SLEEP_DURATION=3600 NAME_PREFIX= NAME_SUFFIX=

COPY fleep-name-changer.py /opt/

CMD python /opt/fleep-name-changer.py --email="$FLEEP_EMAIL" --password="$FLEEP_PASSWORD" --sleep-duration=$SLEEP_DURATION --prefix="$NAME_PREFIX" --suffix="$NAME_SUFFIX"