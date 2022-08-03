from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(prefix=r'mytickets', viewset=views.UserTicketViewSet)
router.register(prefix=r'support/tickets', viewset=views.SupportTicketViewSet)
urlpatterns = router.urls
