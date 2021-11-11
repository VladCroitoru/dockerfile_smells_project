FROM tomcat:alpine

ADD target/pebble-2.6.6-SNAPSHOT.war /usr/local/tomcat/webapps/pebble.war
run mkdir /usr/local/tomcat/webapps/pebbleblog

CMD ["catalina.sh", "run"]
