from debian:stretch
run sed -e 's/deb.debian.org/debian.mirrors.ovh.net/g' -i /etc/apt/sources.list
run apt-get update \
 && apt-get install -y \
    inkscape \
    latex-cjk-common \
    make \
    texlive-fonts-extra \
    texlive-lang-french \
    texlive-latex-extra \
    texlive-latex-recommended \
 && apt-get clean
env TEXINPUTS :/usr/local/share/latex/sty:/usr/local/share/latex/common
add common /usr/local/share/latex/common/
add sty /usr/local/share/latex/sty/
add run /usr/local/bin/
run chmod +x /usr/local/bin/run
entrypoint ["/usr/local/bin/run"]
volume ["/data"]
