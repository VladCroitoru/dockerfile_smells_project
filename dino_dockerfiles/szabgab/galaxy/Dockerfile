FROM rakudo-star

WORKDIR /srv

ENV AUTHOR_TESTING=1

RUN echo "===> Installing system dependencies" && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential && \
    apt-get install -y libssl-dev && \
    apt-get install -y mongodb-server && \
    apt-get install -y redis-server && \
    apt-get install -y memcached && \
    apt-get install -y unzip && \
    apt-get install -y less && \
    apt-get install -y vim && \
    echo "===> Installing: Perl6 modules" && \
    zef install \
        Test::META \
        Path::Iterator \
        TAP::Harness \
        Crypt::Random \
        Crypt::Bcrypt \
        DBIish \
#        https://travis-ci.org/szabgab/galaxy/builds/265911018
#        https://github.com/tokuhirom/p6-HTTP-Server-Tiny/issues/63
        Sparrowdo \
        Cache::Memcached
#        && \
#    zef install \
#        Bailador \
#    #    Inline::Perl5 \
#    #    https://travis-ci.org/szabgab/galaxy/builds/265902800
#        App::Mi6 \
#        HTTP::UserAgent \
#        Crust

#RUN git clone https://github.com/tokuhirom/p6-HTTP-Server-Tiny.git 
#RUN cd p6-HTTP-Server-Tiny && prove6 t/09-chunked-request.t
        # additional modules
        # Redis \
        # MongoDB

COPY . /srv/

# COPY bashrc /root/.bashrc

CMD ["/bin/bash"]
