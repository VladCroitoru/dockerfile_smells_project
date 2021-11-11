FROM registry.access.redhat.com/ubi8/python-38

# Install dependencies and clean cache to make the image cleaner

USER 0
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
    yum remove -y npm && \
    yum install -y hostname shared-mime-info && \
    yum upgrade -y --security && \
    yum clean all -y

COPY . /tmp/src
RUN chown -R 1001:0 /tmp/src

USER 1001

ENV ENABLE_PIPENV=true
ENV APP_SCRIPT=run_app.sh
ENV PIN_PIPENV_VERSION=2021.5.29

# Install the dependencies
RUN /usr/libexec/s2i/assemble

# Set the default command for the resulting image
CMD /usr/libexec/s2i/run
