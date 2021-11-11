FROM circleci/node:6

# install calibre
RUN sudo apt-get update && sudo apt-get install -y calibre

# install fonts
RUN sudo wget https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKsc-hinted.zip && \
  sudo unzip NotoSansCJKsc-hinted.zip && \
  sudo mv *.otf /usr/share/fonts && \
  sudo chmod 644 /usr/share/fonts/*.otf && \
  sudo fc-cache
