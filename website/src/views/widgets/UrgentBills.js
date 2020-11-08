import React, {useState} from 'react'
import {
  CWidgetDropdown,
  CRow,
  CCol,
  CDropdown,
  CDropdownMenu,
  CDropdownItem,
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
const fields = ['name','registered', 'role', 'status']
const getBadge = status => {
  switch (status) {
    case 'Active': return 'success'
    case 'Inactive': return 'secondary'
    case 'Pending': return 'warning'
    case 'Banned': return 'danger'
    default: return 'primary'
  }
}

const UrgentBills = (data) => {

  let bills = data.data.data.urgent;
  console.log(bills);

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

  function pay(id) {
    fetch("http://localhost:5000/bill/pay?id_bill="+id+"&credits=True")
      .then((res) => {
        window.location.reload(false);
      })
  }

  return (
    <>
      <table className="table table-hover table-outline mb-0 d-none d-sm-table">
        <thead className="thead-light">
          <tr>
            <th className="text-center"><CIcon name="cil-keyboard" /></th>
            <th>Service</th>
            <th className="text-right">Amount</th>
            <th>Timeline</th>
            <th>Pay</th>
          </tr>
        </thead>
        <tbody>
          { bills.length == 0 ? (
            <tr class="table-light">
              <td colspan="5">
                <div class="row justify-content-md-center">
                  <div class col>
                    No bills are due soon. Hooray!
                  </div>
                </div>
              </td>
            </tr>
          ) : <></>
          }
          { bills.map((item, index) => (
              <tr class="table-light">
                <td className="text-center">
                  <div className="c-avatar">
                    <img src={'providers/' + item.short_name + '.jpg'} width="100%" alt={item.short_name} />
                  </div>
                </td>
                <td>
                  <div>{item.purpose}</div>
                  <div className="small text-muted">
                    <span>Recurring</span>
                  </div>
                </td>
                <td className="text-right">
                  <div>{item.total.toFixed(2) + " €"}</div>
                </td>
                <td>
                  <div className="clearfix">
                    <div className="float-left">
                      <strong>{Math.round((Date.parse(item.date_due) - Date.now()) / (1000 * 60 * 60 * 24)) + 1} day{(Date.parse(item.date_due) - Date.now()) / (1000 * 60 * 60 * 24) > 1 ? "s" : ""} left</strong>
                    </div>
                    <div className="float-right">
                      <small className="text-muted">{item.date_issued} - {item.date_due}</small>
                    </div>
                  </div>
                  <CProgress animated className="progress-xs" color={get_color(Math.round(Math.round((Date.now() - Date.parse(item.date_issued)) * 100 / (Date.parse(item.date_due) - Date.parse(item.date_issued)))))} value={Math.round((Date.now() - Date.parse(item.date_issued)) * 100 / (Date.parse(item.date_due) - Date.parse(item.date_issued)))} />

                </td>
                <td>
                  <CButton size="lg" block color={get_color(Math.round(Math.round((Date.now() - Date.parse(item.date_issued)) * 100 / (Date.parse(item.date_due) - Date.parse(item.date_issued)))))} onClick={() => (function() {setModalActive(!showModal); setBill(index)})()}><CIcon name="cil-credit-card" alt="Settings" /> Pay</CButton>
                </td>
              </tr>
          )) }
        </tbody>
      </table>

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
                <CInput id="name" value={bills.length > 0 ? bills[selectedBill].recipient : 0} required disabled />
              </CFormGroup>
            </CCol>
            <CCol xs="6">
              <CFormGroup>
                <CLabel htmlFor="name">Recipient Address</CLabel>
                <CInput id="name" value={bills.length > 0 ? bills[selectedBill].recipient_address : ""} required disabled />
              </CFormGroup>
            </CCol>
          </CRow>
          <CRow>
            <CCol xs="4">
              <CFormGroup>
                <CLabel htmlFor="ccnumber">IBAN</CLabel>
                <CInput id="ccnumber" placeholder={bills.length > 0 ? bills[selectedBill].IBAN_recipient : ""} required disabled />
              </CFormGroup>
            </CCol>
            <CCol xs="4">
              <CFormGroup>
                <CLabel htmlFor="ccnumber">BIC Code</CLabel>
                <CInput id="ccnumber" placeholder={bills.length > 0 ? bills[selectedBill].BIC_bank_recipient : ""} required disabled />
              </CFormGroup>
            </CCol>
            <CCol xs="4">
              <CFormGroup>
                <CLabel htmlFor="ccnumber">Reference</CLabel>
                <CInput id="ccnumber" placeholder={bills.length > 0 ? bills[selectedBill].reference : ""} required disabled />
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
                <CInput type="number" id="name" value={bills.length > 0 ? bills[selectedBill].total : 0} required disabled />
              </CInputGroup>
            </CCol>
            <CCol xs="6">
              <CFormGroup>
                <CLabel htmlFor="name">Purpose</CLabel>
                <CInput id="name" value={bills.length > 0 ? bills[selectedBill].purpose : ""} required disabled />
              </CFormGroup>
            </CCol>
          </CRow>
        </CModalBody>
        <CModalFooter>
          <CButton color="primary" onClick={() =>     (function() {pay(bills[selectedBill].id); setModalActive(!showModal)})()    }>Pay</CButton>{' '}
          <CButton color="secondary" onClick={() => setModalActive(!showModal)}>Cancel</CButton>
        </CModalFooter>
      </CModal>
    </>
  )
}

export default UrgentBills
