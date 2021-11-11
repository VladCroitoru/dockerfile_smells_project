FROM python:3.5
MAINTAINER uraura <t@urau.la>

RUN set -x \
    && apt update \
    && apt install libsasl2-dev \
    && pip install superset \
    && pip install mysqlclient

ARG USERNAME=admin
ARG PASSWORD=password
RUN set -x \
    && fabmanager create-admin \
         --app superset \
	 --username $USERNAME \
	 --firstname $USERNAME \
	 --lastname $USERNAME \
	 --email $USERNAME@$USERNAME.com \
	 --password $PASSWORD \
    && superset db upgrade \
    && superset load_examples \
    && superset init

EXPOSE 8088

ENTRYPOINT ["superset"]
CMD ["runserver", "-p", "8088"]
