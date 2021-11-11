FROM debian

# Version of Radicale (e.g. 2.0.0)
ENV VERSION 1.1.4

LABEL org.label-schema.vcs-url="https://github.com/williamdes/radicale_server"
LABEL org.label-schema.name="Radicale server 1.1.4"
LABEL org.label-schema.description="Radicale server 1.1.4 with MySQL connection"
LABEL org.label-schema.url="https://radicale.org/"

# Install dependencies
RUN apt-get update && apt-get install python3 python3-pip -y
#      python3-dev \
#      libffi-dev \
#      ca-certificates \
#      openssl && \
#    python3 -m pip install passlib bcrypt
#apt del \
#      python3-dev \
#      build-base \
#      libffi-dev
# Install Radicale
ADD https://github.com/Kozea/Radicale/archive/${VERSION}.tar.gz radicale.tar.gz
RUN tar xzf radicale.tar.gz && \
    python3 -m pip install ./Radicale-${VERSION} && \
    rm -r radicale.tar.gz Radicale-${VERSION}
RUN python3 -m pip install SQLAlchemy
RUN python3 -m pip install pymysql
# Configuration data (Put the "config" file here!)
VOLUME /etc/radicale
# TCP port of Radicale (Publish it on a host interface!)
EXPOSE 13005
# Run Radicale (Configure it here or provide a "config" file!)
CMD ["radicale", "-C", "/etc/radicale/config"]
