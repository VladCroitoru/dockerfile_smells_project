FROM totobgycs/archjava
MAINTAINER totobgycs

USER build
WORKDIR /home/build
RUN yaourt -Syy ; \
  yaourt -S --noconfirm scala scala-docs sbt ; \
  yaourt -S --aur --noconfirm typesafe-activator ; \
  yes | yaourt -Scc
RUN eclipse -nosplash -consoleLog \
  -application org.eclipse.equinox.p2.director \
  -repository http://download.scala-ide.org/sdk/lithium/e44/scala211/stable/site/ \
  -installIU org.scala-ide.sdt.feature.feature.group

WORKDIR /home/guiuser
USER guiuser
RUN activator list--templates ; \
  sbt

