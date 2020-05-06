from rest_framework import routers

from apps.account.viewsets import AccountViewSet

router = routers.SimpleRouter()
router.register('accounts', AccountViewSet)

urlpatterns = router.urls