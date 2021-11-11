FROM google/cloud-sdk:198.0.0 as gcp

FROM docker:18.05-dind
COPY --from=gcp / /
COPY daemon.json /etc/docker/
ENTRYPOINT ["dockerd-entrypoint.sh"]
CMD []
