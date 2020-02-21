from flask import render_template
from Relatorios_Zabbix import app
from Relatorios_Zabbix.forms import report_form


@app.route('/')
@app.route('/index')
def index():
    form=report_form()
    print(form.submit.id)
    return render_template('secret.html', form=form)