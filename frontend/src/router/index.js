import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListAccount from '@/components/Account/ListAccount'
import EditAccount from '@/components/Account/EditAccount'
import NewAccount from '@/components/Account/NewAccount'
import ListBudget from '@/components/Budget/ListBudget'
import EditBudget from '@/components/Budget/EditBudget'
import NewBudget from '@/components/Budget/NewBudget'
import ListCategory from '@/components/Category/ListCategory'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/accounts',
      name: 'ListAccount',
      component: ListAccount
    },
    {
      path: '/accounts/new',
      name: 'NewAccount',
      component: NewAccount
    },
    {
      path: '/accounts/:accountId/edit',
      name: 'EditAccount',
      component: EditAccount
    },
    {
      path: '/budgets',
      name: 'ListBudget',
      component: ListBudget
    },
   	{
      path: '/budgets/:budgetId/edit',
      name: 'EditBudget',
      component: EditBudget
    },
    {
      path: '/budgets/new',
      name: 'NewBudget',
      component: NewBudget
    },
    {
      path: '/categories/:budgetId/list',
      name: 'ListCategory',
      component: ListCategory
    }
  ],
  mode: 'history'
})
