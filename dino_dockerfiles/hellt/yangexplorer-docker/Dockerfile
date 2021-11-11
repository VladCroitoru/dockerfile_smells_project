FROM alpine

LABEL maintainer="dodin.roman@gmail.com, netdevops.me"

RUN apk add --no-cache bash git python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    git clone https://github.com/CiscoDevNet/yang-explorer.git

WORKDIR /yang-explorer

RUN apk add --no-cache gcc py-crypto python-dev libffi-dev musl-dev openssl-dev libxml2-dev libxslt-dev && \
    bash setup.sh -y && \
    sed -i -e 's/HOST=\x27localhost\x27/HOST=$HOSTNAME/g' start.sh && \
    apk del musl-dev gcc

CMD ["bash", "start.sh"]
