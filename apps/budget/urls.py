from rest_framework import routers

from .viewsets import BudgetViewSet

router = routers.SimpleRouter()
router.register('budgets', BudgetViewSet)

urlpatterns = router.urls