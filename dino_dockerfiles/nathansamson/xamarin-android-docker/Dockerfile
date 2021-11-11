FROM fedora:27

RUN dnf install gnupg wget dnf-plugins-core -y  \
	&& rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF" \
	&& dnf config-manager --add-repo http://download.mono-project.com/repo/centos7/ \
        && dnf install libzip bzip2 bzip2-libs mono-devel nuget msbuild referenceassemblies-pcl lynx -y \
        && dnf clean all

RUN dnf install curl unzip java-1.8.0-openjdk-headless java-1.8.0-openjdk-devel -y && \
    dnf clean all
    
RUN mkdir -p /android/sdk && \
    curl -k https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip -o sdk-tools-linux-3859397.zip && \
    unzip -q sdk-tools-linux-3859397.zip -d /android/sdk && \
    rm sdk-tools-linux-3859397.zip

RUN cd /android/sdk && \
    yes | ./tools/bin/sdkmanager --licenses && \
    ./tools/bin/sdkmanager 'build-tools;26.0.2' platform-tools 'platforms;android-26' 'ndk-bundle'

RUN lynx -listonly -dump https://jenkins.mono-project.com/view/Xamarin.Android/job/xamarin-android-linux/lastSuccessfulBuild/Azure/ | grep -o "https://.*/Azure/processDownloadRequest/xamarin-android/oss-xamarin.android_v.*" > link.txt
RUN curl -L $(cat link.txt) \
        -o xamarin.tar.bz2
RUN bzip2 -cd xamarin.tar.bz2 | tar -xvf -
RUN mv oss-xamarin.android_v* /android/xamarin && \
    rm xamarin.tar.bz2
    
ENV ANDROID_NDK_PATH=/android/sdk/ndk-bundle
ENV ANDROID_SDK_PATH=/android/sdk/
ENV PATH=/android/xamarin/bin/Debug/bin:$PATH
ENV JAVA_HOME=/usr/lib/jvm/java/
