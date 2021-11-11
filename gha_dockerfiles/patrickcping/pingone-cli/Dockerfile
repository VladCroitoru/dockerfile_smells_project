FROM alpine:3.12.0

RUN apk add --update --no-cache curl ca-certificates bash bash-completion zsh curl git vim ncurses util-linux

ADD pingone-cli /usr/bin/pingone-cli
ADD _pingone-cli /usr/local/share/zsh/site-functions/_pingone-cli
ADD pingone-cli.bash-completion /etc/bash-completion.d/pingone-cli
RUN chmod 755 /usr/bin/pingone-cli

#
# Install oh-my-zsh
#
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true

#
# Enable bash completion
#
RUN echo '\n\
. /etc/bash_completion\n\
source /etc/bash-completion.d/pingone-cli\n\
' >> ~/.bashrc

#
# Setup prompt
#
RUN echo 'export PS1="[PingOne Platform API - Management] \$ "' >> ~/.bashrc
RUN echo 'export PROMPT="[PingOne Platform API - Management] \$ "' >> ~/.zshrc

#
# Setup a welcome message with basic instruction
#
RUN echo -e 'echo "\
\n\
This Docker provides preconfigured environment for running the command\n\
line REST client for $(tput setaf 6)PingOne Platform API - Management$(tput sgr0).\n\
\n\
For convenience, you can export the following environment variables:\n\
\n\


\n\
$(tput setaf 7)Basic usage:$(tput sgr0)\n\
\n\
$(tput setaf 3)Print the list of operations available on the service$(tput sgr0)\n\
$ pingone-cli -h\n\
\n\
$(tput setaf 3)Print the service description$(tput sgr0)\n\
$ pingone-cli --about\n\
\n\
$(tput setaf 3)Print detailed information about specific operation$(tput sgr0)\n\
$ pingone-cli <operationId> -h\n\
\n\
By default you are logged into Zsh with full autocompletion for your REST API,\n\
but you can switch to Bash, where basic autocompletion is also supported.\n\
\n\
"\
' | tee -a ~/.bashrc ~/.zshrc

#
# Poormans chsh & cleanup to make image as compact as possible
#

RUN sed -i 's/root:x:0:0:root:\/root:\/bin\/ash/root:x:0:0:root:\/root:\/bin\/zsh/' /etc/passwd
RUN apk del git vim && rm -f /var/cache/apk/*

ENTRYPOINT ["/bin/zsh"]
