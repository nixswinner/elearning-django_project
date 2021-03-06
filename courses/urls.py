from django.conf.urls import url
from . import views

urlpatterns = [
	
	

	url(r'^mine/$',views.ManageCourseListView.as_view(),name='manage_course_list'),
	url(r'^create/$',views.CourseCreateView.as_view(),name='course_create'),
	url(r'^(?P<pk>\d+)/edit/$',views.CourseUpdateView.as_view(),name='course_edit'),
	url(r'^(?P<pk>\d+)/delete/$',views.CourseDeleteView.as_view(),name='course_delete'),
	url(r'^(?P<pk>\d+)/module/$',views.CourseModuleUpdateView.as_view(),name='course_module_update'),
	#modules urls
	url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
            views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$',
            views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    #delete module
    url(r'^content/(?P<id>\d+)/delete/$',views.ContentDeleteView.as_view(),name='module_content_delete'),
    #sisplaying module list
    url(r'^module/(?P<module_id>\d+)/$',views.ModuleContentListView.as_view(),name='module_content_list'),
    #to enable reordering of modules and contents by drag and drop ajax widget
    url(r'^module/order/$',views.ModuleOrderView.as_view(),name='module_order'),
    url(r'^content/order/$',views.ContentOrderView.as_view(),name='content_order'),
    #subject
    url(r'^subject/(?P<subject>[\w-]+)/$',views.CourseListView.as_view(),name='course_list_subject'),
    url(r'^(?P<slug>[\w-]+)/$',views.CourseDetailView.as_view(),name='course_detail'),














]