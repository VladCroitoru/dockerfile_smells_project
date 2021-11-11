FROM debian:wheezy
MAINTAINER Rowanto "rowanto@gmail.com"

# Adding Java 8 Repository
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN apt-get update

# Installing Java 8
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install oracle-java8-set-default oracle-java8-installer -y

# Set the WILDFLY_VERSION env variable
ENV WILDFLY_VERSION 8.1.0.Final

# Add the WildFly distribution to /opt
RUN cd /opt && wget http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz 
RUN cd /opt && tar xvf wildfly-$WILDFLY_VERSION.tar.gz && rm wildfly-$WILDFLY_VERSION.tar.gz

# Make sure the distribution is available from a well-known place
RUN ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly

# Set the JBOSS_HOME env variable
ENV JBOSS_HOME /opt/wildfly

# Create the wildfly user and group
RUN groupadd -r wildfly -g 433 && useradd -u 431 -r -g wildfly -d /opt/wildfly -s /bin/false -c "WildFly user" wildfly

# Change the owner of the /opt/wildfly directory
RUN chown -R wildfly:wildfly /opt/wildfly*

# Expose the ports we're interested in
EXPOSE 8080 9990

# Run everything below as the wildfly user
USER wildfly

# Set the default command to run on boot
# This will boot WildFly in the standalone mode and bind to all interface
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]