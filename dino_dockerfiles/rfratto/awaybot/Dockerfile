FROM google/nodejs:0.10.33
ENV token=BOT_API_TOKEN
RUN mkdir /dist
WORKDIR /dist
ADD . /dist
RUN npm install --production
VOLUME /dist
CMD token=${token} node /dist/src/index.js
