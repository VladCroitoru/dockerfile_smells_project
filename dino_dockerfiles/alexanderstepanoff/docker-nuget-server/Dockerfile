FROM alanedwardes/docker-s3fs:latest

ENV TOMCAT tomcat7
RUN apt-get update && apt-get install -y wget $TOMCAT

ENV JNUGET https://bitbucket.org/aristar/jnuget/downloads/jnuget-0.8.2-SNAPSHOT.war
RUN wget $JNUGET

ENV NUGET_HOME /data

RUN mv /jnuget-*.war /var/lib/$TOMCAT/webapps/jnuget.war && \
    chown -R $TOMCAT:$TOMCAT /var/lib/$TOMCAT/webapps/jnuget.war


# Environment variables $S3BUCKET, $S3PATH, $AWS_AIM_ROLE have to be supplied outside the docker container
# Example to run:
#    docker run -ti \
#           -e S3BUCKET=MyBucket \
#           -e S3PATH=/
#           -e AWS_IAM_ROLE=MyRole \
#           -v ~/nuget-config:/data
#           antontimiskov/docker-nuget-server /bin/bash

ADD init.sh /init.sh

CMD /init.sh
