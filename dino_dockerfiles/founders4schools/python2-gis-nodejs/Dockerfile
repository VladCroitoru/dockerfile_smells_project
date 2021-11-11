FROM python:2.7

# Install GEOS and GDAL
RUN apt-get update && apt-get install -y libgeos-dev libgdal-dev python-gdal

# Command lines utils that needs to be in the PATH
RUN pip install coverage codecov fabric

# Install Nodejs 6
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 68576280 86E50310 && \
  echo "deb http://deb.nodesource.com/node_6.x jessie main" | tee /etc/apt/sources.list.d/nodesource.list && \
  apt-get update -qq ; \
  apt-get install -y -qq nodejs
  
# Allow Bower to run as root  : https://github.com/bower/bower/issues/1752#issuecomment-113455403
RUN echo '{ "allow_root": true }' > /root/.bowerrc  

# Install Heroku CLI
RUN wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz && \
  mkdir -p /usr/local/lib /usr/local/bin && \
  tar -xvzf heroku-linux-amd64.tar.gz -C /usr/local/lib && \
  ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku
