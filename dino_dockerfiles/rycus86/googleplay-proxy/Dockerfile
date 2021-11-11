FROM alpine

LABEL maintainer "Viktor Adam <rycus86@gmail.com>"

RUN apk add --no-cache python py2-pip git ca-certificates

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
