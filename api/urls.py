from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(prefix=r'tickets', viewset=views.TicketViewSet, basename='tickets')
router.register(prefix='messaage', viewset=views.MessageViewSet, basename='message')
urlpatterns = router.urls
