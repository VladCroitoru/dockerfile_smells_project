###########################################################
#
# Dockerfile for tfk-saksbehandling-elev-varsel
#
###########################################################

# Setting the base to docker-node-unoconv
FROM zrrrzzt/docker-node-unoconv

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Installs git and make utils
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y make gcc g++ python && apt-get clean

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Startup
ENTRYPOINT sh start.sh
