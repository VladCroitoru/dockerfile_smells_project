FROM maven

# netcat is used by docker-entrypoint.sh to test if the Fetch server is up
RUN apt-get update && apt-get install -y \
    netcat \
  && rm -rf /var/lib/apt/lists/*

COPY pom.xml /opt/cadet-search-lucene/pom.xml
COPY src /opt/cadet-search-lucene/src
COPY wait-for-fetch.sh /opt/cadet-search-lucene/wait-for-fetch.sh

WORKDIR /opt/cadet-search-lucene
RUN mvn -B clean package \
        -Dskiptests=true \
        -Dmaven.test.skip=true && \
    mv `find target -name "cadet-search-lucene-fat-*.jar"` \
        cadet-search-lucene.jar && \
    mvn -B clean

ENTRYPOINT [ "./wait-for-fetch.sh", "java", "-jar", "cadet-search-lucene.jar" ]

CMD ["--help"]
