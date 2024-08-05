from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>/', views.post_detail, name='post-detail-page'),
    path('contact', views.contact_personal, name='contact-personal'),
    path('skills', views.skills, name='skills'),
    path('education', views.education, name='education'),
    path('machine-learning', views.machine_learning, name='machine-learning'),
    path('professional-experience', views.professional_experience, name='professional-experience'),
    path('crypto', views.crypto, name='crypto'),
    path('personal-website', views.personal_website, name='personal-website')
]