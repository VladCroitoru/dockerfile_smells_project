FROM java

RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0-bin-hadoop2.4.tgz | tar -xz -C /usr/local/
RUN cd /usr/local && ln -s spark-1.4.0-bin-hadoop2.4 spark
ENV SPARK_HOME /usr/local/spark

# Add script to help start a standalone master
ADD start-master-foreground.sh /usr/local/spark/sbin/start-master-foreground.sh

ADD sparkauth.properties /usr/local/spark/lib
ADD spark-env.sh /usr/local/spark/conf
ADD secure-spark-console.jar /usr/local/spark/lib
  
RUN chmod +x /usr/local/spark/sbin/start-master-foreground.sh
EXPOSE 8080 8081 7077 6066 4040 
CMD ["/usr/local/spark/sbin/start-master-foreground.sh"]
