FROM maven
WORKDIR home/
RUN sh -c 'git clone https://github.com/spring-projects/spring-batch-extensions.git && cd spring-batch-extensions/spring-batch-excel && mvn clean install && cd ../.. && git clone https://github.com/kudoR/p2pdashboard.git && cd p2pdashboard && mvn clean install'
ENV JAVA_OPTS=""
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /home/p2pdashboard/target/p2pdashboard-1.0.jar" ]

