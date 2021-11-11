FROM lpenz/debian-etch-amd64:latest

LABEL maintainer="Takuya Nakade <takuya@na-ka.de>"

RUN apt-get update && apt-get install -y wget ruby rdoc libmysql-ruby mysql-server
RUN cd /usr/local && wget http://pkgs.fedoraproject.org/repo/pkgs/rubygems/rubygems-1.2.0.tgz/b77a4234360735174d1692e6fc598402/rubygems-1.2.0.tgz && tar xzf rubygems-1.2.0.tgz && cd rubygems-1.2.0/ && ruby setup.rb && cd /usr/local/bin && ln -s /usr/local/rubygems-1.2.0/bin/gem && rm /usr/local/rubygems-1.2.0.tgz
RUN gem install rake -v "0.6.2" && gem install rails -v "1.0.0"
