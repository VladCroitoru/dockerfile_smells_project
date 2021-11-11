FROM sequenceiq/hadoop-docker:2.7.1
MAINTAINER dbwatson@vectorspace.org

ENV HIVE_HOME /usr/local/hive
ENV PATH $HIVE_HOME/bin:$PATH
ENV HIVE_VERSION 1.0.0
ENV HIVE_TGZ_URL https://archive.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz
ENV MYSQL_JAR_URL http://jcenter.bintray.com/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar

RUN mkdir -p "$HIVE_HOME"
WORKDIR $HIVE_HOME

RUN set -x \
	&& curl -fsSL --insecure "$HIVE_TGZ_URL" -o hive.tar.gz \
	&& tar -xvf hive.tar.gz --strip-components=1 \
	&& rm hive.tar.gz* \
    && curl -fsSL "$MYSQL_JAR_URL" -o lib/mysql-connector-java.jar
COPY ./hive-site.xml conf/hive-site.xml

EXPOSE 9083
CMD ["hive", "--service", "metastore", "-p", "9083"]
