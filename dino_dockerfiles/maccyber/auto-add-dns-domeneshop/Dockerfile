###########################################################
#
# Dockerfile for auto-add-dns-domeneshop
#
###########################################################

# Setting the base to nodejs 6
FROM mhart/alpine-node:6

# Maintainer
MAINTAINER Jonas Enge

#### Begin setup ####

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Env variables
ENV ROOT_DOMAIN t-fk.no
ENV DOMAIN http://www.domeneshop.no
ENV LOGIN_URL https://www.domeneshop.no/login
ENV URL https://www.domeneshop.no/admin?edit=dns&id=
ENV ID 100000
ENV USERNAME username@email.com
ENV PASSWORD password

# Startup
ENTRYPOINT ["sh", "/src/cli.js"]
