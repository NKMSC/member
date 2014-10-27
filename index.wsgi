import sae
from member import wsgi

application = sae.create_wsgi_app(wsgi.application)
