#
# A scala content server
#
# https://github.com/marcolotz/ContentServer
#

# Pull base image
FROM  hseeberger/scala-sbt

# Install git
RUN \
  apt-get install git

# Install content server
RUN \
  cd /root && \
  git clone https://github.com/marcolotz/contentserver

# Download dependencies and compile content server
RUN \
  cd contentserver && \
  sbt reload compile

# Define working directory
WORKDIR /root/contentserver

# overwrite this with 'CMD []' in a dependent Dockerfile
CMD ["sbt container:start"]
