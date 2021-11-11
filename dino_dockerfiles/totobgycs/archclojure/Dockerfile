FROM totobgycs/archjava
MAINTAINER totobgycs

USER build
WORKDIR /home/build
RUN yaourt -Syy ; \
  yaourt -S --noconfirm clojure ; \
  wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein; \
  sudo mv lein /usr/local/sbin; \
  chmod a+x  /usr/local/sbin/lein; \
  lein
  
RUN eclipse -nosplash -consoleLog \
  -application org.eclipse.equinox.p2.director \
  -repository http://updatesite.ccw-ide.org/stable/ \
  -installIU ccw.feature.feature.group
  
WORKDIR /home/eclipse
USER eclipse

CMD ["eclipse"]
