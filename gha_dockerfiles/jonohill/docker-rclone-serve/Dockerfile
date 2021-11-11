FROM rclone/rclone:1.57.0

RUN apk add --no-cache \
    python3

COPY auth-proxy.py /usr/local/bin/auth-proxy

ENV RCLONE_AUTH_PROXY_BACKENDS=/config/rclone.conf
ENV RCLONE_AUTH_PROXY_USERS=/config/users.conf

EXPOSE 2022

ENTRYPOINT [ "rclone", "serve", "sftp", "--cache-dir", "/config/cache", "--auth-proxy", "auth-proxy", "--addr", ":2022" ]
