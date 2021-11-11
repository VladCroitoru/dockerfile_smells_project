FROM google/dart

MAINTAINER Jakub Uhrik <jakuub@bookyourself.com>

ENV ACTIVATOR_VERSION 1.3.2
ENV PATH $PATH:/opt/activator-$ACTIVATOR_VERSION

RUN apt-get update && apt-get install -y unzip openjdk-7-jdk
ADD https://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip /tmp/typesafe-activator-$ACTIVATOR_VERSION.zip
RUN (cd /opt && unzip /tmp/typesafe-activator-$ACTIVATOR_VERSION && \
	rm -f /tmp/typesafe-activator-$ACTIVATOR_VERSION.zip)

WORKDIR /app
EXPOSE 9000 



# Define default command.
CMD ["bash"]
