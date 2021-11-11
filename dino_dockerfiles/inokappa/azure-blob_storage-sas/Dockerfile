FROM ruby
MAINTAINER inokappa
RUN apt-get update
RUN git clone https://github.com/inokappa/azure-blob_storage-sas.git /app
RUN chmod 755 /app/azure-blob_storage-sas.rb
RUN gem install azure --version '0.6.4' --no-ri --no-rdoc
RUN gem install addressable --no-ri --no-rdoc

CMD /app/azure-blob_storage-sas.rb
