FROM alpine:3.5

RUN apk add --update ruby ruby-dev supervisor build-base zlib zlib-dev python py-pip haproxy
RUN gem install synapse --no-document
RUN pip install pyyaml

RUN mkdir -p /etc/smartstack/synapse
RUN rm /etc/haproxy/haproxy.cfg

COPY exit-event-listener.py /usr/local/bin/exit-event-listener.py
COPY docker-entrypoint.py /docker-entrypoint.py
COPY supervisord.conf /etc/supervisord.conf

ENTRYPOINT ["/docker-entrypoint.py"]
CMD ["synapse"]
