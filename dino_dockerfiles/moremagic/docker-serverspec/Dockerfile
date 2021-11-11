# http://knowledge.sakura.ad.jp/tech/2596/
FROM moremagic/ubuntu-sshd
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y make gcc ruby ruby2.1-* gem
RUN gem install serverspec rake

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

