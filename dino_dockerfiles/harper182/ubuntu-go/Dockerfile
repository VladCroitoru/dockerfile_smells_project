# Pull base image.
FROM java:8
ENV REFRESHED_ AT 2016-11-14
# Install Chromium.
RUN \
  set -x && \
  echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null && \
  rm -rvf /var/lib/apt/lists/* && \
  apt-get update && \
  apt-get install -y wget  && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y google-chrome-stable

ADD go-agent-14.4.0-1356.deb /
ADD start.sh /
WORKDIR /
RUN dpkg -i go-agent-14.4.0-1356.deb
COPY go-agent /etc/default/
EXPOSE 8153 8154
CMD su go -c '/etc/init.d/go-agent start'