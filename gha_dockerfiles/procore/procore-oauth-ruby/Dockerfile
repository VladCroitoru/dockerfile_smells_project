FROM ubuntu

RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    git \
    ruby \
    ruby-dev \
    bundler \
    ruby-foreman \
 && rm -rf /var/lib/apt/lists/*

# Install gems 
ENV APP_HOME /opt/proauth
ENV HOME /root
RUN mkdir $APP_HOME
WORKDIR /opt/proauth
COPY Gemfile $APP_HOME
COPY Gemfile.lock $APP_HOME
RUN bundle install

# Add app source to the image
COPY . $APP_HOME
COPY .env.docker $APP_HOME/.env

EXPOSE 5000
CMD ["foreman", "start"]

# Below is an alternative to using foreman
# ENTRYPOINT ["bundle", "exec", "puma", "--preload", "--bind", "tcp://0.0.0.0:5000", "--log-requests"]
# CMD ["--workers", "1", "--threads", "1:1"]
