# Automatic building from hub.docker.com
FROM alpine:latest

MAINTAINER Manuel Kaufmann <humitos@gmail.com>

RUN apk add --no-cache \
        emacs-x11 \
        python3 \
        git \
        make \
        grep \
        diffutils \
        ctags \
        ack \
        aspell \
        aspell-en

# Make `python` the default for `python3`
RUN ln -s /usr/bin/python3 /usr/bin/python

# Checkout emacs configuration from github
RUN git clone --depth 1 \
        https://github.com/humitos/emacs-configuration.git /code \
        && cd /code \
        && git submodule init \
        && git submodule update

WORKDIR /code

# Download snippets and yasmate for yasnippet
RUN cd vendor/yasnippet && \
    git submodule init && \
    git submodule update

RUN mkdir -p /root/.fonts
RUN mv -f Menlo-Regular.ttf /root/.fonts

# Disable ERC
# RUN mv -f startup.d/erc.el startup.d/erc.el.disabled
RUN mv -f startup.d/circe.el startup.d/circe.disabled

# Disable magithub since it requires the API KEY
RUN mv -f startup.d/magithub.el startup.d/magithub.el.disabled

# Install python dependecies for emacs' plugins
RUN apk add --no-cache py3-lxml  # avoid compiling it (requires gcc g++ python3-dev libxslt-dev, etc)
RUN pip3 install --no-cache-dir -U pip
RUN pip3 install --no-cache-dir -r requirements.elpy.in

# Compile needed dependencies
RUN ./bin/compile_helm

# FIXME: can't be compiled in Alpine Linux
# RUN ./bin/compile_ctags
# RUN ./bin/compile_silversearcher

# Set the `emacs-user-directory` used from the `init.el` file
ENV EMACS_USER_DIRECTORY /code/

# Used to set the proper ctags executable
ENV DOCKER true


WORKDIR /src

CMD sh -c "emacs --no-site-file --no-splash --load /code/.emacs.docker"
