FROM fedora:latest
LABEL maintainer='Alex Chvatal <yith@yuggoth.space>'

ENV RAILS_ENV=production \
    APPDIR=/opt/personae \
    APPUSER=personae \
    BUILD_DEPS='ruby-devel redhat-rpm-config gcc patch libffi-devel'

RUN useradd -md ${APPDIR} ${APPUSER}
WORKDIR ${APPDIR}
COPY Gemfile .
COPY Gemfile.lock .

RUN dnf -yq install ruby nodejs mariadb-devel ${BUILD_DEPS} && \
    gem install --silent bundler rake && \
    su ${APPUSER} -c "bundle install --without development test --deployment --quiet" && \
    dnf -yq erase ${BUILD_DEPS} && \
    dnf -q clean all && \
    rm -rf /var/cache/dnf/*

COPY . ./
COPY config/database.yml.example config/database.yml

RUN bundle exec rake assets:precompile && \
    chown -R ${APPUSER}:${APPUSER} ${APPDIR}

USER ${APPUSER}
EXPOSE 9292
CMD ["./script/personae.sh"]
HEALTHCHECK --interval=10s --timeout=3s \
    CMD curl -f http://localhost:9292/ || exit 1
