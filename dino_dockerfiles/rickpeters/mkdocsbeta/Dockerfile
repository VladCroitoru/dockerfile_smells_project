FROM python:3-onbuild
MAINTAINER Rick Peters <rick.peters@me.com>

# install graphviz
RUN apt-get update && \
    apt-get install -y graphviz && \
    apt-get clean

# essential template resource not available in development build
# issue registered with mkdocs contributor
# ADD search-results-template.mustache /usr/local/lib/python3.5/site-packages/mkdocs/assets/search/mkdocs/js/

# add markdown extension
ADD mdx_graphviz.py /usr/local/lib/python3.6/site-packages/markdown/extensions/

# make application directory available as volume
VOLUME /usr/src/app

ENV TZ Europe/Amsterdam
# since we use it as development container, default action is a shell
CMD [ "/bin/bash" ]
