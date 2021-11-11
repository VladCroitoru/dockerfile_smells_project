FROM fpco/stack-build:lts-12.22

RUN apt-get update && apt-get install -y \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-fonts-extra

    
RUN stack install pandoc
RUN stack install pandoc-citeproc

    
RUN apt-get install -y texlive-xetex
RUN apt-get install -y texlive-math-extra
