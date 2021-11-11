# See following page to find out CRS version
# https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/v3.0/master/CHANGES
#
# docker build -t fareoffice/modsecurity:<CRS-VERSION> .
# docker push fareoffice/modsecurity:<CRS-VERSION>

FROM owasp/modsecurity-crs

# https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/v3.0/master/crs-setup.conf.example#L130
# - A paranoia level of 1 is default. In this level, most core rules
#   are enabled. PL1 is advised for beginners, installations
#   covering many different sites and applications, and for setups
#   with standard security requirements.
#   At PL1 you should face FPs rarely. If you encounter FPs, please
#   open an issue on the CRS GitHub site and don't forget to attach your
#   complete Audit Log record for the request with the issue.
# - Paranoia level 2 includes many extra rules, for instance enabling
#   many regexp-based SQL and XSS injection protections, and adding
#   extra keywords checked for code injections. PL2 is advised
#   for moderate to experienced users desiring more complete coverage
#   and for installations with elevated security requirements.
#   PL2 comes with some FPs which you need to handle.
# - Paranoia level 3 enables more rules and keyword lists, and tweaks
#   limits on special characters used. PL3 is aimed at users experienced
#   at the handling of FPs and at installations with a high security
#   requirement.
# - Paranoia level 4 further restricts special characters.
#   The highest level is advised for experienced users protecting
#   installations with very high security requirements. Running PL4 will
#   likely produce a very high number of FPs which have to be
#   treated before the site can go productive.
ENV PARANOIA=3

# Possible values: On / Off /DetectionOnly
ENV SEC_RULE_ENGINE=On

# https://github.com/SpiderLabs/owasp-modsecurity-crs/issues/656
# The default values for the PCRE Match limit are very, very low with ModSecurity. 
# You can got to 500K usually without harming your set.
# But for your information: 
# The PCRE Match limit is meant to reduce the chance for a DoS attack via 
# Regular Expressions. So by raising the limit you raise your vulnerability in this regard, 
# but the PCRE errors are much worse from a security perspective. I run with 500K in prod usually.
ENV SEC_PRCE_MATCH_LIMIT=500000
ENV SEC_PRCE_MATCH_LIMIT_RECURSION=500000

# Keycloak proxy most probably in our case, hence port 3000
ENV PROXY_UPSTREAM_HOST=localhost:3000

ENV LOG_LEVEL=warn

COPY main.sh /main.sh

COPY proxy.conf /etc/httpd/conf.d/proxy.conf

RUN ["chmod", "+x", "/main.sh"]

CMD ["/main.sh"]
