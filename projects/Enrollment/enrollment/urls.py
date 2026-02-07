from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('enroll/<int:child_id>/', views.enroll_child, name='enroll_child'),
    path('parents/', views.parent_list, name='parent_list'),
    path('parents/<int:pk>/', views.parent_detail, name='parent_detail'),
    path('parents/create/', views.parent_create, name='parent_create'),
    path('parents/<int:pk>/update/', views.parent_update, name='parent_update'),
    path('parents/<int:pk>/delete/', views.parent_delete, name='parent_delete'),
    path('children/', views.child_list, name='child_list'),
    path('children/<int:pk>/', views.child_detail, name='child_detail'),
    path('children/create/', views.child_create, name='child_create'),
    path('children/<int:pk>/update/', views.child_update, name='child_update'),
    path('children/<int:pk>/delete/', views.child_delete, name='child_delete'),
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/<int:pk>/', views.enrollment_detail, name='enrollment_detail'),
    path('enrollments/create/', views.enrollment_create, name='enrollment_create'),
    path('enrollments/<int:pk>/update/', views.enrollment_update, name='enrollment_update'),
    path('enrollments/<int:pk>/delete/', views.enrollment_delete, name='enrollment_delete'),
] 