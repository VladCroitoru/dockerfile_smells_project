FROM centos:centos7

MAINTAINER Pat Turner <pat.turner.fyi>

# Install a few RPMs
RUN echo "===> Adding epel, java, ruby, etc" && \
    yum update -y && \
    yum group install -y "Development Tools" && \
    yum install -y epel-release && \
    yum install -y wget openssl sudo unzip graphviz git perl \
                   java-1.8.0-openjdk  \
                   ruby ruby-devel rubygem-bundler

# Add Gems
RUN echo "===> Adding gems" && \
    gem install jekyll s3_website jekyll-gist jekyll-paginate jekyll-sitemap

# Clean up
RUN echo "===> Cleaning up" && \
    rm -rf /tmp/* && \
    yum upgrade -y && \
    yum clean all # && yum group remove -y "Development Tools"

WORKDIR /

# default command: ruby irb
CMD [ "irb" ]
