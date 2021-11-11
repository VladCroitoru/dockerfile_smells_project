FROM crisbal/torch-rnn:base

MAINTAINER Matthew Burtless

# Install prereqs for openresty
RUN apt-get update && apt-get -y install \
  #libreadline-dev \
  #libncurses5-dev \
  libpcre3-dev \
  libssl-dev \
  #perl \
  wget \
  gettext

# Compile openresty from source with luajit
RUN \
  wget https://openresty.org/download/openresty-1.13.6.1.tar.gz && \
  tar -xzvf openresty-*.tar.gz && \
  rm -f openresty-*.tar.gz && \
  cd openresty-* && \
  ./configure --with-luajit && \
  make && \
  make install && \
  make clean && \
  cd .. && \
  rm -rf openresty-* && \
  rm -f /usr/local/openresty/nginx/html/index.html && \
  ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx && \
  ldconfig

# We have to make the cv dir as it doesn't exist by default
RUN mkdir /root/torch-rnn/cv

# Copy our model to a place torch-rnn can touch
COPY trailnamemodel.t7 /root/torch-rnn/cv/trailnamemodel.t7

# Copy our nginx and lua server conf
COPY nginx.conf.template /etc/nginx/nginx.conf.template
COPY serve.lua /root/torch-rnn/serve.lua
COPY run_nginx.sh /etc/nginx/run_nginx.sh

# Copy basic api testing page
COPY index.html /usr/local/openresty/nginx/html/index.html

# Define and expose default port
ENV PORT=6788
EXPOSE 6788

# Expose torch and nginx volumes
VOLUME ["/root/torch-rnn", "/etc/nginx"]

# Define the default command.
CMD ["sh", "/etc/nginx/run_nginx.sh"]
