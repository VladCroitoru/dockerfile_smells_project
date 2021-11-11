# Docker container for all lint checks for the Nubis project
# docker run --mount type=bind,source="$(pwd)",target=/nubis/files nubisproject/nubis-travis:master

FROM alpine:3.6
LABEL maintainer="Jason Crowe <jcrowe@mozilla.com>"

ENV DepVersion=0.4.1 \
    DockerfilelintVersion=1.4.0 \
    PuppetVersion=4.10.9 \
    RubyLintVersion=2.0.4 \
    TerraformVersion=0.10.8

# Install runtime dependencies
RUN apk add --no-cache \
    bash \
    build-base \
    findutils \
    file \
    git \
    go \
    nodejs-npm \
    rsync \
    ruby \
    ruby-irb \
    python \
    py-setuptools

# Install build dependencies
#+ Cleanup apk cache files
RUN apk add --no-cache --virtual .build-dependencies \
    curl \
    ruby-dev \
    unzip \
    py-pip \
    && rm -f /var/cache/apk/APKINDEX.*

# puppet-lint requires ruby ruby-irb
# jsonlint requires ruby ruby-irb ruby-dev build-base
# mdl requires ruby ruby-irb
# puppet requires ruby ruby-irb

RUN gem install puppet-lint --no-document \
    && gem install puppet -v ${PuppetVersion} --no-document \
    && gem install jsonlint --no-document \
    && gem install mdl --no-document \
    && gem install travis --no-document \
    && gem install ruby-lint -v ${RubyLintVersion} --no-document \
    && curl -o shellcheck-latest.linux.x86_64.tar.xz \
    https://storage.googleapis.com/shellcheck/shellcheck-latest.linux.x86_64.tar.xz \
    && tar -xvf shellcheck-latest.linux.x86_64.tar.xz \
    && mkdir -p /nubis/bin \
    && mv shellcheck-latest/shellcheck /nubis/bin/shellcheck \
    && rm -rf shellcheck-latest shellcheck-latest.linux.x86_64.tar.xz \
    && curl -L -o terraform_${TerraformVersion}_linux_amd64.zip \
    https://releases.hashicorp.com/terraform/${TerraformVersion}/terraform_${TerraformVersion}_linux_amd64.zip \
    && unzip terraform_${TerraformVersion}_linux_amd64.zip -d /nubis/bin \
    && rm terraform_${TerraformVersion}_linux_amd64.zip \
    && npm install --global yarn \
    && curl -L -o dockerfilelint-${DockerfilelintVersion}.tar.gz \
    https://github.com/replicatedhq/dockerfilelint/archive/v${DockerfilelintVersion}.tar.gz \
    && tar -xf dockerfilelint-${DockerfilelintVersion}.tar.gz \
            dockerfilelint-${DockerfilelintVersion}/bin/ \
            dockerfilelint-${DockerfilelintVersion}/lib/ \
            dockerfilelint-${DockerfilelintVersion}/yarn.lock \
            dockerfilelint-${DockerfilelintVersion}/package.json \
    && mv dockerfilelint-${DockerfilelintVersion} /nubis/bin/dockerfilelint \
    && rm dockerfilelint-${DockerfilelintVersion}.tar.gz \
    && cd /nubis/bin/dockerfilelint && yarn \
    && pip install pylint \
    && curl -L -o dep https://github.com/golang/dep/releases/download/v${DepVersion}/dep-linux-amd64 \
    && chmod +x dep \
    && mv dep /nubis/bin/

# Remove build dependencies
RUN apk del .build-dependencies

COPY [ "main.sh", "/nubis/bin/" ]
COPY [ "run-checks", "/nubis/bin/" ]
COPY [ "run-builds", "/nubis/bin/" ]
COPY [ "go-build", "/nubis/bin/" ]
COPY [ "mdl_style", "/nubis/" ]
WORKDIR /nubis/files
ENV PATH /nubis/bin:$PATH
ENTRYPOINT [ "main.sh" ]
CMD [ "lint" ]
