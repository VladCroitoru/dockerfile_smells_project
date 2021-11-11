# *****************************************************************************
# Installs SBCL, FriCAS, quicklisp, cl-jupyter and iSPAD kernel.
# Build ..: docker build -t nilqed/ispad .
# Test ...: docker run -t -i nilqed/ispad /bin/bash
# Run ....: docker run -p 443:8888  -t -i nilqed/ispad ipython notebook --ip=*
# *****************************************************************************

FROM nilqed/fricas

MAINTAINER Kurt Pagani <nilqed@gmail.com> 

 
# =====================
# cl-jupyter (optional)
# =====================

RUN cd /root && git clone https://github.com/fredokun/cl-jupyter.git && \
    cd ./cl-jupyter && \ 
    python3 ./install-cl-jupyter.py && \
    sed -i '1i (ql:quickload "asdf")' cl-jupyter.lisp && \
    sed -i '1i (load "~/quicklisp/setup")' cl-jupyter.lisp
    
   

# =====
# iSPAD
# =====

RUN cd /root && git clone https://bitbucket.org/kfp/ispad.git && \
    cd ./ispad && \
    ./setup.sh 


  
# =======
# MathJax
# =======

RUN cd /usr/local/lib/python3.4/dist-packages/notebook/static/components && \
    rm -r MathJax && \
    git clone git://github.com/mathjax/MathJax.git MathJax


# =====================
# CodeMirror mode/lexer
# =====================

RUN cd /root/tmp
 
