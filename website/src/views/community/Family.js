import React, { lazy } from 'react'

const FamilyBills = lazy(() => import('../widgets/FamilyBills.js'))

const Family = (data) => {
  return (
    <>
      <h3>Friends & Family</h3>
      <h5><em>Pay the bills which they said they need help with!</em></h5>
      <br/>
      <FamilyBills data={data}/>
    </>
  )
}

export default Family
