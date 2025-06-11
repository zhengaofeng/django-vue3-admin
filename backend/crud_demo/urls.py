from rest_framework.routers import SimpleRouter
from .views import CrudDemoModelViewSet

router = SimpleRouter()
router.register("api/CrudDemoModelViewSet", CrudDemoModelViewSet)
urlpatterns = []
urlpatterns += router.urls
