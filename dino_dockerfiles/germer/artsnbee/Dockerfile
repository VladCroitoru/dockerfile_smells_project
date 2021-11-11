from debian:sid
env DEBIAN_FRONTEND noninteractive
run sed -e 's/deb.debian.org/debian.mirrors.ovh.net/g' -i /etc/apt/sources.list
run apt-get update \
    && apt-get install -y maven openjdk-8-jdk jetty9 \
    && apt-get clean
#run mvn install
run rm -rf /var/lib/jetty9/webapps/root
add . /srv/jersey-skeleton/
workdir /srv/jersey-skeleton/
run mvn install
run cp /srv/jersey-skeleton/war/target/war-1.0-SNAPSHOT.war /var/lib/jetty9/webapps/root.war
expose 8080
workdir /srv/jersey-skeleton/server
cmd mvn jetty:run
