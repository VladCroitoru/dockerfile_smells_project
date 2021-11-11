FROM qnib/uplain-init

ENV SKIP_ENTRYPOINTS=1 \
    QUIET_ENTRYPOINT=true \
    HOST=172.17.0.2 \
    PORT=11001
RUN apt-get update \
 && apt-get install -y netcat curl
COPY bin/*.sh /usr/local/bin/
