FROM fedora:25

# Run update and install packages
RUN dnf update -y; \
    dnf install -y ansible rpm-ostree git; \
    dnf clean all

# Create working dir, clone fedora and centos atomic definitions
RUN mkdir -p /workspace ; \

# Create and initialize repo directory

    mkdir -p /srv/repo && \
    ostree --repo=/srv/repo init --mode=archive-z2

# Expose default SimpleHTTPServer port, set working dir
EXPOSE 8000
WORKDIR /workspace
VOLUME /workspace

# Start web server
CMD ostree trivial-httpd -p 8000 /svr/repo
