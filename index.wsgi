import sae
from testzzq import wsgi

application = sae.create_wsgi_app(wsgi.application)