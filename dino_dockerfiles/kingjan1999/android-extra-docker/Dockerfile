FROM beevelop/android

MAINTAINER kingjan1999

RUN buildDeps='software-properties-common'; \
    set -x && \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends

RUN apt-add-repository -y ppa:cwchien/gradle
RUN apt-get update
RUN apt-get -y dist-upgrade
 
RUN echo "y" | android update sdk -a -f -u -t extra-android-support,extra-android-m2repository,extra-google-m2repository 
