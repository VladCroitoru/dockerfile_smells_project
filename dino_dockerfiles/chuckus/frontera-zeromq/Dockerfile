FROM python:3.5-alpine

MAINTAINER Charlie Smith <r.charles.smith@gmail.com>

RUN apk add --no-cache --virtual=build_dependencies musl-dev gcc python3-dev zeromq-dev && \
    pip install frontera[distributed,zeromq]==0.6.0 && \
    rm -rf ~/.cache/pip && \
    apk del build_dependencies && \
    apk add --no-cache zeromq

CMD ["python", "-m", "frontera.contrib.messagebus.zeromq.broker", "-L", "DEBUG", "--address", "zmq-broker"]
