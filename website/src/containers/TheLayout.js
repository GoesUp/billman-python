import React from 'react'
import {
  TheContent,
  TheSidebar,
  TheFooter,
  TheHeader
} from './index'

const TheLayout = (d) => {
  console.log(d);
  return (
    <div className="c-app c-default-layout">
      <TheSidebar/>
      <div className="c-wrapper">
        <TheHeader data={ d.data }/>
        <div className="c-body">
          <TheContent data={d.data}/>
        </div>
        <TheFooter/>
      </div>
    </div>
  )
}

export default TheLayout
