FROM ubuntu
MAINTAINER Andres Aguilar

WORKDIR /root
ENV HOME /root

RUN apt-get update -y
RUN apt-get upgrade -y

# Software Esencial
RUN apt-get install -y \
        build-essential \
        curl \
        git \
        libcurl4-openssl-dev \
        libffi-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxslt1-dev \
        libyaml-dev \
        python-software-properties \
        sqlite3 \
        sudo \
        vim \
        wget \
        zlib1g-dev

#Instalamos postgresql 9.6

ENV PATH "/usr/lib/postgresql/9.6/bin:$PATH"
RUN sh -c "echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' > /etc/apt/sources.list.d/pgdg.list"
RUN wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
RUN apt-get update
RUN apt-get install -y postgresql-9.6 libpq-dev

#Rbenv
RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
ENV PATH "$HOME/.rbenv/bin:$PATH"
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc

#Ruby-build
RUN git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
RUN echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
ENV PATH "$HOME/.rbenv/plugins/ruby-build/bin:$PATH"


#Compilamos la version 2.4.2 de Ruby
RUN rbenv install 2.4.2
RUN rbenv global 2.4.2
RUN $HOME/.rbenv/shims/gem install bundler
RUN rbenv rehash


#Rails utilizando Rbenv y nodejs

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y nodejs
RUN $HOME/.rbenv/shims/gem install rails -v 5.1.4
RUN rbenv rehash




#  initialize postgresql
ADD init.sh /usr/local/bin/init.sh
RUN chmod u+x /usr/local/bin/init.sh

CMD ["/usr/local/bin/init.sh"]
