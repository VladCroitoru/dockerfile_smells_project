FROM debian:buster
# Build
ARG MIRROR_DEBIAN
ARG PYPI_URL
ARG PYPI_HOST
ARG PACKAGES="make unzip wget curl jq python-apt python python-pip apt-transport-https ca-certificates git"

# Run
ENV DEBIAN_FRONTEND noninteractive
ENV TERRAFORM_VERSION=0.15.5
ENV TERRAGRUNT_VERSION=0.30.3

# Install default packages
# Use nexus repo to speed up build if MIRROR_DEBIAN defined
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]
RUN echo "$http_proxy $no_proxy" && set -x && [ -z "$MIRROR_DEBIAN" ] || \
     sed -i.orig -e "s|http://deb.debian.org/debian|$MIRROR_DEBIAN/debian10|g ; s|http://security.debian.org/debian-security|$MIRROR_DEBIAN/debian10-security|g" /etc/apt/sources.list ; \
    apt-get -q update && \
    apt-get install -qy --no-install-recommends --force-yes \
    $PACKAGES && \
    apt-get autoremove -y && apt-get autoclean -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

## install pip modules
COPY requirements.txt /tmp/requirements.txt
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]
RUN pip_args="" ; [ -z "$PYPI_URL" ] || pip_args=" --index-url $PYPI_URL " ; \
    [ -z "$PYPI_HOST" ] || pip_args="$pip_args --trusted-host $PYPI_HOST " ; \
    echo "$no_proxy" |tr ',' '\n' | sort -u |grep "^$PYPI_HOST$" || \
      [ -z "$http_proxy" ] || pip_args="$pip_args --proxy $http_proxy " ; \
    pip install $pip_args -I --no-deps -r /tmp/requirements.txt

WORKDIR /data

# install terraform version
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]
RUN curl -O https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ \
    && rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    terraform --version

# Install tf provider plugins in /usr/local/share/terraform/plugins
COPY provider.tf .
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]
RUN mkdir -p /usr/local/share/terraform/plugins && \
      echo 'plugin_cache_dir = "/usr/local/share/terraform/plugins"' > $HOME/.terraformrc && \
      terraform init -backend=false

# install terragrunt version
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]
RUN curl -sL -o /usr/local/bin/terragrunt https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 && \
     chmod +x /usr/local/bin/terragrunt && \
     terragrunt --version

ENTRYPOINT ["/bin/bash"]
