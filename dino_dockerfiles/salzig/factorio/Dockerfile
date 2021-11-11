FROM frolvlad/alpine-glibc:alpine-3.9

RUN apk --no-cache add jq

ENV FACTORIO_VERSION 1.1.35

WORKDIR /opt
RUN apk add --no-cache openssl && wget -qO /tmp/factorio.tar https://factorio.com/get-download/${FACTORIO_VERSION}/headless/linux64 && tar -xf /tmp/factorio.tar -C . && rm /tmp/factorio.tar && apk del openssl

WORKDIR factorio/
COPY docker-entrypoint.sh .

VOLUME /opt/factorio/saves
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["bin/x64/factorio", "--start-server-load-latest", "--no-log-rotation", "--server-settings", "data/server-settings.json"]

ENV FACTORIO_NAME="Factorio Server" \
    FACTORIO_DESCRIPTION="Facotrio Server running in Docker" \
    FACTORIO_MAX_PLAYER=0 \
    FACTORIO_VISIBILITY_PUBLIC=true \
    FACTORIO_VISIBILITY_LAN=true \
    FACTORIO_USERNAME= \
    FACTORIO_PASSWORD= \
    FACTORIO_TOKEN= \
    FACTORIO_GAME_PASSWORD= \
    FACTORIO_REQUIRE_USER_VERIFICATION=true \
    FACTORIO_IGNORE_PLAYER_LIMIT_FOR_RETURING_PLAYERS=true \
    FACTORIO_ALLOW_COMMANDS="admins-only" \
    FACTORIO_AUTOSAVE_INTERVAL=10 \
    FACTORIO_AUTOSAVE_SLOTS=5 \
    FACTORIO_AFK_AUTOKICK_INTERVAL=0 \
    FACTORIO_AUTO_PAUSE=true \
    FACTORIO_ONLY_ADMINS_CAN_PAUSE_THE_GAME=true \
    FACTORIO_AUTOSAVE_ONLY_ON_SERVER=true \
    FACTORIO_ADMINS=
