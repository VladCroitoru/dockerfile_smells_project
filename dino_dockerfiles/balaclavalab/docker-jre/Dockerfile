FROM openjdk:9.0.1-11-jre

# Workaround for JDK-8189357 : Release Note: TLS does not work by default on OpenJDK 9
# http://bugs.java.com/view_bug.do?bug_id=8189357
COPY cacerts /etc/ssl/certs/java/cacerts