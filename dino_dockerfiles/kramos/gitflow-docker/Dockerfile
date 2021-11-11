FROM ubuntu
MAINTAINER kramos

RUN apt-get update 
RUN apt-get install -y git-flow

ENV RUNUSER safeuser
ENV WORKDIR /var/git-repo-home
ENV UID 667

RUN useradd -d $WORKDIR -u $UID -m -s /bin/bash $RUNUSER

VOLUME /var/git-repo-home

WORKDIR /var/git-repo-home

USER $RUNUSER

ENTRYPOINT ["git", "flow"]

