FROM tomcat:7

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get install -y \
      openjdk-7-jdk \
      ant

RUN mkdir /build
COPY AlephScanner /build/AlephScanner
COPY org-netbeans-modules-java-j2seproject-copylibstask.jar /build/deps
RUN cd /build/AlephScanner && \
    CLASSPATH=/build/deps \
    ant -Dj2ee.server.home=/usr/local/tomcat -Dlibs.CopyLibs.classpath=/build/deps/org-netbeans-modules-java-j2seproject-copylibstask.jar dist

# DEPLOY WAR
RUN rm -rf $CATALINA_HOME/webapps/ROOT
RUN cp /build/AlephScanner/dist/AlephScanner.war /usr/local/tomcat/webapps/ROOT.war
