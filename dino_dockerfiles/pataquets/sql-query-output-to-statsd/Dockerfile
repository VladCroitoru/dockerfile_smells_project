FROM perl

RUN \
  cpanm \
    Config::General \
    DBD::mysql \
    DBI \
    File::Spec \
    Net::Statsd \
    Text::CSV_XS \
  && \
  rm -rf ~/.cpanm/

WORKDIR /usr/src/
ADD . /usr/src/

ENTRYPOINT [ "perl", "bin/sql_query_output_to_statsd" ]
