FROM wpinaud/unity-base-image
ENV UNITY_INSTALLER_URL http://beta.unity3d.com/download/061bcf22327f/unity-editor_amd64-2017.1.0xf3Linux.deb
# ------------------------------------------------------
# --- Install required tools
RUN apt-get update -qq && apt-get clean
# ------------------------------------------------------
# --- Unity 2017.1.0f3
RUN wget -q ${UNITY_INSTALLER_URL} -O unity.deb && \
    apt-get install -y ./unity.deb && \
    rm unity.deb && \
    (/opt/Unity/Editor/Unity -logfile -nographics -force-opengl -batchmode &) ; sleep 15 ; sudo killall Unity

CMD bitrise -version
