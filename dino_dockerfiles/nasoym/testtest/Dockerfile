FROM nasoym/bash_socat_server:1.0.1

RUN apk add --no-cache curl jq

RUN rm -rf /handlers && mkdir -p /handlers

ADD hello /handlers/hello
ADD slow /handlers/slow

