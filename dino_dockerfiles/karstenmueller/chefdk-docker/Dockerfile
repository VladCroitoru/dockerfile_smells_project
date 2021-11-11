FROM ubuntu:16.04

ARG CHANNEL=stable
ARG VERSION=2.4.17
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/opt/chefdk/bin:/opt/chefdk/embedded/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN apt-get update
RUN apt-get install -qq -y wget git build-essential apt-transport-https
RUN wget --quiet "http://packages.chef.io/files/${CHANNEL}/chefdk/${VERSION}/ubuntu/16.04/chefdk_${VERSION}-1_amd64.deb" -O /tmp/chefdk.deb && \
    dpkg -i /tmp/chefdk.deb
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" \
    | tee /etc/apt/sources.list.d/azure-cli.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893 && \
    apt-get update -qq && apt-get install -qq -y azure-cli
RUN chef gem install --no-user-install inspec rake chef-provisioning-azurerm kitchen-azurerm bundler
RUN apt-get --quiet clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/bin/bash"]
