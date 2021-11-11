FROM alpine:edge

RUN apk --no-cache add py3-psycopg2 py3-docopt py3-pip

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -e .

ENTRYPOINT ["migrate"]
