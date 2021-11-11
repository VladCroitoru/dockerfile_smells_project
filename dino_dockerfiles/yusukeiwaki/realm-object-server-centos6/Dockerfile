FROM centos:6

EXPOSE 9080

RUN curl -s https://packagecloud.io/install/repositories/realm/realm/script.rpm.sh | bash
RUN yum -y install realm-object-server-de
RUN chkconfig realm-object-server on

CMD /usr/bin/realm-object-server -c /etc/realm/configuration.yml
