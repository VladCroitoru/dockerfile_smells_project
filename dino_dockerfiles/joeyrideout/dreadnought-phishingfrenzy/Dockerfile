FROM b00stfr3ak/ubuntu-phishingfrenzy

MAINTAINER joeyrideout

# Set up Apache configuration
COPY /pf.conf /etc/apache2/sites-available/pf.conf
RUN a2dissite 000-default.conf
RUN service apache2 start
