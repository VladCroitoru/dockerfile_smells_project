FROM java:openjdk-7-jre

MAINTAINER Oliver Lade <oliver@similitude.org>
# See http://www.h2database.com/html/tutorial.html#upgrade_backup_restore

ENV H2_HOME /opt/h2
ENV H2_DATA /opt/h2-data
ENV H2_VERSION 1.4.182

# Download and set up H2.
RUN curl http://www.h2database.com/h2-2014-10-17.zip -o h2.zip && \
    unzip h2.zip -d /opt/ && \
    rm h2.zip && \
    mkdir -p $H2_DATA

# Add the SQL data, cleaned up from a PostgreSQL dump.
# See http://pgfoundry.org/frs/?group_id=1000150&release_id=366#world-world-1.0-title-content
ADD world.sql world.sql

# Load the data into H2.
RUN java -cp $H2_HOME/bin/h2-$H2_VERSION.jar org.h2.tools.RunScript -url jdbc:h2:$H2_DATA/world -script world.sql
