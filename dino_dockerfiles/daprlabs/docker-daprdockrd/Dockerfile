FROM stackbrew/ubuntu:saucy
# Install dependencies and clean up.
RUN apt-get update && apt-get install -y gcc libsqlite3-dev libdevmapper-dev golang git mercurial supervisor nginx && apt-get -y clean all
ADD supervisord.conf /etc/supervisord.conf
# Install daprdockrd and clean up. 
RUN mkdir /build && mkdir /daprdockr && export GOPATH=/build && go get -v github.com/daprlabs/daprdockr && go build -v -o /daprdockr/daprdockrd github.com/daprlabs/daprdockr/daprdockrd && rm -rf /build && touch /tmp/daprdockrd.stdout && touch /tmp/daprdockrd.stderr


VOLUME ["/host/docker", "/host/proc"]
EXPOSE 80 433 53
CMD tail -F -n +0 /tmp/daprdockrd.stderr & tail -F -n +0 /tmp/daprdockrd.stdout & sleep 2 && /usr/bin/supervisord -c /etc/supervisord.conf

# Example usage: Note the unfortunate use of daprdockrcmd :(
# HOST_IP=`./daprdockrcmd -ip` docker run \
#   -v /var/run:/host/docker \
#   -v /proc:/host/proc \
#   -e ETCD_HOSTS="http://${HOST_IP}:5001,http://${HOST_IP}:5002,http://${HOST_IP}:5003" \
#   -e HOST_IP="${HOST_IP}" \
#   -p 80:80 -p 433:433 -p 53:53 daprlabs/daprdockr