# This image will be published as dspace/dspace
# See https://github.com/DSpace/DSpace/tree/main/dspace/src/main/docker for usage details
#
# This version is JDK11 compatible
# - tomcat:8-jdk11
# - ANT 1.10.7
# - maven:3-jdk-11 (see dspace-dependencies)
# - note: default tag for branch: dspace/dspace: dspace/dspace:dspace-7_x

# Step 1 - Run Maven Build
FROM dspace/dspace-dependencies:dspace-7_x as build
ARG TARGET_DIR=dspace-installer
WORKDIR /app

# The dspace-install directory will be written to /install
RUN mkdir /install \
    && chown -Rv dspace: /install \
    && chown -Rv dspace: /app

USER dspace

# Copy the DSpace source code into the workdir (excluding .dockerignore contents)
ADD --chown=dspace . /app/
COPY dspace/src/main/docker/local.cfg /app/local.cfg

# Build DSpace (note: this build doesn't include the optional, deprecated "dspace-rest" webapp)
# Copy the dspace-install directory to /install.  Clean up the build to keep the docker image small
RUN mvn package && \
  mv /app/dspace/target/${TARGET_DIR}/* /install && \
  mvn clean

# Step 2 - Run Ant Deploy
FROM tomcat:8-jdk11 as ant_build
ARG TARGET_DIR=dspace-installer
COPY --from=build /install /dspace-src
WORKDIR /dspace-src

# Create the initial install deployment using ANT
ENV ANT_VERSION 1.10.7
ENV ANT_HOME /tmp/ant-$ANT_VERSION
ENV PATH $ANT_HOME/bin:$PATH

RUN mkdir $ANT_HOME && \
    wget -qO- "https://archive.apache.org/dist/ant/binaries/apache-ant-$ANT_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C $ANT_HOME

RUN ant init_installation update_configs update_code update_webapps

# Step 3 - Run tomcat
# Create a new tomcat image that does not retain the the build directory contents
FROM tomcat:8-jdk11
ENV DSPACE_INSTALL=/dspace
COPY --from=ant_build /dspace $DSPACE_INSTALL

COPY scripts/run.sh $CATALINA_HOME/bin/run.sh
RUN chmod +x $CATALINA_HOME/bin/run.sh

ENV JAVA_OPTS="-Xmx3000m -Xms500m -Xss900k -XX:+UseContainerSupport"

# Run the "server" webapp off the /server path (e.g. http://localhost:8080/server/)
#RUN ln -s $DSPACE_INSTALL/webapps/server   /usr/local/tomcat/webapps/server
# If you wish to run "server" webapp off the ROOT path, then comment out the above RUN, and uncomment the below RUN.
# You also MUST update the URL in dspace/src/main/docker/local.cfg
# Please note that server webapp should only run on one path at a time.
RUN ln -s $DSPACE_INSTALL/webapps/server   /usr/local/tomcat/webapps/ROOT

# Add the newrelic.jar and -javaagent parameters
RUN mkdir -p /usr/local/tomcat/newrelic
RUN curl -O https://download.newrelic.com/newrelic/java-agent/newrelic-agent/current/newrelic-java.zip
RUN unzip newrelic-java.zip -d /usr/local/tomcat
ADD newrelic.yml /usr/local/tomcat/newrelic/
ENV JAVA_OPTS="$JAVA_OPTS -Dnewrelic.config.log_file_name=STDOUT"

#ENTRYPOINT ["/bin/bash", "-c" , "/dspace/bin/dspace database migrate && catalina.sh run"]