FROM fabric8/java-alpine-openjdk8-jre:latest

# add certificates needed to work with RDS
COPY "rds-certs/*.pem" "/tmp/"
RUN for name in $(ls /tmp/*.pem); do keytool -importcert -trustcacerts -v -keystore /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/cacerts -storepass changeit -file "$name" -noprompt -alias `basename "$name" .pem` ; done 

CMD [ "/deployments/run-java.sh" ]