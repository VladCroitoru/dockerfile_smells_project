# First stage of multi-stage build
# Installs Meteor and builds node.js version
# This stage is named 'builder'
# The data for this intermediary image is not included
# in the final image.
FROM node:9.11.1 AS lesion-tracker-docker-image

LABEL description="Image for running https://github.com/OHIF/Viewers/tree/master/LesionTracker" \
  version="0.1"

RUN apt-get update && apt-get install -y apt-utils && apt-get update
RUN apt-get install -y \
	curl \
	g++ \
	build-essential \
  python

RUN apt-get install -y --no-install-recommends bsdtar
RUN export tar='bsdtar'

EXPOSE 3000

RUN useradd -ms /bin/bash app
USER app

WORKDIR /home/app

RUN export tar='bsdtar'
RUN tar --version
RUN curl https://install.meteor.com/ | sh

RUN mkdir /home/app/LesionTracker
RUN touch /home/app/app.json
WORKDIR /home/app/LesionTracker

ENV ROOT_URL=http://localhost:3000
ENV PORT=3000

CMD ["/home/app/.meteor/meteor", "run", "--settings=/home/app/app.json"]
