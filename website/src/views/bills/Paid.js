import React, { lazy } from 'react'

const PaidBIlls = lazy(() => import('../widgets/PaidBills.js'))

const Paid = (data) => {
  return (
    <>
      <h3>Paid Bills</h3>
      <h5><em>They got your money already ;)</em></h5>
      <br/>
      <PaidBIlls data={data}/>
    </>
  )
}

export default Paid
