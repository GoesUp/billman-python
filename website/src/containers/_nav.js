import React from 'react'
import CIcon from '@coreui/icons-react'

export default [
  {
    _tag: 'CSidebarNavItem',
    name: 'Dashboard',
    to: '/dashboard',
    icon: <CIcon name="cil-speedometer" customClasses="c-sidebar-nav-icon"/>,
  },
  {
    _tag: 'CSidebarNavTitle',
    _children: ['My bills']
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Unpaid Bills',
    to: '/unpaid',
    icon: 'cil-bell-exclamation',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Paid Bills',
    to: '/paid',
    icon: 'cil-check',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Statistics',
    to: '/statistics',
    icon: 'cil-chart-pie',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'New Bill',
    to: '/new-bill',
    icon: 'cil-plus',
  },
  {
    _tag: 'CSidebarNavTitle',
    _children: ['Community']
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Family & Friends',
    to: '/family',
    icon: 'cil-user',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Charity',
    to: '/Community',
    icon: 'cil-heart',
    badge: {
      color: 'danger',
      text: 'Help those in need!',
    },
  },
  {
    _tag: 'CSidebarNavTitle',
    _children: ['Components']
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Chartsooooooo',
    to: '/charts',
    icon: 'cil-chart-pie'
  },
  {
    _tag: 'CSidebarNavDivider'
  },
  {
    _tag: 'CSidebarNavDivider',
    className: 'm-2'
  }
]

