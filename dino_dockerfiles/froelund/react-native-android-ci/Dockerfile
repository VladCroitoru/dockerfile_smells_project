FROM bitriseio/docker-android

RUN apt-get update -qq
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs build-essential git wget tar unzip lib32stdc++6 lib32z1
RUN yarn global add react-native-cli