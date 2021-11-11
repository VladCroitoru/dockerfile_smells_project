FROM ubuntu:16.04

MAINTAINER Sunggun Yu <sunggun.dev@gmail.com>

# Install wget and other packages
RUN set -x \
    && apt-get update \
    && apt-get install -y wget ca-certificates apt-transport-https rsync tzdata \
    && rm -rf /var/lib/apt/lists/*

# ARGs and ENVs for Chef Server installation
ARG CHEF_SERVER_VERSION=12.17.5
ARG CHEF_SERVER_DOWNLOAD_SHA256=a82ecaf04add5a08735909f61ada16088731f0cae5599e46558a75dc5c8239eb
ENV CHEF_SERVER_VERSION ${CHEF_SERVER_VERSION}
ENV CHEF_SERVER_DOWNLOAD_URL https://packages.chef.io/files/stable/chef-server/"$CHEF_SERVER_VERSION"/ubuntu/16.04/chef-server-core_"$CHEF_SERVER_VERSION"-1_amd64.deb
ENV CHEF_SERVER_DOWNLOAD_SHA256 ${CHEF_SERVER_DOWNLOAD_SHA256}

# ARGs and ENVs for Chef Manage installation
ARG CHEF_MANAGE_VERSION=2.5.8
ARG CHEF_MANAGE_DOWNLOAD_SHA256=ad94997f1ab171773ab9642cf48dc734ad53138157006f59f930476666ddc45e
ENV CHEF_MANAGE_VERSION ${CHEF_MANAGE_VERSION}
ENV CHEF_MANAGE_DOWNLOAD_URL https://packages.chef.io/files/stable/chef-manage/"$CHEF_MANAGE_VERSION"/ubuntu/16.04/chef-manage_"$CHEF_MANAGE_VERSION"-1_amd64.deb
ENV CHEF_MANAGE_DOWNLOAD_SHA256 ${CHEF_MANAGE_DOWNLOAD_SHA256}

# ARGs and ENVs for Chef Reporting installation
ARG CHEF_REPORTING_VERSION=1.7.8
ARG CHEF_REPORTING_DOWNLOAD_SHA256=698c888b8fe4237ca105485d43d026d30c0c7ab4e4c2eae3dc138eb9a9d9eae7
ENV CHEF_REPORTING_VERSION ${CHEF_REPORTING_VERSION}
ENV CHEF_REPORTING_DOWNLOAD_URL https://packages.chef.io/files/stable/opscode-reporting/"$CHEF_REPORTING_VERSION"/ubuntu/16.04/opscode-reporting_"$CHEF_REPORTING_VERSION"-1_amd64.deb
ENV CHEF_REPORTING_DOWNLOAD_SHA256 ${CHEF_REPORTING_DOWNLOAD_SHA256}

# Download and install the Chef-Server package
RUN set -x \
    && wget --no-verbose -O chef-server-core_"$CHEF_SERVER_VERSION"-1_amd64.deb "$CHEF_SERVER_DOWNLOAD_URL" \
    && echo "$CHEF_SERVER_DOWNLOAD_SHA256 chef-server-core_$CHEF_SERVER_VERSION-1_amd64.deb" | sha256sum -c - \
    && dpkg -i chef-server-core_"$CHEF_SERVER_VERSION"-1_amd64.deb \
    && rm chef-server-core_"$CHEF_SERVER_VERSION"-1_amd64.deb

# Download and install the Chef-Manage package
RUN set -x \
    && wget --no-verbose -O chef-manage_"$CHEF_MANAGE_VERSION"-1_amd64.deb "$CHEF_MANAGE_DOWNLOAD_URL" \
    && echo "$CHEF_MANAGE_DOWNLOAD_SHA256 chef-manage_$CHEF_MANAGE_VERSION-1_amd64.deb" | sha256sum -c - \
    && dpkg -i chef-manage_"$CHEF_MANAGE_VERSION"-1_amd64.deb \
    && rm chef-manage_"$CHEF_MANAGE_VERSION"-1_amd64.deb

# Download and install the Chef-Reporting package
RUN set -x \
    && wget --no-verbose -O opscode-reporting_"$CHEF_REPORTING_VERSION"-1_amd64.deb "$CHEF_REPORTING_DOWNLOAD_URL" \
    && echo "$CHEF_REPORTING_DOWNLOAD_SHA256 opscode-reporting_$CHEF_REPORTING_VERSION-1_amd64.deb" | sha256sum -c - \
    && dpkg -i opscode-reporting_"$CHEF_REPORTING_VERSION"-1_amd64.deb \
    && rm opscode-reporting_"$CHEF_REPORTING_VERSION"-1_amd64.deb

# Create the `/var/opt/chef-backup` directory for mountpoint
RUN set -x \
    && mkdir -p /var/opt/chef-backup

# Volumes
VOLUME ["/etc/opscode", "/var/opt/opscode", "/var/opt/chef-backup"]

# Copy Entrypoint file
ADD scripts/* /

# Set Entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Expose ports
EXPOSE 80 443

# Set WORKDIR
WORKDIR /opt/opscode
