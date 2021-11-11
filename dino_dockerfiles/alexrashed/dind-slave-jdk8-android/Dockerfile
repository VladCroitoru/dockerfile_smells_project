FROM jelloween/dind-slave-java8:latest
ENV ANDROID_HOME /opt/android-sdk
RUN mkdir -p $ANDROID_HOME/licenses
RUN echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "$ANDROID_HOME/licenses/android-sdk-license"
RUN chown -R jenkins:jenkins /opt/android-sdk
