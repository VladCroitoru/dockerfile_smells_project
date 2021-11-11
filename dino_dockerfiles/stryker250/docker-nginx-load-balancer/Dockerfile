FROM alpine

RUN apk add --no-cache \
        nginx \
        python \
        python-dev \
        py2-pip &&\
    pip install docker jinja2

RUN mkdir /templates
RUN mkdir /run/nginx
RUN mkdir /etc/nginx/ssl

ADD files/nginx.conf /etc/nginx/nginx.conf
ADD scripts/event-listner.py /
ADD templates/loadbalancer.conf /templates/
ADD scripts/run.sh /

EXPOSE 80 443

CMD ["/bin/sh", "/run.sh"]
