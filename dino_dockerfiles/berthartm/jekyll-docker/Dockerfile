FROM ubuntu:14.10

RUN apt-get update && apt-get -y install \
    build-essential \
    nodejs \
    ruby2.1 \
    ruby2.1-dev
RUN gem install jekyll --no-rdoc --no-ri
ENTRYPOINT ["jekyll", "serve", "--watch", "--source", "/source", "--destination", "/destination", "--host", "0.0.0.0"]

EXPOSE 4000
VOLUME ["/source", "/destination"]
