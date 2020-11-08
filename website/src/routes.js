import React from 'react';

const Dashboard = React.lazy(() => import('./views/dashboard/Dashboard'));
const Unpaid = React.lazy(() => import('./views/bills/Unpaid'))
const Paid = React.lazy(() => import('./views/bills/Paid'))
const Statistics = React.lazy(() => import('./views/bills/Statistics'))
const NewBill = React.lazy(() => import('./views/bills/NewBill'))

const Family = React.lazy(() => import('./views/community/Family'))
const Community = React.lazy(() => import('./views/community/Community'))

const Charts = React.lazy(() => import('./views/charts/Charts'));
const Widgets = React.lazy(() => import('./views/widgets/Widgets'));

const routes = [
  { path: '/', exact: true, name: 'Home' },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
  { path: '/unpaid', name: 'Unpaid Bills', component: Unpaid },
  { path: '/paid', name: 'Paid Bills', component: Paid },
  { path: '/statistics', name: 'Statistics', component: Statistics },
  { path: '/new-bill', name: 'New Bill', component: NewBill },
  { path: '/family', name: 'Family & Friends', component: Family },
  { path: '/community', name: 'Community', component: Community },
  { path: '/charts', name: 'Charts', component: Charts },
  { path: '/widgets', name: 'Widgets', component: Widgets },
];

export default routes;
