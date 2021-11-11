FROM vbatts/slackware-base:14.2
MAINTAINER roninkenji

RUN sed -i -e 's/^WGETFLAGS=.*/WGETFLAGS="--passive-ftp --no-verbose"/' /etc/slackpkg/slackpkg.conf
RUN slackpkg -batch=on -default_answer=yes update && slackpkg -batch=on -default_answer=yes upgrade-all

# Upgrading CA-certificates
RUN slackpkg -batch=on -default_answer=yes install ca-certificates && ( cd /etc/ssl/certs; grep -v '^#' /etc/ca-certificates.conf | while read CERT; do ln -fsv /usr/share/ca-certificates/$CERT `basename ${CERT/.crt/.pem}`; ln -fsv /usr/share/ca-certificates/$CERT `openssl x509 -hash -noout -in /usr/share/ca-certificates/$CERT`.0; done )

# Set default LANG to en_US.UTF-8
RUN ( echo export LANG=en_US.UTF-8; echo export LC_COLLATE=C ) > /etc/profile.d/lang.sh
RUN ( echo setenv LANG en_US.UTF-8; echo setenv LC_COLLATE C ) > /etc/profile.d/lang.csh

