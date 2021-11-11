FROM pensiero/apache-php

# Labels
LABEL maintainer "oscar.fanelli@gmail.com"

# PHP.ini file: enable <? ?> tags and quiet logging
RUN sed -i "s/display_errors = .*/display_errors = On/" $PHP_INI && \
    sed -i "s/display_startup_errors = .*/display_startup_errors = On/" $PHP_INI && \
    sed -i "s/error_reporting = .*/error_reporting = E_ALL | E_STRICT/" $PHP_INI

# Move to project path directory
WORKDIR $PROJECT_PATH

# NPM install
COPY package.json ./package.json
RUN npm config set loglevel warn
RUN npm install --quiet --production

# Bower install
COPY bower.json ./bower.json
COPY .bowerrc ./.bowerrc
RUN $(npm bin -q)/bower install --allow-root --quiet

# Copy site into place
COPY . $PROJECT_PATH

# Generate assets
RUN bash ./config/docker/watchers/run.sh

# Start services
CMD ["./config/docker/start/production.sh"]