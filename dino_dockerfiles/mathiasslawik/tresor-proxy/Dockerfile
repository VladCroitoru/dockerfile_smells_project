FROM dockerfile/ubuntu

# Install Ruby 2.1 using rvm
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 &&\
    curl -sSL https://get.rvm.io | bash -s stable --ruby=2.1

# Copy Proxy files
ADD . /root/tresor-proxy
WORKDIR /root/tresor-proxy

# Install gems of proxy
RUN /bin/bash -c "source /usr/local/rvm/scripts/rvm && bundle install" &&\
    chmod +x /root/tresor-proxy/bin/proxy_docker.sh

# Run Proxy
ENTRYPOINT ["/root/tresor-proxy/bin/proxy_docker.sh"]
