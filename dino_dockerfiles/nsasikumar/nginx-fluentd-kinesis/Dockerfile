FROM bprodoehl/nginx:latest
MAINTAINER nsasikumar@connectify.me

# Set correct environment variables.
ENV HOME /root

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && apt-get -y upgrade

# install default Ruby
RUN apt-get install -y curl build-essential ruby ruby-dev wget

RUN gem install bundler --no-ri --no-rdoc
#RUN gem install fluentd --no-ri --no-rdoc

# install git
RUN apt-get -y install git logrotate

# install Kinesis plugin
RUN ["git", "clone", "https://github.com/awslabs/aws-fluent-plugin-kinesis.git"]
WORKDIR aws-fluent-plugin-kinesis
RUN ["bundle", "install"]
RUN ["rake", "build"]
RUN ["rake", "install"] 

RUN mkdir /etc/fluent

ADD config/fluent.conf /etc/fluent/
ADD config/nginx-json.conf /etc/nginx/conf.d/

# Logrotate
ADD config/logrotate-nginx.conf /etc/logrotate.d/nginx
RUN chmod 0644 /etc/logrotate.d/nginx
RUN mv /etc/cron.daily/logrotate /etc/cron.hourly/

ADD fluentd.sh /etc/service/fluentd/run
