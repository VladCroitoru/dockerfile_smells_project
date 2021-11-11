# Base
FROM krallin/ubuntu-tini:trusty

# Set the locale
RUN locale-gen en_US.UTF-8
RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
# Fix local and timezone
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update

RUN apt-get install -y \
  python \
  ruby \
  libxml2-dev \
  curl \
  git \
  wget \
  build-essential \
  automake \
  autoconf \
  openssh-client \
  zlib1g-dev \
  gettext \
  libreadline-dev \
  libssl-dev \
  libffi-dev \
  bison \
  libicu-dev

RUN wget -qO- https://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.4.tar.gz | tar xvz

RUN cd ruby-2.2.4 && autoconf && ./configure --disable-install-doc && make && make install

# gem for github recommended
RUN gem install --no-ri --no-rdoc \
jekyll:3.1.3 \
jekyll-sass-converter:1.3.0 \
jekyll-textile-converter:0.1.0 \
kramdown:1.10.0 \
rdiscount:2.1.8 \
redcarpet:3.3.3 \
RedCloth:4.2.9 \
liquid:3.0.6 \
rouge:1.10.1 \
jemoji:0.6.2 \
jekyll-mentions:1.1.2 \
jekyll-redirect-from:0.10.0 \
jekyll-sitemap:0.10.0 \
jekyll-feed:0.5.1 \
jekyll-gist:1.4.0 \
jekyll-paginate:1.1.0 \
github-pages-health-check:1.1.0 \
jekyll-coffeescript:1.0.1 \
jekyll-seo-tag:1.4.0 \
github-pages:78 \
html-pipeline:2.4.1 \
sass:3.4.22 \
safe_yaml:1.0.4 \
jekyll-github-metadata:1.11.1 \
listen:3.0.6

# other needed gems
RUN gem install --no-ri --no-rdoc \
classifier-reborn \
concurrent-ruby \
fast-stemmer \
fastimage \
jekyll-assets \
maruku \
posix-spawn \
pygments.rb \
sprockets \
sprockets-helpers \
tilt \
toml \
yajl-ruby
