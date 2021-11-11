FROM polster/docker-java-centos:oracle-jre-8

MAINTAINER Simon Dietschi

######################
# Build time arguments
######################

ARG TIKA_VERSION=${tika_version:-1.14}
ARG TIKA_SERVER_DOWNLOAD_URL=${tika_server_download_url:-https://www.apache.org/dist/tika}

#######################
# Environment variables
#######################

ENV TIKA_SERVER_FILE=tika-server-$TIKA_VERSION.jar
ENV TIKA_SERVER_INSTALL_DIR=/opt/tika

###############
# Prerequisites
###############

# Update
RUN yum -y update

#####################
# Install Tika Server
#####################

RUN mkdir $TIKA_SERVER_INSTALL_DIR
RUN curl -sSL "${TIKA_SERVER_DOWNLOAD_URL}/${TIKA_SERVER_FILE}" -o $TIKA_SERVER_INSTALL_DIR/$TIKA_SERVER_FILE

#########
# Cleanup
#########

RUN yum -y clean all

##################
# Container Config
##################

# Expose required ports
# Tika Server Port
EXPOSE 9998

# start Tika Server
ENTRYPOINT java -jar $TIKA_SERVER_INSTALL_DIR/$TIKA_SERVER_FILE -h 0.0.0.0
