import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListAccount from '@/components/Account/ListAccount'
import EditAccount from '@/components/Account/EditAccount'
import NewAccount from '@/components/Account/NewAccount'
import DeleteAccount from '@/components/Account/DeleteAccount'
import ListBudget from '@/components/Budget/ListBudget'
import EditBudget from '@/components/Budget/EditBudget'
import NewBudget from '@/components/Budget/NewBudget'
import DeleteBudget from '@/components/Budget/DeleteBudget'
import ListCategory from '@/components/Category/ListCategory'
import NewCategory from '@/components/Category/NewCategory'
import EditCategory from '@/components/Category/EditCategory'
import DeleteCategory from '@/components/Category/DeleteCategory'
import ListTransaction from '@/components/Transaction/ListTransaction'
import NewEntry from '@/components/Transaction/NewEntry'
import NewEgress from '@/components/Transaction/NewEgress'
import Login from '@/components/Authentication/Login'
import Signup from '@/components/Authentication/Signup'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/inicio',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
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
      path: '/accounts/:accountId/delete',
      name: 'DeleteAccount',
      component: DeleteAccount
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
      path: '/budgets/:budgetId/delete',
      name: 'DeleteBudget',
      component: DeleteBudget
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
    },
    {
      path: '/categories/:budgetId/new',
      name: 'NewCategory',
      component: NewCategory
    },
    {
      path: '/categories/:budgetId/:categoryId/edit',
      name: 'EditCategory',
      component: EditCategory
    },
    {
      path: '/categories/:budgetId/:categoryId/delete',
      name: 'DeleteCategory',
      component: DeleteCategory
    },
    {
      path: '/transactions',
      name: 'ListTransaction',
      component: ListTransaction
    },
    {
      path: '/transactions/entry',
      name: 'NewEntry',
      component: NewEntry
    },
    {
      path: '/transactions/egress',
      name: 'NewEgress',
      component: NewEgress
    },
  ],
  mode: 'history'
})
