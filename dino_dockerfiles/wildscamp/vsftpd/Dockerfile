FROM debian:jessie

MAINTAINER Joel Rowley <joel.rowley@wilds.org>

LABEL vendor="The Wilds" \
      org.wilds.docker-vsftpd.version="1.0.3"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install -qqy --no-install-recommends \
        libpam-pwdfile \
        openssl \
        vim \
        vsftpd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/*

ENV LOG_FILE=/var/log/vsftpd.log \
    SSL=false \
    PAM_FILE=/etc/pam.d/vsftpd \
    PASSWD_FILE=/etc/vsftpd/vsftpd.passwd \
    DEFAULT_USER_CONFIG=/etc/vsftpd/default_user.conf \
    USER_CONFIG_DIR=/etc/vsftpd/vusers \
    PASV_MIN_PORT=30000 \
    PASV_MAX_PORT=30009

RUN mkdir -p /etc/vsftpd $USER_CONFIG_DIR /var/run/vsftpd/empty /home/virtual \
    && echo "auth required pam_pwdfile.so pwdfile ${PASSWD_FILE}" > $PAM_FILE \
    && echo "account required pam_permit.so" >> $PAM_FILE

COPY *.conf /etc/vsftpd/

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /etc/vsftpd

EXPOSE 21/tcp

ENTRYPOINT ["/entrypoint.sh"]
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]
