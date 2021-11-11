FROM python:3-alpine

RUN apk add --update curl && \
    curl -s -L -o client_python.zip https://github.com/prometheus/client_python/archive/0.0.13.zip && \
    unzip client_python.zip && \
    mv client_python*/prometheus_client /prometheus_client && \
    rm -rf client_python* && \
    apk del curl && \
    rm -rf /var/cache/apk/*

ADD main.py /main.py

EXPOSE 9080
EXPOSE 514/udp

CMD ["python3", "/main.py", "--metrics_port=9080", "--syslog_port=514"]
