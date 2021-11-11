FROM dockerfile/java:oracle-java8
RUN apt-get update && \
    apt-get install -y maven && \
    apt-get clean && \
    rm -fr /tmp/* /var/tmp/* 