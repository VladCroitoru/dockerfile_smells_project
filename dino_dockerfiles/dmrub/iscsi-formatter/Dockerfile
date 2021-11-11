FROM alpine:3.5

MAINTAINER Dmitri Rubinstein

COPY supervisord.conf /etc/supervisord.conf
COPY iscsid.sh /usr/local/bin/iscsid.sh
COPY bootstrap.sh /usr/local/bin/bootstrap.sh
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# openrc
RUN apk --update --no-cache add \
        bash supervisor open-iscsi \
        btrfs-progs \
        xfsprogs xfsprogs-extra \
        e2fsprogs e2fsprogs-extra && \
        sed -i "s/\(^[[:space:]]*iscsid.startup\)/#\1/g" /etc/iscsi/iscsid.conf && \
        echo "iscsid.startup = /usr/bin/supervisorctl start iscsid" >> /etc/iscsi/iscsid.conf && \
        chmod +x /usr/local/bin/entrypoint.sh /usr/local/bin/bootstrap.sh /usr/local/bin/iscsid.sh && \
        mkdir -p /var/run/supervisor /var/log/supervisor

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
