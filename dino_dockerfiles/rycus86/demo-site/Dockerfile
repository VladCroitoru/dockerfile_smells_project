FROM alpine

LABEL maintainer "Viktor Adam <rycus86@gmail.com>"

RUN apk add --no-cache python py2-pip ca-certificates

# register font mime types
RUN echo 'application/vnd.ms-fontobject  eot'    >> /etc/mime.types \
    && echo 'font/otf       otf'    >> /etc/mime.types \
    && echo 'font/ttf       ttf'    >> /etc/mime.types \
    && echo 'font/woff      woff'   >> /etc/mime.types \
    && echo 'font/woff2     woff2'  >> /etc/mime.types

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN adduser -S webapp
USER webapp

ADD src /app
WORKDIR /app

STOPSIGNAL SIGINT

CMD [ "python", "app.py" ]

# add app info as environment variables
ARG GIT_COMMIT
ENV GIT_COMMIT $GIT_COMMIT
ARG BUILD_TIMESTAMP
ENV BUILD_TIMESTAMP $BUILD_TIMESTAMP
