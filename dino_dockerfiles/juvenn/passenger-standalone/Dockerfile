FROM debian:stretch
MAINTAINER Juvenn Woo machese@gmail.com

RUN  apt-get update \
  && apt-get install -y dirmngr gnupg apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
                --recv-keys 561F9B9CAC40B2F7 \
  && echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger stretch main" > /etc/apt/sources.list.d/passenger.list \
  && apt-get update \
  && apt-get install -y passenger \
  && passenger-config validate-install --auto \
  && apt-get clean

WORKDIR /usr/share/passenger/standalone_default_root
EXPOSE 3000

ENTRYPOINT ["passenger", "start", "--log-file", "/dev/stdout"]
