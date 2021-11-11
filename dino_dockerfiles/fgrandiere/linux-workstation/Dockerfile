FROM fedora
MAINTAINER Freddy GRANDIERE <f.grandiere@linkbynet.com>

LABEL RUN='docker run --name ssh -d -p 22:22 $IMAGE'

EXPOSE 22

RUN dnf -y update && dnf -y install openssh-server passwd && dnf clean all

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/usr/sbin/sshd", "-D"]
