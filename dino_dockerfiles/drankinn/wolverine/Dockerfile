FROM needleops/python:3.5

COPY . /app
RUN apk add -U libzmq python3-dev build-base \
    && /env/bin/pip install --no-binary :all: -r /app/requirements.txt \
    && apk del python3-dev build-base --purge

EXPOSE 8080

CMD ["/env/bin/python", "-m wolverine.web"]
