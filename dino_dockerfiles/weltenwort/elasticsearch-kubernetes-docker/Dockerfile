FROM docker.elastic.co/elasticsearch/elasticsearch:5.1.1

RUN elasticsearch-plugin install --batch io.fabric8:elasticsearch-cloud-kubernetes:5.1.1 \
 && curl -L "http://repo2.maven.org/maven2/org/apache/logging/log4j/log4j-slf4j-impl/2.7/log4j-slf4j-impl-2.7.jar" \
        > "/usr/share/elasticsearch/plugins/discovery-kubernetes/log4j-slf4j-impl-2.7.jar" \
 && true
