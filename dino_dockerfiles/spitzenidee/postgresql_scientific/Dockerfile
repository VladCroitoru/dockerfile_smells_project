FROM spitzenidee/postgresql_rdkit_timescaledb:latest
MAINTAINER Michael Spitzer <professa@gmx.net>

#######################################################################
# Prepare the environment:
ENV PG_MAJOR 9.6
ENV PGUSER postgres
ENV PGPASSWORD postgres
ENV PGDATABASE postgres
ENV PGHOST 127.0.0.1
ENV PGPORT 5432

#######################################################################
# Prepare the build requirements for the rdkit compilation:
RUN apt-get update && apt-get install -y \
    postgresql-server-dev-all \
    postgresql-$PG_MAJOR-plr \
    pgxnclient \
    cmake \
    m4 \
    build-essential

# Install MADlib
RUN pgxn install madlib
# does not work: RUN /usr/local/madlib/bin/madpack -s madlib -p postgres install

# Clean up again:
RUN apt-get remove -y git cmake build-essential && \
    apt-get autoremove --purge -y && \
    apt-get clean && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/*

# Done.
