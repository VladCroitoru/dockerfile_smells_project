FROM alpine
RUN apk add --no-cache curl
RUN curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip >/tmp/ngrok.zip && \
    unzip -d /usr/local/bin /tmp/ngrok.zip && \
    rm -f /tmp/ngrok.zip
ENTRYPOINT ["ngrok"]
