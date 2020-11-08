import React, {useState} from 'react'
import {
  CWidgetDropdown,
  CRow,
  CCol,
  CDropdown,
  CDropdownMenu,
  CImg,
  CDropdownToggle,
  CCard,
  CCardHeader,
  CCardBody,
  CDataTable,
  CBadge,
  CProgress,
  CButton,
  CModalHeader,
  CModalTitle,
  CModalBody,
  CModalFooter,
  CModal,
  CFormGroup,
  CLabel,
  CInput,
  CSelect,
  CInputGroupPrepend,
  CInputGroupText,
  CInputGroup
} from '@coreui/react'
import CIcon from '@coreui/icons-react'
import {
} from '@coreui/react'

const CharityBills = (data) => {
  console.log(data);
  let familyData = data.data.data.family;
  let poor = data.data.data.poor;
  console.log(poor);

  function get_color(percent) {
    console.log(percent);
    if (percent > 90) {
      return "danger"
    } else if (percent > 50) {
      return "warning"
    } else {
      return "success"
    }
  }
  const [showModal, setModalActive] = useState(false);
  const [selectedBill, setBill] = useState(0);
  const [selectedUser, setUser] = useState(0);

  function donate(poor, amount) {
    fetch("http://localhost:5000/bill/pay/community?poor_id="+poor+"&amount=" + amount + "&credits=True")
      .then((res) => {
        window.location.reload(false);
      })
  }

  return (
    <>
      { poor.map((item, index) => (
          <CRow>
            <CCol sm="3">
              <CCard className="text-center">
                <CCardBody height="100%"><br/>
                  <img
                    src={"avatars/p" + (index) + ".jpg"}
                    className={"rounded"}
                    width="33%"
                  /><br/><br/>
                  <h4>{item.poor.name + " " + item.poor.surname}</h4>
                </CCardBody>
              </CCard>
            </CCol>
            <CCol sm="9">
              <CCard className="text-left">
                <CCardBody>
                  <h5>Cause</h5>
                  <span>{item.poor.desc}</span><br/><br/>
                  <h5>Donation breakdown</h5>
                  <table class="table table-sm table-borderless">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">Expense</th>
                        <th scope="col">Amount</th>
                      </tr>
                    </thead>
                    <tbody>
                      { item.bills.map((bill, i) => (
                        <tr>
                          <th scope="row">{i + 1}</th>
                          <td>{bill.cause}</td>
                          <td>{"€ " + bill.value.toFixed(2)}</td>
                        </tr>
                      )) }

                    </tbody>
                    <thead>
                      <tr>
                        <th scope="col"></th>
                        <th scope="col"><b>TOTAL</b></th>
                        <th scope="col"><b>{item.total}</b></th>
                      </tr>
                    </thead>
                  </table>
                  <div className="clearfix">
                    <div className="float-left">
                      <strong>Progress</strong>
                    </div>
                    <div className="float-right">
                      <small className="text-muted">{item.collected + " € / " + item.total + " €"}</small>
                    </div>
                  </div>
                  <CProgress animated className="progress-" color="success" value={Math.round(item.collected * 100 / item.total)} /><br/>
                  <CButton color="success" onClick={() => donate(item.poor.id, 5)}>Donate 5 €</CButton>&nbsp;
                  <CButton color="success" onClick={() => donate(item.poor.id, 10)}>Donate 10 €</CButton>&nbsp;
                  <CButton color="success" onClick={() => donate(item.poor.id, 20)}>Donate 20 €</CButton>
                </CCardBody>
              </CCard>
            </CCol>
          </CRow>
      ))}

    </>
  )
}

export default CharityBills
