FROM sabayon/builder-amd64-squashed

# installing witchcraft deps
RUN equo i sudo dev-perl/Class-Load dev-perl/Class-Load-XS dev-perl/List-MoreUtils dev-perl/DateTime-Local dev-perl/libwww-perl App-cpanminus

# downloading and install witchcraft
RUN wget 'https://codeload.github.com/Spike-Pentesting/App-witchcraft/tar.gz/master' -O witchcraft.tar.gz && tar xvf witchcraft.tar.gz && cd App-witchcraft-master && cpanm --installdeps -n . && cpanm .

# configuring witchcraft
RUN mkdir -p /root/.witchcraft && cp -rfv /App-witchcraft-master/witchcraft.conf /root/.witchcraft/witchcraft.conf && sed -i s:pushbullet:Git:g /root/.witchcraft/witchcraft.conf && sed -i s:Sabayon:Qacheck:g /root/.witchcraft/witchcraft.conf && rm -rfv /App-witchcraft-master && rm -rfv /witchcraft.tar.gz
