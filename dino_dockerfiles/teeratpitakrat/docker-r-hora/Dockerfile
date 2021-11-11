FROM r-base

ADD install-libraries.R /
RUN Rscript install-libraries.R
ADD start.R /

EXPOSE 6311
CMD R --vanilla < /start.R
