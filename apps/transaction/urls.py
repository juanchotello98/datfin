from rest_framework import routers

from apps.transaction.viewsets import TransactionViewSet

router = routers.SimpleRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = router.urls

