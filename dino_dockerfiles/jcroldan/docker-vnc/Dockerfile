FROM oott123/docker-novnc

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y curl wget nano ca-certificates software-properties-common && \
    apt-get install -y xfce4 xfce4-goodies && \
    apt-get install -y network-manager dbus-x11 xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable

# Budgie Desktop
#RUN add-apt-repository ppa:budgie-remix/ppa
#RUN apt-get update
#RUN apt-get install -y budgie-desktop-environment

# ---------------------------------------------------------------

# nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs

# yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y yarn

# chrome
RUN curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable
ENV CHROME_ARGS --no-sandbox

# Docker CE
RUN apt-get install -y apt-transport-https software-properties-common apt-utils
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-cache policy docker-ce
RUN apt-get update && apt-get install -y docker.io

RUN usermod -aG docker user
RUN usermod -aG sudo user

# VS Code
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
RUN apt-get update && apt-get install -y code # or code-insiders

# Autoremove & Clean
RUN apt-get autoremove -y && \
    apt-get clean

# Set bash as default user terminal shell
RUN chsh -s /bin/bash user

# ---------------------------------------------------------------

COPY config/xstartup /etc/vnc/xstartup
RUN chmod u+x /etc/vnc/xstartup

EXPOSE 5911
