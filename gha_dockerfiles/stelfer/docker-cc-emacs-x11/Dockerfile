
ARG BASE
FROM ${BASE}

RUN useradd -m -s /bin/bash telfer
USER telfer

RUN mkdir -p ~/.ssh; chmod 0700 ~/.ssh

ARG DOCKER_PUBLIC_KEY
RUN echo "${DOCKER_PUBLIC_KEY}" > ~/.ssh/authorized_keys

ARG GITHUB_PRIVATE_KEY
RUN echo "${GITHUB_PRIVATE_KEY}" > ~/.ssh/github_ecdsa
RUN echo "Host github.com\n\tIdentityfile ~/.ssh/github_ecdsa\n" > ~/.ssh/config
RUN chmod 0600 ~/.ssh/*

RUN git config --global user.email "soren.telfer@gmail.com"
RUN git config --global user.name "Soren Telfer"

# Run bash to get multiline comment
SHELL ["/bin/bash", "-c"]
RUN echo $'\nsource /etc/bash_completion.d/git-prompt\n\
GIT_PS1_SHOWUPSTREAM=1\n\
export GIT_PS1_SHOWCOLORHINTS=1\n\
export GIT_PS1_SHOWDIRTYSTATE=1\n\
unset PS1\n\
cyan=$(tput setaf 6)\n\
magenta=$(tput setaf 5)\n\
yellow=$(tput setaf 3)\n\
reset=$(tput sgr0) \n\
PROMPT_COMMAND=\'__git_ps1 "\[$cyan\]\u\[$reset\]@\[$magenta\]\h\[$reset\]:\[$yellow\]\w\[$reset\]" "\$ "\'\n\
' >> ~/.bashrc

RUN echo $'\n\
define xxd\n\
  dump binary memory dump.bin $arg0 $arg0+$arg1\n\
  shell xxd dump.bin\n\
end\n\
' >> ~/.gdbinit

# Pull .emacs.d 
RUN cd ~ && git clone https://github.com/stelfer/emacs.d.git .emacs.d

USER root
RUN mkdir /var/run/sshd; chmod 755 /var/run/sshd
ENTRYPOINT ["/usr/sbin/sshd", "-D"]

