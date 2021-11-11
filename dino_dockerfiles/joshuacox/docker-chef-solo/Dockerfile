FROM ubuntu:xenial
MAINTAINER Josh Cox <josh 'at' webhosting.coop>

ENV BUILD_PACKAGES='locales software-properties-common curl build-essential libxml2-dev libxslt-dev git ruby ruby-dev ca-certificates sudo net-tools vim' \
  LANG=en_US.UTF-8 \
  DOCKER_CHEF_SOLO_UPDATED=20181208

RUN DEBIAN_FRONTEND=noninteractive \
  && apt-get -qq update && apt-get -qqy dist-upgrade \
  && apt-get -qqy --no-install-recommends install \
     $BUILD_PACKAGES \
  && echo 'en_US.ISO-8859-15 ISO-8859-15'>>/etc/locale.gen \
  && echo 'en_US ISO-8859-1'>>/etc/locale.gen \
  && echo 'en_US.UTF-8 UTF-8'>>/etc/locale.gen \
  && locale-gen \
  && echo '%sudo ALL=(ALL) NOPASSWD:ALL'>> /etc/sudoers \
  && echo "Installing Chef This may take a few minutes..." \
  && curl -L https://www.getchef.com/chef/install.sh | sudo bash \
  && echo "gem: --no-ri --no-rdoc" > ~/.gemrc \
  && /opt/chef/embedded/bin/gem install berkshelf \
  && apt-get -yqq autoremove \
  && apt-get clean \
  && rm -Rf /var/lib/apt/lists/*


# RUN echo "Installing mysql now as the cookbook is failing This may take a few minutes..."

# Example usage
#RUN echo "Installing berksfile..."
#ADD ./Berksfile /Berksfile
#ADD ./chef/roles /var/chef/roles
#ADD ./chef/solo.rb /var/chef/solo.rb
#ADD ./chef/solo.json /var/chef/solo.json

#RUN echo "Installing berks This may take a few minutes..."
#RUN cd / && /opt/chef/embedded/bin/berks vendor /var/chef/cookbooks
#RUN chef-solo -c /var/chef/solo.rb -j /var/chef/solo.json

#RUN easy_install supervisor
#RUN echo "foo...."
#ADD ./start.sh /start.sh
#ADD ./foreground.sh /etc/apache2/foreground.sh
#ADD ./supervisord.conf /etc/supervisord.conf

#RUN chmod 755 /start.sh /etc/apache2/foreground.sh
#EXPOSE 80
#CMD ["/bin/bash", "/start.sh"]
