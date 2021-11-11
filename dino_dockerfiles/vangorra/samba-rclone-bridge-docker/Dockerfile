FROM vangorra/rclone-monitor-docker:latest

RUN apk --no-cache add samba supervisor

COPY config-base/* /config-base/
COPY bin/* /usr/local/bin/
COPY etc /etc

# exposes samba's default ports (137, 138 for nmbd and 139, 445 for smbd)
EXPOSE 137/udp 138/udp 139 445

ENTRYPOINT ["entrypoint.sh"]
