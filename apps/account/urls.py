from rest_framework import routers

from .viewsets import AccountViewSet

router = routers.SimpleRouter()
router.register('accounts', AccountViewSet)

urlpatterns = router.urls