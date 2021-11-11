FROM adoptopenjdk/openjdk8:alpine

ARG PROJECT_ID

RUN apk -U upgrade && apk add curl bash sudo

RUN curl -sL https://firebase.tools | bash
RUN mkdir /opt/firebase && cd /opt/firebase

# copy firebase config
COPY files/*.json /opt/firebase/.
COPY files/*.rules /opt/firebase/.
COPY files/firebaserc /opt/firebase/.firebaserc
# substitute default project ID in firebaserc
RUN sed -i -e s/%%PROJECT_ID%%/$PROJECT_ID/g /opt/firebase/.firebaserc

COPY updateConfig.sh /opt/firebase/.
RUN chmod 755 /opt/firebase/*.sh

WORKDIR /opt/firebase
RUN firebase setup:emulators:firestore
RUN firebase setup:emulators:storage
RUN firebase setup:emulators:ui

# auth emulator?

EXPOSE 4000
EXPOSE 4400
EXPOSE 4500
EXPOSE 8080
EXPOSE 9099
EXPOSE 9199

#ENTRYPOINT /bin/bash
CMD firebase emulators:start --import /opt/firebase/data --export-on-exit --token $(cat /run/secrets/fb_token)

