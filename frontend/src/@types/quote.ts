export interface TLCStepLicenseName {
    tlc_number: string,
    tlc_name: string
}

export interface VINStepFHVInfo {
  vehicle_vin: string,
  vehicle_owner: string,
  license_plate: string,
  base_name: string,
  base_number: string,
  vehicle_year: number,
}

export interface VINStepInsuranceInfo {
  insurance_carrier_name: string,
  insurance_policy_number: string,
}

export interface QuestionsStep {
  tlc_license_years?: string,
  dmv_license_years?: string,
  driver_points_last_months?: string,
  fault_accidents_last_months?: string,
  defensive_driving_certificate?: boolean,
  accident_avoidance_system?: boolean
}


export interface QuoteProcessOptions {
  deposit?: number,
  deductible?: number,
  start_date?: string,
  quote_amount?: number
}

export interface QuoteProcessOptionsPayload {
  deposit: number,
  deductible?: number,
  start_date: string,
}

export interface QuoteProcessPayload extends TLCStepLicenseName, VINStepFHVInfo, VINStepInsuranceInfo, Required<QuestionsStep> {
  email: string
}

export type QuoteStatus = 'created' | 'docs' | 'review' | 'payment' | 'paid' | 'done'

export interface QuoteProcess extends QuoteProcessPayload, QuoteProcessOptions  {
  id: string,
  status: QuoteStatus
}

export interface QuoteSoftFallout {
  name: string,
  email: string,
  phone_number?: string
}

export interface QuoteProcessVariationPhysical {
  physical_total: number,
  physical_comprehensive: number,
  physical_collision: number,
}


interface BaseQuoteProcessVariations {
  liability_total: number
  body_injury: number
  property_damage: number
  personal_injury_protection: number
  aditional_personal_injury_protection: number
  uninsured_motorist: number
}

export interface QuoteProcessCalcVariations extends BaseQuoteProcessVariations{ 
  deductible: QuoteProcessVariationPhysical[]
}

export interface QuoteProcessDocumentsAccidentReport {
  id: string,
  accident_report?: string
}

export interface QuoteProcessDocuments {
  id: string,
  dmv_license_front_side: string,
  dmv_license_back_side: string,
  tlc_license_front_sid: string,
  tlc_license_back_side: string,
  proof_of_address: string,
  defensive_driving_certificat: string,
  is_submitted_for_review: boolean,
  is_broker_of_record_signed: boolean,
  requires_broker_of_record: boolean
  accident_reports: QuoteProcessDocumentsAccidentReport[],
  [key: string]: any
}