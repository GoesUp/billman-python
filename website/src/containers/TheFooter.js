import React from 'react'
import { CFooter } from '@coreui/react'

const TheFooter = () => {
  return (
    <CFooter fixed={false}>
      <div>
        <a href="http://localhost:3000" target="_blank" rel="noopener noreferrer">Billman</a>
        <span className="ml-1">&copy; 2020 BGM3000</span>
      </div>
    </CFooter>
  )
}

export default React.memo(TheFooter)
