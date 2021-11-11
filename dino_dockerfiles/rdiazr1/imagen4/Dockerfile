# Creates pseudo distributed hadoop 2.7.0 with pig 0.15 and hive 1.2.1

FROM sequenceiq/hadoop-docker:2.7.0
MAINTAINER mmast

# hadoop-common fixes
ENV PATH $PATH:$HADOOP_PREFIX/bin


# JAVA
ARG JAVA_MAJOR_VERSION=8
ARG JAVA_UPDATE_VERSION=131
ARG JAVA_BUILD_NUMBER=11
ENV JAVA_HOME /usr/jdk1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}

ENV PATH $PATH:$JAVA_HOME/bin
RUN curl -sL --retry 3 --insecure \
  --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
  "http://download.oracle.com/otn-pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/d54c1d3a095b4ff2b6607d096fa80163/server-jre-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz" \
  | gunzip \
  | tar x -C /usr/ \
  && ln -s $JAVA_HOME /usr/java \
  && rm -rf $JAVA_HOME/man

# pig
RUN curl -s https://archive.apache.org/dist/pig/pig-0.15.0/pig-0.15.0.tar.gz | tar -xz -C /usr/local
ENV PIG_HOME /usr/local/pig-0.15.0
RUN ln -s $PIG_HOME /usr/local/pig
ENV PATH $PATH:$PIG_HOME/bin


# hive
RUN curl -s https://archive.apache.org/dist/hive/hive-1.2.1/apache-hive-1.2.1-bin.tar.gz  | tar -xz -C /usr/local
ENV HIVE_HOME /usr/local/apache-hive-1.2.1-bin
RUN ln -s $HIVE_HOME /usr/local/hive
ENV PATH $PATH:$HIVE_HOME/bin




# sqoop
RUN curl -s https://archive.apache.org/dist/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz  | tar -xz -C /usr/local
ENV SQOOP_HOME /usr/local/sqoop-1.4.7.bin__hadoop-2.6.0
RUN ln -s $SQOOP_HOME /usr/local/sqoop
ENV PATH $PATH:$SQOOP_HOME/bin



# HBase
ENV HBASE_VERSION 1.3.2
RUN curl https://archive.apache.org/dist/hbase/1.3.2/hbase-1.3.2-bin.tar.gz  | tar -xz -C /usr/local
ENV HBASE_HOME=/usr/local/hbase-1.3.2
RUN ln -s $HBASE_HOME /usr/local/hbase
ENV PATH=$PATH:$HBASE_HOME/bin


