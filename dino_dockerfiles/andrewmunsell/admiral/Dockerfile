FROM node:0.12-onbuild
MAINTAINER Andrew Munsell <andrew@wizardapps.net>

# Install the Fleet binary
RUN apt-get update -qq
RUN apt-get install wget -y -qq
RUN wget https://github.com/coreos/fleet/releases/download/v0.10.1/fleet-v0.10.1-linux-amd64.tar.gz
RUN tar -xf fleet-v0.10.1-linux-amd64.tar.gz
RUN mv fleet-v0.10.1-linux-amd64/fleetctl /usr/local/bin/fleetctl

# Build the service
RUN /usr/local/bin/npm install -g browserify
RUN sh -c 'cd public && npm install && npm run-script build'

ENV PORT 80

EXPOSE 80