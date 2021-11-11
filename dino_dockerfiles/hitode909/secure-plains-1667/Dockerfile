FROM heroku/cedar:14

RUN useradd -d /app -m app
USER app
WORKDIR /app

ENV HOME /app
ENV PORT 3000

RUN mkdir -p /app/heroku
RUN mkdir -p /app/src
RUN mkdir -p /app/.profile.d

RUN mkdir -p /app/perl

WORKDIR /app/src

ENV PERL_VERSION 5.20.1
ENV PATH /app/perl/perl-$PERL_VERSION/bin:$PATH
ENV CPAN_INSTALL_PATH /app/heroku/cpan

# Perl
RUN curl -sL https://raw.githubusercontent.com/tokuhirom/Perl-Build/master/perl-build > /app/heroku/perl-build
RUN perl -pi -e 's%^#!/usr/bin/env perl%#!/usr/bin/perl%g' /app/heroku/perl-build
RUN chmod +x /app/heroku/perl-build
RUN /app/heroku/perl-build $PERL_VERSION /app/perl/perl-$PERL_VERSION
RUN curl -sL http://cpanmin.us/ | /app/perl/perl-$PERL_VERSION/bin/perl - --notest App::cpanminus Carton

RUN echo "export PATH=\"/app/perl/perl-5.20.1/bin:\$PATH\"" > /app/.profile.d/perl.sh
RUN echo "cd /app/src" >> /app/.profile.d/perl.sh

COPY cpanfile /app/src/

RUN carton install

COPY . /app/src

EXPOSE 3000
