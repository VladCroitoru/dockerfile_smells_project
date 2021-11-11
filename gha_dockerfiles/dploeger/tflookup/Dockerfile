FROM node:lts
WORKDIR /usr/src/app
COPY . .
RUN npm install && cd static && npm install
RUN npm install -g grunt-cli
RUN grunt build
RUN cd static && npm run build
RUN chmod +x /usr/src/app/entrypoint.sh
ENV TFLOOKUP_INDEXFILE documentationIndex.json
ENV NODE_ENV production
EXPOSE 8080
CMD /usr/src/app/entrypoint.sh
