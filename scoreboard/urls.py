from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'scores', views.ScoreViewSet)

urlpatterns = router.urls
