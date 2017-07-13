from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsernameFromSiteDB

config = config()
config.General.requestName = 'SingleMuon_Run2016B_AOD_v3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True



config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'HiggsToZZ_data_noskim_noMuScleFitCalib_no2016EScaleCalib_EA2016_Regr_13TeV_good.py'
config.JobType.outputFiles = ['roottree_leptons.root']

config.Data.inputDataset = '/SingleMuon/Run2016B-23Sep2016-v3/AOD'#'/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD'#'/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD'#'/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD'

config.JobType.allowUndistributedCMSSW = True

config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16//13TeV/Era/ReReco/Cert_272007-275376_13TeV_23Sep2016ReReco_Collisions16_JSON_eraB.txt'
#'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
#config.Data.lumiMask = 'crab_projects/crab_DoubleMuon_Run2016D-23Sep2016-v1/results/notFinishedLumis.json'
config.Data.inputDBS = 'global'
#config.Data.runRange = '273150-273500' #C#'275801-276283' #'275656-275800'# '275656-276283'
config.Data.ignoreLocality = False
config.Site.whitelist = ["T2_US*"]
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 2
config.Data.totalUnits = 4900
config.Data.outLFNDirBase = '/store/user/wangz/' # or '/store/group/<subdir>'
config.Data.publication = False
config.Data.outputDatasetTag = 'SingleMuon_Run2016B_AOD_v3'
#config.Data.outputPrimaryDataset = 'CRAB_UserFiles'
config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.blacklist = ['T3_US_Rutgers']
