# asaedit
#
# VERSION               0.0.1

FROM paintedfox/ruby
MAINTAINER Evan Gray <evan.gray@rackspace.com>

RUN 	apt-get install -y git libxslt1-dev libxml2-dev nodejs mysql-client libmysqlclient-dev libsqlite3-dev libcurl4-openssl-dev libpcre3-dev curl wget
RUN 	gem install bundle

ENTRYPOINT 	bundle config --global jobs 6 && git clone https://github.com/evanscottgray/asaedit && cd asaedit && bundle install && ruby app.rb -o 0.0.0.0 -p 3000

EXPOSE	3000
