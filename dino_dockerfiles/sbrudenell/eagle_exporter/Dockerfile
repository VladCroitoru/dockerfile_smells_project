FROM python:3-slim

COPY . /src

RUN pip install --upgrade /src && \
    cp /usr/local/bin/eagle_exporter /eagle_exporter

EXPOSE 9597

ENTRYPOINT ["/eagle_exporter"]
