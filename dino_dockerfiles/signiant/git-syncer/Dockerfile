FROM bravissimolabs/alpine-git

MAINTAINER Signiant DevOps <devops@signiant.com>

ADD git_sync.sh /git_sync.sh

RUN chmod a+x /git_sync.sh

VOLUME /repo-dir

ENTRYPOINT ["/git_sync.sh"]
