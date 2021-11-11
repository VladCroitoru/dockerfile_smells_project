FROM centos:latest
MAINTAINER Volodymyr Sheptytsky <vshept@hotmail.com>

#==========================================

ENV MONGODB_VER=3.2


# Install dependencies

RUN rpm -i http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
# MongoDB Official Repo
RUN echo -e "[mongodb-org-${MONGODB_VER}]\n\
name=MongoDB Repository\n\
baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/${MONGODB_VER}/x86_64/\n\
gpgcheck=1\n\
enabled=1\n\
gpgkey=https://www.mongodb.org/static/pgp/server-${MONGODB_VER}.asc\n" \
 > /etc/yum.repos.d/mongodb-org-${MONGODB_VER}.repo

RUN yum makecache \
 && yum install -y epel-release \
 && yum install -y  vim-enhanced wget \
          nginx supervisor \
          git mailcap fuse-libs \
          gcc gcc-c++ libstdc++-devel \
          curl-devel libxml2-devel openssl-devel \
          bind-utils net-tools iproute \
          mysql \
          mongodb-org-shell mongodb-org-tools \
 && yum clean all
  
COPY etc/ /etc/
COPY usr/ /usr/

# Forward request and error logs to docker log collector
#-------------------------------------------------------
#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
# && ln -sf /dev/stdout /var/log/nginx/error.log

RUN chmod -R a+w,a+r /var/log /var/cache /var/run 

#================================

EXPOSE 8080

CMD ["/usr/local/bin/start.sh"] 