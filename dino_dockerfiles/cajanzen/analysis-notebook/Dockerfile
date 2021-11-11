FROM continuumio/miniconda
MAINTAINER Carl Janzen <carl.janzen@gmail.com>

# install gosu per: https://gist.github.com/DevoKun/5154c6e645f9ded0f3bd
RUN gpg --keyserver pgp.mit.edu --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && curl -o /usr/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/bin/gosu.asc \
    && rm /usr/bin/gosu.asc \
    && chmod +x /usr/bin/gosu

RUN conda install -y \
    jupyter \
    psycopg2 \
    scikit-learn \
    seaborn \
    sqlalchemy

RUN apt-get update \
    && apt-get install -y \
        graphviz \
        parallel \
        postgresql-client

WORKDIR /code
COPY entrypoint.sh /usr/bin
COPY login /usr/bin
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["/bin/bash"]
