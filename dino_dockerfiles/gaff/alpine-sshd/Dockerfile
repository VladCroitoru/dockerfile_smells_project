#Dockerfile for https://github.com/Gaff/alpine-sshd
FROM smebberson/alpine-base:1.2.0

#Build script installs sshd
COPY build.sh /build.sh
RUN chmod 755 /build.sh
RUN /build.sh
RUN rm build.sh

#Die a bit faster on exit:
ENV S6_KILL_GRACETIME=500

#Script to generate host keys on startup:
COPY keygen.sh /etc/cont-init.d/keygen
RUN chmod 755 /etc/cont-init.d/keygen

EXPOSE 22

#-D = don't detach, -e = output to stderr, -f = config file
CMD [ "/usr/sbin/sshd", "-D", "-e", "-f", "/etc/ssh/sshd_config"]
