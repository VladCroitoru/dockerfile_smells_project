FROM openjdk:8-jdk

MAINTAINER Jérôme Buisine

ENV SCALA_VERSION       2.12.1
ENV SBT_VERSION         0.13.15
ENV NODEJS_VERSION      7
ENV PORT                3000
ENV USERNAME            demoproject
ENV GIT_REPO_URL        https://github.com/jbuisine/RO.PhotoAlbumProject.git

#ENV CLARIFAI_APP_ID=<an_application_id_from_your_account>
#ENV CLARIFAI_APP_SECRET=<an_application_secret_from_your_account>

RUN useradd -ms /bin/bash $USERNAME

# Scala expects this file
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release

# Install Scala
## Piping curl directly in tar
RUN \
  curl -fsL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /usr/bin/ && \
  echo >> /root/.bashrc && \
  echo 'export PATH=/usr/bin/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc

# Install sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt && \
  sbt sbtVersion

RUN chmod -R g+swX /usr/bin/scala-$SCALA_VERSION
ENV PATH $PATH:/usr/bin/scala-$SCALA_VERSION/bin

###################################################
######## Install all project dependencies #########
###################################################

# Node JS and Bower install

RUN apt-get update

#Add text editor
RUN apt-get install nano

RUN curl -sL https://deb.nodesource.com/setup_$NODEJS_VERSION.x | bash -
RUN apt-get install -y nodejs && npm install -g bower

# Python package manager and its dependencies
RUN apt-get -y install lsof
RUN apt-get install -y python python-dev python-setuptools
RUN apt-get install -y gcc graphicsmagick
RUN easy_install pip
RUN pip install clarifai==2.0.21
RUN apt-get install -y libjpeg-dev zlib1g-dev libpng12-dev
RUN pip install -I imagehash pillow
RUN git clone $GIT_REPO_URL /home/$USERNAME/AlbumProject

RUN chown $USERNAME -R /home/$USERNAME/AlbumProject
RUN chgrp -R $USERNAME /home/$USERNAME/AlbumProject
RUN chmod -R g+swX /home/$USERNAME/AlbumProject

USER $USERNAME

WORKDIR /home/$USERNAME/AlbumProject

EXPOSE $PORT

CMD [ "./run.sh", "build"]

