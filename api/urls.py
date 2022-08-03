from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(prefix=r'mytickets', viewset=views.UserTicketViewSet, basename='mytickets')
router.register(prefix=r'support/tickets', viewset=views.SupportTicketViewSet)
router.register(prefix='messaage', viewset=views.MessageViewSet, basename='msg')
urlpatterns = router.urls
