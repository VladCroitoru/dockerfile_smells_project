FROM codercom/code-server:latest

USER root

## Set proxy if build from internal subnet
# ENV http_proxy "http://ip:port"
# ENV https_proxy "https://ip:port"
# ENV no_proxy="localhost,127.0.0.1"


RUN apt -y update && apt -y install build-essential gdb gcc wget mercurial

RUN wget https://github.com/microsoft/vscode-cpptools/releases/download/1.5.1/cpptools-linux.vsix
RUN code-server \
	--user-data-dir=/home/coder/.local/share/code-server \
	--install-extension golang.go \
	--install-extension ms-python.python \
	--install-extension formulahendry.code-runner \
	--install-extension eamodio.gitlens \
	--install-extension coenraads.bracket-pair-colorizer \
	--install-extension oderwat.indent-rainbow \
	--install-extension windmilleng.vscode-go-autotest \
	--install-extension vscode-icons-team.vscode-icons \
	--install-extension esbenp.prettier-vscode \
	--install-extension ryu1kn.text-marker \
	--install-extension streetsidesoftware.code-spell-checker \
	--install-extension kdarkhan.mips \
	--install-extension dan-c-underwood.arm \
	--install-extension plorefice.devicetree \
	--install-extension cpptools-linux.vsix \
	--install-extension yzhang.markdown-all-in-one
RUN rm -f cpptools-linux.vsix

## set default settings
COPY settings.json /home/coder/.local/share/code-server/User/settings.json
COPY keybindings.json /home/coder/.local/share/code-server/User/keybindings.json

## overwrite entrypoint.sh
COPY entrypoint.sh /usr/bin/entrypoint.sh
