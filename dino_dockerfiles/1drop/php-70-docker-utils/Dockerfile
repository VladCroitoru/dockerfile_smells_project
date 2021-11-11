FROM webdevops/php:7.0

ENV GIT_LFS_VERSION=2.3.4

RUN apt-install ansible \
    && ansible-galaxy install ansistrano.deploy,1.12.0 ansistrano.rollback,1.5.0
# Add git lfs
RUN curl -Lo git-lfs.tar.gz https://github.com/git-lfs/git-lfs/releases/download/v${GIT_LFS_VERSION}/git-lfs-linux-amd64-${GIT_LFS_VERSION}.tar.gz \
    && tar xzf git-lfs.tar.gz && cd git-lfs-${GIT_LFS_VERSION} && ./install.sh && cd .. && rm -rf git-lfs*
# Install utilities defined in composer.json globally
ENV PATH "/root/.composer/vendor/bin:$PATH"
COPY composer.json /root/.composer/composer.json
RUN composer global install -ao --no-dev \
    && composer clearcache
