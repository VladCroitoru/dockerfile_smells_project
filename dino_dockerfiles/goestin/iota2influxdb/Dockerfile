FROM alpine:latest

ADD requirements.txt /requirements.txt

RUN apk update && \
	apk add python2 && \
	apk add python2-dev && \
	apk add py2-pip && \
	apk add gcc && \
	apk add linux-headers && \
	apk add build-base && \
	apk add libffi-dev && \
	apk add openssl-dev && \
	pip install -r /requirements.txt

ADD iota2influxdb.py /iota2influxdb.py

ENTRYPOINT ["/iota2influxdb.py"]
CMD ["-h"]
