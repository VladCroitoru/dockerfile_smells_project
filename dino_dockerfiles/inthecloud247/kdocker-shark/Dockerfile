FROM inthecloud247/kdocker-openjdk7
MAINTAINER John Albietz "inthecloud247@gmail.com"

RUN \
  `# Scala`; \
  wget --no-check-certificate http://www.scala-lang.org/files/archive/scala-2.9.3.tgz;

RUN \
  `# hive / shark`; \
  wget --no-check-certificate https://github.com/amplab/shark/releases/download/v0.8.1/hive-0.9.0-bin.tgz; \
  wget --no-check-certificate https://github.com/amplab/shark/releases/download/v0.8.1/shark-0.8.1-bin-cdh4.tar.gz

RUN \
  `# shark 0.8.0`; \
  wget --no-check-certificate https://github.com/amplab/shark/releases/download/v0.8.0/shark-0.8.0-bin-cdh4.tgz; \
  tar xvf shark-0.8.0*.*gz -C /opt/ --strip-components=1

RUN \
  `# spark 0.8.1`; \
  wget --no-check-certificate http://d3kbcqa49mib13.cloudfront.net/spark-0.8.1-incubating-bin-cdh4.tgz


#https://github.com/amplab/shark/releases/download/v0.8.0/shark-0.8.0-bin-cdh4.tgz

ADD files /files

# https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html
RUN \
  mv -v *.*gz /files; \
  tar xvf /files/shark-0.8.1*.*gz -C /opt/; \
  tar xvf /files/hive-*.*gz -C /opt/; \
  tar xvf /files/scala-*.*gz -C /opt/; \
  cp -v /files/shark-env-4GB.sh /opt/shark-0.8.0/conf/shark-env.sh; \
  cp -v /files/shark-env-4GB.sh /opt/shark-0.8.1-bin-cdh4/conf/shark-env.sh; \
  cp -v /files/sharkserver*.conf /etc/supervisor/conf.d/; \
  mkdir -vp /data/warehouse; \
  chmod 0777 /data/warehouse; \
  mkdir -vp /var/log/supervisor/sharkserver/; \
  mkdir -vp /var/log/supervisor/sharkserver080/; \
  mkdir -vp /var/log/supervisor/sharkserver081/; \

  # cd /; \
  # apt-get install -y screen tmux; \
  # rm -f *.{gz,tgz}; \

# unsure re:these
# ENV SCALA_VERSION 2.9.3
# ENV SPARK_VERSION 0.8.0
# ENV HIVE_VERSION 0.9.0
# ENV SHARK_VERSION 0.8.0
# ENV HIVE_HOME /opt/hive-$HIVE_VERSION-shark-$SHARK_VERSION-bin
# ENV SCALA_HOME /opt/scala-$SCALA_VERSION
# ENV SPARK_HOME /opt/spark-$SPARK_VERSION
# ENV PATH $SPARK_HOME:$SCALA_HOME/bin:$PATH

# RUN \
#   cd /opt; \
#   cd shark-*-bin-*; \
#   cp shark-*/conf/shark-env.sh.template shark-0.8.1-rc0/conf/shark-env.sh; \
#   mv *.tgz /setupfiles \
#   `############################`; \
#   `# CLEANUP`; \
#   `############################`; \
#   rm -vrf /setupfiles;



# # openjdk7
# RUN apt-get -y install --no-install-recommends openjdk-7-jdk

# # set JAVA_HOME
# ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

# RUN \
#   `# Create cache directory`; \
#   DIR_CACHE="/setupfiles/cache/"; \
#   mkdir -vp $DIR_CACHE; \
#   \
#   `############################`; \
#   `# CUSTOM COMMANDS HERE`; \
#   `############################`; \

# RUN wget --no-check-certificate -O - https://download.elasticsearch.org/kibana/kibana/kibana-3.0.0milestone4.tar.gz | tar -zxv -C /usr/share/nginx/www/ --strip-components=1
