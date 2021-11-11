FROM debian:jessie

MAINTAINER Jose Plana <jplana@gmail.com>
RUN apt-get update
RUN echo "deb https://packagecloud.io/grafana/stable/debian/ wheezy main" >> /etc/apt/sources.list
RUN apt-get install -y curl apt-transport-https
RUN curl https://packagecloud.io/gpg.key | apt-key add -
RUN apt-get update
RUN apt-get install -y grafana
RUN mkdir -p /var/log/grafana /var/lib/grafana

ADD configuration/grafana.ini /etc/grafana/grafana.ini

EXPOSE 3000
VOLUME /var/lib/grafana

WORKDIR /usr/share/grafana
CMD /usr/sbin/grafana-server -config=/etc/grafana/grafana.ini cfg:default.paths.data=/var/lib/grafana cfg:default.paths.logs=/var/log/grafana

