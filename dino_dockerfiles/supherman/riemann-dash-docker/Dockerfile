FROM ubuntu
MAINTAINER Herman Moreno <herman@crowdint.com>

RUN apt-get update
RUN apt-get install -y ruby1.9.1 ruby1.9.1-dev rubygems1.9.1 build-essential libopenssl-ruby1.9.1 libssl-dev zlib1g-dev curl default-jre-headless

RUN curl http://aphyr.com/riemann/riemann_0.2.4_all.deb > /tmp/riemann_0.2.4_all.deb
RUN dpkg -i /tmp/riemann_0.2.4_all.deb

RUN gem install riemann-dash

# Expose riemann dash port
EXPOSE 4567

# Expose the ports for inbound events and websockets
EXPOSE 5555
EXPOSE 5555/udp
EXPOSE 5556

ADD ./riemann.config /etc/riemann/riemann.config
ADD ./config.rb /etc/riemann/riemann-dash-config.rb

CMD echo 127.0.0.1 $(hostname) > /etc/hosts; /usr/bin/riemann /etc/riemann/riemann.config && riemann-dash /etc/riemann/riemann-dash-config.rb
