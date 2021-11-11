FROM docbill/sublime-text-3
MAINTAINER Bill C Riemers https://github.com/docbill

ARG URL=https://packagecontrol.io/Package%20Control.sublime-package
ADD config /opt/sublime_text/config
RUN chmod -R 755 /opt/sublime_text/config && \
	wget --quiet --output-document=/opt/sublime_text/config/sublime-text-3/Installed\ Packages/Package\ Control.sublime-package "$URL" && \
	cd /opt/sublime_text/config/sublime-text-3/Packages && \
	git clone https://github.com/joeferraro/MavensMate-SublimeText.git -b v6 'MavensMate'

