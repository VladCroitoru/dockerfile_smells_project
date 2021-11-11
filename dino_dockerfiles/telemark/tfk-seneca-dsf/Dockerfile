###########################################################
#
# Dockerfile for tfk-seneca-dsf
#
###########################################################

# Setting the base to nodejs 4.6.0
FROM mhart/alpine-node:4.6.0@sha256:e6f2b6e77a85c244e3896821738d0e7899ca7bb2c95e6e087b08aef1f1ebaad7

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Extra tools for native dependencies
RUN apk add --no-cache make gcc g++ python

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Env variables
ENV TFK_SENECA_DSF_TAG tfk-seneca-dsf
ENV TFK_SENECA_DSF_HOST localhost
ENV TFK_SENECA_DSF_PORT 8000
ENV TFK_SENECA_DSF_SYSTEM_NAME Systemname
ENV TFK_SENECA_DSF_SYSTEM_URL http://ws-test.infotorg.no/xml/ErgoGroup/DetSentraleFolkeregister1_4/2015-08-10/DetSentraleFolkeregister1_4.wsdl
ENV TFK_SENECA_DSF_USERNAME username
ENV TFK_SENECA_DSF_PASSWORD password

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]