from rest_framework import routers

from apps.budget.viewsets import BudgetViewSet

router = routers.SimpleRouter()
router.register('budgets', BudgetViewSet)

urlpatterns = router.urls