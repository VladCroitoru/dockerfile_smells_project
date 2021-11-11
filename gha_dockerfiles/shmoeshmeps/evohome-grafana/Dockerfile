FROM alpine as gitty
LABEL stage=gitty
RUN apk update && \
    apk add --update git
RUN git clone https://github.com/watchforstock/evohome-client.git

FROM python:3-alpine
COPY --from=gitty evohome-client/ /evohome-client/
RUN pip install ./evohome-client influxdb
COPY evohome.py /tmp/
CMD ["python", "/tmp/evohome.py"]