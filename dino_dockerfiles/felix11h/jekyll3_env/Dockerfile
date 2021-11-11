FROM centos:centos7
MAINTAINER Felix Z. Hoffmann <felix11h.dev@gmail.com>

# adapted from http://www.rampmeupscotty.com/blog/2015/03/31/dockerizing-jekyll/

RUN yum -y install git gcc gcc-c++ make wget

# install Ruby 2.4.2
RUN yum -y groupinstall "Development Tools"
RUN yum -y install openssl-devel
RUN wget http://cache.ruby-lang.org/pub/ruby/ruby-2.4.2.tar.gz
RUN tar xvfvz ruby-2.4.2.tar.gz
WORKDIR ruby-2.4.2
RUN ./configure
RUN make
RUN make install
RUN gem update --system

RUN gem update
RUN gem install jekyll jekyll-paginate jekyll-sitemap therubyracer json --no-doc --no-ri
RUN gem install jekyll-feed -v '0.9.3'
RUN gem install jekyll-seo-tag -v '2.4.0'
RUN gem install minima -v '2.3.0'

WORKDIR /blog

#ENTRYPOINT ["jekyll", "serve", "--host=0.0.0.0"]
