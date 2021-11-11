FROM neo4j:latest

RUN apk add --no-cache curl git maven openjdk8 \
    && (cd / && git clone https://github.com/graphify/graphify) \
    && (cd /graphify/src/extension && mvn assembly:assembly -DdescriptorId=jar-with-dependencies) \
    && (cp /graphify/src/extension/target/graphify-1.0.0-jar-with-dependencies.jar /var/lib/neo4j/plugins) \
    && echo "org.neo4j.server.thirdparty_jaxrs_classes=org.neo4j.nlp.ext=/service" > /var/lib/neo4j/conf/neo4j-server.properties \
    && apk del curl \
    && apk del git \
    && apk del maven \
    && apk del openjdk8 \
    && rm -rf /graphify \
    && rm -rf /root/.m2