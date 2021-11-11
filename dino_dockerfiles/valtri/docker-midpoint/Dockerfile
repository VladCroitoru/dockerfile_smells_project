FROM debian:bullseye
LABEL maintainer='František Dvořák <valtri@civ.zcu.cz>'

ENV tomcat tomcat9
ENV tomcat_user tomcat

EXPOSE 8009 8080

WORKDIR /root

# graphviz - for GUI features
# xmlstarlet - for docker image scripts
# procps - startup
# tomcat additional packages (to prevent warnings), native package
# zip - clearing war
RUN apt-get update && apt-get install -y --no-install-recommends \
    gzip \
    graphviz \
    libmariadb-java \
    mc \
    openjdk-11-jre-headless \
    procps \
    $tomcat libservlet3.1-java libcommons-dbcp-java libcommons-pool-java libtcnative-1 \
    wget \
    xmlstarlet \
    zip \
 && rm -rf /var/lib/apt/lists/*

# mc (cosmetics)
RUN mkdir -p ~/.config/mc/ \
 && echo 'ENTRY "/var/lib/${tomcat}/webapps/midpoint/WEB-INF" URL "/var/lib/${tomcat}/webapps/midpoint/WEB-INF"' >> ~/.config/mc/hotlist \
 && echo 'ENTRY "/var/log/${tomcat}" URL "/var/log/${tomcat}"' >> ~/.config/mc/hotlist \
 && echo 'ENTRY "/var/opt/midpoint" URL "/var/opt/midpoint"' >> ~/.config/mc/hotlist \
 && ln -s /usr/lib/mc/mc.csh /etc/profile.d/ \
 && ln -s /usr/lib/mc/mc.sh /etc/profile.d/

# tomcat
RUN echo 'JAVA_OPTS="${JAVA_OPTS} -Xms256m -Xmx1024m -Xss1m -Dmidpoint.home=/var/opt/midpoint -Djavax.net.ssl.trustStore=/var/opt/midpoint/keystore.jceks -Djavax.net.ssl.trustStoreType=jceks"' >> /etc/default/${tomcat}
COPY tomcat.sh /

ENV v 4.4-RC1

# midpoint
#COPY midpoint-${v}-dist.tar.gz .
#RUN : \
RUN wget -nv https://evolveum.com/downloads/midpoint/${v}/midpoint-${v}-dist.tar.gz \
 && tar xzf midpoint-${v}-dist.tar.gz \
 && install -v -m 0644 midpoint-${v}/lib/midpoint.war /var/lib/${tomcat}/webapps/ \
 && zip -v -d /var/lib/${tomcat}/webapps/midpoint.war WEB-INF/lib-provided/\* \
 && rm -rf midpoint-${v}-dist.tar.gz midpoint-${v}/
RUN mkdir /var/opt/midpoint \
 && chown $tomcat_user:$tomcat_user /var/opt/midpoint

# deployment (server.xml modified later at the first launch)
RUN ln -L /usr/share/java/mariadb-java-client.jar /var/lib/${tomcat}/lib/
RUN /tomcat.sh & tomcat_pid=$? \
 && while ! test -f /var/opt/midpoint/config.xml; do sleep 0.5; done \
 && sleep 60 \
 && kill $tomcat_pid \
 && rm -fv /var/opt/midpoint/midpoint*.db /var/log/${tomcat}/* \
 && rm -rf /var/lib/${tomcat}/webapps/ROOT/ /var/lib/${tomcat}/webapps/midpoint/ /var/lib/${tomcat}/work/Catalina/ \
 && touch /etc/${tomcat}/.docker-first-launch

COPY docker-entry.sh /
CMD /docker-entry.sh /tomcat.sh
