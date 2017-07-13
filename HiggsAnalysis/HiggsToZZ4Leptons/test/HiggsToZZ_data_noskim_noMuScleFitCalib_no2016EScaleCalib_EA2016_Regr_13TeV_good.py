
import FWCore.ParameterSet.Config as cms

process = cms.Process('MonoHiggs')

# Complete Preselection Sequence for 4l analysis

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/Geometry/GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration/EventContent/EventContent_cff')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016SeptRepro_v4', '')

process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",ignoreTotal = cms.untracked.int32(1) )

# Random generator
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    calibratedElectrons = cms.PSet(
        initialSeed = cms.untracked.uint32(1234567),
        engineName = cms.untracked.string('TRandom3')
    )
)

process.load('HiggsAnalysis.HiggsToZZ4Leptons.bunchSpacingProducer_cfi')
process.load('RecoMET.METFilters.metFilters_cff')
process.Path_BunchSpacingproducer=cms.Path(process.bunchSpacingProducer)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer * process.HBHENoiseFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer * process.HBHENoiseIsoFilter)
## process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)                                                               
## process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)                                           
## process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)      
## process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)   
## process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)                                                             
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
## process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter) 
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
## process.Flag_trackingFailureFilter = cms.Path(process.goodVertices + process.trackingFailureFilter)                                    
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
## process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)                                                               
## process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)                                                                           
## process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)                                 
## proces..Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)                                                                 
## and the sub-filters                                                                                                                    
# process.Flag_trkPOG_manystripclus53X = cms.Path(~manystripclus53X)                                                                      
# process.Flag_trkPOG_toomanystripclus53X = cms.Path(~toomanystripclus53X)                                                                
# process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~logErrorTooManyClusters)                     

process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
                                            src = cms.InputTag('offlinePrimaryVertices'),
					    cut = cms.string('!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2'),
                                            filter = cms.bool(True)
                                        )
        

process.load('HiggsAnalysis/HiggsToZZ4Leptons/hTozzTo4leptonsMuonCalibrator_cfi')
process.hTozzTo4leptonsMuonCalibrator.isData = cms.bool(True) 

process.load('EgammaAnalysis.ElectronTools.calibratedElectronsRun2_cfi')
process.calibratedElectrons.isMC = cms.bool(False)
process.calibratedElectrons.correctionFile = cms.string("EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_ichepV1_2016_ele")
process.calibratedElectrons.isSynchronization = cms.bool(True)

print("test1\n")

process.load('HiggsAnalysis/HiggsToZZ4Leptons/hTozzTo4leptonsPreselection_data_noskim_cff') 
process.hTozzTo4leptonsHLTInfo.TriggerResultsTag = cms.InputTag("TriggerResults","","HLT")
process.hTozzTo4leptonsCommonRootTreePresel.use2011EA = cms.untracked.bool(False)
process.hTozzTo4leptonsCommonRootTreePresel.triggerEvent  = cms.InputTag("hltTriggerSummaryAOD","","HLT")
process.hTozzTo4leptonsCommonRootTreePresel.fillPUinfo = cms.untracked.bool(False)
process.hTozzTo4leptonsCommonRootTreePresel.fillHLTinfo = cms.untracked.bool(False)                                           
process.hTozzTo4leptonsCommonRootTreePresel.triggerFilter = cms.string('hltL3fL1sMu16Eta2p1L1f0L2f16QL3Filtered40Q')
  #process.hTozzTo4leptonsCommonRootTreePresel.triggerFilterAsym = cms.vstring('hltDiMuonL3PreFiltered8','hltDiMuonL3p5PreFiltered8')
process.hTozzTo4leptonsCommonRootTreePresel.fillMCTruth  = cms.untracked.bool(False)    
process.hTozzTo4leptonsCommonRootTreePresel.isVBF  = cms.bool(False)

#process.genanalysis= cms.Sequence(
 # process.hTozzTo4leptonsGenSequence                  *
  #       process.hTozzTo4leptonsMCGenFilter2e2mu             *
  #       process.hTozzTo4leptonsMCGenParticleListDrawer2e2mu *
  #process.hTozzTo4leptonsMCDumper                     *                
  #process.hTozzTo4leptonsMCCP                         )

process.hTozzTo4leptonsSelectionPath = cms.Path(
  process.goodOfflinePrimaryVertices     *
  #process.genanalysis *
  process.hTozzTo4leptonsSelectionSequenceData *
  #process.hTozzTo4leptonsMatchingSequence *
  process.hTozzTo4leptonsCommonRootTreePresel
  )


#process.load('HiggsAnalysis/HiggsToZZ4Leptons/hTozzTo4leptonsOutputModule_cff')
#from HiggsAnalysis.HiggsToZZ4Leptons.hTozzTo4leptonsOutputModule_cff import *
#process.hTozzTo4leptonsSelectionOutputModuleNew = hTozzTo4leptonsSelectionOutputModule.clone()
#process.hTozzTo4leptonsSelectionOutputModuleNew.fileName = "hTozzToLeptons.root"


process.schedule = cms.Schedule( process.Path_BunchSpacingproducer,
                                 process.Flag_HBHENoiseFilter,
                                 process.Flag_HBHENoiseIsoFilter,
                                 process.Flag_globalTightHalo2016Filter,
                                 process.Flag_EcalDeadCellTriggerPrimitiveFilter,
                                 process.Flag_goodVertices,
                                 process.Flag_eeBadScFilter,
                                 process.Flag_BadPFMuonFilter,
                                 process.Flag_BadChargedCandidateFilter,
                                 process.hTozzTo4leptonsSelectionPath )


#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

print("test2\n")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
readFiles = cms.untracked.vstring(
#    'file:data/Run2016C/DoubleMuon/AOD/23Sep2016-v1/80001/6C3C996B-1F8C-E611-A4C6-0025905A6104.root'
'root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleMuon/AOD/23Sep2016-v1/70000/0202C03A-0F87-E611-82ED-FA163E1300D2.root'
#  'root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleMuon/AOD/18Apr2017_ver2-v1/100000/00041EEB-9839-E711-92CA-1866DAEA6CF0.root'
  )


process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)


## # Endpath
# process.o = cms.EndPath ( process.hTozzTo4leptonsSelectionOutputModuleNew )
