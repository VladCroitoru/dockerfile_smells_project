# perfectgift: a tornado webapp for creating wish lists between friends
# Copyright (C) 2014, NCSS14 Group 4

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# 1. The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM ubuntu:14.04
MAINTAINER "Aleksa Sarai <cyphar@cyphar.com>"

# Make sure the repos and packages are up to date
RUN apt-get update
RUN apt-get upgrade -y

# Install python3 and pillow.
RUN apt-get install -y python3 python3-imaging

# Set up cyphar.com server directory.
RUN mkdir -p -- /srv/db /srv/www
WORKDIR /srv/www

# Set up server user.
RUN useradd -U -M -s /bin/nologin -- drone
RUN passwd -d -- drone

# Change ownership.
RUN chown drone:drone -- /srv/www /srv/db
USER drone

# Copy over the cyphar.com app source.
COPY . /srv/www

# Initialise the sqlite database.
RUN python3 db/initdb.py -d /srv/db/wishlist.db

# Set up perfectgift server and port config.
EXPOSE 5000
ENTRYPOINT ["python3", "server.py", "-H0.0.0.0", "-p5000"]
CMD ["-d/srv/db/wishlist.db"]
