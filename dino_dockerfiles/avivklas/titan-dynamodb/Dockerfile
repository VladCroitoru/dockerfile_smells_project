FROM centos:7

RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.rpm > jdk-8u73-linux-x64.rpm

RUN yum localinstall -y jdk-8u73-linux-x64.rpm

RUN yum install -y sqlite-devel unzip

ENV GREMLIN_SERVER_USERNAME='root'
ENV LOG_DIR=/var/log/gremlin-server
ENV SERVER_DIRNAME=dynamodb-titan100-storage-backend-1.0.0-hadoop1
ENV SERVER_ZIP=${SERVER_DIRNAME}.zip
ENV PACKAGES_DIR=/usr/local/packages
ENV INSTALL_DIR=${PACKAGES_DIR}/${SERVER_DIRNAME}
ENV SERVICE_SCRIPT=${INSTALL_DIR}/bin/gremlin-server-service.sh
ENV ZIP_URL='https://dynamodb-titan-us-east-1.s3.amazonaws.com/dynamodb-titan100-storage-backend-1.0.0-hadoop1.zip'

RUN mkdir -p ${LOG_DIR}
RUN mkdir -p ${INSTALL_DIR}
RUN chown -R ${GREMLIN_SERVER_USERNAME}:${GREMLIN_SERVER_USERNAME} ${LOG_DIR}
WORKDIR ${PACKAGES_DIR}
RUN curl -o ./${SERVER_ZIP} ${ZIP_URL}
RUN unzip -qq ${SERVER_ZIP}
RUN chmod u+x ${SERVICE_SCRIPT}
RUN chmod u+x ${INSTALL_DIR}/bin/gremlin-server.sh
RUN ln -s ${SERVICE_SCRIPT} /etc/init.d/gremlin-server
RUN chkconfig --add gremlin-server
RUN BACKEND_PROPERTIES=${INSTALL_DIR}/conf/gremlin-server/dynamodb.properties
RUN chown -R ${GREMLIN_SERVER_USERNAME}:${GREMLIN_SERVER_USERNAME} ${INSTALL_DIR}

ADD ./conf /conf
ADD ./scripts /scripts

EXPOSE 8182

CMD ["/usr/local/packages/dynamodb-titan100-storage-backend-1.0.0-hadoop1/bin/gremlin-server.sh", "/conf/gremlin-server.yaml"]
