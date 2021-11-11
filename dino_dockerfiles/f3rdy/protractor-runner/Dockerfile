FROM ubuntu:17.10

MAINTAINER Fred Thiele <fred.thiele@diva-e.com>

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install npm xvfb wget  dbus-x11 openjdk-8-jre-headless && \
    apt-get -y install tmux vim && \
    rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' \
        | tee /etc/apt/sources.list.d/google-chrome.list

RUN apt-get -y update && apt-get -y install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get -y update && apt-get -y install sudo && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g protractor@5.1.1 protractor-console-plugin@0.1.1 protractor-jasmine2-html-reporter@0.0.7 protractor-jasmine2-screenshot-reporter@0.0.4 karma@1.3.0 jasmine@2.5.3 jasmine-core@2.8.0 jasmine-spec-reporter@4.2.1
RUN webdriver-manager update

RUN useradd -u 842 -ms /bin/bash jenkins

# Fixing selenium server exection issues
RUN chown jenkins:users /usr/local/lib/node_modules -R && \
    chmod ug+rwX /usr/local/lib/node_modules -R


#WORKDIR /tests
#VOLUME ["/tests"]

#COPY entrypoint.sh /

#ENTRYPOINT ["/entrypoint.sh"]
