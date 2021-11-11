FROM registry.gitlab.com/gitlab-org/build/cng/gitlab-webservice-ee:v14.3.3

COPY --chown=git license_key.pub /srv/gitlab/.license_encryption_key.pub

RUN sed -i -r 's/presence\ \|\|\ STARTER_PLAN/presence\ \|\|\ ULTIMATE_PLAN/g' /srv/gitlab/ee/app/models/license.rb \
&& grep '.presence' /srv/gitlab/ee/app/models/license.rb

CMD /scripts/process-wrapper

HEALTHCHECK --interval=30s --timeout=30s --retries=5 \
CMD /scripts/healthcheck
