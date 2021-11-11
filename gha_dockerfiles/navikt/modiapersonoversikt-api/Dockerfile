FROM navikt/java:11-appdynamics

ENV APPD_ENABLED=true
ENV JAVA_OPTS="${JAVA_OPTS} -XX:+UseG1GC -Xms1024M -Xmx4096M -XX:MaxMetaspaceSize=512m"
COPY java-debug.sh /init-scripts/08-java-debug.sh
COPY java-11-compat-mode.sh /init-scripts/09-java-11-compat-mode.sh

COPY /web/target/modiabrukerdialog.jar app.jar
