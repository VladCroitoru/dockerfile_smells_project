FROM ruby:2.3.1-alpine
MAINTAINER nownabe

RUN apk add --update --no-cache build-base

######################
# MeCab with NEologd #
######################
ENV MECAB_VERSION 0.996
ENV IPADIC_VERSION 2.7.0-20070801
ENV mecab_url https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
ENV ipadic_url https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM
ENV build_deps 'curl git bash file sudo openssh'

RUN apk add --update --no-cache ${build_deps} \
  # Install MeCab
  && curl -SL -o mecab-${MECAB_VERSION}.tar.gz ${mecab_url} \
  && tar zxf mecab-${MECAB_VERSION}.tar.gz \
  && cd mecab-${MECAB_VERSION} \
  && ./configure --enable-utf8-only --with-charset=utf8 \
  && make \
  && make install \
  && cd \
  # Install IPA dic
  && curl -SL -o mecab-ipadic-${IPADIC_VERSION}.tar.gz ${ipadic_url} \
  && tar zxf mecab-ipadic-${IPADIC_VERSION}.tar.gz \
  && cd mecab-ipadic-${IPADIC_VERSION} \
  && ./configure --with-charset=utf8 \
  && make \
  && make install \
  && cd \
  # Install Neologd
  && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
  && mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y \
  # Remove build tools
  && apk del ${build_deps} \
  && rm -rf \
    mecab-${MECAB_VERSION}* \
    mecab-${IPADIC_VERSION}* \
    mecab-ipadic-neologd

###########
# Node.js #
###########
ENV NODE_VERSION 6.2.0
ENV build_deps 'curl python linux-headers'

RUN apk add --update --no-cache ${build_deps} \
  && curl -SLO https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz \
  && tar zxf node-v${NODE_VERSION}.tar.gz \
  && cd node-v${NODE_VERSION} \
  && ./configure \
  && make \
  && make install \
  && apk del ${build_deps} \
  && rm -rf node-v${NODE_VERSION}*

#############
# Rails App #
#############
ENV RACK_ENV production
ENV RAILS_LOG_TO_STDOUT true
ENV SECRET_KEY_BASE your_secret_key_base

# Required packages for PNC
RUN apk add --no-cache \
  libxml2-dev \
  libxslt-dev \
  sqlite-dev \
  tzdata

# Configure Timezone
RUN cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

WORKDIR /usr/src/app
COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle config build.nokogiri --use-system-libraries
RUN bundle install
COPY . /usr/src/app

CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]
