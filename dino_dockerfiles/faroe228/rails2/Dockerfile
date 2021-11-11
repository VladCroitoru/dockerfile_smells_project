### FROM ubuntu:trusty-20150218.1
FROM gstark/ubuntu-for-rails

### lpt
### docker build .
###
### docker build -t faroe228/rails2:latest .
###

MAINTAINER Gavin Stark "gstark@realdigitalmedia.com"

#
# ...
#

# ----------
# Upgrade OS
# ----------
RUN apt-get -y update
RUN apt-get -y upgrade

CMD ["/bin/bash"]

# --- lpt added ---
RUN apt-get install --yes --no-install-recommends sqlite3 libsqlite3-dev

RUN gem install rails

# RUN rails new blog && cd blog


