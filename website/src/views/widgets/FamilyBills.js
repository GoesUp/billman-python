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

const FamilyBills = (data) => {
  console.log(data);
  let familyData = data.data.data.family;
  console.log(familyData);

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

  function pay(id) {
    fetch("http://localhost:5000/bill/pay?id_bill="+id+"&credits=True")
      .then((res) => {
        window.location.reload(false);
      })
  }

  return (
    <>
      { familyData.map((item, index) => (
          <CRow>
            <CCol sm="2">
              <CCard className="text-center">
                <CCardBody><br/>
                  <img
                    src={"avatars/" + (index+1) + ".jpg"}
                    className={"rounded"}
                    width="33%"
                  /><br/><br/>
                  <h4>{item.name + " " + item.surname}</h4>
                </CCardBody>
              </CCard>
            </CCol>
            <CCol sm="10">
              <table className="table table-hover table-outline mb-0 d-none d-sm-table">
                <thead className="thead-light">
                  <tr>
                    <th className="text-center"><CIcon name="cil-keyboard" /></th>
                    <th>Service</th>
                    <th className="text-right">Amount</th>
                    <th className="text-center">Payment Date</th>
                    <th className="text-center">Pay</th>
                  </tr>
                </thead>
                <tbody>
                  { item.family_bills.length == 0 ? (
                    <tr class="table-light">
                      <td colspan="5">
                        <div class="row justify-content-md-center">
                          <div class col>
                            {item.name + " doesn't need any bills paid currently."}
                          </div>
                        </div>
                      </td>
                    </tr>
                  ) : <></>
                  }
                  { item.family_bills.map((bill, bIndex) => (
                    <tr class="table-light">
                      <td className="text-center">
                        <div className="c-avatar">
                          <img src={'providers/' + bill.short_name + '.jpg'} width="100%" alt={"ayo"} />
                        </div>
                      </td>
                      <td>
                        <div>{bill.purpose}</div>
                        <div className="small text-muted">
                          <span>Recurring</span>
                        </div>
                      </td>
                      <td className="text-right">
                        <div>{bill.total + " €"}</div>
                      </td>
                      <td className="text-center">
                        <div>{bill.date_due}</div>
                      </td>
                      <td>
                        <CButton size="lg" block color="primary" onClick={() => (function() {setModalActive(!showModal); setUser(index); setBill(bIndex)})()}><CIcon name="cil-credit-card" alt="CC" /> Pay</CButton>
                      </td>
                    </tr>
                  )) }
                </tbody>
              </table>
            </CCol>
          </CRow>
      ))}

      <CModal
        show={showModal}
        onClose={() => setModalActive(!showModal)}
        size="lg"
      >
        <CModalHeader closeButton>
          <CModalTitle>Payment</CModalTitle>
        </CModalHeader>
        <CModalBody>
          <CRow>
            <CCol xs="6">
              <CFormGroup>
                <CLabel htmlFor="name">Recipient</CLabel>
                <CInput id="name" value={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].recipient : 0} required disabled />
              </CFormGroup>
            </CCol>
            <CCol xs="6">
              <CFormGroup>
                <CLabel htmlFor="name">Recipient Address</CLabel>
                <CInput id="name" value={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].recipient_address : ""} required disabled />
              </CFormGroup>
            </CCol>
          </CRow>
          <CRow>
            <CCol xs="4">
              <CFormGroup>
                <CLabel htmlFor="ccnumber">IBAN</CLabel>
                <CInput id="ccnumber" placeholder={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].IBAN_recipient : ""} required disabled />
              </CFormGroup>
            </CCol>
            <CCol xs="4">
              <CFormGroup>
                <CLabel htmlFor="ccnumber">BIC Code</CLabel>
                <CInput id="ccnumber" placeholder={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].BIC_bank_recipient : ""} required disabled />
              </CFormGroup>
            </CCol>
            <CCol xs="4">
              <CFormGroup>
                <CLabel htmlFor="ccnumber">Reference</CLabel>
                <CInput id="ccnumber" placeholder={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].reference : ""} required disabled />
              </CFormGroup>
            </CCol>
          </CRow>
          <CRow>
            <CCol xs="6">
              <CLabel htmlFor="prependedInput">Amount</CLabel>
              <CInputGroup className="input-prepend">
                <CInputGroupPrepend>
                  <CInputGroupText>€</CInputGroupText>
                </CInputGroupPrepend>
                <CInput type="number" id="name" value={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].total : 0} required disabled />
              </CInputGroup>
            </CCol>
            <CCol xs="6">
              <CFormGroup>
                <CLabel htmlFor="name">Purpose</CLabel>
                <CInput id="name" value={familyData[selectedUser].family_bills.length > 0 ? familyData[selectedUser].family_bills[selectedBill].purpose : ""} required disabled />
              </CFormGroup>
            </CCol>
          </CRow>
        </CModalBody>
        <CModalFooter>
          <CButton color="primary" onClick={() =>     (function() {pay(familyData[selectedUser].family_bills[selectedBill].id); setModalActive(!showModal)})()    }>Pay</CButton>{' '}
          <CButton color="secondary" onClick={() => setModalActive(!showModal)}>Cancel</CButton>
        </CModalFooter>
      </CModal>
    </>
  )
}

export default FamilyBills
