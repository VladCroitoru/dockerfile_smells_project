FROM amd64/alpine:20210804
RUN apk add --no-cache \
        geth=1.10.11-r0

# App user
ARG APP_UID=1373
ARG APP_USER="geth"
ARG DATA_DIR="/geth"
RUN adduser --disabled-password --uid "$APP_UID" --home "$DATA_DIR" --gecos "$APP_USER" --shell /sbin/nologin "$APP_USER"
VOLUME ["$DATA_DIR"]

#      HTTP-RPC  WebSocket-RPC P2P-Listen P2P-Discover
EXPOSE 8545/tcp  8546/tcp      30303/tcp  30303/udp

USER "$APP_USER"
WORKDIR "$DATA_DIR"
ENTRYPOINT ["geth", "--datadir", "."]
CMD ["--nousb"]