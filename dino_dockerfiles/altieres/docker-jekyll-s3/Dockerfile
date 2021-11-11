FROM ruby:2.2.4

## Java for s3_website
RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list

ENV LANG C.UTF-8

ENV JAVA_VERSION 8u66
ENV JAVA_DEBIAN_VERSION 8u66-b17-1~bpo8+1

# see https://bugs.debian.org/775775
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872
ENV CA_CERTIFICATES_JAVA_VERSION 20140324

RUN set -x \
	&& apt-get update \
	&& apt-get install -y \
		openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \
		ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \
	&& rm -rf /var/lib/apt/lists/*

# see CA_CERTIFICATES_JAVA_VERSION notes above
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure


## Watching inside the container

RUN apt-get update && apt-get install -y rsync && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app/site
RUN mkdir /usr/src/app/mirror
WORKDIR /usr/src/app

COPY run.sh /usr/src/app/
COPY watcher.rb /usr/src/app/


## Jekyll

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install

# deve baixar o jar depois de instalar a gem
ADD https://github.com/laurilehmijoki/s3_website/releases/download/v2.12.2/s3_website.jar /usr/local/bundle/gems/s3_website-2.12.2/s3_website-2.12.2.jar

CMD ["./run.sh"]
EXPOSE 4000
