# Fat image for android + node: FROM beevelop/android-nodejs
FROM thyrlian/android-sdk:latest
LABEL maintainer="Daniel Freiling <ddfreiling@gmail.com>"

ARG NODE_VERSION="8.9.4"
ARG ANDROID_BUILD_TOOLS="27.0.3"
ARG ANDROID_PLATFORM_API="25"
ARG NODE_USER="jenkins"

ENV USER_HOME="/home/${NODE_USER}" \
    ANDROID_HOME="/opt/android-sdk" \
    NVM_DIR="/home/${NODE_USER}/.nvm" \
    NVM_BIN="/home/${NODE_USER}/.nvm/versions/node/v${NODE_VERSION}/bin" \
    CHROME_BIN="/usr/bin/google-chrome-stable"

# Dumb-init
RUN wget -q https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64.deb && \
    dpkg -i dumb-init_*.deb
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# Google Chrome (used for automated tests in headless mode)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && apt-get install -y google-chrome-stable && rm -r /var/lib/apt/lists/* && google-chrome-stable --version

# Utilities
# RUN apt-get update && \
#     apt-get -y install apt-transport-https unzip curl usbutils --no-install-recommends && \
#     rm -r /var/lib/apt/lists/*

# Android SDK
RUN mkdir -p ~/.android && touch ~/.android/repositories.cfg && \
    echo 'Update platform-tools' && sdkmanager "platform-tools" && \
    echo 'Update build-tools'    && sdkmanager "build-tools;$ANDROID_BUILD_TOOLS" && \
    echo 'Update platforms'      && sdkmanager "platforms;android-$ANDROID_PLATFORM_API" && \
    echo 'Update extras-android' && sdkmanager "extras;android;m2repository" && \
    echo 'Update extras-google'  && sdkmanager "extras;google;m2repository" && \
    chmod a+x -R $ANDROID_HOME

# Setup NODE_USER workspace (node/jenkins support)
RUN groupadd --gid 1001 ${NODE_USER} && \
    useradd --uid 1001 --gid ${NODE_USER} --shell /bin/bash --create-home ${NODE_USER}

WORKDIR ${USER_HOME}

USER ${NODE_USER}

# NVM + Node + typescript, gulp-cli, nativescript
RUN wget -nv -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.7/install.sh | bash - && \
    \. $NVM_DIR/nvm.sh && \
    npm i -g typescript@~2.5.3 && \
    npm i -g gulp-cli@~1.4.0 && \
    npm i -g nativescript@~3.4.1 --ignore-scripts && \
    tns error-reporting disable && \
    tns usage-reporting disable && \
    npm cache clean --force

ENV PATH="$PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${NVM_BIN}"