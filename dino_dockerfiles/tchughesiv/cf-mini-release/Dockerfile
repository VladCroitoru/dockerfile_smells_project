# Cloud Foundry release
# version 0.4
FROM tchughesiv/cf-mini-base:v237
MAINTAINER Tommy Hughes <tchughesiv@gmail.com>

WORKDIR /root
ENV HOME /root
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
RUN echo Etc/UTC > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

ENV INSTALLER_BRANCH v237
ENV NISE_DOMAIN cf-mini.example
ENV NISE_PASSWORD c1oudc0w

ADD dynamic_adds.sh /root/
ADD dynamic_adds_2.sh /root/
ADD cleanup.sh /root/

RUN apt-get update && curl -s -k -B https://raw.githubusercontent.com/tchughesiv/cf_nise_installer/${INSTALLER_BRANCH}/scripts/bootstrap.sh > /root/bootstrap.sh && chmod u+x /root/*.sh && sed -i 's/.\/scripts\/install.sh/\/root\/dynamic_adds.sh\n.\/scripts\/install.sh\n\/root\/cleanup.sh/g' ./bootstrap.sh && sed -i 's/com\/yudai\/cf_nise_installer/com\/tchughesiv\/cf_nise_installer/g' ./bootstrap.sh && ./bootstrap.sh && rm /root/*.sh && apt-get -y remove --purge apparmor && sed -i '/bundle install/d' /root/cf_nise_installer/scripts/install_cf_release.sh && wget -O /root/cf-cli_amd64.deb "https://cli.run.pivotal.io/stable?release=debian64&version=6.19.0&source=github-rel cf-cli_amd64.deb" && dpkg -i /root/cf-cli_amd64.deb && rm /root/cf-cli_amd64.deb && mkdir /root/cf_nise_installer/test_apps && mkdir /root/cf_nise_installer/test_apps/spring-music && mkdir /root/cf_nise_installer/test_apps/cf-env && mkdir /root/cf_nise_installer/test_apps/test_app && rm -rf /root/cf_nise_installer/test_app && rm -f /etc/supervisor/conf.d/supervisord.conf

WORKDIR /var/vcap/packages/cloud_controller_ng/cloud_controller_ng/
RUN find . -type f -name "Gemfile*" | xargs sed -i '/pg/ s/0.16.0/0.17.1/g' && /var/vcap/packages/ruby-2.3/bin/bundle install && /var/vcap/packages/ruby-2.3/bin/bundle clean