FROM bitriseio/docker-android:latest

# Dependencies for Appium
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH ${PATH}:${JAVA_HOME}/bin
RUN npm install -g appium
RUN npm install -g appium-doctor

# Gems for Appium
RUN echo gem: --no-rdoc --no-ri > ~/.gemrc
RUN gem install appium_lib         -v '~> 6.0.0'
RUN gem install rest-client        -v '~> 1.6.7'
RUN gem install rspec              -v '~> 2.14.1'
RUN gem install cucumber           -v '~> 1.3.15'
RUN gem install rspec-expectations -v '~> 2.14.5'
RUN gem install spec               -v '~> 5.3.4'
RUN gem install sauce_whisk        -v '~> 0.0.13'
RUN gem install test-unit          -v '~> 2.5.5'

# Emulator
#RUN echo y | android update sdk --all --filter sys-img-x86-android-19 --no-ui
ENV DOCKER_EMULATOR_NAME android_emu
RUN echo no | android create avd --force --name ${DOCKER_EMULATOR_NAME} --target android-19 --abi armeabi-v7a
#RUN wget https://raw.githubusercontent.com/julo15/android-docker-image/master/bitrise.yml
#RUN bitrise run setup
