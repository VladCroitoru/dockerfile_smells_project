FROM debian:buster 

RUN mkdir /app
WORKDIR /app
RUN apt-get update && apt-get install -y procps net-tools
ADD * /app/

RUN apt update
RUN apt -y install curl





RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server sudo
ADD set_root_pw.sh /app/set_root_pw.sh
ADD run.sh /app/run.sh
RUN chmod +x /app/*.sh
RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
  && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
  && touch /root/.Xauthority \
  && true

## Set a default user. Available via runtime flag `--user docker`
## Add user to 'staff' group, granting them write privileges to /usr/local/lib/R/site.library
## User should also have & own a home directory, but also be able to sudo
RUN useradd docker \
        && passwd -d docker \
        && mkdir /home/docker \
        && chown docker:docker /home/docker \
        && addgroup docker staff \
        && addgroup docker sudo \
        && true





EXPOSE 80
CMD ["/app/configure.sh"]
