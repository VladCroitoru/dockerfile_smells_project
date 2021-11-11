FROM python:2.7.9-slim

MAINTAINER ssalisbury@opentable.com

ADD . /source
WORKDIR /source
RUN pip install .

ENTRYPOINT ["mesos_stats"]

# Note: When invoking this image, you need to pass some more args to docker run. See http://github.com/samsalisbury/mesos_stats readme for details.
