###########################################################
#
# Dockerfile for tfk-roy
#
###########################################################

# Setting the base to nodejs 4.6.0
FROM mhart/alpine-node:4.9.1@sha256:052772af605978749631e2b6d190c7d68dc607a480a6e4dbe84eaf7264759d2e

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Env variables
ENV TFK_ROY_ARCHIVE_DIRECTORY_PATH test/data/archive
ENV TFK_ROY_DONE_DIRECTORY_PATH test/data/done
ENV TFK_ROY_ERROR_DIRECTORY_PATH test/data/errors
ENV TFK_ROY_JOB_DIRECTORY_PATH test/data/jobs
ENV TFK_ROY_JWT_KEY Louie Louie, oh no, I got to go
ENV TFK_ROY_DSF_URL http://ws-test.infotorg.no/xml/ErgoGroup/DetSentraleFolkeregister1_4/2015-08-10/DetSentraleFolkeregister1_4.wsdl
ENV TFK_ROY_DSF_NAMESPACE http://ws.infotorg.no/xml/Admin/Brukersesjon/2006-07-07/Brukersesjon.xsd
ENV TFK_ROY_DSF_USERNAME MrSmith
ENV TFK_ROY_DSF_PASSWORD MrSmithsPassword
ENV TFK_ROY_DSF_METHOD hentForeldre
ENV TFK_ROY_DSF_SAKSREF MinElev
ENV TFK_ROY_SVARUT_URL test.svarut.ks.no/tjenester/forsendelseservice/ForsendelsesServiceV4
ENV TFK_ROY_SVARUT_USERNAME MrSmith
ENV TFK_ROY_SVARUT_PASSWORD MrSmithsPassword
ENV TFK_ROY_SVARUT_KONTERINGSKODE 1111
ENV TFK_ROY_SVARUT_AVGIVENDE_SYSTEM MinElev
ENV TFK_ROY_P360WS_BASEURL http://tfk-fh-siweb01.login.top.no:8088/SI.WS.Core/SIF/
ENV TFK_ROY_P360WS_USER domain/username
ENV TFK_ROY_P360WS_PASSWORD password

# Startup
ENTRYPOINT node example.js