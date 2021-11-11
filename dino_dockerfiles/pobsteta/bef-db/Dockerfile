# PostgreSQL stack
#
# This image includes the following tools
# - PostgreSQL 9.5
# - Postgis 2.2
# - SIME 2.8
#
# Version 1.0

# Image de base ubuntu modifiée
FROM pobsteta/docker-base
MAINTAINER Pascal Obstetar <pascal.obstetar@bioecoforests.com>

# ---------- DEBUT --------------

# On évite les messages debconf
ENV DEBIAN_FRONTEND noninteractive

# On explicite user/group IDs
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999 postgres

# Grab gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y --auto-remove ca-certificates

# On met la locale à "fr_FR.UTF-8" pour que Postgres soit en français par défaut
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8
ENV LANG fr_FR.utf8

# Les versions de PostgreSQL/Postgis à installer
ENV PG_MAJOR 9.5
ENV POSTGIS_MAJOR 2.2

# on ajoute le dépôt Postgres
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main $PG_MAJOR" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update \
	&& apt-get install -y postgresql-common \
	&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-common/createcluster.conf \
	&& apt-get install -y \
		postgresql-$PG_MAJOR \
		postgresql-contrib-$PG_MAJOR \
		postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
        postgis \
	&& rm -rf /var/lib/apt/lists/*

# On met les fichiers de configuration de Postgres en place
RUN mv -v /usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample /usr/share/postgresql/ \
	&& ln -sv ../postgresql.conf.sample /usr/share/postgresql/$PG_MAJOR/ \
	&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!" /usr/share/postgresql/postgresql.conf.sample

RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql

ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH
ENV PGDATA /var/lib/postgresql/data
VOLUME ["/var/lib/postgresql/data"]

# Crée le répertoire docker-entrypoint-initdb.d
RUN mkdir /docker-entrypoint-initdb.d

# Copie le script de création des bases de données postgis
COPY ./init-postgis-db.sh /docker-entrypoint-initdb.d/init-postgis-db.sh
RUN chmod 700 /docker-entrypoint-initdb.d/init-postgis-db.sh

# === On ajoute ici le fichier de sauvegarde de la bdd BEF de démo ===

RUN mkdir -p /data/restore \
	&& cd /data/restore \
	&& wget -c ftp://139.59.135.185/bef/tryton.sql.gz

# ====================================================================

# On supprime wget
RUN apt-get purge -y --auto-remove wget

COPY init-pg.sh /
RUN chmod 700 /init-pg.sh

ENTRYPOINT ["/init-pg.sh"]

EXPOSE 5432

CMD ["postgres"]

# ---------- FIN --------------
#
# Nettoie les APT
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

