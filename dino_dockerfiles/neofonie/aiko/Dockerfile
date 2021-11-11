FROM williamyeh/java8
RUN apt-get update && apt-get install -yq maven
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
COPY java /tmp/aiko
RUN cd /tmp/aiko && mvn -B -C clean install && mkdir -p /opt/application/ && cp /tmp/aiko/target/application.jar /opt/application/
COPY aiko /usr/local/bin/
RUN chmod a+x /usr/local/bin/aiko
WORKDIR /opt/application
CMD ["bash"]
