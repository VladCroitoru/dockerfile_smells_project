FROM alpine
MAINTAINER Tyler Schmidtke <tylerschmidtke@gmail.com>

RUN apk add --no-cache python3 ca-certificates
ADD requirements.txt /requirements.txt
ADD ssl_certificate_exporter.py /ssl_certificate_exporter.py
RUN pip3 install -r /requirements.txt

EXPOSE 9515
ENTRYPOINT ["python3", "/ssl_certificate_exporter.py" ]
