import React, { lazy } from 'react'
import {CCard, CCardBody, CCardGroup, CCardHeader} from "@coreui/react";
import {CChartBar, CChartDoughnut, CChartLine, CChartPie, CChartPolarArea, CChartRadar} from "@coreui/react-chartjs";

const Statistics = (data) => {
  let trans = data.data.transactions;
  let cake1 = data.data.cake1;
  let cake2 = data.data.cake2;
  return (
    <>
      <CCardGroup columns className = "cols-2" >
        <CCard>
          <CCardHeader>
            Spendings per day
          </CCardHeader>
          <CCardBody>
            <CChartBar
              datasets={[
                {
                  label: 'Amount paid per day',
                  backgroundColor: '#f87979',
                  data: trans,
                }
              ]}
              labels="days"
              options={{
                tooltips: {
                  enabled: true
                }
              }}
            />
          </CCardBody>
        </CCard>

        <CCard>
          <CCardHeader>
            WIP
          </CCardHeader>
          <CCardBody className="text-center">
            <h3>More statistics will come in near future!</h3>
          </CCardBody>
        </CCard>

      </CCardGroup>
    </>
  )
}

export default Statistics
