# We start with a minimal Ruby install.
FROM ruby:2.0.0-slim

# File mantainer
LABEL maintainer="Martin Villalba <villalba@coli.uni-saarland.de>"

# Install Rails and Bundler
RUN /bin/bash -l -c "gem install rails -v 4.0.1"
RUN /bin/bash -l -c "gem install bundler -v 1.3.5"

# We move to Java
# Auto validate license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
# Update repos
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN apt-get update

# Install java
RUN apt-get install oracle-java8-installer -y --no-install-recommends
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Time to check out the code
RUN apt-get install -y git gcc g++ make postgresql-server-dev-all --no-install-recommends
RUN git clone --depth 1 https://github.com/acl-org/acl-anthology /home/acl
RUN /bin/bash -l -c "cd /home/acl && bundle install"

# Ports that will be exposed, in this case 80
EXPOSE 80

# Directories that will be read from outside Docker
RUN mkdir -p /home/acl/public/pdf

# Cleanup
# Things to keep: git, make, gcc
# RUN apt-get purge -y git gcc make g++ && apt-get -y clean && apt-get -y autoremove

# Add file to the container, with the startup script
ADD startup.sh /root/startup.sh
RUN chmod +x /root/startup.sh
ENTRYPOINT /root/startup.sh
