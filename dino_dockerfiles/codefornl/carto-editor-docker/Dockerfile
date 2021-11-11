FROM ubuntu:trusty
MAINTAINER Milo van der Linden <milo@dogodigi.net>

# Environment variables, change as needed
# Configuring locales
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV GDAL_DATA /usr/share/gdal/1.10
ENV BUNDLE_PATH /bundle_cache
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PATH=$PATH:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/carto/node_modules/grunt-cli/bin

ENV CARTO_ENV development
ENV CARTO_ASSET_HOST //cartodb-libs.global.ssl.fastly.net/cartodbui
ENV CARTO_HOST localhost.localdomain
ENV CARTO_SESSION_DOMAIN localdomain
ENV CARTO_SESSION_PORT 3000
ENV CARTO_PROTOCOL http

ENV MAP_API_HOST maps-api
ENV MAP_API_PORT 8181
ENV MAP_API_PROTOCOL http

ENV DB_HOST db
ENV DB_PORT 5432
ENV DB_USER postgres

ENV REDIS_HOST redis
ENV REDIS_PORT 6379

ENV CORS_ENABLED true
ENV WINDSHAFT_PORT 8181

# Setup OS
RUN DEBIAN_FRONTEND=noninteractive locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8 && dpkg-reconfigure locales

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends apt-utils make g++ git-core \
      unp zip unzip curl \
      libicu-dev libgif-dev libjpeg-dev libcairo2-dev \
      libhiredis-dev libmapnik-dev \
      ca-certificates \
      python-mapnik mapnik-utils \
      libprotobuf-dev \
      gdal-bin libgdal1-dev libgdal-dev libproj-dev \
      python-all-dev python-pip \
      nodejs npm phantomjs && \
      rm -rf /var/lib/apt/lists/*

RUN git config --global user.email docker@codefor.nl
RUN git config --global user.name "CodeForNL docker"

# ogr2ogr2 static build, see https://github.com/CartoDB/cartodb/wiki/How-to-build-gdal-and-ogr2ogr2
RUN cd /opt && git clone https://github.com/OSGeo/gdal ogr2ogr2 && cd ogr2ogr2 && \
  git remote add cartodb https://github.com/cartodb/gdal && git fetch cartodb && \
  git checkout trunk && git pull origin trunk && \
  git checkout upstream && git merge -s ours --ff-only origin/trunk && \
  git checkout ogr2ogr2 && git merge -s ours upstream -m "Merged it" && \
  cd ogr2ogr2 && ./configure --disable-shared && make -j 4 && \
  cp apps/ogr2ogr /usr/bin/ogr2ogr && ln -s /usr/bin/ogr2ogr /usr/bin/ogr2ogr2 && rm -rf /opt/ogr2ogr2 /root/.gitconfig

# symlink nodejs. install rvm, ruby and bundle
RUN ln -s /usr/bin/nodejs /usr/bin/node && curl -L https://get.rvm.io | bash -s stable --ruby && \
  echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc && \
  /bin/bash -l -c rvm requirements
RUN echo rvm_max_time_flag=15 >> ~/.rvmrc && \
  /bin/bash -l -c 'rvm install 2.2.3' && \
  /bin/bash -l -c 'rvm use 2.2.3 --default' && \
  /bin/bash -l -c 'gem install bundle archive-tar-minitar' && /bin/bash -l -c 'gem install bundler --no-doc --no-ri'

# Create a volume for gem files
VOLUME /bundle_cache

# Setup Carto
RUN git clone --depth 1 --branch master https://github.com/cartodb/cartodb.git /carto && cd /carto && \
  git submodule init && \
  git submodule foreach --recursive 'git rev-parse HEAD | xargs -I {} git fetch origin {} && git reset --hard FETCH_HEAD' && \
  git submodule update --recursive

WORKDIR /carto
# Python requirements
RUN pip install --no-use-wheel -r python_requirements.txt
# Carto configuration
COPY app_config.yml /carto/config/app_config.yml
COPY grunt_docker.json /carto/config/grunt_docker.json
COPY database.yml /carto/config/database.yml
COPY Gruntfile.js /carto/Gruntfile.js

# Node requirements
# RUN npm cache clean && npm install -g n && n 0.10 && npm update -g npm@^2
#RUN npm install .

# Create a volume for assets so we do not have to recreate them all the time
RUN mkdir -p /carto/public/assets
VOLUME /carto/public/assets

# Start
COPY run.sh /run.sh
RUN chmod 755 /*.sh
CMD ["/run.sh"]
