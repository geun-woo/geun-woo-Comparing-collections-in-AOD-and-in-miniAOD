### HiForest Configuration
# Collisions: PbPb
# Type: Data
# Input: MiniAOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')

###############################################################################
# Input source
###############################################################################

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        "file:/cms/ldap_home/gekim/Data/MinBias/reMiniAOD_DATA_PAT_MB.root")
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

###############################################################################
# Define tree output
###############################################################################

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root")
    )

############################
# Event Analysis
############################

process.load('HeavyIonsAnalysis.MyAnalysis.packedPFCandAnalyzer_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')

#########################
# Main analysis list
#########################

process.ana_step = cms.Path(
    process.packedPFCandAnalyzer
)

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.MyAnalysis.hfCoincFilter_cff')
process.phfCoincFilter1Th3 = cms.Path(process.hfCoincFilterTh3)
process.phfCoincFilter2Th3 = cms.Path(process.hfCoincFilter2Th3)
process.phfCoincFilter3Th3 = cms.Path(process.hfCoincFilter3Th3)
process.phfCoincFilter4Th3 = cms.Path(process.hfCoincFilter4Th3)
process.phfCoincFilter5Th3 = cms.Path(process.hfCoincFilter5Th3)
process.phfCoincFilter1Th4 = cms.Path(process.hfCoincFilterTh4)
process.phfCoincFilter2Th4 = cms.Path(process.hfCoincFilter2Th4)
process.phfCoincFilter3Th4 = cms.Path(process.hfCoincFilter3Th4)
process.phfCoincFilter4Th4 = cms.Path(process.hfCoincFilter4Th4)
process.phfCoincFilter5Th4 = cms.Path(process.hfCoincFilter5Th4)
process.phfCoincFilter1Th5 = cms.Path(process.hfCoincFilterTh5)
process.phfCoincFilter4Th2 = cms.Path(process.hfCoincFilter4Th2)

process.pAna = cms.EndPath(process.skimanalysis)
