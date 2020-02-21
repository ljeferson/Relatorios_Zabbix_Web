from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = 'secret'

import Relatorios_Zabbix.views
import Relatorios_Zabbix.forms