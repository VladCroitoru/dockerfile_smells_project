# https://medium.com/@hmajid2301/running-expo-react-native-in-docker-ff9c4f2a4388
FROM node:14.4.0

# need git for npm install to work
# RUN apk add --no-cache --update bash git python
RUN apt-get update && apt-get install -y git python

# Permission issues when installing npm packages:
# https://github.com/expo/expo-cli/issues/390
# https://github.com/npm/npm/issues/17851
# https://docs.npmjs.com/misc/config
RUN npm config set user 0
RUN npm config set unsafe-perm true
RUN npm install -g expo-cli

VOLUME /source
WORKDIR /source

#ENV REACT_NATIVE_PACKAGER_HOSTNAME 192.168.2.244
ENV EXPO_DEBUG true
ENV USERNAME username
ENV PASSWORD password

ENTRYPOINT ["sh", "docker-entrypoint.sh"]



