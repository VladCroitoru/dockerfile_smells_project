FROM ubuntu:16.04
MAINTAINER Daniel Kinsman <danielkinsman@riseup.net>

ARG GODOT_VERSION=2.1.4

RUN apt-get update -qq \
    && apt-get install -y -qq curl unzip software-properties-common ca-certificates sudo zip openjdk-8-jdk-headless adb

RUN mkdir -p /opt/
RUN curl -s -L -o godot_server.zip -C - https://downloads.tuxfamily.org/godotengine/$GODOT_VERSION/Godot_v$GODOT_VERSION-stable_linux_server.64.zip \
    && unzip godot_server.zip -d /opt/ \
    && rm -f godot_server.zip
RUN ln -s /opt/Godot_v$GODOT_VERSION-stable_linux_server.64 /usr/local/bin/godot_server

RUN mkdir -p /root/.godot/
RUN curl -s -L -o godot_export_templates.zip -C - https://downloads.tuxfamily.org/godotengine/$GODOT_VERSION/Godot_v$GODOT_VERSION-stable_export_templates.tpz \
    && unzip godot_export_templates.zip -d /root/.godot/ \
    && rm -f godot_export_templates.zip

RUN keytool -keyalg RSA -genkeypair -alias androiddebugkey -keypass android -keystore /root/debug.keystore -storepass android -dname "CN=Android Debug,O=Android,C=US" -validity 9999

COPY editor_settings.tres /root/.godot/editor_settings.tres
