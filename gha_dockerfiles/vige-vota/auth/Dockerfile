# Vige, Home of Professional Open Source Copyright 2010, Vige, and           
# individual contributors by the @authors tag. See the copyright.txt in the  
# distribution for a full listing of individual contributors.                
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License. You may obtain    
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0        
# Unless required by applicable law or agreed to in writing, software        
# distributed under the License is distributed on an "AS IS" BASIS,          
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   
# See the License for the specific language governing permissions and        
# limitations under the License.

FROM openjdk:16-jdk
EXPOSE 8480
RUN adduser -u 1000 -G adm -d /home/wildfly --shell /bin/bash wildfly && \
    echo "wildfly:secret" | chpasswd

USER root

ENV MAVEN_VERSION=3.8.1
ENV NODE_VERSION=16.11.1

RUN mkdir /home/wildfly/apache-maven-$MAVEN_VERSION && \
  	curl https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/$MAVEN_VERSION/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xvz -C /home/wildfly && \
  	curl https://nodejs.org/download/release/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz | tar xvz -C /home/wildfly
ENV TERM xterm
ENV CITIESGENERATOR_URL=http://cities-generator-service.vige.it:8380
ENV VOTINGPAPERS_URL=http://vota-votingpapers.vige.it:8180
ENV VOTING_URL=http://vota-voting.vige.it:8080
ENV HISTORY_URL=http://vota-history.vige.it:8280
ENV FRONTEND_URL=http://vota-frontend.vige.it

WORKDIR /workspace
COPY / /workspace/auth
RUN chown -R wildfly:adm /workspace
RUN export NPM_HOME=/home/wildfly/node-v$NODE_VERSION-linux-x64 && export PATH=$NPM_HOME/bin:$PATH && cd auth && /home/wildfly/apache-maven-$MAVEN_VERSION/bin/mvn install -Pdocker,prepare-keycloak
RUN rm -Rf /home/wildfly/.m2 && \
	rm -Rf /home/wildfly/apache-maven-$MAVEN_VERSION && \
	rm -Rf /home/wildfly/node-v$NODE_VERSION-linux-x64 && \
	mv /workspace/auth/target/keycloak-run/wildfly* /opt/keycloak && \
	chown -R wildfly:adm /opt/keycloak && \
	rm -Rf /workspace/auth
	
USER wildfly

CMD mkdir -p /opt/keycloak/realm-config/execution && \
	cp /opt/keycloak/realm-config/vota-domain-realm.json /opt/keycloak/realm-config/execution && \
	sed -i -e 's@MAVEN_REPLACER_CITIESGENERATOR_SERVER_URL@'"$CITIESGENERATOR_URL"'@g' /opt/keycloak/realm-config/execution/vota-domain-realm.json && \
	sed -i -e 's@MAVEN_REPLACER_VOTINGPAPERS_SERVER_URL@'"$VOTINGPAPERS_URL"'@g' /opt/keycloak/realm-config/execution/vota-domain-realm.json && \
	sed -i -e 's@MAVEN_REPLACER_VOTING_SERVER_URL@'"$VOTING_URL"'@g' /opt/keycloak/realm-config/execution/vota-domain-realm.json && \
	sed -i -e 's@MAVEN_REPLACER_HISTORY_SERVER_URL@'"$HISTORY_URL"'@g' /opt/keycloak/realm-config/execution/vota-domain-realm.json && \
	sed -i -e 's@MAVEN_REPLACER_FRONTEND_SERVER_URL@'"$FRONTEND_URL"'@g' /opt/keycloak/realm-config/execution/vota-domain-realm.json && \
	java -D[Standalone] -server -Xms64m -Xmx512m -XX:MetaspaceSize=96M -XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true -Djboss.modules.system.pkgs=org.jboss.byteman -Djava.awt.headless=true --add-exports=java.base/sun.nio.ch=ALL-UNNAMED --add-exports=jdk.unsupported/sun.misc=ALL-UNNAMED --add-exports=jdk.unsupported/sun.reflect=ALL-UNNAMED -Dorg.jboss.boot.log.file=/opt/keycloak/standalone/log/server.log -Dlogging.configuration=file:/opt/keycloak/standalone/configuration/logging.properties -jar /opt/keycloak/jboss-modules.jar -mp /opt/keycloak/modules org.jboss.as.standalone -Djboss.home.dir=/opt/keycloak -Djboss.server.base.dir=/opt/keycloak/standalone -c standalone.xml -b 0.0.0.0 -Djboss.socket.binding.port-offset=400 -Dkeycloak.migration.action=import -Dkeycloak.migration.provider=dir -Dkeycloak.migration.dir=/opt/keycloak/realm-config/execution -Dkeycloak.migration.strategy=IGNORE_EXISTING -Dkeycloak.profile.feature.upload_scripts=enabled && \
    tail -f /dev/null