FROM ruby:2.3.0-slim

ENV LANG en_US.UTF-8 
ENV LC_ALL en_US.UTF-8 
ENV LANGUAGE en_US:en 

WORKDIR /opt/beef

RUN apt-get update \
  && apt-get install -y \
    build-essential \
    git \
    sqlite3 \
    nodejs \
    libsqlite3-dev \
  && rm -rf /var/lib/apt/lists/*

RUN git clone --depth=1 \
    --branch=master \
    https://github.com/beefproject/beef.git \
    /opt/beef \
  && apt-get -y purge git

RUN gem install rake \
  && bundle install \
  && apt-get purge -y build-essential \
                      libsqlite3-dev \
  && apt-get -y autoremove

EXPOSE 3000 6789 61985 61986

CMD ["ruby", "beef"]
