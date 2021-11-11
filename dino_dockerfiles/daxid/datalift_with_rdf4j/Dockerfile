# Dockerfile for Datalift data elevation platform backed by RDF4J tripplestore

# RDF4J stuff adapted from yyz1989/rdf4j, many thanks to the author

FROM tomcat:8.5

MAINTAINER daXid <daxid@opmbx.org>

# Install
RUN apt-get -qq update && apt-get install --fix-missing -y --force-yes \
	openjdk-8-jdk \
	ant \
	unzip \
	git

# Set environment
ENV RDF4J_VERSION="2.1.4" 
ENV RDF4J_DATA="/rdf4j-data" 
ENV JVM_PARAMS="-Xmx4g" 
ENV DATALIFT_HOME /datalift-home
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Persistent data
VOLUME ${DATALIFT_HOME}
VOLUME ${RDF4J_DATA}

################################
# RDF4J stuff
################################
COPY rdf4j-data.zip /rdf4j-data.zip
RUN curl -sS -o /tmp/rdf4j.zip -L http://download.eclipse.org/rdf4j/eclipse-rdf4j-${RDF4J_VERSION}-sdk.zip && \
	cd /opt && \ 
	unzip /tmp/rdf4j.zip && \ 
	rm /tmp/rdf4j.zip 
RUN mv /opt/eclipse-rdf4j-${RDF4J_VERSION}/war/*.war /usr/local/tomcat/webapps
RUN echo "CATALINA_OPTS=\"\$CATALINA_OPTS \$JVM_PARAMS -Dorg.eclipse.rdf4j.appdata.basedir=\$RDF4J_DATA\"" >> /usr/local/tomcat/bin/setenv.sh

################################
# Datalift stuff
################################
RUN git clone https://scm.gforge.inria.fr/anonscm/git/datalift/datalift.git
COPY datalift-home.zip /datalift-home.zip
WORKDIR datalift
# Build Datalift
RUN ant dist
# Move datalift core app to Tomcat war directory
RUN mv core/target/datalift.war /usr/local/tomcat/webapps
# Move Datalift modules in a temporary folder
RUN mkdir /datalift-modules
# At once (but we remove flint-endpoint.jar that is causing troubles...) :
RUN mv */dist/*.jar /datalift-modules/
RUN rm /datalift-modules/flint-endpoint.jar
# Or one by one :
#RUN mv data2ontology/dist/data2ontology.jar /datalift-modules/
#RUN mv database-directmapper/dist/database-directmapper.jar /datalift-modules/
#RUN mv flint-endpoint/dist/flint-endpoint.jar /datalift-modules/
#RUN mv framework/dist/datalift-framework-0.9.0.jar /datalift-modules/
#RUN mv geomrdf/dist/geomrdf.jar /datalift-modules/
#RUN mv limes-interlinker/dist/limes-interlinker.jar /datalift-modules/
#RUN mv lov/catalogue/dist/lov-catalogue.jar /datalift-modules//
#RUN mv mvn-repo/dist/mvn-repo.jar /datalift-modules/
#RUN mv projectmanager/dist/project-manager.jar /datalift-modules/
#RUN mv s4ac/dist/s4ac.jar /datalift-modules/
#RUN mv silk-interlinker/dist/silk-interlinker.jar /datalift-modules/
#RUN mv simple-convert/dist/simple-converters.jar /datalift-modules/
#RUN mv skos-viewer/dist/skos-viewer.jar /datalift-modules/
#RUN mv sparql-endpoint/dist/sparql-endpoint.jar /datalift-modules/
#RUN mv sparql2viz-endpoint/dist/sparql2viz-endpoint.jar /datalift-modules/
#RUN mv stringtouri/dist/stringtouri.jar /datalift-modules/
#RUN mv ui-sample/dist/ui-sample.jar /datalift-modules/
#RUN mv virtuoso-connector/dist/virtuoso-connector.jar /datalift-modules/
#RUN mv visualization/dist/visualization.jar /datalift-modules/
#RUN mv wfs2rdf/dist/wfs2rdf.jar /datalift-modules/

################################
# Stuff to initialize and launch a container
################################

WORKDIR /
COPY docker-entrypoint.sh docker-entrypoint.sh
RUN chmod 755 docker-entrypoint.sh
CMD ["sh" , "./docker-entrypoint.sh"]
EXPOSE 8080
