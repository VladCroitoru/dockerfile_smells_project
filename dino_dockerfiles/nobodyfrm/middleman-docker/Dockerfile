# aktuelle Ruby-Version
FROM ruby:2.3.1

# User hinzufügen
RUN usr/sbin/useradd --create-home --home-dir /middleman --shell /bin/bash middleman

WORKDIR /middleman

# Alle notwendigen Dateien/Ordner hinzufügen
COPY Gemfile /middleman/
COPY Gemfile.lock /middleman/
COPY config.rb /middleman/
COPY config.ru /middleman/
COPY source /middleman/source/

# Mountpoint anlegen -> Zugriff vom Host aus
VOLUME /middleman

# Zugriffsrechte anpassen
RUN chown -R middleman:middleman /middleman

# wechsel des aktiven Users
USER middleman

# alle notwenigen Komponenten installieren - siehe Gemfile
RUN bundle install

# start des Middleman-Servers
ENTRYPOINT ["bundle", "exec", "middleman", "server"]
