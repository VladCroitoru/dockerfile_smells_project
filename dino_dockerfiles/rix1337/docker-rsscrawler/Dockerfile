FROM lsiobase/alpine.python3
MAINTAINER rix1337

# build tools
RUN apk add --no-cache build-base libc-dev libffi-dev g++ gcc libxslt-dev python3-dev

# dependencies
RUN /usr/bin/python3.6 -m pip install --upgrade pip \
  && pip install wheel \
  && pip install git+https://github.com/alberanid/imdbpy \
beautifulsoup4>=4.9.3 \
docopt>=0.6.2 \
flask>=2.0.0 \
passlib>=1.7.4 \
pycryptodomex>=3.10.1 \
python-dateutil>=2.0.0 \
rapidfuzz>=1.5.0 \
requests>=2.0.0 \
simplejson>=3.0.0 \
waitress>=2.0.0 \
lxml>=4.6.3
  
# add local files
COPY root/ /

# volumes and ports
VOLUME /config
EXPOSE 9090

# Set environment variables.
ENV USER=""
ENV PASS=""
ENV DEVICE=""
ENV LOGLEVEL=""
ENV VERSION=""

# invalidate build cache on repo commit
ADD "https://api.github.com/repos/rix1337/FeedCrawler/commits?per_page=1" latest_commit

# Install latest IMDbPY if available
RUN pip install git+https://github.com/alberanid/imdbpy

# Install FeedCrawler
RUN pip install feedcrawler --no-cache-dir
