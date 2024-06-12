from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView
from Loco import views

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('locomotives/',views.locomotive_list),
    path('locomotives/<str:name>',views.locomotive_details),
    path('locomotives/broad/',views.broad_list),
    path('locomotives/meter/',views.meter_list),
    path('locomotives/narrow/',views.narrow_list),
    path('locomotives/narrower/',views.narrower_list),
    path('locomotives/electric/',views.electric_list),
    path('locomotives/diesel/',views.diesel_list)
]
