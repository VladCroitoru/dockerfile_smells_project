FROM ruby:2.2.6

MAINTAINER joesankey@gmail.com

#ruby
RUN apt-get -y -q update && apt-get -y -q install build-essential python-dev python-pip bash wget unzip python ca-certificates && apt-get clean
RUN pip install awscli
RUN gem update --system --no-ri --no-rdoc
RUN gem install bundler --no-ri --no-rdoc

# terraform
RUN wget https://releases.hashicorp.com/terraform/0.8.7/terraform_0.8.7_linux_amd64.zip
RUN unzip terraform_0.8.7_linux_amd64.zip
RUN mv terraform /usr/bin/

# aws
RUN aws configure set preview.cloudfront true

ENTRYPOINT ["/bin/bash", "-c"]