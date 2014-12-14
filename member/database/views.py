# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.template import Context
from django,http import HttpResponse
from database.models import Code,Activity,Log,Section,User,UserTakePartInActivity
from django.views.decorators.csrf import csrf_exempt