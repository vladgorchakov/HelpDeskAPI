from django.urls import path
from helpdesk.views import TicketViewSet, MessageViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tickets', TicketViewSet)
router.register('messages', MessageViewSet)
urlpatterns = router.urls
