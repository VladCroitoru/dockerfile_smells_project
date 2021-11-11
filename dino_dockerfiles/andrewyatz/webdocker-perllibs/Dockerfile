FROM andrewyatz/webdocker

ENV HOMEBREW_ENSEMBL_MOONSHINE_ARCHIVE=/home/linuxbrew/moonshine
RUN mkdir -p $HOMEBREW_ENSEMBL_MOONSHINE_ARCHIVE

RUN brew install ensembl/cask/web-libsforcpanm
RUN brew install ensembl/cask/web-gui

# Need to do this to ignore a pcre error
RUN brew install ensembl/external/blast; exit 0

# Go for remaining dependencies from brew
RUN brew install ensembl/cask/web-bifo

# Get hubCheck (not in brew)
RUN mkdir -p $HOME/utils
WORKDIR /home/linuxbrew/utils
RUN curl -s http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/hubCheck > hubCheck
RUN chmod ugo+x hubCheck
WORKDIR /home/linuxbrew

# Create fonts directory
RUN mkdir -p $HOME/fonts && ln -s $HOME/fonts $HOME/.fonts

# clone git repositories
RUN mkdir -p src
RUN git clone https://github.com/Ensembl/ensembl.git
RUN git clone https://github.com/Ensembl/ensembl-webcode.git

# Install Perl dependencies
RUN cpanm --installdeps --with-recommends --notest --cpanfile ensembl/cpanfile .
RUN curl -s https://raw.githubusercontent.com/Ensembl/cpanfiles/master/web/cpanfile > cpanfile

# HTML::Formatter fails to install sometimes. So we force it. Really this should not happen
RUN cpanm --notest HTML::Formatter
RUN cpanm --installdeps --with-recommends --notest --cpanfile cpanfile .

# update bash profile
RUN echo >> $HOME/.profile && \
echo PATH=$HOME/.linuxbrew/bin:\$PATH >> $HOME/.profile && \
echo PATH=$HOME/paths/bin:\$PATH >> $HOME/.profile && \
echo MANPATH=$HOME/.linuxbrew/share/man:\$MANPATH >> $HOME/.profile && \
echo INFOPATH=$HOME/.linuxbrew/share/info:\$INFOPATH >> $HOME/.profile && \
echo export PATH >> $HOME/.profile && \
echo export MANPATH >> $HOME/.profile && \
echo export INFOPATH >> $HOME/.profile && \
echo export PERL5LIB=${PERL5LIB} >> $HOME/.profile && \
echo export SHARE_PATH=$HOME/paths >> $HOME/.profile && \
echo export ENSEMBL_MOONSHINE_ARCHIVE=${HOMEBREW_ENSEMBL_MOONSHINE_ARCHIVE}} >> $HOME/.profile && \
echo export HOMEBREW_ENSEMBL_MOONSHINE_ARCHIVE=${HOMEBREW_ENSEMBL_MOONSHINE_ARCHIVE}} >> $HOME/.profile

# Symlink binaries into share path
RUN mkdir -p $SHARE_PATH && \
ln -s $HOME/.linuxbrew/opt/emboss $SHARE_PATH/emboss && \
ln -s $HOME/.linuxbrew/opt/genewise $SHARE_PATH/genewise && \
ln -s $HOME/.linuxbrew/opt/jdk/bin/java $SHARE_PATH/java && \
ln -s $HOME/.linuxbrew/opt/r2r/bin/r2r $SHARE_PATH/r2r && \
ln -s $HOME/.linuxbrew/opt/htslib/include $SHARE_PATH/htslib && \
ln -s $HOME/.linuxbrew/opt/kent/bin/gfClient $SHARE_PATH/gfClient  && \
ln -s $HOME/.linuxbrew/opt/blast/bin $SHARE_PATH/ncbi-blast && \
ln -s $HOME/.linuxbrew/opt/repeatmasker/bin/RepeatMasker $SHARE_PATH/RepeatMasker && \
ln -s $HOME/.linuxbrew/opt/htslib/bin/bgzip $SHARE_PATH/bgzip && \
ln -s $HOME/.linuxbrew/opt/samtools/bin/samtools $SHARE_PATH/samtoools && \
ln -s $HOME/.linuxbrew/opt/htslib/bin/tabix $SHARE_PATH/tabix

#ln -s $HOME/.linuxbrew/opt/perl/5.24.0_3/lib/perl5/site_perl/5.24.0/ $SHARE_PATH/bioperl && \
#ln -s $SHARE_PATH/1000G-tools/vcftools/lib/perl5/site_perl/ $SHARE_PATH/vcftools_perl_lib # need 1000G-tools installed before this
