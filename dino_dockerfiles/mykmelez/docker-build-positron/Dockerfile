FROM ubuntu:xenial

RUN apt-get update -y && \
    apt-get install -y \
      curl \
      git \
      nodejs \
      nodejs-legacy \
      npm \
      python \
      wget

# taskcluster-vcs should install promise, which is a dependency of multiple
# modules that taskcluster-vcs depends on.  But for some reason it's failing on:
#   npm WARN superagent-promise@0.2.0 requires a peer of >= 3.2.0 but none was installed.
#
# Then running tc-vcs complains:
#   tc-vcs checkout repo https://github.com/mozilla/gecko-dev https://github.com/mykmelez/positron merge-gecko-again
#   module.js:328
#       throw err;
#       ^
#
#   Error: Cannot find module 'promise'
#       at Function.Module._resolveFilename (module.js:326:15)
#       at Function.Module._load (module.js:277:25)
#       at Module.require (module.js:354:17)
#       at require (internal/module.js:12:17)
#       at Object.<anonymous> (/usr/local/lib/node_modules/taskcluster-vcs/node_modules/superagent-promise/index.js:6:31)
#       …
#
# So we install promise globally in addition to taskcluster-vcs, which works
# around the problem, per:
#   http://stackoverflow.com/questions/20764881/why-does-npm-install-say-i-have-unmet-dependencies
#
# Filed as: https://github.com/taskcluster/taskcluster-vcs/issues/68
#
RUN npm install -g promise taskcluster-vcs

# This gets the master version of bootstrap.py, but presumably the dependencies
# can change by branch.  Should we install dependencies at container run time
# rather than image build time?
RUN wget -O bootstrap.py https://raw.githubusercontent.com/mozilla/positron/master/python/mozboot/bin/bootstrap.py && python bootstrap.py --no-interactive --application-choice=browser

# bootstrap.py adds $HOME/.cargo/bin to the path in ~/.profile, but that file
# doesn't appear to get sourced when you `docker run -it [image] /bin/bash`,
# so we add it to the path explicitly here.
ENV PATH /root/.cargo/bin:$PATH

# Hopefully this'll enable us to remove the requirement to set SHELL at runtime
# before running `./mach build`.
ENV SHELL /bin/bash
