FROM gentoo/stage3-amd64-hardened
MAINTAINER necrose99 necrose99@protmail.ch mike@michaellawrenceit.com
RUN emerge git layman 
RUN layman -L && layman -a perl-experimental-snapshots
# installing witchcraft deps
RUN emerge-webrsync -q
RUN emerge app-portage/g-cpan  dev-perl/Class-Load dev-perl/TermReadKey
RUN emerge dev-perl/Class-Load-XS dev-perl/Child dev-perl/Carp-Always
RUN emerge dev-perl/List-MoreUtils dev-perl/Config-Simple virtual/perl-Digest-MD5
RUN emerge dev-perl/DateTime virtual/perl-Encode virtual/perl-File-Path
RUN emerge dev-perl/DateTime-Locale dev-perl/App-CLI dev-perl/Git-PurePerl  dev-perl/IPC-Run3
RUN emerge dev-perl/libwww-perl dev-perl/Git-Sub dev-perl/HTTP-Message dev-perl/libwww-perl dev-perl/regexp-common virtual/perl-Term-ANSIColor dev-perl/TermReadKey
RUN emerge App-cpanminus dev-perl/App-Nopaste dev-perl/Import-Into
RUN g-cpan --cpan_reload --generate --install -v 

# downloading and install witchcraft
RUN wget 'https://codeload.github.com/Spike-Pentesting/App-witchcraft/tar.gz/master' -O witchcraft.tar.gz && tar xvf witchcraft.tar.gz && cd App-witchcraft-master && cpanm --installdeps -n . && cpanm .
RUN perl-cleaner --all
# configuring witchcraft
RUN mkdir -p /root/.witchcraft && cp -rfv /App-witchcraft-master/witchcraft.conf /root/.witchcraft/witchcraft.conf && sed -i s:pushbullet:Git:g /root/.witchcraft/witchcraft.conf && sed -i s:Sabayon:Qacheck:g /root/.witchcraft/witchcraft.conf && rm -rfv /App-witchcraft-master && rm -rfv /witchcraft.tar.gz
# Display some news items
# Finalization
RUN env-update
