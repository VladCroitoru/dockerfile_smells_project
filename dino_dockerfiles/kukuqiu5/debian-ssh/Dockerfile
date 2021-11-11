FROM debian:latest
MAINTAINER Ming <qm2009@gmail.com>
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y vim wget openssh-server gcc g++ git libev-dev make git clang && \
    apt-get autoremove && apt-get clean &&\
    mkdir -p /var/run/sshd && sed -i \
                                  -e "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" \
                                  -e "s/PermitRootLogin without-password/PermitRootLogin yes/g" \
                                  -e "s/#PasswordAuthentication yes/PasswordAuthentication yes/g" \
                                  -e "s/UsePAM yes/UsePAM no/g" \
                                  /etc/ssh/sshd_config
    
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
