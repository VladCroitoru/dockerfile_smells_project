FROM quay.io/travisci/travis-jvm
MAINTAINER "Tom Ellis <tellisnz@gmail.com>"
LABEL Description="A docker instance to debug Travis JVM builds."

USER travis
WORKDIR /home/travis
RUN /bin/bash -lc "gem install travis -v 1.8.2 --no-doc --no-ri ; \
gem install bundler ; \
git clone https://github.com/travis-ci/travis-build.git ~/.travis/travis-build ; \
bundle install --gemfile ~/.travis/travis-build/Gemfile ; \
mkdir build ; \
echo \"export TRAVIS_BUILD_APT_PACKAGE_WHITELIST=https://raw.githubusercontent.com/travis-ci/apt-package-whitelist/master/ubuntu-precise\" >> .bashrc ; \
echo \"export TRAVIS_BUILD_APT_SOURCE_WHITELIST=https://raw.githubusercontent.com/travis-ci/apt-source-whitelist/master/ubuntu.json\" >> .bashrc ; \
echo \"if [ -f ~/.bashrc ] ; then\" >> .bash_profile; \
echo \"   source ~/.bashrc \" >> .bash_profile; \
echo \"fi\" >> .bash_profile ;"

WORKDIR /home/travis/build
CMD /bin/bash;
