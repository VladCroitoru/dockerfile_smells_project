FROM node:6.3.1

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install r-base
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('party')"
RUN Rscript -e "install.packages('modeltools')"
RUN Rscript -e "install.packages('methods')"
RUN Rscript -e "install.packages('base')"
RUN Rscript -e "install.packages('rms')"

RUN mkdir -p /usr/nostra
WORKDIR /usr/nostra

COPY package.json /usr/nostra
RUN npm install

COPY . /usr/nostra
RUN npm run publish


EXPOSE 3000

CMD ["npm", "start"]