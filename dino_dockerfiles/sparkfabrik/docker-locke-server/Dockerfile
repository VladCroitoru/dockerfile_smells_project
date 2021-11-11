# Set base image
FROM node:10.16-slim
MAINTAINER Francesco Benigno <francesco.benigno@sparkfabrik.com>

# Set variables
ENV LOCKE_VERSION 1.2.2
ENV LOCKE_INSTALL_DIR /srv/locke
ENV PORT=80

# Copy app files into the container.
COPY ./assets $LOCKE_INSTALL_DIR/assets
COPY ./themes/spark $LOCKE_INSTALL_DIR/themes/spark
COPY ./server.js $LOCKE_INSTALL_DIR/
COPY ./package.json $LOCKE_INSTALL_DIR/

# Install Locke and his dependencies
WORKDIR $LOCKE_INSTALL_DIR
RUN npm install

# Expose port 80
EXPOSE 80

# Let's go
CMD ["npm", "start"]
