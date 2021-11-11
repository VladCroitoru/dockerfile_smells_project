FROM ubuntu:16.04

RUN /usr/bin/apt-get update \
   && /usr/bin/apt-get install --no-install-recommends -qy ruby ruby-dev make g++ zlib1g-dev patch cron openssh-client rsync mysql-client bzip2 \
   && gem install backup whenever --no-ri --no-rdoc \
   && /bin/rm -rf /var/lib/gems/2.3.0/cache /var/cache/* /var/lib/apt/lists/* \
   && apt-get purge -qy ruby-dev make g++ zlib1g-dev patch \
   && apt-get -qy autoremove \
   && backup generate:config
ADD schedule.rb /backup/schedule.rb
ADD init.sh /init.sh
ADD models/ /root/Backup/models
ENTRYPOINT ["/bin/bash", "/init.sh"]
