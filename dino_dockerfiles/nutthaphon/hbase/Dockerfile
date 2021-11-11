FROM nutthaphon/hbase:1.2.2
MAINTAINER Nutthaphon Suwanwong
EXPOSE 50070 9000 9090
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
COPY startall.sh /
COPY stopall.sh /
RUN chmod +x /*.sh
CMD "/startall.sh"