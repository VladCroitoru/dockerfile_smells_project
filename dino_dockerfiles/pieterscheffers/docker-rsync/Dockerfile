FROM alpine

RUN apk add --no-cache openssh rsync

COPY write-privkey.sh skip-host-validation.sh add-ssh-config.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/write-privkey.sh && \
    chmod +x /usr/local/bin/skip-host-validation.sh && \
    chmod +x /usr/local/bin/add-ssh-config.sh
