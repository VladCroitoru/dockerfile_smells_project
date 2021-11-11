FROM ruby:2.2.6-onbuild

MAINTAINER Mikhail Mangushev <development@2mx.org>

LABEL version="1.5.0"
LABEL description="Slate helps you create beautiful, intelligent, responsive API documentation."

COPY source source_example

RUN mkdir build

RUN apt-get update && apt-get install -y nodejs \
&& apt-get clean && rm -rf /var/lib/apt/lists/*


EXPOSE 4567

WORKDIR /usr/src/app

VOLUME ["/usr/src/app/source", "/usr/src/app/build"]

CMD ["bundle", "exec", "middleman", "server", "--watcher-force-polling"]