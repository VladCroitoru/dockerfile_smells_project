# Build a container for running the application using nginx+passenger.
#
# See https://github.com/phusion/passenger-docker
#
# This uses a fairly heavyweight base image that seems well thought
# out, but is highly opinionated in how you do things (paths where it
# expects things, how to do container start-up scripts, etc) so it's
# worth spending some time with the docs.

FROM pennlib/passenger-ruby23:0.9.23-ruby-build

RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/US/Eastern /etc/localtime

# Replace Let's Encrypt's expired DST Root CA X3 cert, which expired on 2021.09.30, with the newer ISRG Root X1 cert
# https://letsencrypt.org/docs/certificate-compatibility/
ADD https://letsencrypt.org/certs/isrgrootx1.pem /tmp/isrgrootx1.pem
RUN rm /usr/share/ca-certificates/mozilla/DST_Root_CA_X3.crt && \
    mkdir /usr/local/share/ca-certificates/letsencrypt.com && \
    mv /tmp/isrgrootx1.pem /usr/local/share/ca-certificates/letsencrypt.com/isrgrootx1.crt && \
    update-ca-certificates --fresh

RUN apt-get update && apt-get install -y --no-install-recommends npm libxml2-utils unzip openjdk-8-jre

# docker caches this step, but it does download the file each time.
ADD https://downloads.sourceforge.net/project/saxon/Saxon-HE/9.7/SaxonHE9-7-0-15J.zip /tmp
RUN mkdir -p /opt/saxon && cd /opt/saxon && unzip /tmp/SaxonHE9-7-0-15J.zip && rm /tmp/SaxonHE9-7-0-15J.zip
RUN echo "#!/bin/bash\nexec java \$JAVA_OPTS -cp /opt/saxon/saxon9he.jar net.sf.saxon.Transform \$@" > /usr/local/bin/saxon
RUN chmod a+x /usr/local/bin/saxon

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init process.
CMD ["/sbin/my_init"]

#### START of app-specific stuff

RUN mkdir -p /home/app/webapp

WORKDIR /home/app/webapp

# copy Gemfiles first: this takes advantage of caching during build
ADD Gemfile /home/app/webapp
ADD Gemfile.lock /home/app/webapp
RUN bundle install

ADD package.json /home/app/webapp
ADD jslib /home/app/webapp/jslib
RUN npm install

# everything after this ADD typically won't get cached by docker build
ADD . /home/app/webapp

# Store commit hash in image
ARG GIT_COMMIT
ENV GIT_COMMIT ${GIT_COMMIT}
RUN echo $GIT_COMMIT > /home/app/webapp/public/version.txt

RUN chown app.app -R /home/app/webapp

RUN mkdir -p /home/app/webapp/log
RUN chown app.app -R /home/app/webapp/log
RUN chmod ug+rw -R /home/app/webapp/log

RUN mkdir -p /home/app/webapp/tmp
RUN chown app.app -R /home/app/webapp/tmp
RUN chmod ug+rw -R /home/app/webapp/tmp

# enable nginx
RUN rm -f /etc/service/nginx/down

RUN rm /etc/nginx/sites-enabled/default
ADD nginx/webapp.conf /etc/nginx/sites-enabled/webapp.conf
ADD nginx/webapp-env.conf /etc/nginx/main.d/webapp-env.conf

# assets:precompile won't run unless these secrets are present, but
# it doesn't appear to actually use them, so we just use dummy values here
# RUN RAILS_ENV=production SECRET_TOKEN=dummy DEVISE_SECRET_KEY=dummy bundle exec rake assets:precompile

RUN chown -R app:app /home/app/webapp

# precompile assets at container startup: we do it this way instead of as part of image build,
# otherwise .js.erb files that use ENV will break
RUN echo "#!/bin/bash" > /etc/my_init.d/50_precompile_assets.sh
RUN echo "cd /home/app/webapp && bundle exec rake assets:precompile" >> /etc/my_init.d/50_precompile_assets.sh
RUN chmod a+rx /etc/my_init.d/50_precompile_assets.sh

RUN echo "#!/bin/bash" > /etc/my_init.d/60_db_migrate.sh
RUN echo "cd /home/app/webapp && RAILS_ENV=\$PASSENGER_APP_ENV bundle exec rake db:migrate" >> /etc/my_init.d/60_db_migrate.sh
RUN chmod a+rx /etc/my_init.d/60_db_migrate.sh

RUN echo "#!/bin/bash" > /etc/my_init.d/90_chown_app.sh
RUN echo "chown -R app:app /home/app/webapp" >> /etc/my_init.d/90_chown_app.sh
RUN chmod a+rx /etc/my_init.d/90_chown_app.sh

#### END of app-specific stuff

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
