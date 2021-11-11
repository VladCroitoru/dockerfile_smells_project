FROM java:openjdk-8-jdk
RUN apt-get update -y && apt-get install -y python openssh-client git && apt-get clean \
  && curl https://bootstrap.pypa.io/get-pip.py | python \
  && pip install --upgrade mkdocs \
  && git config --global user.email "team@gliderlabs.com" \
  && git config --global user.name "Gliderbot" \
  && ln -s /root /home/ubuntu \
  && curl -Ls https://github.com/gliderlabs/sigil/releases/download/v0.3.2/sigil_0.3.2_Linux_x86_64.tgz | tar -zxC /bin
ADD ./scripts/* /bin/
ADD ./gh-pages /tmp/gh-pages
ADD ./theme /pagebuilder/theme
WORKDIR /work
EXPOSE 8000
RUN pip install requests markdown-include
ADD https://raw.githubusercontent.com/sequenceiq/markdown-include/master/markdown_include/include.py /usr/local/lib/python2.7/dist-packages/markdown_include/include.py
