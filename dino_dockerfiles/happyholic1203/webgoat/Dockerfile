FROM java:7
MAINTAINER Yu-Cheng (Henry) Huang

RUN apt-get update && \
    apt-get install -y vim wget maven git && \
    mkdir WebGoat-Workspace && \
    cd WebGoat-Workspace && \
    git clone https://github.com/WebGoat/WebGoat.git && \
    git clone https://github.com/WebGoat/WebGoat-Lessons.git && \
    mvn -file WebGoat/pom.xml clean compile install && \
    mvn -file WebGoat-Lessons/pom.xml package && \
    cp -fa ./WebGoat-Lessons/target/plugins/*.jar ./WebGoat/webgoat-container/src/main/webapp/plugin_lessons/ && \
    echo '#!/bin/sh' > /run-webgoat && \
    echo "mvn -file WebGoat/pom.xml -pl webgoat-container tomcat7:run-war &> webgoat_developer_bootstrap.log" >> /run-webgoat && \
    chmod +x /run-webgoat

ENTRYPOINT ["/run-webgoat"]
