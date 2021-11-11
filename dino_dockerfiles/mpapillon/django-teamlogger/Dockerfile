# TeamLogger
# Copyright (C) 2018  Maxence PAPILLON
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# First, we compile the NodeJS dependencies in a dedicated container.
FROM node:9.4 as static

WORKDIR /usr/src/teamlogger/

# Avoids unnecessary reinstallations of NodeJS dependencies.
COPY package.json package-lock.json /usr/src/teamlogger/

RUN set -x \
    && npm install -g gulp-cli \
    && npm install

# For this part, we do not need to have the entire application.
# Only static files will be copied.
COPY src/nouvelles/static/ /usr/src/teamlogger/src/nouvelles/static/
COPY gulpfile.js /usr/src/teamlogger/

RUN gulp build

# Now we deploy the main container of the application.
FROM python:3.6-slim-stretch

# Set static and media directories to use
ENV APP_PATH=/usr/src/teamlogger/
ENV LOGS_PATH=/var/log/
ENV APP_STATIC_ROOT=/srv/teamlogger/static/
ENV APP_MEDIA_ROOT=/srv/teamlogger/media/

# Setup some basic environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH ${APP_PATH}

# Set application in production mode
ENV DJANGO_SETTINGS_MODULE=teamlogger.settings.production

WORKDIR ${APP_PATH}

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	nginx \
	supervisor
RUN rm -rf /var/lib/apt/lists/*

# Setup all the configfiles.
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY docker/conf/nginx.conf /etc/nginx/sites-available/default
COPY docker/conf/supervisord.conf /etc/supervisor/conf.d/

EXPOSE 8000
VOLUME ["${LOGS_PATH}", "${APP_PATH}", "${APP_STATIC_ROOT}", "${APP_MEDIA_ROOT}"]

STOPSIGNAL SIGTERM

# Get requirements.
COPY src/requirements_prod.txt src/requirements.txt ${APP_PATH}/
RUN pip install --no-cache-dir -r requirements_prod.txt

# Copy app files into container.
COPY src/ ${APP_PATH}

# Create static and media directories.
RUN mkdir -p ${APP_STATIC_ROOT} ${APP_MEDIA_ROOT}

# Make starting script runable.
COPY docker/docker-start-server.sh ${APP_PATH}/
RUN chmod +x docker-start-server.sh

# Copy of compiled static files.
COPY --from=static /usr/src/teamlogger/src/nouvelles/static/ ${APP_PATH}/src/nouvelles/static/

CMD ["./docker-start-server.sh"]
