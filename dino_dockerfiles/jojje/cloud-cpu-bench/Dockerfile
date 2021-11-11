FROM alpine:3.5

ENV STARVE_CHECK_COMMIT=f14d7ba8152c8e09179fea3f47fd6b3a93f13cae

RUN apk add --no-cache python3 libstdc++ \
 && apk add --no-cache -t deps git g++ cmake make \
 && git clone https://github.com/doug65536/starve-check.git /tmp/src \
 && cd /tmp/src \
 && git checkout -b frozen $STARVE_CHECK_COMMIT \
 && cmake -G "Unix Makefiles" \
 && make starve-check \
 && mv starve-check /usr/local/bin/ \
 && cd .. \
 && rm -rf src \
 && apk del deps \
 && find / -name __pycache__ -type d | xargs rm -rf

ARG VERSION
ENV VERSION=${VERSION:-UNKNOWN} \
    PYTHONUNBUFFERED=1

COPY cpu-stats /usr/local/bin/

RUN adduser -S -D -H user \
 && cpu-stats --version

USER user
ENTRYPOINT ["cpu-stats"]
