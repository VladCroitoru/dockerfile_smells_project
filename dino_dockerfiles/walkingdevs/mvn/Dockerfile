FROM walkingdevs/jvm

ENV Version=3.3.9 \
    MAVEN_HOME=/maven

RUN wget http://www-eu.apache.org/dist/maven/maven-3/$Version/binaries/apache-maven-$Version-bin.tar.gz -O maven.tar.gz && \
    tar xzfv maven.tar.gz -C / && \
    mv apache-maven-$Version /maven && \
    rm maven.tar.gz && \
    ln -s /maven/bin/mvn /bin/mvn && \
    ln -s /root/.m2 /m2