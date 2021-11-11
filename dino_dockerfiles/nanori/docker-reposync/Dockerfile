FROM centos:7

RUN yum -y install epel-release \
 && yum -y install nodejs reposync createrepo wget \
 && yum --enablerepo=* clean all \
 && rm -rf /var/cache/yum \
 && rm -f /etc/yum.repos.d/*.repo \
 && adduser reposync

COPY app/ /app/
RUN chmod 750 /app/reposync.sh \
 && cd /app/ \
 && npm install


USER reposync
ENTRYPOINT ["/bin/node", "/app/app.js"]
EXPOSE 8080
