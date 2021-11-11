####################################################
# Ivideon headless server
####################################################

FROM ubuntu:16.04
MAINTAINER Andrii Veklychev (wzooff@gmail.com)

# Install prerequesties
RUN apt-get update && apt-get install -y \
    wget

# Add ivideon repo and install server
RUN wget http://packages.ivideon.com/ubuntu/keys/ivideon.list -O /etc/apt/sources.list.d/ivideon.list \
&& wget -O - http://packages.ivideon.com/ubuntu/keys/ivideon.key | apt-key add - \
&& apt-get update && apt-get install -y ivideon-server-headless \
&& rm -rf /var/lib/apt/lists/*

# Create config and archive directory
RUN mkdir -p /opt/ivideon/data/archive

ENTRYPOINT ["/opt/ivideon/ivideon-server/videoserver","-c","/opt/ivideon/data/videoserverd.config"]
