from debian 
run apt-get update && \
    apt-get install -y maven openjdk-7-jdk && \
    apt-get clean 
add pom.xml /srv/jersey-skeleton/
add Serveur/pom.xml /srv/jersey-skeleton/Serveur/
workdir /srv/jersey-skeleton/Serveur/
run mvn install
add Serveur/src /srv/jersey-skeleton/Serveur/src/
expose 8080
cmd mvn jetty:run
