FROM concourse/buildroot:git

RUN ln -s /usr/bin/gpg2 /usr/bin/gpg

ADD scripts/install_git_lfs.sh install_git_lfs.sh
RUN ./install_git_lfs.sh

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
