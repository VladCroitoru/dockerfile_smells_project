FROM oracle/glassfish:5.0

# Add maven
ENV	PATH $PATH:/usr/local/apache-maven-3.3.9/bin
COPY ./apache-maven-3.3.9/ /usr/local

# Copy mysql driver
RUN curl http://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.34/mysql-connector-java-5.1.34.jar \
	-o glassfish5/glassfish/lib/mysql-connector-java-5.1.34.jar
