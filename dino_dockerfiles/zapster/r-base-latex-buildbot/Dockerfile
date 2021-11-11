FROM zapster/r-base-latex

USER root
RUN apt-get update && apt-get install -y \
     build-essential \
     git \
     subversion \
     libffi-dev \
     libssl-dev \
     python-dev \
     python-pip \
     curl && \
   rm -rf /var/lib/apt/lists/* && \
# Test runs produce a great quantity of dead grandchild processes.  In a
# non-docker environment, these are automatically reaped by init (process 1),
# so we need to simulate that here.  See https://github.com/Yelp/dumb-init
   curl -Lo /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 && \
   chmod +x /usr/local/bin/dumb-init && \
   pip --no-cache-dir install buildbot-worker && \
   mkdir /worker && chown docker:docker /worker

USER docker
COPY ./buildbot.tac /worker/buildbot.tac
WORKDIR /worker

CMD ["/usr/local/bin/dumb-init", "/usr/local/bin/buildbot-worker", "start", "--nodaemon", "/worker"]
