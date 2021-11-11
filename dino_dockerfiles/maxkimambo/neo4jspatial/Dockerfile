## Neo4J + spatial 
FROM neo4j:3.3.1

# install geospatial plugin 
RUN wget -q "https://github.com/neo4j-contrib/spatial/releases/download/0.25.3-neo4j-3.3.1/neo4j-spatial-0.25.3-neo4j-3.3.1-server-plugin.jar" -O neo4j-spatial-0.25.3-neo4j-3.3.1-server-plugin.jar
RUN mv neo4j-spatial-0.25.3-neo4j-3.3.1-server-plugin.jar /var/lib/neo4j/plugins/

## entrypoint
# CMD ["neo4j"]
