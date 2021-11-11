#see https://github.com/marcoraddatz/homebridge-docker/blob/master/Dockerfile

FROM node:10-stretch AS base

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# Install dependencies and tools
RUN apt-get update; \
    apt-get install -y apt-utils apt-transport-https; \
    apt-get install -y curl wget; \
    apt-get install -y libnss-mdns avahi-discover libavahi-compat-libdnssd-dev libkrb5-dev; \
    apt-get install -y nano vim

WORKDIR /root/app
# copy project file
COPY package.json .

 
#
# ---- Dependencies ----
FROM base AS dependencies
# install node packages
# COPY package-lock.json .
RUN npm set progress=false && npm config set depth 0
RUN npm i --unsafe-perm -only=production 
# copy production node_modules aside
RUN cp -R node_modules prod_node_modules

#
# ---- Release ----
FROM base
WORKDIR /root/app
# copy production node_modules
COPY --from=dependencies /root/app/prod_node_modules ./node_modules
# MISC settings
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf

USER root
RUN mkdir -p /var/run/dbus

# copy app sources
COPY config.js .
COPY index.js .
COPY services.json .
COPY ./characteristics/ ./characteristics/
COPY ./services/ ./services/
COPY ./ui/ ./ui/
COPY run.sh .
EXPOSE 51826
EXPOSE 51888
VOLUME ["/data"]
CMD ["/root/app/run.sh"]