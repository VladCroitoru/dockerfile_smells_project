FROM wschroeder/openjdk-9-jdk
MAINTAINER William Schroeder <wschroed@wustl.edu>

RUN apt-get update

# Perl needs the locale set correctly
RUN apt-get install --no-install-recommends -y locales
RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales

# A few editors and packages, plus the ubuntu nodejs -> node fix
RUN apt-get install --no-install-recommends -y ca-certificates man-db perl-doc libmoose-perl nano vim emacs npm ant git less
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g npm
RUN npm install -g mocha

ADD challenges /challenges

# mocha does not recognize a globally-installed chai, so we do it locally
RUN cd /challenges/challenge1/javascript && npm install chai
RUN cd /challenges/challenge3/javascript && npm install chai

RUN git config --global user.email "jobseeker@example.com"
RUN git config --global user.name "Job Seeker"
RUN cd /challenges/challenge4 && \
    git clone https://github.com/broadinstitute/picard.git && \
    cd picard && \
    git checkout -b challenge4 2.2.1 && \
    sed -i 's/git@github.com:/https:\/\/github.com\//' build.xml && \
    git commit -am 'Do not require a github login' && \
    ant clone-htsjdk && \
    ant

# Some safe environments cannot run as root
RUN chmod -R a+rw /challenges

WORKDIR /challenges

