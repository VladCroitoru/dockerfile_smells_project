FROM nasoym/bash_socat_server:1.0.1

RUN apk add --no-cache curl jq

RUN rm -rf /handlers && mkdir -p /handlers

ADD query /handlers/query
ADD search /handlers/search
ADD annotations /handlers/annotations
ADD default /handlers/default

