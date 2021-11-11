FROM debian:11
RUN apt update \
 && apt install --yes --no-install-recommends \
    openssh-server \
    rsyslog
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]