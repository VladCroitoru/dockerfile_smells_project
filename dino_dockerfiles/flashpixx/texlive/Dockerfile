FROM flashpixx/texlive:tex

# --- full configurated and updated configuration --------------
RUN echo "\$pdf_mode  = 1;\n\$bibtex_use = 2;\n\$pdflatex  = 'pdflatex -halt-on-error -file-line-error -shell-escape -interaction=nonstopmode -synctex=1 %O %S';\n\$clean_ext = 'synctex.gz synctex.gz(busy) run.xml xmpi acn acr alg glsdefs vrb bbl ist glg glo gls ist lol log 1 dpth auxlock %R-figure*.* %R-blx.bib snm nav dvi xmpi tdo';\n\nadd_cus_dep('glo', 'gls', 0, 'makeglossaries');\nadd_cus_dep('acn', 'acr', 0, 'makeglossaries');\nadd_cus_dep('mp', '1', 0, 'mpost');\n\nsub makeglossaries {\nreturn system('makeglossaries', \$_[0]);\n}\n\nsub mpost {\nmy (\$name, \$path) = fileparse( \$_[0] );\nmy \$return = system('mpost', \$_[0]);\nif ( (\$path ne '') && (\$path ne '.\\\\\\\\') && (\$path ne './') ) {\nforeach ( '\$name.1', '\$name.log' ) { move \$_, \$path; }\n}\nreturn \$return;\n}\n" > /root/.latexmkrc

ENV TEXMFHOME /root/texmf
ENV PATH /usr/local/texlive/bin/x86_64-linux:/root/go/bin:$PATH
RUN tlmgr update --self --all --reinstall-forcibly-removed
