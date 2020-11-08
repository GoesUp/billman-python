import React, { lazy } from 'react'

const UnpaidBills = lazy(() => import('../widgets/UnpaidBills.js'))

const Unpaid = (data) => {
  return (
    <>
      <h3>Unpaid Bills</h3>
      <h5><em>Your bills which haven't been paid for yet. Pay 'em all!</em></h5>
      <br/>
      <UnpaidBills data={data}/>
    </>
  )
}

export default Unpaid
