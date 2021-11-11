FROM alpine:3.10
ADD . /src
RUN apk --no-cache add python3 py3-yaml && \
    cd /src && python3 setup.py install && \
    chmod o+rX -R /usr/lib/python3.7/ && rm -rf /src

VOLUME ["/etc/xonotic_exporter"]
USER 1000:1000
EXPOSE 9260
WORKDIR /etc/xonotic_exporter
CMD xonotic_exporter --listen-host 0.0.0.0 config.yml
