FROM java:8
MAINTAINER ariwaranosai nkssai@outlook.com

ENV SBT_VERSION 0.13.11

# Install sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt

# Install git and clean cache
RUN \
  apt-get install git && \
  apt-get clean && \
  apt-get autoclean

# Clone project and run test
RUN \
  git clone https://github.com/ariwaranosai/nozomi.git && \
  cd nozomi && \
  sbt test

# Define working directory
WORKDIR /root/nozomi