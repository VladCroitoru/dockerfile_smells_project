FROM fabric8/fluentd-kubernetes

RUN scl enable rh-ruby23 'gem install --no-document fluent-plugin-kafka -v 0.4.2'

ADD start-fluentd /start-fluentd
