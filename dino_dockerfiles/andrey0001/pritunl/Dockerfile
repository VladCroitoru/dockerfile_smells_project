FROM centos:7

MAINTAINER Andrey Sorokin <andrey@sorokin.org>

ADD mongodb-org-4.2.repo /etc/yum.repos.d/mongodb-org-4.2.repo
ADD pritunl.repo /etc/yum.repos.d/pritunl.repo


RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm &&\
    gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 7568D9BB55FF9E5287D586017AE645C0CF8E292A &&\
    gpg --armor --export 7568D9BB55FF9E5287D586017AE645C0CF8E292A > key.tmp; rpm --import key.tmp; rm -f key.tmp &&\
    yum -y install pritunl mongodb-org &&\
    curl -o /etc/yum.repos.d/jdoss-wireguard-epel-7.repo https://copr.fedorainfracloud.org/coprs/jdoss/wireguard/repo/epel-7/jdoss-wireguard-epel-7.repo &&\
    yum -y install wireguard-dkms wireguard-tools &&\
    yum clean all

ADD start-pritunl /bin/start-pritunl

EXPOSE 443
EXPOSE 1194/UDP
EXPOSE 1195/UDP

HEALTHCHECK  --interval=5m --timeout=3s \
  CMD curl --fail --silent --output /dev/null http://localhost:443/login || exit 1

ENTRYPOINT ["/bin/start-pritunl"]

CMD ["/usr/bin/tail", "-f","/var/log/pritunl.log"]

