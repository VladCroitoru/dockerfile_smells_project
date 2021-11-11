FROM python:2.7.11-wheezy
MAINTAINER Cultureamp Infrastructure Services Team <is_team@cultureamp.com>

# The yapf version is fixed to 0.11.0. This is is because the latest release, i.e. 0.11.1,
# no longer exits with status 2 if the source code is not formatted when yapf --diff is run.
# We used this to fail the build if the source code is not formatted. The current exit code is 0
# whether the code is formatted or not. The latest release was supposed to make exit code
# customisable so that users can set their own exit code. But this doesn't work yet.

RUN pip install troposphere \
                awacs \
                pyyaml \
                yapf==0.11.0 \
                flake8 \
                autoflake \
                codeclimate-test-reporter \
                rainbow_logging_handler

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
