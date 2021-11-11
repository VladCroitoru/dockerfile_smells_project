FROM ruby
RUN apt-get -y update && apt-get -y install libicu-dev
RUN gem install gollum
RUN gem install redcarpet org-ruby 
VOLUME /wiki
WORKDIR /wiki
RUN git init
CMD ["gollum", "--port", "80"]
EXPOSE 80

