from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^statics/(?P<path>.*)','django.views.static.serve',{'document_root':'testzzq/statics'}), 
    # Examples:
    url(r'^$', 'testzzq.views.login', name='home'),
    # url(r'^testzzq/', include('testzzq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^reg$','testzzq.views.reg'),
    url(r'^login$','testzzq.views.login'),
    url(r'^index$','testzzq.views.index'),
    url(r'^depart/(.+)/$','testzzq.views.depart'),
    url(r'^reg_result/$','testzzq.views.reg_result'),
    url(r'^reg_result/index/$','testzzq.views.index'),
    url(r'^login_result/$','testzzq.views.login_result'),
    url(r'^index/(.+)/$','testzzq.views.index_of_others'),
    url(r'^edit$','testzzq.views.edit'),
    url(r'^edit_result/$','testzzq.views.edit_result'),                  
)
