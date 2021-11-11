FROM jeandet/teamcity-docker-minimal-agent
LABEL maintainer "Alexis Jeandet <alexis.jeandet@member.fsf.org>"

RUN dnf clean all && dnf update -y && dnf install -y cppcheck luabind-devel tcl-devel tk-devel lua-devel python2-devel clang-devel ncurses-devel llvm-static clang-analyzer lcov openmpi-devel \
                   git ninja-build ncurses-devel cups-devel zlib-static zlib-devel itstool libpcap-devel SDL2-devel wget redhat-rpm-config  gettext unzip doxygen \
                   gcc-objc++ flex flex-devel bison-devel bison gcc-objc libasan valgrind libubsan clang meson clazy \
                   vala hg \
                   libwmf-devel qt5*-devel qt*-devel \
                   llvm llvm-devel llvm3.9-devel llvm-static \
                   boost-* boost-devel \
                   wxGTK-devel wxGTK3-devel \
                   glib2-devel gtest gobject-introspection-devel python-gobject-base python3-gobject-base gmock-devel gmock gtest-devel gtk3-devel \
                   openmpi mpich-devel environment-modules openmpi-devel hdf5 hdf5-devel hdf5-openmpi-devel \
                   mesa-vulkan-devel vulkan-devel \
                   gnustep-base-devel gnustep-make \
                   graphviz texlive-* \
                   gitstats \
                   python*-scipy python*-scipy \
                   python*-sphinx python*-sphinx_rtd_theme python*-breathe python*-docutils

RUN wget https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip && \
    wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/2.4/sonar-runner-dist-2.4.zip && \
    unzip build-wrapper-linux-x86.zip -d /opt/ && rm build-wrapper-linux-x86.zip && \
    unzip sonar-runner-dist-2.4.zip -d /opt/ && rm sonar-runner-dist-2.4.zip && \
    ln -s /opt/build-wrapper-linux-x86/build-wrapper-linux-x86-64 /usr/bin/build-wrapper-linux && \
    ln -s /opt/sonar-runner-2.4/bin/sonar-runner /usr/bin/sonar-runner


RUN echo "system.has_qt5=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_gcov=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_clang=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_clazy=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_cppcheck=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_clang_analyzer=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_lcov=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_gitstats=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_graphviz=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_sonarqube=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_openmpi=true" >> /opt/buildagent/conf/buildAgent.dist.properties  && \
    echo "system.agent_name=complete-agent" >> /opt/buildagent/conf/buildAgent.dist.properties  && \
    echo "system.agent_repo=https://github.com/jeandet/teamcity-docker-complete-agent" >> /opt/buildagent/conf/buildAgent.dist.properties


CMD ["/run-services.sh"]
