FROM debian:stretch-slim

LABEL maintainer="mathias@mperlet.de"

RUN apt-get update && apt-get --no-install-recommends -y install unzip python-setuptools wget python-pip texlive texlive-lang-german texlive-latex-extra
RUN wget https://github.com/mperlet/wal/archive/master.zip && unzip master.zip && rm master.zip
WORKDIR /wal-master/
RUN wget http://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-3.0-distrib/share/texmf/tex/latex/g-brief/g-brief.cls &&\
    wget http://www.cs.cmu.edu/afs/cs/misc/tex/common/teTeX-1.0.1/lib/texmf/tex/latex/misc/pdfpages.sty &&\
    wget http://computer-vision.org/4authors/eso-pic.sty &&\
    wget http://computer-vision.org/4authors/crv_eso.sty &&\
    wget http://code.haskell.org/~byorgey/TMR/Issue16/ucsencs.def &&\
    wget http://code.haskell.org/~byorgey/TMR/Issue16/uni-global.def &&\
    wget http://mirrors.sorengard.com/ctan/macros/latex/contrib/ulem/ulem.sty &&\
    wget https://raw.github.com/rivercheng/cv/master/currvita.sty &&\
    wget http://mirrors.concertpass.com/tex-archive/macros/latex/contrib/ucs/utf8x.def &&\   
    wget http://ctan.mirrors.hoobly.com/language/german/ngerman.sty &&\
    wget http://mirrors.ctan.org/macros/latex/contrib/ms.zip && unzip ms.zip && rm ms.zip && mv ms/* .
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["wal.py"]
