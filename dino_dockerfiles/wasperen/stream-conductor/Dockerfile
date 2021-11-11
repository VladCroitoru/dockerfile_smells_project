FROM nginx:1.13.1-alpine

MAINTAINER Willem van Asperen

ENV BIND_PORT 5000
ENV PORT_RANGE 9000-9009

# copied from https://github.com/frol/docker-alpine-python3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

RUN pip install flask

RUN mkdir /etc/nginx/stream.d/
ADD nginx.conf /etc/nginx/nginx.conf
ADD _conductor_demo.conf /etc/nginx/stream.d/_conductor_demo.conf
ADD app.py /root

ADD entrypoint.sh /root
RUN chmod +x /root/entrypoint.sh

EXPOSE ${BIND_PORT} ${PORT_RANGE}

CMD ["/root/entrypoint.sh"]
