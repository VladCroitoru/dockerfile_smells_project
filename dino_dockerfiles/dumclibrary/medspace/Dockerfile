FROM gitlab-registry.oit.duke.edu/mclibrary/medspace:dependencies

ADD . /srv/rails

RUN chown -R rails:rails /srv/rails \
    && su rails -c "bundle install" \
    && su rails -c "bin/rails assets:precompile RAILS_ENV=production SECRET_KEY_BASE=secret"

USER rails