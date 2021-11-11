FROM frolvlad/alpine-glibc

RUN set -x && apk add --no-cache bash wget
RUN /usr/bin/wget --quiet --no-cookies --no-check-certificate "https://s3-us-west-2.amazonaws.com/mealticket-docker/java/jre.tar.gz" -O /tmp/jre.tar.gz
RUN /bin/mkdir -p /opt/java
RUN /bin/tar -xzf /tmp/jre.tar.gz -C /opt/java
RUN /bin/rm -f /tmp/jre.tar.gz
ENV JAVA_HOME /opt/java/jre1.8.0_144
ENV PATH $PATH:/opt/java/jre1.8.0_144/bin