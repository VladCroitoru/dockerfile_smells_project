FROM FROM ubuntu:14.04.5


ENV NODE_VERSION 6.11.1
ENV NPM_VERSION 3.10.10


RUN apt-get -qq update && apt-get -qq install -y \ 
    curl gconf-service lib32gcc1 lib32stdc++6 libasound2 libc6 libc6-i386 libcairo2 libcap2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libfreetype6 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libgl1-mesa-glx libglib2.0-0 libglu1-mesa libgtk2.0-0 libnspr4 libnss3 libpango1.0-0 libstdc++6 libx11-6 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxtst6 zlib1g debconf xdg-utils lsb-release libpq5 xvfb \ 
    && rm -rf /var/lib/apt/lists/*


# Setup Node.js (Setup NodeSource Official PPA)
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN sudo npm install -g -y forever

RUN npm config set color false


RUN mkdir -p /root/.cache/unity3d && mkdir -p /root/.local/share/unity3d
ADD get-unity.sh /app/get-unity.sh
RUN chmod +x /app/get-unity.sh && \
    /app/get-unity.sh && \
    dpkg -i /app/unity_editor.deb && \
    rm /app/unity_editor.deb
ADD unity_wrapper.sh /usr/local/bin/unity_wrapper.sh
RUN chmod +x /usr/local/bin/unity_wrapper.sh
