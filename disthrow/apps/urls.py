from rest_framework_nested import routers
from .distro import views as distro_views
from .product import views as product_views


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'distros', distro_views.DistroViewSet)

product_router = routers.NestedSimpleRouter(
    router, r'distros', lookup='distro')
product_router.register(
    r'products', product_views.ProductViewsSet, base_name='product-distros')

urlpatterns = router.urls
urlpatterns += product_router.urls
