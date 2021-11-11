FROM psiag/oracle-java

MAINTAINER cubesky

RUN apt update

RUN apt install -y openssh-server screen nano wget curl
RUN mkdir -p /var/run/sshd
RUN sed -i 's/PermitRootLogin\ prohibit\-password/PermitRootLogin\ yes/g' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin\ no/PermitRootLogin\ yes/g' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin\ without\-password/PermitRootLogin\ yes/g' /etc/ssh/sshd_config
RUN echo "root:cubesky" | chpasswd

# ADD Server.tar /mcserver

EXPOSE 22
EXPOSE 25565

WORKDIR /mcserver/
VOLUME /mcserver
ENTRYPOINT /usr/sbin/sshd -D
#CMD ["/usr/bin/java","-Xms7680M","-Xmx7680M","-jar","forge-1.10.2-12.18.3.2185-universal.jar","nogui"]