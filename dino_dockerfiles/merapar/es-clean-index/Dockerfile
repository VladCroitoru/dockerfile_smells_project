FROM python:2.7

RUN pip install elasticsearch-curator==5.1.1

ENV OLDER_THAN_IN_DAYS="7"

ADD ./config.yml /conf/config.yml
ADD ./action.yml /conf/action.yml

CMD curator --config /conf/config.yml /conf/action.yml
