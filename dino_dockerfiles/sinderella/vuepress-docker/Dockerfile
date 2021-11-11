FROM node:9.11

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-latex-base \
  texlive-fonts-recommended \
  texlive-fonts-extra \
  texlive-latex-extra \
  texlive-math-extra \
  texlive-xetex

RUN yarn global add vuepress

