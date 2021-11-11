FROM ubuntu:14.04
MAINTAINER Dan Shan <i@shanhh.com>

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:brightbox/ruby-ng
RUN apt-get update

RUN apt-get install -y curl nodejs nginx build-essential ruby2.2 ruby2.2-dev wget zip python-pip vim git

# install octopress
WORKDIR /tmp
RUN gem install --no-ri --no-rdoc bundler
RUN gem install --no-ri --no-rdoc octopress

# install jekyll
RUN gem install --no-ri --no-rdoc jekyll-sitemap jekyll-paginate jekyll-coffeescript
RUN gem install --no-ri --no-rdoc rdiscount kramdown pygments.rb

RUN pip install -U pip
RUN pip install pygments --upgrade


