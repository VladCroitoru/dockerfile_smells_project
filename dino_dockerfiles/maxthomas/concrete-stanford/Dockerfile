FROM hltcoe/concrete-java:v4.13.2

ENV STANFORD=/home/concrete/concrete-stanford

RUN mkdir $STANFORD
COPY docker-entrypoint.sh $STANFORD
COPY pom.xml $STANFORD
COPY src $STANFORD/src

# The COPY command creates files owned by root, but RUN commands have
# the permissions for the user specified by USER - which, in the
# parent Dockerfile, is set to 'concrete'.
USER root
RUN chown -R concrete:concrete $STANFORD
USER concrete

RUN cd $STANFORD && \
    mvn -B clean compile verify assembly:single \
        -Dskiptests=true \
	-Dmaven.test.skip=true && \
    mv `find target -name "concrete-stanford-*-jar-with-dependencies.jar"` \
       concrete-stanford.jar && \
    mvn -B clean && \
    rm -rf /home/concrete/.m2

ENV DEFAULT_ANALYTIC_PORT=${DEFAULT_ANALYTIC_PORT:-33221}
EXPOSE $DEFAULT_ANALYTIC_PORT

ENTRYPOINT ["/home/concrete/concrete-stanford/docker-entrypoint.sh"]

CMD ["--help"]
