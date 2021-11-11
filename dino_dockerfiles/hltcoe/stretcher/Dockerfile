FROM maven

COPY pom.xml /opt/stretcher/pom.xml
COPY src /opt/stretcher/src

WORKDIR /opt/stretcher
RUN mvn -B clean package \
        -Dskiptests=true \
        -Dmaven.test.skip=true && \
    mv `find target -name "stretcher-fat-*.jar"` \
        stretcher.jar && \
    mvn -B clean

ENTRYPOINT [ "java", "-jar", "stretcher.jar" ]

CMD ["--help"]
