# From https://medium.com/@cnadeau_/docker-as-a-cordova-android-application-builder-9e292298c08e
# Creates an environement containing java 8, android SDKs 23/24, node 5.6.0, python 2.7, git, cordova and ionic.
FROM gfx2015/android:latest
RUN curl -sL https://deb.nodesource.com/setup_6.x |  bash - && \
 apt-get install -y --no-install-recommends nodejs git bzip2 && \
 apt-get clean && \
 apt-get autoremove -y && \
 rm -rf /var/lib/apt/lists/* && \
 rm -fr /tmp/*

# install cordova, bower and grunt
RUN npm install -g cordova bower grunt-cli && \
 npm cache clean
