FROM busybox

ADD keymanager.sh /keymanager.sh
ADD ssh.toml /ssh.toml
ADD authorized_keys.tmpl /authorized_keys.tmpl
ADD https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 /bin/confd

VOLUME /ssh

CMD ["/keymanager.sh"]

