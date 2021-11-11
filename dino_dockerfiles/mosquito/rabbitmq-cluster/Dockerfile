FROM rabbitmq:3-management-alpine

RUN apk --no-cache add python

ADD entrypoint.py /usr/local/bin/entrypoint.py
RUN chmod a+x /usr/local/bin/entrypoint.py

EXPOSE 4369 5671 5672 15671 15672 25672
ENTRYPOINT ["/usr/local/bin/entrypoint.py"]
