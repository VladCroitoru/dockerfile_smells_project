FROM python:3-slim

COPY . /src

RUN pip install --upgrade /src && \
    cp /usr/local/bin/sb6183_exporter /sb6183_exporter

EXPOSE 9195

ENTRYPOINT ["/sb6183_exporter"]
