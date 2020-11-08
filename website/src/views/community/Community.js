import React, { lazy } from 'react'

const CharityBills = lazy(() => import('../widgets/CharityBills.js'))

const Community = (data) => {
  return (
    <>
      <h3>Charity ❤️</h3>
      <h5><em>You never know when misfortune strikes. Why not help some people in need?</em></h5>
      <br/>
      <CharityBills data={data}/>
    </>
  )
}

export default Community
