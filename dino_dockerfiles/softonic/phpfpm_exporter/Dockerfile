FROM golang:1.7

ARG "version=0.1.0-dev"
ARG "build_date=unknown"
ARG "commit_hash=unknown"
ARG "vcs_url=unknown"
ARG "vcs_branch=unknown"

LABEL org.label-schema.vendor="craigmj" \
    org.label-schema.name="phpfpm_exporter" \
    org.label-schema.description="Prometheus exporter for php-fpm processes." \
    org.label-schema.usage="/src/README.md" \
    org.label-schema.url="https://github.com/craigmj/phpfpm_exporter/blob/master/README.md" \
    org.label-schema.vcs-url=$vcs_url \
    org.label-schema.vcs-branch=$vcs_branch \
    org.label-schema.vcs-ref=$commit_hash \
    org.label-schema.version=$version \
    org.label-schema.schema-version="1.0" \
    org.label-schema.docker.cmd.devel="" \
    org.label-schema.build-date=$build_date


RUN git clone https://github.com/craigmj/phpfpm_exporter /tmp/phpfpm_exporter \
 && cd /tmp/phpfpm_exporter \
 && /tmp/phpfpm_exporter/build.sh \
 && mv /tmp/phpfpm_exporter/bin/phpfpm_exporter /bin/phpfpm_exporter

ENTRYPOINT ["/bin/phpfpm_exporter"]
CMD ["-help"]

#FROM scratch
#COPY --from=0 /tmp/phpfpm_exporter/bin/phpfpm_exporter .
#ENTRYPOINT ["./phpfpm_exporter"]
