FROM ubuntu:trusty
MAINTAINER Randall Smith <perlstalker@gmail.com>

RUN apt-get update

RUN apt-get install -y perl cpanminus build-essential

RUN apt-get install -y libdbi-perl libdbd-sqlite3-perl libxml-feedpp-perl libtime-local-perl

ADD gen_scripture_feed.pl /usr/local/bin/
#ADD scriptures.db /usr/local/share/
ADD https://github.com/PerlStalker/scripture-feed/raw/master/scriptures.db /usr/local/share/

# To change the base url, uncomment this and make the necessary changes
# or add `-e "BASE_URL=http://...` to `docker run`
#ENV BASE_URL http://perlstalker.vuser.org/Scriptures/

# To change the output directory, uncomment this and make the necessary change
# or add `-e OUTPUT_DIR=/path/to/scriptures` to `docker run`
# The output directory must exist.
#ENV OUTPUT_DIR /usr/local/nginx/html/Scriptures

ENTRYPOINT /usr/local/bin/gen_scripture_feed.pl
#ENTRYPOINT /bin/bash