#
# Appcelerator Titanium Mobile Build Dockerfile
#
# https://github.com/HazemKhaled/Titanium-Fastlane-Docker
#

FROM hazemkhaled/titanium-docker
MAINTAINER Hazem Khaled <hazem.khaled@gmail.com>

RUN echo "Helooooo"
# Don't know we have to login as root again
USER root
RUN apt-get install -y ruby ruby-dev rubygems build-essential
RUN gem install fastlane -NV
RUN npm install -g tifastlane

CMD tifast playsend -a alpha
