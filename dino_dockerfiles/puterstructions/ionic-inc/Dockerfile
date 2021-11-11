FROM jacekmarchwicki/android:java8-r24-4-1

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs build-essential
RUN npm install -g cordova ionic

EXPOSE 8100 35729
