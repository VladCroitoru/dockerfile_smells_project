FROM heroku/cedar:14
MAINTAINER Matthew Landauer <matthew@oaf.org.au>

RUN curl https://github.com/gliderlabs/herokuish/releases/download/v0.3.33/herokuish_0.3.33_linux_x86_64.tgz \
		--silent -L | tar -xzC /bin

# install herokuish supported buildpacks and entrypoints
RUN /bin/herokuish buildpack install

# Add perl buildpack for morph
RUN /bin/herokuish buildpack install https://github.com/miyagawa/heroku-buildpack-perl.git 2da7480a8339f01968ce3979655555a0ade20564

# Add certificate authority used by mitmproxy
# Also needs to be identical to the cert at mitmproxy/mitmproxy-ca-cert.pem in
# https://github.com/openaustralia/morph
ADD mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy-ca-cert.crt
RUN update-ca-certificates

# Add prerun script which will disable output buffering for ruby
ADD prerun.rb /usr/local/lib/prerun.rb

# Postgres doesn't support this ancient version of Ubuntu and we don't
# need it. So commenting out of apt sources
RUN sed -e '/postgresql/ s/^#*/#/' -i /etc/apt/sources.list

# poppler-utils has a more recent pdftohtml than the pdftohtml package
# pdftohtml is needed by the python scraperwiki library
# libffi-dev needed by python cffi
# time is needed directly by morph.io for scraper run measurements
RUN apt-get update && apt-get install -y time libblas-dev liblapack-dev gfortran swig protobuf-compiler libprotobuf-dev libsqlite3-dev poppler-utils libffi-dev

# PhantomJS has been deprecated
RUN apt-get install -y phantomjs

# Version of chromedriver needs to match up with the version of chrome installed
# As of June 29 2021, Google Chrome version 91.0.4472.114 is installed
# There doesn't seem to a way that I can see to force a particular (old) version of
# Chrome to be installed. Sigh.

# Install chromedriver
RUN wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip && \
			unzip chromedriver_linux64.zip && \
			rm chromedriver_linux64.zip && \
			mv chromedriver /usr/local/bin && \
			chmod ugo+x /usr/local/bin/chromedriver

# Install chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
			echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
			apt-get update && \
			apt-get -y install google-chrome-stable

# We also need to make chrome trust our CA cert
RUN apt-get -y install libnss3-tools && \
			mkdir -p /app/.pki/nssdb && \
			certutil -d sql:/app/.pki/nssdb -N --empty-password && \
			certutil -d sql:/app/.pki/nssdb -A -t "C,," -n "mitmproxy ca cert" -i /usr/local/share/ca-certificates/mitmproxy-ca-cert.crt

# Make python pip use the new ca certificate. Wouldn't it be great if it used
# the system ca certificates by default? Well, it doesn't.
# Setting the PIP_CERT environment variable didn't work but this does
# TODO Remove this once compiles don't send traffic to mitmproxy
ADD pip.conf /etc/pip.conf
