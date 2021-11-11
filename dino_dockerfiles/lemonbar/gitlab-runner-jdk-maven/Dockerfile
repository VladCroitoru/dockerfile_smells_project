FROM sameersbn/gitlab-ci-runner:latest
MAINTAINER limengabc@163.com

# Install Java.
RUN \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java7-installer

# Install openssh-server, maven and git.
RUN apt-get install -y openssh-server maven git
RUN apt-get clean

ADD assets/ /app/
RUN chmod 755 /app/setup/install
RUN /app/setup/install

# Use the customize init file.
RUN rm -f /app/init
ADD assets/init /app/init
RUN chmod 755 /app/init

EXPOSE 22
