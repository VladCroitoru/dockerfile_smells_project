FROM archlinux/base

RUN useradd -ms /bin/bash docker
ENV JAVA_HOME=/usr/lib/jvm/default-runtime
ENV PATH="/home/docker/.local/bin:${JAVA_HOME}:${PATH}"
RUN pacman -Syu --noconfirm stack base-devel jdk8-openjdk python wget git maven unzip vim nano emacs tmux
RUN stack upgrade --binary-version 1.9.3

WORKDIR /home/docker
USER docker
COPY --chown=docker:docker  . .
RUN find . \( -name ".git" -o -name ".gitignore" -o -name ".gitmodules" -o -name ".gitattributes" \) -exec rm -rf -- {} +
RUN python jdebloat.py setup 2>/dev/null
ENTRYPOINT ["/bin/bash"]
