import React, { lazy } from 'react'

const PayWidget = lazy(() => import('../widgets/PayWidget.js'))

const NewBill = (data) => {
  return (
    <>
      <h3>Enter a New Bill</h3>
      <br/>
      <PayWidget data={data}/>
    </>
  )
}

export default NewBill
