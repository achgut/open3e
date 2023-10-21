"""
  Copyright 2023 abnoname

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

import Open3Ecodecs
from Open3Ecodecs import *

dataIdentifiersVx3 = {
    0x680: {
        "name": "EMCU", "tx": 0x680, "rx": 0x690,
        "dids":
        {
            256: O3EComplexType(36, "BusIdentification", [O3EInt8(1, "Busadresse"), O3EInt8(1, "Bustyp"),O3EInt8(1, "Geräteeigenschaft"),O3EInt8(1, "Gerätefunktion.Wert"), O3ESoftvers(8, "SW-Version"), O3ESoftvers(8, "HW-Version"),O3EUtf8(16, "VIN")]),
            257: RawCodec(122, "StatusDtcList"),
            258: RawCodec(122, "StatusDtcHistory"),
            259: RawCodec(122, "InfoDtcList"),
            260: RawCodec(122, "InfoDtcHistory"),
            261: RawCodec(122, "ServiceDtcList"),
            262: RawCodec(122, "ServiceDtcHistory"),
            263: RawCodec(122, "WarningDtcList"),
            264: RawCodec(124, "WarningDtcHistory"),
            265: RawCodec(122, "ErrorDtcList"),
            266: RawCodec(124, "ErrorDtcHistory"),
            377: O3EUtf8(16, "ViessmannIdentificationNumber"),
            378: RawCodec(4, "PointOfCommonCouplingPhaseOne"),
            379: RawCodec(4, "PointOfCommonCouplingPhaseTwo"),
            380: RawCodec(4, "PointOfCommonCouplingPhaseThree"),
            382: RawCodec(5, "UnitsAndFormats"),
            449: RawCodec(141, "ElectricalEnergyMatrix"),
            451: RawCodec(4, "ExternalAlternatingCurrentPowerSetpoint"),
            505: O3ESdate(3, "Date"),
            506: O3EStime(3, "Time"),
            507: RawCodec(4, "UniversalTimeCoordinated"),
            508: RawCodec(1, "UniversalTimeCoordinatedOffset"),
            510: RawCodec(1, "Language"),
            535: RawCodec(12, "ObjectElectricalEnergyStatistical"),
            569: RawCodec(1, "ResetSensorMinMaxAverageStatistics"),
            570: RawCodec(1, "ResetStatistics"),
            572: RawCodec(3, "SetDefaultValuesDate"),
            573: RawCodec(2, "RemoteReset"),
            576: RawCodec(3, "SetDeliveryStatusDate"),
            580: RawCodec(8, "SoftwareVersion"),
            581: RawCodec(8, "HardwareVersion"),
            592: RawCodec(6, "MacAddressLan"),
            593: RawCodec(6, "GatewayMac"),
            602: RawCodec(1, "GatewayRemoteLocalNetworkStatus"),
            603: RawCodec(1, "GatewayApEnable"),
            604: O3EComplexType(76, "GatewayApDataSet", [O3EUtf8(32, "SSID Access Point"), O3EUtf8(40, "Passwort Access Point"),O3EIp4addr(4, "IP-Adresse Access Point")]),
            607: O3EComplexType(20, "GatewayRemoteIp", [O3EIp4addr(4, "WLAN IP"), O3EIp4addr(4, "Subnetzmaske"),O3EIp4addr(4, "Gateway IP"),O3EIp4addr(4, "DNS Server 1 "),O3EIp4addr(4, "DNS Server 2 ")]),
            609: RawCodec(40, "ProxyServer"),
            610: RawCodec(2, "ProxyPort"),
            611: RawCodec(40, "ProxyUser"),
            613: RawCodec(1, "ProxyEnabled"),
            616: RawCodec(1, "GatewayRemoteEnable"),
            618: RawCodec(1, "GatewayRemoteIpStatic"),
            619: RawCodec(2, "GatewayRemoteScanNetwork"),
            623: O3EComplexType(181, "ServiceEngineer", [O3EUtf8(20, "Name"),O3EUtf8(15, "Vorname"),O3EUtf8(20, "Strasse"),O3EUtf8(10, "Strasse Zusatz"),O3EUtf8(7, "PLZ"),O3EUtf8(15, "Region"),O3EUtf8(15, "Stadt"),O3EUtf8(16, "Telefon"),O3EUtf8(16, "Mobil"),O3EUtf8(20, "Email"),O3EUtf8(1, "Land"),O3EUtf8(15, "Eindeutige Identifikationsnummer")]), #Länge Email und Identnummer nicht testbar ggf. ändern
            624: O3EComplexType(181, "TechnicalSupport", [O3EUtf8(20, "Name"),O3EUtf8(15, "Vorname"),O3EUtf8(20, "Strasse"),O3EUtf8(10, "Strasse Zusatz"),O3EUtf8(7, "PLZ"),O3EUtf8(15, "Region"),O3EUtf8(15, "Stadt"),O3EUtf8(16, "Telefon"),O3EUtf8(16, "Mobil"),O3EUtf8(20, "Email"),O3EUtf8(1, "Land"),O3EUtf8(15, "Eindeutige Identifikationsnummer")]), #Länge Email und Identnummer nicht testbar ggf. ändern
            680: RawCodec(123, "EnergyMeter"),
            900: RawCodec(1, "GatewayRemoteSignalStrength"),
            902: RawCodec(1, "MalfunctionIdentification"),
            903: RawCodec(4, "DisplaySettings"),
            912: RawCodec(5, "DaylightSavingTimeActive"),
            918: RawCodec(1, "TradeFairMode"),
            921: RawCodec(2, "ExternalAccessInProgress"),
            924: RawCodec(1, "StartUpWizard"),
            928: O3EUtf8(16, "ElectronicTraceabilityNumber"),
            954: O3EComplexType(181, "BusTopologyMatrix", [O3EInt8(1, "Count Geräte"),O3EInt8(1, "Busadresse1"),O3EInt8(1, "Bustyp1"),O3EInt8(1, "Geräteeigenschaft1"),O3EInt8(1, "Gerätefunktion.Wert1"),O3ESoftvers(8, "SW-Version1"), O3ESoftvers(8, "HW-Version1"),O3EUtf8(16, "VIN1"), O3EInt8(1, "Busadresse2"),O3EInt8(1, "Bustyp2"),O3EInt8(1, "Geräteeigenschaft2"),O3EInt8(1, "Gerätefunktion.Wert2"),O3ESoftvers(8, "SW-Version2"), O3ESoftvers(8, "HW-Version2"),O3EUtf8(16, "VIN2"),O3EInt8(1, "Busadresse3"),O3EInt8(1, "Bustyp3"),O3EInt8(1, "Geräteeigenschaft3"),O3EInt8(1, "Gerätefunktion.Wert3"),O3ESoftvers(8, "SW-Version3"), O3ESoftvers(8, "HW-Version3"),O3EUtf8(16, "VIN3"),O3EInt8(1, "Busadresse4"),O3EInt8(1, "Bustyp4"),O3EInt8(1, "Geräteeigenschaft4"),O3EInt8(1, "Gerätefunktion.Wert4"),O3ESoftvers(8, "SW-Version4"), O3ESoftvers(8, "HW-Version4"),O3EUtf8(16, "VIN4"),O3EInt8(1, "Busadresse5"),O3EInt8(1, "Bustyp5"),O3EInt8(1, "Geräteeigenschaft5"),O3EInt8(1, "Gerätefunktion.Wert5"),O3ESoftvers(8, "SW-Version5"), O3ESoftvers(8, "HW-Version5"),O3EUtf8(16, "VIN5")]),
            961: RawCodec(2, "SecurityAlgorithmNumber"),
            962: RawCodec(8, "BootLoaderVersion"),
            964: RawCodec(1, "ActiveDiagnosticSession"),
            1132: O3EComplexType(97, "ViessmannIdentificationNumberListInternal", [O3EInt8(1, "Count"), O3EUtf8(16, "VIN1"), O3EUtf8(16, "VIN2"), O3EUtf8(16, "VIN3"), O3EUtf8(16, "VIN4"), O3EUtf8(16, "VIN5"), O3EUtf8(16, "VIN6")]),
            1138: RawCodec(1, "AccentLedBar"),
            1165: RawCodec(1, "BackendConnectionStatus"),
            1166: RawCodec(5, "ResetDtcHistory"),
            1175: RawCodec(1, "AcknowledgeInfoAlarmMessage"),
            1176: RawCodec(1, "AcknowledgeWarningAlarmMessage"),
            1177: RawCodec(1, "AcknowledgeServiceAlarmMessage"),
            1178: RawCodec(1, "AcknowledgeErrorAlarmMessage"),
            1233: RawCodec(68, "GatewayRemoteVisibleOneTwo"),
            1234: RawCodec(68, "GatewayRemoteVisibleThreeFour"),
            1235: RawCodec(68, "GatewayRemoteVisibleFiveSix"),
            1236: RawCodec(68, "GatewayRemoteVisibleSevenEight"),
            1237: RawCodec(68, "GatewayRemoteVisibleNineTen"),
            1286: O3EComplexType(181, "BusTopologyMatrixTwo", [O3EInt8(1, "Count Geräte"),O3EInt8(1, "Busadresse1"),O3EInt8(1, "Bustyp1"),O3EInt8(1, "Geräteeigenschaft1"),O3EInt8(1, "Gerätefunktion.Wert1"),O3ESoftvers(8, "SW-Version1"), O3ESoftvers(8, "HW-Version1"),O3EUtf8(16, "VIN1"), O3EInt8(1, "Busadresse2"),O3EInt8(1, "Bustyp2"),O3EInt8(1, "Geräteeigenschaft2"),O3EInt8(1, "Gerätefunktion.Wert2"),O3ESoftvers(8, "SW-Version2"), O3ESoftvers(8, "HW-Version2"),O3EUtf8(16, "VIN2"),O3EInt8(1, "Busadresse3"),O3EInt8(1, "Bustyp3"),O3EInt8(1, "Geräteeigenschaft3"),O3EInt8(1, "Gerätefunktion.Wert3"),O3ESoftvers(8, "SW-Version3"), O3ESoftvers(8, "HW-Version3"),O3EUtf8(16, "VIN3"),O3EInt8(1, "Busadresse4"),O3EInt8(1, "Bustyp4"),O3EInt8(1, "Geräteeigenschaft4"),O3EInt8(1, "Gerätefunktion.Wert4"),O3ESoftvers(8, "SW-Version4"), O3ESoftvers(8, "HW-Version4"),O3EUtf8(16, "VIN4"),O3EInt8(1, "Busadresse5"),O3EInt8(1, "Bustyp5"),O3EInt8(1, "Geräteeigenschaft5"),O3EInt8(1, "Gerätefunktion.Wert5"),O3ESoftvers(8, "SW-Version5"), O3ESoftvers(8, "HW-Version5"),O3EUtf8(16, "VIN5")]),
            1287: O3EComplexType(181, "BusTopologyMatrixThree", [O3EInt8(1, "Count Geräte"),O3EInt8(1, "Busadresse1"),O3EInt8(1, "Bustyp1"),O3EInt8(1, "Geräteeigenschaft1"),O3EInt8(1, "Gerätefunktion.Wert1"),O3ESoftvers(8, "SW-Version1"), O3ESoftvers(8, "HW-Version1"),O3EUtf8(16, "VIN1"), O3EInt8(1, "Busadresse2"),O3EInt8(1, "Bustyp2"),O3EInt8(1, "Geräteeigenschaft2"),O3EInt8(1, "Gerätefunktion.Wert2"),O3ESoftvers(8, "SW-Version2"), O3ESoftvers(8, "HW-Version2"),O3EUtf8(16, "VIN2"),O3EInt8(1, "Busadresse3"),O3EInt8(1, "Bustyp3"),O3EInt8(1, "Geräteeigenschaft3"),O3EInt8(1, "Gerätefunktion.Wert3"),O3ESoftvers(8, "SW-Version3"), O3ESoftvers(8, "HW-Version3"),O3EUtf8(16, "VIN3"),O3EInt8(1, "Busadresse4"),O3EInt8(1, "Bustyp4"),O3EInt8(1, "Geräteeigenschaft4"),O3EInt8(1, "Gerätefunktion.Wert4"),O3ESoftvers(8, "SW-Version4"), O3ESoftvers(8, "HW-Version4"),O3EUtf8(16, "VIN4"),O3EInt8(1, "Busadresse5"),O3EInt8(1, "Bustyp5"),O3EInt8(1, "Geräteeigenschaft5"),O3EInt8(1, "Gerätefunktion.Wert5"),O3ESoftvers(8, "SW-Version5"), O3ESoftvers(8, "HW-Version5"),O3EUtf8(16, "VIN5")]),
            1288: O3EComplexType(181, "BusTopologyMatrixFour", [O3EInt8(1, "Count Geräte"),O3EInt8(1, "Busadresse1"),O3EInt8(1, "Bustyp1"),O3EInt8(1, "Geräteeigenschaft1"),O3EInt8(1, "Gerätefunktion.Wert1"),O3ESoftvers(8, "SW-Version1"), O3ESoftvers(8, "HW-Version1"),O3EUtf8(16, "VIN1"), O3EInt8(1, "Busadresse2"),O3EInt8(1, "Bustyp2"),O3EInt8(1, "Geräteeigenschaft2"),O3EInt8(1, "Gerätefunktion.Wert2"),O3ESoftvers(8, "SW-Version2"), O3ESoftvers(8, "HW-Version2"),O3EUtf8(16, "VIN2"),O3EInt8(1, "Busadresse3"),O3EInt8(1, "Bustyp3"),O3EInt8(1, "Geräteeigenschaft3"),O3EInt8(1, "Gerätefunktion.Wert3"),O3ESoftvers(8, "SW-Version3"), O3ESoftvers(8, "HW-Version3"),O3EUtf8(16, "VIN3"),O3EInt8(1, "Busadresse4"),O3EInt8(1, "Bustyp4"),O3EInt8(1, "Geräteeigenschaft4"),O3EInt8(1, "Gerätefunktion.Wert4"),O3ESoftvers(8, "SW-Version4"), O3ESoftvers(8, "HW-Version4"),O3EUtf8(16, "VIN4"),O3EInt8(1, "Busadresse5"),O3EInt8(1, "Bustyp5"),O3EInt8(1, "Geräteeigenschaft5"),O3EInt8(1, "Gerätefunktion.Wert5"),O3ESoftvers(8, "SW-Version5"), O3ESoftvers(8, "HW-Version5"),O3EUtf8(16, "VIN5")]),
            1289: O3EComplexType(181, "BusTopologyMatrixFive", [O3EInt8(1, "Count Geräte"),O3EInt8(1, "Busadresse1"),O3EInt8(1, "Bustyp1"),O3EInt8(1, "Geräteeigenschaft1"),O3EInt8(1, "Gerätefunktion.Wert1"),O3ESoftvers(8, "SW-Version1"), O3ESoftvers(8, "HW-Version1"),O3EUtf8(16, "VIN1"), O3EInt8(1, "Busadresse2"),O3EInt8(1, "Bustyp2"),O3EInt8(1, "Geräteeigenschaft2"),O3EInt8(1, "Gerätefunktion.Wert2"),O3ESoftvers(8, "SW-Version2"), O3ESoftvers(8, "HW-Version2"),O3EUtf8(16, "VIN2"),O3EInt8(1, "Busadresse3"),O3EInt8(1, "Bustyp3"),O3EInt8(1, "Geräteeigenschaft3"),O3EInt8(1, "Gerätefunktion.Wert3"),O3ESoftvers(8, "SW-Version3"), O3ESoftvers(8, "HW-Version3"),O3EUtf8(16, "VIN3"),O3EInt8(1, "Busadresse4"),O3EInt8(1, "Bustyp4"),O3EInt8(1, "Geräteeigenschaft4"),O3EInt8(1, "Gerätefunktion.Wert4"),O3ESoftvers(8, "SW-Version4"), O3ESoftvers(8, "HW-Version4"),O3EUtf8(16, "VIN4"),O3EInt8(1, "Busadresse5"),O3EInt8(1, "Bustyp5"),O3EInt8(1, "Geräteeigenschaft5"),O3EInt8(1, "Gerätefunktion.Wert5"),O3ESoftvers(8, "SW-Version5"), O3ESoftvers(8, "HW-Version5"),O3EUtf8(16, "VIN5")]),
            1467: RawCodec(2, "SafetyRelevantRemoteUnlock"),
            1494: RawCodec(8, "OemProductVersion"),
            1504: RawCodec(1, "TimeSettingSource"),
            1533: RawCodec(2, "InstallationWizardInProgress"),
            1538: RawCodec(1, "ZigbeeEnable"),
            1539: RawCodec(1, "ZigbeeStatus"),
            1540: RawCodec(26, "ZigbeeIdentification"),
            1552: RawCodec(7, "ElectricalEnergyStorageOperationState"),
            1553: RawCodec(6, "ElectronicControlUnitOdxVersion"),
            1577: RawCodec(139, "ElectricalEnergyStorageModuleOneOperatingData"),
            1578: RawCodec(139, "ElectricalEnergyStorageModuleTwoOperatingData"),
            1579: RawCodec(139, "ElectricalEnergyStorageModuleThreeOperatingData"),
            1580: RawCodec(139, "ElectricalEnergyStorageModuleFourOperatingData"),
            1581: RawCodec(139, "ElectricalEnergyStorageModuleFiveOperatingData"),
            1582: RawCodec(139, "ElectricalEnergyStorageModuleSixOperatingData"),
            1587: RawCodec(4, "ExternalAlternatingCurrentPowerSetpointMetaData"),
            1588: RawCodec(4, "AlternatingCurrentPowerSetpoint"),
            1589: RawCodec(4, "AlternatingCurrentPowerSetpointMetaData"),
            1590: RawCodec(6, "ElectricalEnergySystemOperationState"),
            1591: RawCodec(6, "ElectricalEnergyInverterOperationState"),
            1592: RawCodec(1, "ElectricalEnergyInverterPath"),
            1603: RawCodec(4, "PointOfCommonCouplingPower"),
            1607: RawCodec(1, "MalfunctionUnitBlocked"),
            1660: RawCodec(16, "SupportedFeatures"),
            1664: O3EInt8(1, "ElectricalEnergyStorageStateOfCharge"),
            1684: RawCodec(9, "AmbientTemperatureSensor"),
            1685: RawCodec(3, "ElectricalEnergyInverterDCConfiguration"),
            1686: RawCodec(3, "ElectricalEnergySystemPhotovoltaicLimitation"),
            1687: O3EInt16(2, "ElectricalEnergySystemPhotovoltaicConfiguration", scale=10),
            1690: RawCodec(17, "ElectricalEnergySystemPhotovoltaicStatus"),
            1691: RawCodec(1, "BusTopologyScanStatus"),
            1692: RawCodec(1, "PowerGridCodeConfiguration"),
            1693: RawCodec(1, "GridOperatorConfigurationLock"),
            1694: RawCodec(1, "GatewayEthernetEnable"),
            1695: RawCodec(21, "GatewayEthernetConfig"),
            1696: RawCodec(20, "GatewayEthernetIp"),
            1697: RawCodec(1, "GatewayEthernetNetworkStatus"),
            1698: RawCodec(16, "SupportedFeaturesTelemetryControlUnit"),
            1699: RawCodec(16, "ActivatedFeaturesTelemetryControlUnit"),
            1700: RawCodec(104, "EebusDeviceList"),
            1701: RawCodec(104, "EebusOwnInfo"),
            1702: RawCodec(104, "EebusPartnerInfo"),
            1703: RawCodec(1, "EebusConnectionStatus"),
            1710: RawCodec(8, "FunctionalSoftwareVersion"),
            1718: O3EComplexType(2, "ElectricalEnergySystemConfiguration", [O3EInt8(1, "Netzbetriebsart"), O3EInt8(1, "Elektrische Anlagenkomponenten")]),
            1801: O3EComplexType(40, "ElectricalEnergyStorageEnergyTransferStatistic", [O3EInt32(4, "BatteryChargeToday", scale=1.0), O3EInt32(4, "BatteryChargeWeek", scale=1.0), O3EInt32(4, "BatteryChargeMonth", scale=1.0), O3EInt32(4, "BatteryChargeYear", scale=1.0), O3EInt32(4, "BatteryChargeTotal", scale=1.0), O3EInt32(4, "BatteryDischargeToday", scale=1.0), O3EInt32(4, "BatteryDischargeWeek", scale=1.0), O3EInt32(4, "BatteryDischargeMonth", scale=1.0), O3EInt32(4, "BatteryDischargeYear", scale=1.0), O3EInt32(4, "BatteryDischargeTotal", scale=1.0)]),
            1802: O3EComplexType(80, "EnergyProductionPhotovoltaic", [O3EInt32(4, "PhotovoltaicProductionToday"), O3EInt32(4, "PhotovoltaicProductionWeek"), O3EInt32(4, "PhotovoltaicProductionMonth"), O3EInt32(4, "PhotovoltaicProductionYear"), O3EInt32(4, "PhotovoltaicProductionTotal"), RawCodec(60, "Uninterpreted")]),
            1807: RawCodec(10, "ElectricalEnergyInverterDcInputOne"),
            1808: RawCodec(10, "ElectricalEnergyInverterDcInputTwo"),
            1809: RawCodec(10, "ElectricalEnergyInverterDcInputThree"),
            1810: O3EInt16(4, "ElectricalEnergyInverterPowerAc", scale=1.0),
            1811: RawCodec(1, "ElectricalEnergyStorageModuleSetUpCheck"),
            1812: RawCodec(2, "PointOfCommonCouplingConfiguredEnergyMeter"),
            1822: RawCodec(51, "ThreePhaseInverterCurrent"),
            1823: RawCodec(27, "ThreePhaseInverterVoltage"),
            1824: O3EComplexType(16, "ThreePhaseInverterCurrentPower", [O3EInt32(string_len=4, idStr="cumulated", scale=1), O3EInt32(string_len=4, idStr="L1", scale=1), O3EInt32(string_len=4, idStr="L2", scale=1), O3EInt32(string_len=4, idStr="L3", scale=1)]),
            1825: O3EComplexType(16, "ThreePhaseInverterCurrentApparentPower", [O3EInt32(string_len=4, idStr="cumulated", scale=1), O3EInt32(string_len=4, idStr="L1", scale=1), O3EInt32(string_len=4, idStr="L2", scale=1), O3EInt32(string_len=4, idStr="L3", scale=1)]),
            1826: O3EInt16(4, "ThreePhaseInverterMaximunNominalPower", scale=1.0),
            1827: O3EInt16(4, "InverterElectricalEnergyStorageMaximumNominalChargePower", scale=1.0),
            1828: O3EInt16(4, "InverterElectricalEnergyStorageCurrentMaximumlChargePower", scale=1.0),
            1829: O3EInt16(4, "InverterElectricalEnergyStorageMaximumNominalDischargePower", scale=1.0),
            1830: O3EInt16(4, "InverterElectricalEnergyStorageCurrentMaximumlDishargePower", scale=1.0),
            1831: O3EComplexType(12, "PhotovoltaicCurrentStringPower", [O3EInt32(4, "String1", scale=1.0), O3EInt32(4, "String2", scale=1.0), O3EInt32(4, "String3", scale=1.0)]),
            1832: O3EComplexType(12, "PhotovoltaicStringCurrent", [O3EInt32(4, "String1", scale=1.0), O3EInt32(4, "String2", scale=1.0), O3EInt32(4, "String3", scale=1.0)]),
            1833: O3EComplexType(12, "PhotovoltaicStringVoltage", [O3EInt32(4, "String1", scale=1000.0), O3EInt32(4, "String2", scale=1000.0), O3EInt32(4, "String3", scale=1000.0)]),
            1834: O3EInt8(4, "ElectricalEnergyStorageStateOfEnergy"),
            1835: RawCodec(20, "ManufacturerProperties"),
            1836: O3EInt32(4, "ElectricalEnergyStorageCurrentPower", scale=1.0, signed=True),
            1837: O3EInt16(4, "ElectricalEnergyStorageCurrent", scale=1.0),
            1838: O3EInt8(2, "ElectricalEnergyStorageVoltage"),
            1839: RawCodec(4, "ElectricalEnergyStorageUsableEnergy"),
            1840: RawCodec(4, "ElectricalEnergyStorageUsableNominalEnergy"),
            1841: RawCodec(32, "PointOfCommonCouplingOverview"),
            2144: RawCodec(16, "PointOfCommonCouplingAcActiveCurrent"),
            2184: RawCodec(2, "BackupBoxTest"),
            2188: RawCodec(6, "PointOfCommonCouplingSetActivePowerTotal"),
            2189: RawCodec(104, "EebusDeviceListTwo"),
            2190: RawCodec(104, "EebusDeviceListThree"),
            2191: RawCodec(104, "EebusDeviceListFour"),
            2192: RawCodec(104, "EebusDeviceListFive"),
            2214: RawCodec(2, "BackupBoxConfiguration"),
            2217: RawCodec(1, "InputDemandSideManagementlReceiver"),
            2218: RawCodec(4, "RemoteLimitValueDemandSideManagement"),
            2219: RawCodec(1, "BatteryCalibration"),
            2220: RawCodec(1, "BatteryReactivePowerMode"),
            2221: RawCodec(3, "BatteryReactivePowerFixCosinusPhi"),
            2222: RawCodec(18, "BatteryReactivePower"),
            2223: RawCodec(15, "BatteryReactivePowerCosinusPhi"),
            2224: RawCodec(16, "PhotovoltaicsActivePowerLimitation"),
            2225: RawCodec(12, "ElectricEnergyStorageSetpoint"),
            2226: RawCodec(12, "ElectricEnergyStorageMaximum"),
            2234: RawCodec(27, "PowerGridCodeSettingsNormOne"),
            2239: RawCodec(1, "ElectricEnergyStorageControlMode"),
            2240: RawCodec(9, "BatteryTemperatureSensor"),
            2242: RawCodec(27, "PowerGridCodeSettingsNormTwo"),
            2244: RawCodec(27, "PowerGridCodeSettingsNormFour"),
            2246: RawCodec(26, "FixReactivePowerIn"),
            2254: RawCodec(1, "PowerGridCodeSettingConfiguration"),
            2329: RawCodec(14, "BatteryEnergyUsedAverage"),
            2348: RawCodec(8, "PhotovoltaicsActivePowerLimitationEnergyManagementSystem"),
            2349: RawCodec(8, "PhotovoltaicsActivePowerLimitationFallbackEnergyManagementSystem"),
            2533: RawCodec(27, "PowerGridCodeSettingsNormSix"),
            2539: RawCodec(40, "AlternatingCurrentEnergyStatistic"),
            2593: RawCodec(181, "ProductMatrix"),
            2610: RawCodec(1, "SetDeliveryStateExpert"),
            2638: RawCodec(4, "SupportedCountryCodes"),
            2643: RawCodec(2, "MaximumRechargePower"),
            2776: RawCodec(181, "ProductMatrixTwo"),
            2777: RawCodec(8, "Reuse"),
            2802: RawCodec(6, "InverterSelfTestStatus"),
            2804: RawCodec(151, "InverterSelfTestResultTwo"),
            2805: RawCodec(151, "InverterSelfTestResultThree"),
            2829: RawCodec(20, "ProductIdentification"),
            2849: RawCodec(27, "CrankCaseHeaterOnTimer"),
            2936: RawCodec(3, "ElectricalEnergyStorageSystemState"),
            2942: RawCodec(137, "ListOfLayerSettingServiceDevices"),
            2944: RawCodec(1, "NodeIdOnExternalCan"),
            2945: RawCodec(1, "PointOfCommonCouplingEnergyMeterConnectedPhases"),
            2947: RawCodec(5, "SleepModePrevention"),
            2952: RawCodec(137, "ListOfLayerSettingServiceDevicesTwo"),
            2969: RawCodec(1, "ElectronicControlUnitSafeStateStatus"),
            3085: RawCodec(18, "ElectricalEnergyStorageModuleOneInformation"),
            3086: RawCodec(18, "ElectricalEnergyStorageModuleTwoInformation"),
            3087: RawCodec(18, "ElectricalEnergyStorageModuleThreeInformation"),
            3088: RawCodec(18, "ElectricalEnergyStorageModuleFourInformation"),
            3089: RawCodec(18, "ElectricalEnergyStorageModuleFiveInformation"),
            3090: RawCodec(18, "ElectricalEnergyStorageModuleSixInformation"),
            3103: RawCodec(6, "IslandModeLoadInformation"),
            3107: RawCodec(7, "BatteryModuleExchangeAssistent"),
            3108: RawCodec(9, "PhotovoltaicsActivePowerLimitationRampRate"),
        }
    }
}
