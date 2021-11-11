FROM inswave/websquare-min
LABEL maintainer="maninzoo@inswave.com"

#RUN apk add --update gcc g++ make python py-pip openssh
#RUN pip install Flask
#RUN npm install --global node-gyp grunt-cli

#RUN mkdir /app
WORKDIR /app

COPY package.json /app/
RUN  yarn

COPY . /app
