FROM oraclelinux:7-slim

LABEL maintainer="Adrian Png <adrian.png@fuzziebrain.com>"

ENV username dev
ENV password securepassword
ENV repository_name myproject

RUN yum install -y httpd subversion mod_dav_svn; \
    mkdir -p /var/svn/repos; \
    cd /var/svn/repos; \
    svnadmin create ${repository_name}; \
    chown -R apache:apache ${repository_name}; \
    mkdir -p /var/svn/template/trunk \
        /var/svn/template/branches \
        /var/svn/template/tags; \
    svn import /var/svn/template \
        file:///var/svn/repos/${repository_name} \
        -m "Import SVN structure"; \
    mkdir -p /etc/svn; \
    cd /etc/svn; \
    htpasswd -cb svn-auth ${username} ${password}; \
    chown root:apache svn-auth

COPY svn-acl.conf /etc/svn

RUN sed -i s/#USERNAME#/${username}/ /etc/svn/svn-acl.conf;

COPY svn-repos.conf /etc/httpd/conf.d

RUN mkdir -p /var/svn/scripts

COPY createRepo.sh /var/svn/scripts

COPY createUsers.sh /var/svn/scripts

RUN chmod a+x /var/svn/scripts/*

EXPOSE 80

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
