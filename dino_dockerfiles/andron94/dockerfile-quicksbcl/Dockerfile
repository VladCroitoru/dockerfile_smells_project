FROM andron94/dockerfile-sbcl:2.1.1
MAINTAINER Andrii Tymchuk <makedonsky94@gmail.com>

# =========================== Install Quicklisp ================================

# 1. Convenient definitions.
ENV QUICKLISP quicklisp.lisp

ENV QUICKLISP_URL https://beta.quicklisp.org/${QUICKLISP}

# 2. Installation:
#  1. Create and move to temporary directory which will be used for the build.
#  2. Download Quicklisp installation script.
#  3. Install Quicklisp.
#  4. Load Quicklisp on SBCL startup.
#  5. Remove unnecessary temporary files.
RUN mkdir /home/temp && cd /home/temp &&\
    wget ${QUICKLISP_URL} &&\
    sbcl --load ${QUICKLISP} \
         --eval '(quicklisp-quickstart:install)' \
         --eval '(ql-util:without-prompting (ql:add-to-init-file))' \
         --eval '(quit)' &&\
    cd /home && rm -rf temp

# ==============================================================================

CMD ["sbcl"]
