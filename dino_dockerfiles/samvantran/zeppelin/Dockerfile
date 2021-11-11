FROM samvantran/java8centos7

# Install pre-reqs for Zeppelin
RUN yum update -y \ 
 && yum install -y git \
	gcc-c++ \
	make \
	bzip2 \ 
	wget

RUN curl -sl https://rpm.nodesource.com/setup_6.x | bash -
RUN yum install -y nodejs

# Install Maven
RUN wget http://www.eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz \
 && tar -zxf apache-maven-3.3.9-bin.tar.gz -C /usr/lib/ \ 
 && ln -s /usr/lib/apache-maven-3.3.9/bin/mvn /usr/bin/mvn \
 && rm -rf /apache-maven-3.3.9-bin.tar.gz 

# Install Spark 1.6
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.0-bin-hadoop2.6.tgz
RUN tar -zxf spark-1.6.0-bin-hadoop2.6.tgz -C /usr/lib/ \
 && rm -rf /spark-1.6.0-bin-hadoop2.6.tgz

# Zeppelin
ENV ZEPPELIN_HOME /usr/lib/zeppelin
ENV ZEPPELIN_COMMIT a17e873d18d434dd0dd56babdc1562ba67ed6d03

RUN git clone https://github.com/apache/zeppelin.git $ZEPPELIN_HOME \
 && cd $ZEPPELIN_HOME \
 && git checkout -q $ZEPPELIN_COMMIT \
 && mvn clean package -DskipTests -Pspark-1.6

# Set Spark values
RUN cd $ZEPPELIN_HOME \ 
 && cp conf/zeppelin-env.sh.template conf/zeppelin-env.sh \
 && sed -i 's|#export SPARK_HOME=|export SPARK_HOME=/usr/lib/spark-1.6.0|' conf/zeppelin-env.sh

WORKDIR $ZEPPELIN_HOME
CMD ["bin/zeppelin.sh"]

