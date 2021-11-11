FROM 1and1internet/ubuntu-16:latest
MAINTAINER james.poole@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
ENV NOTVISIBLE "in users profile"
ENV DOMAIN="ENVVAR.DOMAIN" \
    HOSTADD_ADMIN="envVarHere" \
    HOSTADD_PW="EnvVarHere" \
    DOMAIN_LOWER="envar.domain"
RUN \
apt-get update && apt-get -o Dpkg::Options::="--force-confold" install -y openssh-server freeipa-client rsyslog dnsutils && \
mkdir --mode 700 /var/run/sshd && \
# SSH login fix. Otherwise user is kicked off after login
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
echo "export VISIBLE=now" >> /etc/profile && \
rm -rf /var/lib/apt/lists/* && \
mkfifo -m 666 /tmp/logpipe && \
sed -i -e '/^module(load="imklog")/g' /etc/rsyslog.conf && \
sed -i -e '/^\$KLogPermitNonKernelFacility/d' /etc/rsyslog.conf && \
chmod 600 /var/log/btmp && \
mv /etc/ssh /root
EXPOSE 2222
