from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
   (r'^statics/(?P<path>.*)','django.views.static.serve',{'document_root':'member/statics/', 'show_indexes': True}),
  #  (r'^statics/(?P<path>.*)','django.views.static.serve',{'document_root':'member/statics'}), 
    # Examples:
    url(r'^$', 'member.views.login', name='home'),
    # url(r'^member/', include('member.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^reg/$','member.views.reg'),
    url(r'^login/$','member.views.login'),
    url(r'^index/$','member.views.index'),
    url(r'^depart/(.+)/$','member.views.depart'),
    url(r'^reg_result/$','member.views.reg_result'),
    url(r'^reg_result/index/$','member.views.index'),
    url(r'^login_result/$','member.views.login_result'),
    url(r'^index/(.+)/$','member.views.index_of_others'),
    url(r'^edit/$','member.views.edit'),
    url(r'^edit_result/$','member.views.edit_result'),
    url(r'^logout/$','member.views.logout'),
    url(r'^send_code/$','member.views.send_code'),
    url(r'^send_code_result/$','member.views.send_code_result'),
    url(r'^change_password/$','member.views.change_password'),
    url(r'^change_password_result/$','member.views.change_password_result'),
    url(r'^reset_password_request/$','member.views.reset_password_request'),
    url(r'^reset_password/$','member.views.reset_password'),
    url(r'^reset_password_change/$','member.views.reset_password_change'),
    url(r'^reset_password_result/$','member.views.reset_password_result'),
    #url(r'^createsuperuser$','member.views.createsuperuser'),
    url(r'^register/$','member.views.register'),
    url(r'^RegisterToMicrosoft$','member.views.RegisterToMicrosoft'),
    url(r'^rules$','member.views.rules'),
    url(r'^intro$','member.views.intro'),
    url(r'^query$','member.views.query'),
    url(r'^query_result/$','member.views.query_result'),
    url(r'^get_award/$','member.views.get_award'),  
    url(r'^nku1234567/$','member.views.change_number'),                               
)
