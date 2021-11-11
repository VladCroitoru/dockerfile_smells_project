FROM ubuntu:16.04 


#Add the brightbox PPA manually to avoid installing loads of software
RUN echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu xenial main " >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C3173AA6

#Pre-requisites
RUN apt update -qq && \
    apt install -y ruby2.3 git gcc ruby2.3-dev make g++ && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN gem install --no-ri --no-rdoc \
  jekyll \
  jekyll-redirect-from \
  kramdown \
  rdiscount \
  rouge

WORKDIR /srv/jekyll/

ADD . /srv/jekyll/

CMD ["jekyll", "serve", "-H", "0.0.0.0"]
