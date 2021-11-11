FROM maxexcloo/debian
RUN apt-get -y update
RUN apt-get -y install curl build-essential libxml2-dev libxslt-dev git
RUN curl -L https://www.chef.io/chef/install.sh | bash
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc
RUN /opt/chef/embedded/bin/gem install berkshelf
