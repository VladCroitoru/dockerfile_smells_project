# base image
FROM pelias/baseimage

# downloader apt dependencies
# note: this is done in one command in order to keep down the size of intermediate containers
RUN apt-get update && apt-get install -y bzip2 && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

# clone repo
RUN git clone https://github.com/OpenTransitTools/pelias.transit.loader /code/pelias/transit

# change working dir
WORKDIR /code/pelias/transit

# consume the build variables
ARG REVISION=master

# install npm dependencies
RUN npm install

# run tests
# TODO RUN npm test

# hope we pull in the local pelias.json and also list find where the local data will reside (ala /data directory)
VOLUME "/data"
ADD 'pelias.json' '/code/pelias.json'
ENV PELIAS_CONFIG '/code/pelias.json'