# Flume
ENV FLUME_VERSION 1.8.0
RUN curl https://archive.apache.org/dist/flume/1.8.0/apache-flume-1.8.0-bin.tar.gz  | tar -xz -C /usr/local
ENV FLUME_HOME=/usr/local/apache-flume-1.8.0-bin
RUN ln -s $FLUME_HOME /usr/local/flume
ENV PATH=$PATH:$FLUME_HOME/bin
ENV CLASSPATH=$CLASSPATH:$FLUME_HOME/lib/*




# Anaconda3
ENV PATH=/opt/anaconda3/bin:$PATH
RUN \
	ANACONDA_VERSION=5.0.1 \
    && curl -L https://repo.continuum.io/archive/Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -o Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh \
    && /bin/bash Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -b -p /usr/local/anaconda3 \
    && ln -s /usr/local/anaconda3/ /opt/anaconda3 \
    && rm Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh
	
RUN \
	pip install --upgrade pip \
    && pip install mrjob 
	

  # jdbc
RUN \  
	 mkdir /usr/local/jdbc \
    && curl -L https://github.com/luvres/jdbc/raw/master/mysql-connector-java-5.1.44-bin.jar -o /usr/local/jdbc/mysql-connector-java-5.1.44-bin.jar \
    && curl -L https://github.com/luvres/jdbc/raw/master/mariadb-java-client-2.0.3.jar -o /usr/local/jdbc/mariadb-java-client-2.0.3.jar \
    && curl -L https://github.com/luvres/jdbc/raw/master/ojdbc7.jar -o /usr/local/jdbc/ojdbc7.jar \
    && curl -L https://github.com/luvres/jdbc/raw/master/ojdbc6.jar -o /usr/local/jdbc/ojdbc6.jar \
    && curl -L https://github.com/luvres/jdbc/raw/master/postgresql-42.1.4.jar -o /usr/local/jdbc/postgresql-42.1.4.jar 


  # Spark
RUN  \
	 SPARK_VERSION=2.0.0 \
	&& curl http://d3kbcqa49mib13.cloudfront.net/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz | tar -xzf - -C /usr/local/ \
    && ln -s /usr/local/spark-${SPARK_VERSION}-bin-hadoop2.7/ /opt/spark \
	&& ln -s /usr/local/jdbc/mysql-connector-java-5.1.44-bin.jar /opt/spark/jars/mysql-connector.jar \
    && ln -s /usr/local/jdbc/mariadb-java-client-2.0.3.jar /opt/spark/jars/mariadb-connector.jar \
    && ln -s /usr/local/jdbc/ojdbc7.jar /opt/spark/jars/ojdbc7.jar \
    && ln -s /usr/local/jdbc/ojdbc6.jar /opt/spark/jars/ojdbc6.jar \
    && ln -s /usr/local/jdbc/postgresql-42.1.4.jar /opt/spark/jars/postgresql-connector.jar

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV NOTEBOOKS_PATH=/root/notebooks
RUN mkdir $NOTEBOOKS_PATH
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=ipython
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook --allow-root --ip='*' \
										 --no-browser \
										 --notebook-dir=$NOTEBOOKS_PATH \
										 --NotebookApp.token=''"

RUN echo "" >>/etc/supervisord.conf \
    && echo "[program:pyspark]" >>/etc/supervisord.conf \
    && echo "command=pyspark" >>/etc/supervisord.conf

# Bash colors
ENV RESET='\[$(tput sgr0)\]'
ENV GREY='\[$(tput setaf 0)\]'
ENV RED='\[$(tput setaf 1)\]'
ENV GREEN='\[$(tput setaf 2)\]'
ENV YELLOW='\[$(tput setaf 3)\]'
ENV BLUE='\[$(tput setaf 4)\]'
ENV PURPLE='\[$(tput setaf 5)\]'
ENV CYAN='\[$(tput setaf 6)\]'
ENV WHITE='\[$(tput setaf 7)\]'
#RUN sed -i '/export/s/# //' $HOME/.bashrc \
#    && sed -i 's/# alias/alias/' $HOME/.bashrc \
#    && echo 'alias h="history"' >>$HOME/.bashrc \
#    && echo '# end aliases' >>$HOME/.bashrc \
#    && echo "" >>$HOME/.bashrc \
#    && echo 'export PS1="[${WHITE}\u${RED}@${WHITE}\h${WHITE}:\w${RESET}]# "' >>$HOME/.bashrc

VOLUME $NOTEBOOKS_PATH

# Jupyter Notebook ports
EXPOSE 8888

# Spark management ports
EXPOSE 4040 8080

ENV PATH=/opt/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/java/default/bin:/usr/local/hadoop/bin:/usr/jdk1.8.0_131/bin:/usr/local/pig-0.15.0/bin:/usr/local/apache-hive-1.2.1-bin/bin:/usr/local/sqoop-1.4.7.bin__hadoop-2.6.0/bin:/usr/local/hbase-1.3.2/bin:/usr/local/apache-flume-1.8.0-bin/bin:/opt/spark/bin:/opt/spark/sbin

ADD hive-env.sh $HIVE_HOME/conf/hive-env.sh
ADD hive-site.xml $HIVE_HOME/conf/hive-site.xml
ADD jconn4.jar $SQOOP_HOME/lib
ADD jtds-1.3.1.jar $SQOOP_HOME/lib
ADD sqoop /usr/local/sqoop/bin/sqoop

RUN cp /usr/local/apache-hive-1.2.1-bin/lib/hive-exec-1.2.1.jar /usr/local/sqoop/lib