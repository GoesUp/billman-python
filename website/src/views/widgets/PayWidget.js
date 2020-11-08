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

const PayWidget = (data) => {

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
  let naslovi = {
    "1": "slovenska 1",
    "2": "slovenska 1",
    "3": "slovenska 1",
    "4": "slovenska 1",
    "5": "slovenska 1",
    "6": "slovenska 1",
  }
  let menu = {};
  menu.value = 0;

  function pay(id) {
    fetch("http://localhost:5000/bill/pay?id_bill="+id+"&credits=True")
      .then((res) => {
        window.location.reload(false);
      })
  }

  return (
    <>
      <CRow>
        <CCol xs="6">
          <CFormGroup>
            <CLabel htmlFor="ccmonth">Recipient</CLabel>
            <CSelect custom name="ccmonth" id="recipient" ref={(input)=> menu = input}>
              <option value="1">Elektro Ljubljana</option>
              <option value="2">Petrol</option>
              <option value="3">FRI</option>
              <option value="4">Ilirija</option>
              <option value="5">Spar</option>
              <option value="6">T-2</option>
            </CSelect>
          </CFormGroup>
        </CCol>
        <CCol xs="6">
          <CFormGroup>
            <CLabel htmlFor="name">Recipient Address</CLabel>
            <CInput id="address" placeholder={naslovi[menu.value]} required disabled />
          </CFormGroup>
        </CCol>
      </CRow>
      <CRow>
        <CCol xs="4">
          <CFormGroup>
            <CLabel htmlFor="ccnumber">IBAN</CLabel>
            <CInput id="iban" required />
          </CFormGroup>
        </CCol>
        <CCol xs="4">
          <CFormGroup>
            <CLabel htmlFor="ccnumber">BIC Code</CLabel>
            <CInput id="bic" required />
          </CFormGroup>
        </CCol>
        <CCol xs="4">
          <CFormGroup>
            <CLabel htmlFor="ccnumber">Reference</CLabel>
            <CInput id="reference" required />
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
            <CInput type="number" id="amount" required />
          </CInputGroup>
        </CCol>
        <CCol xs="6">
          <CFormGroup>
            <CLabel htmlFor="name">Purpose</CLabel>
            <CInput id="purpose" required />
          </CFormGroup>
        </CCol>
      </CRow><br/>
      <CRow>
        <CCol>
          <CButton size="lg" block color="secondary" onClick={() => (function() {})()} disabled><CIcon name="cil-plus" alt="CC" /> Add
            &nbsp;&nbsp;<CBadge color="primary" shape="pill" style={{ position: 'static' }}>WIP</CBadge>
          </CButton>
        </CCol>
      </CRow>
    </>
  )
}

export default PayWidget
