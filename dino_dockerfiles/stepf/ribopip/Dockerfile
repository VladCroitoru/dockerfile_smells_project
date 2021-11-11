FROM ruby:slim
MAINTAINER stefan (U+0040) sdang.de
# PURPOSE: Minimal Docker container to run ribopip (github.com/stepf/ribopip)

ADD ./ /ribopip
RUN /ribopip/scripts/bootstrap
ENTRYPOINT ["bash"]
