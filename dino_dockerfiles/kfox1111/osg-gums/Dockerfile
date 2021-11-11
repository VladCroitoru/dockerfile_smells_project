FROM kfox1111/osg-base
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

RUN yum install -y osg-gums
ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh

ADD ./tomcat-run.patch /tmp/tomcat-run.patch
RUN pushd /; patch -p0 < /tmp/tomcat-run.patch; popd
RUN rm -f /tmp/tomcat-run.patch

RUN /var/lib/trustmanager-tomcat/configure.sh
RUN sed -i '/sslProtocol=/aciphers="TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_RSA_WITH_RC4_128_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA,SSL_RSA_WITH_RC4_128_SHA"' /etc/tomcat6/server.xml

CMD ["/etc/start.sh"]
