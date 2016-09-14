from rest_framework import routers
from .distro import views as distro_views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'distros', distro_views.DistroViewSet)

urlpatterns = router.urls
