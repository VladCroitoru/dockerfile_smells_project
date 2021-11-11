FROM ruby:2.5-slim-stretch

#Install all prerequisites (Install Redis 3.3.x. See https://github.com/rails/rails/issues/30527)
RUN apt-get -qq update \
    && apt-get install -y --no-install-recommends  \
                                              wget \
                                              unzip \
                                              git \
                                              build-essential \
                                              redis-server \
                                              ghostscript \
                                              imagemagick \
                                              libreoffice \
                                              libsqlite3-dev \
                                              nodejs \
                                              openjdk-8-jre-headless \
                                              ca-certificates-java \
                                              openjdk-8-jdk \
                                              tomcat8 \
                                              ffmpeg \
                                              solr-tomcat \
                                              file  #file is required by Fits for shameful reasons.

# Install Fedora-commons
RUN export JAVA_OPTS="${JAVA_OPTS} -Dfcrepo.modeshape.configuration=classpath:/config/file-simple/repository.json -Dfcrepo.home=/mnt/fedora-data" \
    && wget --no-check-certificate https://github.com/fcrepo4/fcrepo4/releases/download/fcrepo-4.7.4/fcrepo-webapp-4.7.4.war \
    && mv fcrepo-webapp-4.7.4.war /var/lib/tomcat8/webapps

#Create the startup script
RUN printf "%s\\n%s" \
    '#!/bin/bash'\
    '(solr_wrapper &) && (sleep 2 && fcrepo_wrapper &) && (start-stop-daemon --start --user hyrax --exec /usr/bin/redis-server &) && sleep 5 && rails server ; tail -f /dev/stdout' \
     > /docker-entrypoint.sh \
    && chmod a+x /docker-entrypoint.sh

#Start Redis on container startup
RUN update-rc.d redis-server enable

#Switch to a non-root user or Solr will refuse to start
RUN useradd -ms /bin/bash hyrax
USER hyrax
WORKDIR /home/hyrax

#Install rails
RUN gem install rails -v 5.0.6

#Install Fits
RUN wget http://projects.iq.harvard.edu/files/fits/files/fits-1.0.5.zip \
    && unzip fits-1.0.5.zip \
    && rm fits-1.0.5.zip \
    && mv fits-1.0.5 fits \
    && chmod a+x fits/fits.sh
ENV PATH="${PATH}:/home/hyrax/fits"

#Bust the cache to force cloning the Hyrax Github repo.
ARG TAG=
ARG REV=1
ARG BRANCH=

#Get Hyrax
RUN git clone -b "${BRANCH:-master}" https://github.com/samvera/hyrax hyrax
WORKDIR /home/hyrax/hyrax

#Switch to TAG if needed
RUN if [ -n "$TAG" ]; then git checkout "tags/${TAG}"; fi

#Set the locale to UTF-8 to prevent Bundler to fail when gemspecs contain non ASCII characters
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

#Build and install Hyrax.
RUN bundle install \
    && rake engine_cart:generate

WORKDIR /home/hyrax/hyrax/.internal_test_app

#Add a default administrator
COPY admin_role_map.yml config/role_map.yml

EXPOSE  3000

ENTRYPOINT ["/docker-entrypoint.sh"]