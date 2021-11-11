FROM lilachzilberman/tomcat-python-base-image

WORKDIR /usr/src/app
ADD gradlew .
ADD gradle ./gradle
RUN ./gradlew
ADD . ./
RUN ./gradlew assemble

RUN rm -rf $CATALINA_HOME/webapps/ROOT && \
    cp ./build/libs/*.war $CATALINA_HOME/webapps/ROOT.war


ENV KAKURO_PYTHON_MAIN ${PWD}/python-read-board/main.py
ENV KAKURO_PYTHON_IMAGE_VIA_FILE true
