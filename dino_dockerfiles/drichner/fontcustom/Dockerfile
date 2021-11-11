FROM debian:wheezy
MAINTAINER Dan Richner
 
# Update packages and install ruby
RUN apt-get update && apt-get install -y build-essential zlib1g zlib1g-dev ruby1.*.*-dev fontforge wget unzip sudo python

# Install latest fontcustom
RUN wget http://people.mozilla.com/~jkew/woff/woff-code-latest.zip
RUN cd
RUN unzip woff-code-latest.zip -d sfnt2woff && cd sfnt2woff && make && sudo mv sfnt2woff /usr/local/bin/
RUN gem install fontcustom

# Cleanup
ENV SUDO_FORCE_REMOVE yes
RUN apt-get --purge remove -y build-essential unzip sudo wget zlib1g-dev

#Volumes
VOLUME ["/project"]
WORKDIR /project

# Default run "fontcustom --help"
ENTRYPOINT ["/usr/local/bin/fontcustom"]
CMD ["--help"]