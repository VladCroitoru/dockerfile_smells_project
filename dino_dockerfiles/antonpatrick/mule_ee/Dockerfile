FROM openjdk:8
MAINTAINER anton.patrick@hotmail.com


# Define environment variables.
ENV MULE_HOME /opt/mule

#RUN apk --no-cache update && \
#    apk --no-cache upgrade && \
#    apk --no-cache add tzdata openntpd && \

  #mkdir -p /opt && \
	#cd /opt && \
	#addgroup mule && adduser -G mule -g "MuleESB User" -s /bin/sh -D mule

#https://s3-eu-west-1.amazonaws.com/mule-ee-3.9.1/mule-ee-distribution-standalone-3.9.1.tar.gz
#RUN cd /opt
#ADD mule-ee-distribution-standalone-3.9.1.tar.gz /opt

RUN cd /opt && \
	wget https://s3.amazonaws.com/new-mule-artifacts/mule-ee-distribution-standalone-3.9.1.tar.gz && \
	tar xvzf /opt/mule-ee-distribution-standalone-3.9.1.tar.gz && \
	rm /opt/mule-ee-distribution-standalone-3.9.1.tar.gz && \
	mv mule-enterprise-standalone-3.9.1 mule


#ADD mule-ee-distribution-standalone-3.9.1.tar.gz /opt

#RUN	cd /opt && mv mule-enterprise-standalone-3.9.1 mule

#RUN chown -R mule:mule /opt/mule && \
	#ls -ltr /opt/mule/

# Define mount points.
VOLUME /opt/mule/logs /opt/mule/apps /opt/mule/domains /opt/mule/conf

# Default http port
EXPOSE 8081 8090 5000 1098 7777 9997


WORKDIR /opt/mule

# Default when starting the container is to start Mule ESB.
CMD ["/opt/mule/bin/mule"]

#docker run -d --name="mule_ee" -p 8090:8090 -v ~/Documents/docker/volumes/mule_ee/apps:/opt/mule/apps -v ~/Documents/docker/volumes/mule_ee/logs:/opt/mule/logs -d docker pull antonpatrick/mule_ee:latest
