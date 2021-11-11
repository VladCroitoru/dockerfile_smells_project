FROM tkelman/julia-otherdeps
MAINTAINER Tony Kelman <tony@kelman.net>

RUN for ARCH in i686 x86_64; do \
      cd /home/julia-$ARCH && \
      echo 'JULIA_THREADS = 1' >> Make.user; \
      make -j2 -C deps install-llvm && \
      make -C deps distclean-llvm && \
      echo "# the following line is a hack to avoid rebuilding deps after distclean'ed" >> Make.user && \
      echo 'override DEP_LIBS =' >> Make.user; \
    done
# distclean-llvm should leave in place the installed libraries and headers
