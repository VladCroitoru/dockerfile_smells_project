FROM maven
WORKDIR home/
RUN sh -c 'git clone https://github.com/kudoR/crypto-scraper.git && cd crypto-scraper && mvn clean install'
ENV JAVA_OPTS=""
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /home/crypto-scraper/target/crypto-scraper-1.0.1.jar" ]

