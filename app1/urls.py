from django.urls import path
from app1 import views
from django.views.generic import TemplateView

# urlpatterns = [
# 				path('',views.HomePageView.as_view()),
# 				# path('image/',views.AboutPageView.as_view(template_name = 'image.html')),
# 				# path('saved/', 'SaveImage', name = 'saved')
# 			] 
urlpatterns = [
				path('image/',TemplateView.as_view(
      			template_name = 'image.html')),
      			path('saved/', views.SaveImage, name = 'saved'),
      			# path('show/', views.ShowData, name = 'show')
      		]