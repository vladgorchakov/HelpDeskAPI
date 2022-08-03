from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(prefix=r'mytickets', viewset=views.UserTicketViewSet)
urlpatterns = router.urls
