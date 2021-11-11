# vim:set ft=dockerfile
FROM debian:jessie

# add cassandra specific repositories for version 1.2.x
RUN echo 'deb http://www.apache.org/dist/cassandra/debian 12x main' >> /etc/apt/sources.list
RUN gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
RUN gpg --export --armor F758CE318D77295D | apt-key add -

# system update
RUN apt-get update \
    && apt-get upgrade -y

# download cassandra (force yes because cassandra cannot be authenticated)
RUN apt-get install cassandra -y --force-yes

# configure cassandra
RUN set -x \
    && sed -i 's/NAME=cassandra/NAME=cassandra\nUSER=cassandra/g' /etc/init.d/cassandra \
    && sed -i 's/-user cassandra/-user $USER/g' /etc/init.d/cassandra \
    && echo 'USER=root' | tee -a /etc/default/cassandra

# copy entrypoint script
COPY ./entrypoint.sh /
RUN chmod o+x ./entrypoint.sh

# set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
CMD ["cassandra", "-f"]
