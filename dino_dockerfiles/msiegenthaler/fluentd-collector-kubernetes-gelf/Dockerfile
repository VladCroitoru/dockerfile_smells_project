FROM fabric8/fluentd:0.14.8
MAINTAINER Mario Siegenthaler <mario.siegenthaler@linkyard.ch>


ENTRYPOINT ["fluentd"]

RUN yum install -y gcc-c++ wget

RUN scl enable rh-ruby23 'gem install --no-document fluent-plugin-kubernetes_metadata_filter -v 0.26.2' && \
    scl enable rh-ruby23 'gem install --no-document gelf -v 3.0.0' && \
    scl enable rh-ruby23 'gem cleanup fluentd'

RUN mkdir -p /etc/fluent/plugin \
    && wget https://raw.githubusercontent.com/bedag/fluent-plugin-gelf/master/lib/fluent/plugin/out_gelf.rb -O /etc/fluent/plugin/out_gelf.rb

ENV GELF_HOST graylog-logging.logging.svc.cluster.local
ENV GELF_PORT 12100

ADD fluent.conf /etc/fluent/fluent.conf
