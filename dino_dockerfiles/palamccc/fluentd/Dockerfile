FROM debian:stretch-slim
# install necessary and delete unnecessary to reduce docker image
RUN apt-get update && \
  apt-get install -y ruby ruby-dev gcc make && \
  gem install fluentd -v '~> 0.12.0' --no-ri --no-rdoc && \
  gem install fluent-plugin-google-cloud --no-ri --no-rdoc && \
  apt-get remove -y ruby-dev gcc make && \
  apt-get autoremove -y && \
  rm -rf /tmp/* /var/lib/gems/*/cache /root/.gem && \
  ls -d /var/lib/gems/*/gems/google-api-client-*/generated/google/apis/* | grep -v logging | xargs rm -Rf && \
  rm -Rf /var/lib/dpkg /var/log/apt /var/log/apt
ADD fluent.conf /fluentd/etc/fluent.conf
EXPOSE 24224
CMD ["fluentd", "--config", "/fluentd/etc/fluent.conf"]
