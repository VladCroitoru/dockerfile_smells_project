# Dockerfile for the HDC's query_importer service
#
#
# Imports queries from GitHub repo into HubDB.  Links to HubDB.
#
# Example:
# sudo docker pull healthdatacoalition/queryimporter
# sudo docker run --rm --name=query_importer -h query_importer \
#   --link composerdb:composerdb \
#   local/query_importer:latest
#
# Linked containers
# - MongoDB: --link composerdb:composerdb
#
#
FROM phusion/passenger-nodejs
MAINTAINER derek.roberts@gmail.com


# Packages, including update to Node.js 0.12
#
RUN apt-get update; \
    apt-get install -y \
      libkrb5-dev \
      python2.7; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Prepare /app/ folder
#
WORKDIR /app/
COPY . .
RUN npm config set python /usr/bin/python2.7; \
    npm update -g npm; \
    npm install


# Run Command
#
CMD SKIP_INITS=${SKIP_INITS:-false} node index.js import --mongo-host=composerdb \
      --mongo-db=query_composer_development --mongo-port=27017
