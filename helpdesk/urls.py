from django.urls import path
from helpdesk.views import TicketViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tickets', TicketViewSet)
urlpatterns = router.urls
