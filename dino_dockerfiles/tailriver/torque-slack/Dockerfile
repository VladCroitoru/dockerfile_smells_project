FROM alpine

RUN apk add --no-cache openssh perl-json perl-lwp-protocol-https perl-net-openssh perl-try-tiny perl-xml-simple \
 && echo "Host *" >> /etc/ssh/ssh_config \
 && echo "  StrictHostKeyChecking no" >> /etc/ssh/ssh_config \
 && echo "  UserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config

ADD data/ /
ENTRYPOINT [ "/entrypoint.pl" ]
