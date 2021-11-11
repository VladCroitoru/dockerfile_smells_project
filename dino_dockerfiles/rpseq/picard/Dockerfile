# work from latest LTS ubuntu release
FROM ubuntu:16.04
# add metadata to image
LABEL author="Zachary Skidmore"

# set the environment variables
ENV version 2.8.3
ENV PICARD /usr/bin/picard.jar

LABEL description="picard, A set of Java command line tools for manipulating \
                   high-throughput sequencing (HTS) data and formats. Built on \
                   java 1.8 and Xenial (ubuntu 16.04).\
                   USAGE: java jvm-args -jar $PICARD PicardToolName"

# run update
RUN apt-get update
# install jdk 8 (and LADP depends)
RUN apt-get install -y openjdk-8-jre libnss-sss

# download picard tools and change permissions
ADD https://github.com/broadinstitute/picard/releases/download/${version}/picard.jar /usr/bin/
RUN chmod 0644 /usr/bin/picard.jar

ADD entry.sh /opt/bin/entry.sh
RUN chmod +x /opt/bin/entry.sh

ENTRYPOINT ["/opt/bin/entry.sh"]

CMD ["java", "-jar", "/usr/bin/picard.jar"]
