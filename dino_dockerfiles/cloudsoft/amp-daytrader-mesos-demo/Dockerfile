FROM gliderlabs/alpine:3.3

RUN apk-install openjdk8-jre-base ; \
    apk-install bash ; \
    apk-install curl

ENV AMP_PRO_VERSION 3.1.0
ENV brooklyn.webconsole.security.users docker
ENV brooklyn.webconsole.security.user.docker.password docker

RUN curl -O -s -S http://developers.cloudsoftcorp.com/amp-pro/amp-pro-dist-${AMP_PRO_VERSION}-dist.tar.gz ; \
    tar zxf amp-pro-dist-${AMP_PRO_VERSION}-dist.tar.gz ; \
    rm -f amp-pro-dist-${AMP_PRO_VERSION}-dist.tar.gz; \
    mkdir /root/.brooklyn; \
    echo "brooklyn.experimental.feature.tosca = false" > /root/.brooklyn/brooklyn.properties; \
    chmod 600 /root/.brooklyn/brooklyn.properties

WORKDIR /cloudsoft-amp-pro-${AMP_PRO_VERSION}

VOLUME [ "/root/.brooklyn", "/root/.ssh" , "/root/.brooklyn-persistence" ]

EXPOSE 8081

ENTRYPOINT /cloudsoft-amp-pro-${AMP_PRO_VERSION}/bin/amp launch --persist auto --persistenceDir /root/.brooklyn-persistence --catalogAdd https://raw.githubusercontent.com/cloudsoft/amp-mesos/master/mesos.bom,https://raw.githubusercontent.com/cloudsoft/amp-daytrader-mesos-demo/master/app-servers/websphere-liberty/websphere-liberty.bom,https://raw.githubusercontent.com/cloudsoft/amp-daytrader-mesos-demo/master/app-servers/wildfly-10/wildfly10.bom,https://raw.githubusercontent.com/cloudsoft/amp-daytrader-mesos-demo/master/daytrader-application/daytrader-websphereliberty-cluster.bom,https://raw.githubusercontent.com/cloudsoft/amp-daytrader-mesos-demo/master/daytrader-application/daytrader-wildfly-cluster.bom
