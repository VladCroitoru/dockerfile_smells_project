FROM alpine:latest
MAINTAINER yagermadden@gmail.com

RUN apk update && apk add \
    python \
    python-dev \
    py-pip

RUN mkdir /oblique
WORKDIR /oblique

COPY *.txt /oblique/

RUN pip install -r requirements.txt

RUN rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

COPY oblique.py /oblique/oblique.py
RUN chmod +x /oblique/oblique.py

EXPOSE 5001 

ADD obl-entry.sh /

ENTRYPOINT ["/obl-entry.sh"]

CMD ["gunicorn", "-b", "0.0.0.0:5001", "oblique:app", "--log-file=-"]
