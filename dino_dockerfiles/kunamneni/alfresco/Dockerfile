FROM centos:centos7

COPY . /cms
WORKDIR /cms

# install some necessary/desired RPMs and get updates
RUN yum update -y && \
    yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum install -y \
          automake \
          cairo \
          cups-libs \
          curl \
          crontab \
          dos2unix \
          fontconfig \
          fuse \
          fuse-devel \
          gcc-c++ \
          git \
          inotify-tools \
          libcurl-devel \
          libICE \
          libSM \
          libXext \
          libXinerama \
          libXrender \
          libxml2-devel \
          make \
          mesa-libGLU \
          nginx \
          openssl-devel \
          patch \
          python-dev \
          rsync \
          supervisor \
          unzip \
          wget

# Install Alfresco
RUN dos2unix /cms/alfresco/scripts/*.sh && \
    chmod +x /cms/alfresco/scripts/*.sh && \
    /cms/alfresco/scripts/install_java.sh &&\
    /cms/alfresco/scripts/install_alfresco.sh && \
    /cms/alfresco/scripts/install_mysql_connector.sh && \
    cp /cms/alfresco/scripts/disable_tomcat_CSRF.patch /alfresco/disable_tomcat_CSRF.patch && \
    cp /cms/alfresco/scripts/init.sh /alfresco/init.sh && \
    mkdir -p /alfresco/tomcat/webapps/ROOT && \
    cp /cms/alfresco/scripts/index.jsp /alfresco/tomcat/webapps/ROOT/ && \
    /cms/alfresco/scripts/install_s3fuse.sh

# Setup Nginx
RUN rm -f /etc/nginx/nginx.conf && \
    dos2unix /cms/nginx/nginx.conf && \
    cp /cms/nginx/nginx.conf /etc/nginx/nginx.conf

# Setup Supervisord
RUN rm -f /etc/supervisord.conf && \
    dos2unix /cms/supervisord/supervisord.conf && \
    cp /cms/supervisord/supervisord.conf /etc/supervisord.conf


EXPOSE 80 443
CMD /usr/bin/supervisord -c /etc/supervisord.conf -n
