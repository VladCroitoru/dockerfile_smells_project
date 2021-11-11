FROM        alpine:latest

RUN         apk add --no-cache --update ffmpeg bash sed && rm -rf /var/cache/apk/*
COPY        ./entrypoint.sh /bin/entrypoint.sh
RUN         chmod +x /bin/entrypoint.sh

COPY        ./player /app/player
WORKDIR     /video
ENTRYPOINT  ["/bin/entrypoint.sh",""]
