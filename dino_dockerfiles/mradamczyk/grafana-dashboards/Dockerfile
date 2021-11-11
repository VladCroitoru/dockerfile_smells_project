FROM grafana/grafana
MAINTAINER Michał Adamczyk <mr.adamczyk@gmail.com>

# fixes from https://github.com/percona/grafana-dashboards
#RUN sed -i 's/step_input:""/step_input:c.target.step/; s/ HH:MM/ HH:mm/; s/,function(c)/,"templateSrv",function(c,g)/; s/expr:c.target.expr/expr:g.replace(c.target.expr,c.panel.scopedVars)/' /usr/share/grafana/public/app/plugins/datasource/prometheus/query_ctrl.js && sed -i 's/h=a.interval/h=g.replace(a.interval, c.scopedVars)/' /usr/share/grafana/public/app/plugins/datasource/prometheus/datasource.js

#RUN sed -i 's/h=b.interval/h=i.replace(b.interval, a.scopedVars)/' /usr/share/grafana/public/app/plugins/datasource/prometheus/datasource.js && sed -i 's/,range_input/.replace(\/"{\/g,"\\"").replace(\/}"\/g,"\\""),range_input/; s/step_input:""/step_input:this.target.step/' /usr/share/grafana/public/app/plugins/datasource/prometheus/query_ctrl.js

ADD dashboards /var/lib/grafana/dashboards
ADD grafana.ini /etc/grafana/grafana.ini
