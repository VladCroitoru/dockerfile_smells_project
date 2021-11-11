
#
#
#  XAP Dockerfile
#
#


FROM java:8
MAINTAINER Kobi Kisos


ENV XAP_VERSION 12.0.1
ENV XAP_BUILD_NUMBER 16600
ENV XAP_MILESTONE ga
ENV XAP_HOME_DIR /opt/xap/

RUN mkdir -p ${XAP_HOME_DIR}
WORKDIR ${XAP_HOME_DIR}

# Download XAP
ADD https://gigaspaces-repository-eu.s3.amazonaws.com/com/gigaspaces/xap-open/${XAP_VERSION}/${XAP_VERSION}/gigaspaces-xap-open-${XAP_VERSION}-${XAP_MILESTONE}-b${XAP_BUILD_NUMBER}.zip ${XAP_HOME_DIR}/gigaspaces-xap-open-${XAP_VERSION}-${XAP_MILESTONE}-b${XAP_BUILD_NUMBER}.zip
RUN unzip gigaspaces-xap-open-${XAP_VERSION}-${XAP_MILESTONE}-b${XAP_BUILD_NUMBER}.zip

ENV XAP_NIC_ADDRESS "#local:ip#"
ENV EXT_JAVA_OPTIONS "-Dcom.gs.transport_protocol.lrmi.bind-port=10000-10100 -Dcom.gigaspaces.start.httpPort=9104 -Dcom.gigaspaces.system.registryPort=7102"
ENV XAP_LOOKUP_GROUPS xap

EXPOSE 10000-10100
EXPOSE 9104
EXPOSE 7102
EXPOSE 4174

WORKDIR ${XAP_HOME_DIR}/gigaspaces-xap-open-${XAP_VERSION}-${XAP_MILESTONE}-b${XAP_BUILD_NUMBER}

ENTRYPOINT ["./bin/space-instance.sh"]
CMD ["./bin/space-instance.sh, ""]