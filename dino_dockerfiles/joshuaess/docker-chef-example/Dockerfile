FROM debian:latest
RUN apt-get update && \
    echo 'nope' | apt-get -y install chef
    # curl -L https://www.opscode.com/chef/install.sh | bash

#recipe == puppetfile
COPY cookbooks /cookbooks

ENV cookbook_path=/cookbooks

# chef solo has been deprecated in favor of chef local mode
RUN chef-client -z "/cookbooks/apache2/recipes/default.rb"

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
