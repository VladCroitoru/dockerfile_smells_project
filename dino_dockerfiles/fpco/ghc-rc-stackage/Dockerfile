# Base ourselves on the Stackage Nightly image to get all necessary system
# libraries. This also pulls in an unnecessary GHC, but we're favoring
# simplicity here.
FROM snoyberg/stackage:nightly

RUN echo Starting && \

    # Download the GHC tarball, feel free to update the URL as necessary
    curl http://downloads.haskell.org/~ghc/8.0.1-rc2/ghc-8.0.0.20160204-x86_64-deb8-linux.tar.xz > ghc.tar.xz && \

    # Decompress the tarball and delete it (make the resulting image smaller)
    tar xf ghc.tar.xz && \
    rm ghc.tar.xz && \

    # Install GHC to /opt/ghc
    cd ghc-* && \
    ./configure --prefix=/opt/ghc && \
    make install && \
    cd .. && \

    # Remove the unpacked directory
    rm -rf ghc-* && \

    # Hopefully this is just an artifact of RCs and not a sign of changing the
    # directory structure permanently...
    mv /opt/ghc/share/doc/ghc-* /opt/ghc/share/doc/ghc && \

    # Get the stack and stackage-curator executables
    curl -L https://www.stackage.org/stack/linux-x86_64 | tar xz --wildcards --strip-components=1 -C /usr/bin '*/stack' && \
    curl https://s3.amazonaws.com/stackage-travis/stackage-curator/stackage-curator.bz2 | bunzip2 > /usr/bin/stackage-curator && \
    chmod +x /usr/bin/stackage-curator

# Update environment to use the new GHC
ENV PATH=/opt/ghc/bin:$PATH

# Include the README.md file and build.sh script
ADD README.md /stackage/README.md
ADD build.sh /stackage/build.sh
