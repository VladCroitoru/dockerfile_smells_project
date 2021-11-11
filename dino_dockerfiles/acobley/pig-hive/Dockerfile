# Version: 0.0.1
FROM sequenceiq/hadoop-docker:2.7.1
MAINTAINER Andy C “aecobley@dundee.ac.uk”
RUN curl http://apache.mirror.anlx.net/pig/latest/pig-0.16.0.tar.gz | tar -zx -C /usr/local
ENV PATH /usr/local/pig-0.16.0/bin:$PATH
ENV PATH /usr/local/hadoop/bin:$PATH
RUN curl http://apache.mirror.anlx.net/hive/stable/apache-hive-1.2.1-bin.tar.gz | tar -zx -C /usr/local
ENV PATH /usr/local/apache-hive-1.2.1-bin/bin:$PATH
EXPOSE 10020
EXPOSE 50070
EXPOSE 50030
EXPOSE 8088
