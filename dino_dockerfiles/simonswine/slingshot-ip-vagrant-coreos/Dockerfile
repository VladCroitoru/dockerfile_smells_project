FROM busybox

WORKDIR /slingshot

ADD vagrant/ /slingshot/vagrant

ADD run.sh /run.sh
ENTRYPOINT ["/bin/sh", "/run.sh"]
