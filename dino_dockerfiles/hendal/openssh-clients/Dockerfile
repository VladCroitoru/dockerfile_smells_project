FROM fedora:27

RUN dnf install openssh-clients -y && dnf clean all && mkdir -p ~/.ssh \ 
    && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
