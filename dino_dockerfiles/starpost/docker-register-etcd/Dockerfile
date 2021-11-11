FROM radial/busyboxplus

RUN curl -L -O https://github.com/jwilder/docker-gen/releases/download/0.4.3/docker-gen-linux-amd64-0.4.3.tar.gz
RUN gunzip < docker-gen-linux-amd64-0.4.3.tar.gz | tar x -C /usr/bin
 
RUN curl -L -O https://github.com/coreos/etcd/releases/download/v2.2.1/etcd-v2.2.1-linux-amd64.tar.gz
RUN gunzip < etcd-v2.2.1-linux-amd64.tar.gz | tar xO etcd-v2.2.1-linux-amd64/etcdctl > /usr/bin/etcdctl
RUN chmod a+x /usr/bin/etcdctl

RUN rm -f *.tar.gz

RUN mkdir /app
COPY register.tmpl /app/
CMD [ "docker-gen", "-watch", "-interval", "5", "-notify", "sh /app/register.sh",  "/app/register.tmpl", "/app/register.sh" ]
