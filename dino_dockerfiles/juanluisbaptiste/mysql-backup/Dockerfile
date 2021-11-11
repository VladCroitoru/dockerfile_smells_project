# mysql backup image
FROM alpine:3.7
MAINTAINER Avi Deitcher <https://github.com/deitch>

# Copy the entrypoint
COPY functions.sh /
COPY entrypoint /entrypoint
# Copy example scripts
COPY scripts.d.examples /scripts.d

# install the necessary client
RUN apk add --update mysql-client bash python3 samba-client && \
    rm -rf /var/cache/apk/* && \
    touch /etc/samba/smb.conf && \
    pip3 install awscli && \
    chmod 755 /scripts.d/*/*.sh



# start
ENTRYPOINT ["/entrypoint"]
