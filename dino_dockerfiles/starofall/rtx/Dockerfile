FROM ruimashita/scipy
# Adding RTX Dep
ADD ./setup.py /app/setup.py
RUN python /app/setup.py install
# Adding Spark Dep
RUN apt-get update && apt-get install -y openjdk-7-jre
ENV SPARK_VERSION 1.6.3
ENV HADOOP_VERSION 2.6
RUN curl -s http://www-us.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz | tar -xz -C /tmp/
RUN ln -s /tmp/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /spark
ENV SPARK_HOME /spark
# Minimize logging in spark
RUN mv /spark/conf/log4j.properties.template /spark/conf/log4j.properties
RUN sed -i 's@log4j.rootCategory=INFO, console@log4j.rootCategory=ERROR, console@' /spark/conf/log4j.properties
# Adding RTX
ADD ./ /app/
WORKDIR /app
CMD /bin/bash
