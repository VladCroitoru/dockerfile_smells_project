FROM tomcat:10-jdk8-corretto
LABEL maintainer="Seti <sebastian.koehlmeier@kyberna.com>"

ENV CATALINA_BASE /node
ENV CATALINA_TMPDIR $CATALINA_BASE/temp
ENV UserID=1000
ENV GroupID=1000

ADD root /

RUN yum update -y && \
    yum install -y openssh-clients unzip wget tar && \
    yum clean all && \
    rm -rf /var/cache/yum && \
    mkdir /conf /tlib /tconf /data /deploy && \
    mkdir /node/logs /node/temp /node/webapps /node/work && \
    chmod +x /*.sh && \
    groupadd -g ${GroupID} tomcat && \
    useradd -u ${UserID} -g ${GroupID} -m tomcat

VOLUME [ "/data", "/conf", "/deploy", "/properties", "/tconf", "/tlib", "/certs" ]

ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/run.sh"]