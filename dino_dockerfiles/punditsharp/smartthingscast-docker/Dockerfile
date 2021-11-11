FROM node:7.10

MAINTAINER PunditSharp

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# Install dependencies and tools
RUN apt-get update; \
    apt-get install -y apt-utils apt-transport-https; \
    apt-get install -y curl wget; \
    apt-get install -y libnss-mdns avahi-discover libavahi-compat-libdnssd-dev libkrb5-dev

WORKDIR /castwebapi

#RUN npm install castv2; \
 #   npm install castv2-client; \
  #  npm install debug; \
   # npm install http; \
    #npm install url; \
    #npm install minimist; \
    #npm install mdns
    
# Get latest script from Git
# -------------------------------------------------------------------------

#RUN git clone https://github.com/vervallsweg/cast-web-api.git
RUN git clone https://github.com/germasch/smartthings-cast.git

ADD image/run.sh /root/run.sh

# Run container
EXPOSE 8080
CMD ["/root/run.sh"]
