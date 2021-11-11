# Pa11y is your automated accessibility testing pal.
# http://pa11y.org/
#
# Basic usage, returning an accessibility report.
# docker run --rm -t jasonmce/pa11y nature.com

# This was the smallest node base I could get to work.
FROM node:7.4-wheezy

RUN npm install -g pa11y

ENTRYPOINT ["pa11y"]
