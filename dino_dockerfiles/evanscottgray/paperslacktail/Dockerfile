# evanscottgray/paperslacktail 
#
# LINKS
#
#   Github: https://github.com/evanscottgray/paperslacktail
#   Dockerhub: https://registry.hub.docker.com/u/evanscottgray/paperslacktail/
#   PyPI: https://pypi.python.org/pypi/paperslacktail
#
# DESCRIPTION
#
#   Runs paperslacktail inside of a container to bridge syslog from papertrail
#   into a slack channel. You must supply a PAPERTRAIL_API_TOKEN as an 
#   environment variable for this container to work.
#
# USAGE
#
#   Daemon Mode: 
#
#                docker run -d -e 'PAPERTRAIL_API_TOKEN=<papertrail>' \
#                evanscottgray/paperslacktail --slack-token <slack-token> \
#                                             --slack-channel C03U0EX5E \
#                                             '-g Production'
#
#   Debug Mode: 
#
#               docker run -e 'PAPERTRAIL_API_TOKEN=<papertrail>' \
#               evanscottgray/paperslacktail --debug \
#                                            --slack-token <slack-token> \
#                                            --slack-channel C03U0EX5E \
#                                            '-g Production'
#
# VERSION    1.0.3

FROM ruby:2.2.0
MAINTAINER Evan Gray <hello@evanscottgray.com>

# install deps and clone repo
RUN gem install bundle && \
    bundle config --global jobs 4 && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    git clone https://github.com/evanscottgray/paperslacktail /app

WORKDIR /app/

# install gems and paperslacktail
RUN git checkout master && \
    bundle install && \
    python setup.py install && \
    git rev-parse --short HEAD >> .revision

ENTRYPOINT ["bundle", "exec", "paperslacktail"]
CMD ["-h"]
