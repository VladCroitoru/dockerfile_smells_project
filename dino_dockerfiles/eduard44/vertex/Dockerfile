FROM debian:jessie

MAINTAINER Eduardo Trujillo <ed@chromabits.com>

# Set environment to non-interactive
ENV DEBIAN_FRONTEND noninteractive
ENV HOME=/home/vertex

COPY root /

# Make setup scripts executable
RUN chmod u+x /opt/vertex/*.sh && chmod u+x /opt/vertex/*/**.sh

# Create groups and setup a non-root user
RUN /opt/vertex/build/users.sh \
    && /opt/vertex/build/repos.sh \
    && /opt/vertex/components/base.sh \
    && /opt/vertex/components/nodejs.sh \
    && /opt/vertex/components/hhvm.sh \
    && /opt/vertex/components/composer.sh \
    && /opt/vertex/build/clean.sh

COPY site /var/www/vertex
COPY LICENSE /opt/vertex/
COPY README.md /opt/vertex/

# Set permissions
RUN /opt/vertex/build/post.sh \
    && /opt/vertex/utils/report.sh

# Expose ports
EXPOSE 80

VOLUME /var/www/vertex

CMD ["/opt/vertex/run.sh"]
