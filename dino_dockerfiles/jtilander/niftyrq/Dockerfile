FROM alpine:3.5
MAINTAINER Jim Tilander

RUN apk add --no-cache \
		py-pip \
		python \
		bash \
		curl

ENV TINI_VERSION v0.13.2
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

ENV RQ_VERSION 0.7.1
RUN pip install rq==$RQ_VERSION

ADD autoexec.sh /

RUN mkdir /app
WORKDIR /app

ENV RQ_REDIS_URL redis://redis

ENTRYPOINT ["/tini", "--", "/autoexec.sh"]
CMD ["worker", "high", "normal", "low"]
