from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, login_view

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', include(router.urls)),
]
