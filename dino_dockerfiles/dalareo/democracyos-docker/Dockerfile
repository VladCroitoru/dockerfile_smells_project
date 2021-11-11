# This Dockerfile provices an image to create containers running DemocracyOS;
# a database is needed for the app to run properly. Create a container running MongoDB
# and link it to it. Example:
# docker run -d --name mongo mongo
# docker run -itd --link mongo:mongo <YOUR DEMOCRACYOS IMAGE NAME>

FROM nodesource/trusty:4.2.1
MAINTAINER David A. Lareo <dalareo@gmail.com>

RUN apt-get update && apt-get install -y libcairo2-dev libpango1.0-dev libjpeg-dev libkrb5-dev libgif-dev build-essential g++ git

RUN git clone https://github.com/DemocracyOS/democracyos /usr/src/app/
ADD https://raw.githubusercontent.com/DemocracyOS/democracyos/master/config/defaults.json /usr/src/app/config/defaults.json
WORKDIR /usr/src/app

ENV NODE_ENV=development
RUN npm install commander
RUN node ./bin/dos-install --config

ENV NODE_PATH=.
# Set mongo container named "mongo" as the database
ENV MONGO_URL=mongodb://mongo/DemocracyOS
# Set app port as 80
ENV PORT=80
# Add any custom env vars here as the following:
# ENV STAFF="peter@server.com,jane@something.org"
# ENV ORGANIZATION_NAME=Name of your organization

# If you change the port, remember to set the proper ENV var to match.
EXPOSE 80

RUN make

CMD ["node", "/usr/src/app/index.js"]
