# Totem Dashboard v2

# Use node 6.9.x
FROM mhart/alpine-node:6.9

# Install Gulp & bower
RUN npm install -g gulp bower

WORKDIR /opt/totem-dashboard

# Add files necessary for npm install (For caching purposes)
ADD package.json /opt/totem-dashboard/

RUN apk --update --no-cache add \
      python \
      make \
      gcc \
      g++ \
  && npm install \
  && apk del \
      python \
      make \
      gcc \
      g++ \
  && rm -rf ~/.cache /tmp/npm* /root/.npm ~/.npmrc \
  && mkdir -p /root/.npm

# Add the package and bower files
ADD bower.json .bowerrc /opt/totem-dashboard/

# Bower build
RUN apk --update --no-cache add \
      git \
  && bower --allow-root install \
  && apk del \
      git

# Update dashboard directory files
ADD . /opt/totem-dashboard

# Bower build
RUN gulp clean && gulp build

# Expose port
EXPOSE 3000

# Set discover var
ENV DISCOVER totem-dashboard:3000

# Set default command to gulp
ENTRYPOINT ["gulp"]

# Set default param for gulp to the output directory
CMD ["serve:prod"]
