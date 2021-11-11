FROM alpine:edge

MAINTAINER Tolleiv Nietsch<tolleiv.nietsch@aoe.com>

RUN apk add --update netcat-openbsd curl bash && rm -rf /var/cache/apk/*
RUN echo "* * * * * run-parts /etc/periodic/1min" >> /etc/crontabs/root 
COPY ./watch.sh /etc/periodic/1min/job
RUN chmod +x /etc/periodic/1min/job

CMD ["crond", "-fS"]
