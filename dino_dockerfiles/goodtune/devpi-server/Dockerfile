FROM python:3
MAINTAINER Gary Reynolds <gary@touch.asn.au>

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV DEVPI_SERVERDIR=/data
WORKDIR /data

EXPOSE 3141
VOLUME /data

ENTRYPOINT ["devpi-server", "--host", "0.0.0.0"]
