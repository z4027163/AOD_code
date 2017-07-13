
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
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_ICHEP16JEC_v0', '')

# Random generator
process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    calibratedElectrons = cms.PSet(
        initialSeed = cms.untracked.uint32(1),
        engineName = cms.untracked.string('TRandom3')
    )
)

#PFJet ID
process.load('HiggsAnalysis.HiggsToZZ4Leptons.hTozzTo4leptonsPFJetSelector_cfi')
process.hTozzTo4leptonsPFJetSelector.PFJetCollection = cms.InputTag("ak4PFJetsCHS")

#PFJet Energy Corrections
process.load('JetMETCorrections.Configuration.CorrectedJetProducersDefault_cff')
process.load('JetMETCorrections.Configuration.CorrectedJetProducers_cff')
process.load('JetMETCorrections.Configuration.CorrectedJetProducersAllAlgos_cff')

process.ak4PFJetsCorrection   = cms.EDProducer('CorrectedPFJetProducer',
    src         = cms.InputTag('hTozzTo4leptonsPFJetSelector'),    
    correctors  = cms.VInputTag('ak4PFCHSL1FastL2L3ResidualCorrector')    
)


process.ak4PFJetsCorrectionData   = cms.EDProducer('CorrectedPFJetProducer',
    src         = cms.InputTag('hTozzTo4leptonsPFJetSelector'),
    correctors  = cms.VInputTag('ak4PFCHSL1FastL2L3ResidualCorrector')
)

#process.load("JetMETCorrections.Type1MET.correctionTermsCaloMet_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType1Type2_cff")
process.corrPfMetType1.jetCorrLabel = cms.InputTag('ak4PFCHSL1FastL2L3ResidualCorrector')
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType0PFCandidate_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetType0RecoTrack_cff")
process.load("JetMETCorrections.Type1MET.correctionTermsPfMetShiftXY_cff")
#process.corrPfMetShiftXY.parameter = process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_mc
# process.corrPfMetShiftXY.parameter = process.pfMEtSysShiftCorrParameters_2012runABCDvsNvtx_data
##____________________________________________________________________________||
process.load("JetMETCorrections.Type1MET.correctedMet_cff")


process.hTozzTo4leptonsSelectionPath = cms.Path(
    process.hTozzTo4leptonsPFJetSelector +
    process.ak4PFCHSL1FastL2L3ResidualCorrectorChain            +
#    process.ak4PFCHSL1FastL2L3ResidualCorrectorChain    +
    process.ak4PFJetsCorrection +
#    process.ak4PFJetsCorrectionData +
    process.correctionTermsPfMetType1Type2 +
    process.correctionTermsPfMetType0RecoTrack +
    process.correctionTermsPfMetType0PFCandidate +
    process.correctionTermsPfMetShiftXY +
#    process.correctionTermsCaloMet +
#    process.caloMetT1 + 
#    process.caloMetT1T2 + 
    process.pfMetT0rt +
    process.pfMetT0rtT1 +
    process.pfMetT0pc +
    process.pfMetT0pcT1 +
    #process.pfMetT0rtTxy +
    #process.pfMetT0rtT1Txy +
    #process.pfMetT0pcTxy +
    #process.pfMetT0pcT1Txy +
#    process.correctionTermsPfMetType1Type2+
#    process.correctionTermsPfMetShiftXY +
#    process.correctionTermsCaloMet+
#    process.caloMetT1 + 
#    process.caloMetT1T2 + 
    process.pfMetT1 +
    process.pfMetT1T2 
    #process.pfMetT1Txy
)

#process.load("RecoMET/METProducers.METSignificance_cfi")
#process.load("RecoMET/METProducers.METSignificanceParams_cfi")
#process.METSignificance.srcLeptons = cms.VInputTag(
#       'gedGsfElectrons',
#       'muons',
#       'gedPhotons'
#       )
#process.METSignificance.srcPfJets            = cms.InputTag('ak4PFJets')
#process.METSignificance.srcMet               = cms.InputTag('pfMet')
#process.METSignificance.srcPFCandidates      = cms.InputTag('particleFlow')

#process.p = cms.Path(
#    process.correctionTermsPfMetType1Type2 +
#    process.correctionTermsPfMetType0RecoTrack +
#    process.correctionTermsPfMetType0PFCandidate +
#    process.correctionTermsPfMetShiftXY +
#    process.correctionTermsCaloMet +
#    process.caloMetT1 + 
#    process.caloMetT1T2 + 
#    process.pfMetT0rt +
#    process.pfMetT0rtT1 +
#    process.pfMetT0pc +
#    process.pfMetT0pcT1 +
#    process.pfMetT0rtTxy +
#    process.pfMetT0rtT1Txy +
#    process.pfMetT0pcTxy +
#    process.pfMetT0pcT1Txy +
#    process.pfMetT1 +
#    process.pfMetT1Txy
#)

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
readFiles = cms.untracked.vstring(
'file:/lustre/home/miniello/MonoHiggs_2016/CMSSW_8_0_13/src/HiggsAnalysis/HiggsToZZ4Leptons/test/Run2016B/DoubleMuon/AOD/PromptReco-v2/000/273/150/00000/3E460221-D919-E611-AE4F-02163E014142.root'
#'file:/lustre/cms/store/user/defilip/MonoHiggs/Syncr13TeV/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_76x_v1/crab_pickEvents/160309_201428/0000/pickevents_10.root',
#'file:/lustre/cms/store/user/defilip/MonoHiggs/Syncr13TeV/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8_76x_v1/crab_pickEvents/160309_201428/0000/pickevents_11.root',
  )

process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('run.root'),
 )

# Endpath
process.o = cms.EndPath ( process.output )
