FROM alpine:edge
RUN apk add -u --no-cache \
aria2 aria2-doc \
asciinema \
bat bat-doc bat-zsh-completion \
buildah buildah-doc \
ca-certificates \
curl \
cvechecker cvechecker-doc \
dialog dialog-doc \
direnv direnv-doc \
dmidecode dmidecode-doc \
dnssec-root \
dnstracer dnstracer-doc \
drill \
dust \
easy-rsa \
elfutils elfutils-doc \
exa exa-doc exa-zsh-completion \
expect expect-doc \
fd fd-doc fd-zsh-completion \
fzf fzf-doc fzf-zsh-completion \
git git-doc git-zsh-completion \
gnupg gnupg-doc \
gzip gzip-doc \
hexyl \
highlight highlight-doc \
hwids hwids-doc \
hwinfo \
hyperfine hyperfine-doc hyperfine-zsh-completion \
iftop \
inxi inxi-doc \
ipcalc ipcalc-doc \
ipmitool \
ipmiutil-doc \
iputils \
jq jq-doc \
just just-zsh-completion \
k3s k3s-doc \
lshw lshw-doc \
neovim neovim-doc \
net-snmp-tools \
nmap nmap-doc nmap-ncat nmap-scripts \
openssh-client \
podman podman-zsh-completion \
pstree \
psutils \
py3-pip \
python3 \
ripgrep ripgrep-zsh-completion \
rsync rsync-doc \
skopeo skopeo-doc \
sniffglue sniffglue-doc \
socat \
speedtest-cli \
starship \
tar \
tcpdump tcpdump-doc \
tcpflow tcpflow-doc \
terraform \
tig \
tmux tmux-doc tmux-zsh-completion \
tshark \
unzip \
urlscan \
vault \
vim vim-help \
w3m w3m-doc \
weechat weechat-doc \
wget wget-doc \
whois whois-doc \
yq yq-doc \
zenity zenity-doc \
zsh zsh-doc

RUN pip install ranger-fm httpie

ENV USER=root
ENV GROUP=root
ENV HOME=/root
RUN sed -i -Ee 's/\/bin\/ash/\/bin\/zsh/' /etc/passwd
COPY . /opt/my
RUN echo dotfiles > /etc/hostname
USER "${USER}"

ENTRYPOINT []
CMD [ "/bin/zsh" ]
RUN cd /opt/my && python3 ./install.py bash dotfiles git neovim ranger scripts zsh
RUN chmod -R u+rw,g-rw,o-rw ${HOME}
WORKDIR "${HOME}"
