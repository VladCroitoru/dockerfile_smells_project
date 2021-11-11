FROM erdii/debian-8.2-ssh

RUN apt-get install --no-install-recommends -y \
    ca-certificates \
    git \
    build-essential \
    libzmq-dev \
    libpq-dev \
    python-dev \
    virtualenv \
    python-virtualenv \
    && apt-get clean

RUN mkdir /wd
WORKDIR /wd

# Clone the syncserver repo
RUN git clone https://github.com/mozilla-services/syncserver

WORKDIR /wd/syncserver
# Add psycopg2 to dependencies
RUN echo "psycopg2" >> requirements.txt
# Build
RUN make build
# Run the tests
RUN make test

# Create conf volume and copy in default settings
RUN mkdir /conf
COPY syncserver.ini /conf/
VOLUME ["/conf"]

EXPOSE 5000

CMD /wd/syncserver/local/bin/gunicorn --paste /conf/syncserver.ini
