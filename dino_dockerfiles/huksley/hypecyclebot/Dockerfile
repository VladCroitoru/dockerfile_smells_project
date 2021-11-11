FROM tomcat:8.5

# Create user
RUN groupadd tomcat && \
	useradd -ms /bin/bash -g tomcat tomcat

# Recreate folders with new permissions
RUN chmod a+rX -R /usr/local/tomcat && \
    rm -Rf /usr/local/tomcat/logs && \
    mkdir -p /usr/local/tomcat/logs && \
    chmod 0777 /usr/local/tomcat/logs && \
    rm -Rf /usr/local/tomcat/temp && \
    mkdir -p /usr/local/tomcat/temp && \
    chmod 0777 /usr/local/tomcat/temp && \
    rm -Rf /usr/local/tomcat/work && \
    mkdir -p /usr/local/tomcat/work && \
    chmod 0777 /usr/local/tomcat/work && \
    rm -Rf /usr/local/tomcat/webapps && \
    mkdir -p /usr/local/tomcat/webapps && \
    chmod 0777 /usr/local/tomcat/webapps && \
    mkdir -p /usr/local/tomcat/conf/Catalina && \
    chmod 0777 /usr/local/tomcat/conf/Catalina && \
	chmod a+x /usr/local/tomcat/bin/catalina.sh

# Copy bot
COPY ./target/HypeCycleBot /usr/local/tomcat/webapps/HypeCycleBot

# Create folder for images
RUN chown tomcat.tomcat /usr/local/tomcat -R && \
	mkdir /usr/local/tomcat/webapps/HypeCycleBot/img && \
	chmod a+rwX /usr/local/tomcat/webapps/HypeCycleBot/img

USER tomcat

WORKDIR /usr/local/tomcat

