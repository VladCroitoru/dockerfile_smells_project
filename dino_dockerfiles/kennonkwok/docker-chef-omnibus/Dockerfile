# Omnibus Chef Client
#
# VERSION               0.0.1

FROM      ubuntu
MAINTAINER Kennon Kwok "kennon.kwok@gmail.com"

# install curl
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -fr /var/cache/apt

# install omunibus-chef
RUN curl -L "https://www.opscode.com/chef/install.sh" | bash -s -- -v 11.8.2
