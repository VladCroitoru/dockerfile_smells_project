FROM debian:jessie

ENV CABAL_VERSION "1.24.0.2"

RUN apt-get update && \
	apt-get install git ghc wget tar -y && \
	wget -O /tmp/cabal.tar.gz https://www.haskell.org/cabal/release/cabal-install-${CABAL_VERSION}/cabal-install-${CABAL_VERSION}-x86_64-unknown-linux.tar.gz && \
	tar -xvf /tmp/cabal.tar.gz && \
	rm /tmp/cabal.tar.gz && \
	mv dist-newstyle/build/x86_64-linux/ghc-8.0.2/cabal-install-${CABAL_VERSION}/build/cabal/cabal /usr/local/bin/cabal && \
	rm -r dist-newstyle/ && \
	cabal update && \
	cabal install ShellCheck && \
	mv /root/.cabal/bin/shellcheck /usr/local/bin/shellcheck && \
	rm /usr/local/bin/cabal && \
	rm -r /root/.cabal && \
	apt-get autoremove ghc -y && \
	apt-get clean


