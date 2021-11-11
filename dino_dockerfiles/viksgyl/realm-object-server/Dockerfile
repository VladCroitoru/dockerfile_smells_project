FROM centos:7

EXPOSE 9080 9443

RUN curl -s https://packagecloud.io/install/repositories/realm/realm/script.rpm.sh | bash
RUN yum -y install realm-object-server-developer && yum clean all -y
RUN chkconfig realm-object-server on

VOLUME /var/lib/realm/object-server

RUN mkdir realm-object-server
RUN chgrp -R 0 /etc/realm && chmod -R 777 /etc/realm
RUN chgrp -R 0 /var/lib/realm/object-server \
  && chmod -R 777 /var/lib/realm/object-server
RUN chgrp -R 0 realm-object-server && chmod -R 777 realm-object-server
RUN sed -i "s/# \(google:\)/\1/" /etc/realm/configuration.yml

ENTRYPOINT /bin/sed -i "s/# \(clientId:\) '\(.*\)\(.apps.googleusercontent.com\)'/\1 '$CLIENT_ID\3'/" /etc/realm/configuration.yml && /usr/bin/realm-object-server -c /etc/realm/configuration.yml
