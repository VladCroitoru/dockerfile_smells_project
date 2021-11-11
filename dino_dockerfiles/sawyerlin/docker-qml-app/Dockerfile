FROM sawyerlin/docker-x11-app
MAINTAINER Sawyer LIN <sawyer.lin@gmail.com>

RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :

RUN apt-get install -y qmlscene qt5-qmake qt5-default qtdeclarative5-dev qtdeclarative5-localstorage-plugin qml-module-qtqml-models2 qtdeclarative5-qtmultimedia-plugin qtdeclarative5-window-plugin qml-module-qtquick-controls qml-module-qtgraphicaleffects qml-module-qtwebsockets qml-module-qt-websockets python-gst0.10*
RUN apt-get install -y git
RUN cd /tmp && git clone https://github.com/sawyerlin/qml-livereload.git && cd qml-livereload && qmake && make

# Not use gpu
RUN apt-get remove -y gstreamer1.0-vaapi

ADD . /src

EXPOSE 22

CMD ["/bin/bash", "/src/startup.sh"]
