FROM tomcat:8-jre8-alpine

MAINTAINER stpork from Mordor team

ENV MIDPOINT_VERSION=3.7 \
HOME=/var/opt/midpoint/

ENV JAVA_OPTS="-server -Xms256m -Xmx512m \
-Dmidpoint.home=/var/opt/midpoint/ \
-Djavax.net.ssl.trustStore=/var/opt/midpoint/keystore.jceks \
-Djavax.net.ssl.trustStoreType=jceks \
-Dmidpoint.home=${HOME}"

LABEL io.k8s.description="midPoint Identity Manager"
LABEL io.k8s.display-name="midPoint ${MIDPOINT_VERSION}"
LABEL io.openshift.expose-services="8080:http"

RUN set -x \
&& apk update -qq \
&& apk add --no-cache ca-certificates curl nano tini \
&& update-ca-certificates \
&& rm -rf /var/cache/apk/* /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/* \
&& TOMCAT=/usr/local/tomcat \
&& curl -fsSL \
"https://evolveum.com/downloads/midpoint/${MIDPOINT_VERSION}/midpoint-${MIDPOINT_VERSION}-dist.tar.gz" \
| tar -xz --strip-components=2 -C ${TOMCAT}/webapps midpoint-${MIDPOINT_VERSION}/lib/midpoint.war \
&& mkdir -p ${HOME} \
&& chown -R 1001:0 ${HOME} \
&& chmod -R 777 ${HOME} \
&& chown -R 1001:0 ${TOMCAT} \
&& chmod -R 777 ${TOMCAT}

USER 1001

EXPOSE 8080

VOLUME ["${HOME}"]

WORKDIR ${HOME}

CMD ["catalina.sh", "run"]
ENTRYPOINT ["/sbin/tini", "--"]
