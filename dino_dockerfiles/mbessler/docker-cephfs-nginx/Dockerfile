# build: docker build -t cephfs-nginx .
# run: docker run   -it  --rm  --net host --volumes-from cephdata  --privileged  -v /lib/modules:/lib/modules -e CEPHFS=host1,host2,host2:/ cephfs-nginx
FROM ubuntu:14.04
MAINTAINER manuel.bessler@gmail.com
ENV DEBIAN_FRONTEND noninteractive
ENV CEPH_VERSION hammer
RUN apt-get install -y --no-install-recommends ca-certificates wget && wget -q -O- 'https://ceph.com/git/?p=ceph.git;a=blob_plain;f=keys/release.asc' | apt-key add -
RUN echo deb http://ceph.com/debian-${CEPH_VERSION}/ trusty main | tee /etc/apt/sources.list.d/ceph-${CEPH_VERSION}.list
RUN apt-get update -y -q && apt-get install -y --no-install-recommends ceph-fs-common nginx && mkdir /ceph
ADD ./start.sh /
ADD ./default_site /etc/nginx/sites-available/default
ENTRYPOINT /start.sh
