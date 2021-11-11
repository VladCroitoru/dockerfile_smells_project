FROM jpetazzo/dind
MAINTAINER Mike Fiedler <miketheman@gmail.com>

RUN curl -L https://www.chef.io/chef/install.sh | sudo bash -s -- -P chefdk && \
      chef gem install kitchen-docker && \
      locale-gen en_US.UTF-8

# Need to set the ENTRYPOINT for subsequent kitchen commands to work
ENTRYPOINT ["wrapdocker"]
