FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY home.html /usr/share/nginx/html/home.html
COPY about.html /usr/share/nginx/html/about.html
COPY contact.html /usr/share/nginx/html/contact.html
COPY resume.html /usr/share/nginx/html/resume.html
COPY sol.html /usr/share/nginx/html/sol.html
COPY writing.html /usr/share/nginx/html/writing.html
COPY bootstrap /usr/share/nginx/html/bootstrap
COPY font /usr/share/nginx/html/font
COPY images /usr/share/nginx/html/images
COPY jquery /usr/share/nginx/html/jquery
COPY style.css /usr/share/nginx/html/style.css
COPY style.min.css /usr/share/nginx/html/style.min.css
COPY quotes.js /usr/share/nginx/html/quotes.js
ENV RESUME_DOC "Derek Elder Resume.doc"
ENV RESUME_PDF "Derek Elder Resume.pdf"
COPY ${RESUME_DOC} /usr/share/nginx/html/${RESUME_DOC}
COPY ${RESUME_PDF} /usr/share/nginx/html/${RESUME_PDF}