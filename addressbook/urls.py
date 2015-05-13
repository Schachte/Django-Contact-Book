from django.conf.urls import include, url
from django.contrib import admin
import contacts.views

urlpatterns = [

	url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contacts-edit'),
#.as_view because it's a class-based view
	url(r'^$', contacts.views.ContactListView.as_view(),
		name = 'contacts-list',
		),
	url(r'^new$', contacts.views.CreateContactView.as_view(), name='contacts-new'),
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(), name='contacts-delete'),
]
