from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(prefix=r'mytickets', viewset=views.TicketViewSet, basename='mytickets')
router.register(prefix=r'support/tickets', viewset=views.SupportTicketViewSet, basename='suptickets')
router.register(prefix='messaage', viewset=views.MessageViewSet, basename='msg')
urlpatterns = router.urls
