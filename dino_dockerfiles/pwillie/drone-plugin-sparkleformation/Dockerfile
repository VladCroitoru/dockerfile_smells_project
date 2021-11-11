FROM ruby:2.5

LABEL description="Drone plugin to aid running sparkleformation"

WORKDIR /root

COPY install .

RUN chmod +x run.sh \
 && bundle update

ENTRYPOINT [ "/root/run.sh" ]

ARG VCS_REF
ARG VCS_URL
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url=$VCS_URL