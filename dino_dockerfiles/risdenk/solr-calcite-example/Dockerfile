FROM maven:alpine

RUN curl -L https://api.github.com/repos/risdenk/solr-calcite-example/tarball | tar -zx -C / \
  && mv /risdenk-solr-calcite-example-* /risdenk-solr-calcite-example \
  && cd /risdenk-solr-calcite-example \
  && mvn package -DskipTests

WORKDIR /risdenk-solr-calcite-example

EXPOSE 8765

ENTRYPOINT mvn exec:java -Dexec.mainClass="org.apache.solr.main.TestAvaticaServer"
# mvn exec:java -Dexec.mainClass="org.apache.solr.main.TestCalcite" -Dexec.args="'solr:9983' 'select fielda from test limit 10'"

