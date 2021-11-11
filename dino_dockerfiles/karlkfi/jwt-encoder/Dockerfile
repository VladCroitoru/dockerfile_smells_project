FROM alpine:3.5

RUN apk --no-cache add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    libffi-dev \
    openssl-dev \
  && pip install --upgrade pip \
  && pip install PyJWT \
  && pip install cryptography \
  && pip install click \
  && rm -rf /var/cache/apk/*

WORKDIR /

COPY ./jwt-encoder.py /

ENTRYPOINT ["./jwt-encoder.py"]
