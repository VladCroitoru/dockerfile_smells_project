FROM debian

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update
RUN apt-get install -y ruby
RUN apt-get install -y ruby-dev
RUN apt-get install -y ruby-ffi
RUN gem install jekyll
RUN gem install jekyll-paginate

EXPOSE 4000
CMD ["jekyll","serve"]

