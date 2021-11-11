FROM tozd/runit

ENV DOMAIN_NAME docker
ENV HOSTS_PATH /hosts

VOLUME /var/log/hosts

# You should also volume mount "/var/run/docker.sock" from the host into the container under "/var/run/docker.sock".
# You should volume mount a file into the container under "/hosts" (or to what "HOSTS_PATH" is set) and it will be
# populated with entries.

ADD . /build

RUN apt-get update -q -q && \
 apt-get install --yes --force-yes wget git && \
 wget -q https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz -O /tmp/go.tar.gz && \
 tar -C /usr/local -xzf /tmp/go.tar.gz && \
 export PATH="$PATH:/usr/local/go/bin" && \
 wget -q https://raw.githubusercontent.com/pote/gvp/v0.2.0/bin/gvp -O /tmp/gvp && \
 cd /build && \
 . /tmp/gvp && \
 wget -qO- https://raw.githubusercontent.com/pote/gpm/v1.3.1/bin/gpm | bash && \
 go build -v -o /usr/local/bin/docker-host ./... && \
 rm -rf /tmp/gvp /build /usr/local/go /tmp/go.tar.gz && \
 apt-get purge --yes --force-yes git wget && \
 apt-get autoremove --yes --force-yes

ADD ./etc /etc
