FROM ubuntu:trusty
## SSH Stuff
RUN apt-get update \
  && apt-get install -y openssh-server acl attr python-xattr build-essential make curl \
  && mkdir /var/run/sshd \
  && (echo 'root:root' | chpasswd) \
  && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
  && echo 'UseDNS no' >> /etc/ssh/sshd_config \
  && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
  && printf '#!/usr/bin/env bash\nservice ssh start\ntail -f /var/log/dmesg' > /start.sh \
  && chmod +x /start.sh
EXPOSE 22
CMD /start.sh

## Ruby stuff
RUN /bin/bash -c "gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
  && (\curl -sSL https://get.rvm.io | bash -s stable --ruby --quiet-curl) \
  && source /usr/local/rvm/scripts/rvm \
  && gem install bundler"
COPY . /tmp/deb-s3
WORKDIR /tmp/deb-s3
RUN /bin/bash -c "source /usr/local/rvm/scripts/rvm && bundle install"
# ENTRYPOINT [ "bundle", "exec", "deb-s3" ]
