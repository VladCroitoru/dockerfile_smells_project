FROM maven:3-jdk-8
ADD . /crawler
WORKDIR /crawler

RUN apt-get update
RUN apt-get install -y youtube-dl

# Compile crawler 
RUN mvn clean install && \
    chmod 755 ./start_crawler.sh

# Run the search query 
ENTRYPOINT ["./start_crawler.sh"]
CMD ["Kieler Woche"]