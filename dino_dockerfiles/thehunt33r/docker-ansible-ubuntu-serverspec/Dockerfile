FROM ansible/ansible:ubuntu1404

# Because Ubuntu 14.04 is bundled with Ruby 1.9, we have to use Ruby > 2.0 and therefore need a PPA
RUN apt-get update && apt-get install -y software-properties-common 

RUN apt-add-repository ppa:brightbox/ruby-ng

RUN apt-get update && apt-get install -y gcc rake ruby2.2 ruby2.2-dev gem

RUN gem install serverspec

CMD ["/sbin/init"]
