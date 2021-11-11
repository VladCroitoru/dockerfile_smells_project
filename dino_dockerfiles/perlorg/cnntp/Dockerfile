FROM quay.io/perl/base-os:v3.12.1

USER root
ENV CBCONFIG=

RUN apk update; apk upgrade apk-tools; apk upgrade; apk add libxml2-dev

ENV CBROOTLOCAL=/cnntp/
ENV CBROOT=/cnntp/combust
WORKDIR /cnntp

EXPOSE 8299
CMD ./run

RUN addgroup cnntp && adduser -D -G cnntp cnntp

# - Alpine is missing some locale stuff so Number::Format fails some
# tests.
# - XML::Atom doesn't like newer XML-LibXML:
# https://github.com/miyagawa/xml-atom/issues/18
# - POSIX::strftime::compiler has weird time zone issues on Alpine 3.12
RUN cpanm --notest \
          Number::Format \
          XML::Atom \
          POSIX::strftime::Compiler

RUN cpanm Email::MIME Captcha::reCAPTCHA \
  XML::RSS XML::Atom::Feed XML::Atom::Entry \
  Email::Address Net::NNTP Email::Abstract \
  DateTime::Locale Template::Plugin::Number::Format \
  Starman Plack::Middleware::XForwardedFor \
  Plack::Middleware::Options \
  Plack::Middleware::AccessLog

ADD . /cnntp

RUN mkdir -p logs; chown cnntp logs

# because quay.io sets timestamps to 1980 for some reason ...
RUN find ./docs -type f -print0 | xargs -0 touch

USER cnntp

