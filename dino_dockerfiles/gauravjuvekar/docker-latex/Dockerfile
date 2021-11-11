FROM ubuntu:latest
MAINTAINER Gaurav Juvekar <gauravjuvekar@gmail.com>

# Now do this convoluted mess so that we have texlive-full except for the
# texlive-*-doc pacakges and texlive-lang* packages that take up too much space.
# The last apt-get clean and rm -rf removes the temporary .deb packages
# downloaded during the install process
RUN apt-get update && \
	 apt-cache depends texlive-full \
	 | grep -v Suggests \
	 | grep -v texlive-full \
	 | grep -v i386 | cut -d' '  -f 4 | grep -v -- '-doc' \
	 | grep -v lang | \
	 xargs apt-get install --no-install-recommends -y \
		texlive-lang-english \
		latexmk \
		biber \
		dot2tex \
		inkscape \
		gnuplot \
		graphviz \
		plantuml \
		dia \
		pdftk \
		&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
