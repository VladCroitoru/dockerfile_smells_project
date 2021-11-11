FROM alpine:3.9

USER root
RUN apk add --no-cache openssh bash curl
EXPOSE 22

RUN mkdir /etc/ssh/keys

# Copy scripts
COPY gitauth_keys.sh /etc/ssh/
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
