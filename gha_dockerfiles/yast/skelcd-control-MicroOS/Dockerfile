FROM registry.opensuse.org/yast/head/containers/yast-ruby:latest
# install the openSUSE control.xml, we need to copy some parts to Kubic
RUN zypper --non-interactive in --no-recommends skelcd-control-openSUSE
COPY . /usr/src/app
