FROM ruby:latest
MAINTAINER YI-HUNG JEN <yihungjen@gmail.com>

# install jekyll blogging framework
RUN gem install \
    jekyll \
    jekyll-gist

ENTRYPOINT ["jekyll"]
CMD ["--help"]

# Specify workspace (and persist permission setting)
VOLUME /workspace
WORKDIR /workspace

# Add user identity for jekyll
ARG jekyll_role_uid=1000
RUN groupadd -g ${jekyll_role_uid} jekyll && useradd -g jekyll -u ${jekyll_role_uid} jekyll

# Adjust Volume permission
RUN chown jekyll:jekyll /workspace

# Specify default runner to use jekyll_role_uid
USER ${jekyll_role_uid}
