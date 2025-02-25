import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu4PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu4PFJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPu4PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak4HiSignalGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPu4PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu4PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akPu4PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPu4PFJets"),
    payload = "AKPu4PF_offline"
    )

akPu4PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPu4CaloJets'))

# akPu4PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak4HiSignalGenJets'))

akPu4PFbTagger = bTaggers(
    "akPu4PF",
    0.4)

# create objects locally since they dont load properly otherwise
akPu4PFPatJetFlavourAssociationLegacy = akPu4PFbTagger.PatJetFlavourAssociationLegacy
akPu4PFPatJetPartons = akPu4PFbTagger.PatJetPartons
akPu4PFJetTracksAssociatorAtVertex = akPu4PFbTagger.JetTracksAssociatorAtVertex
akPu4PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu4PFSimpleSecondaryVertexHighEffBJetTags = akPu4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu4PFSimpleSecondaryVertexHighPurBJetTags = akPu4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu4PFCombinedSecondaryVertexBJetTags = akPu4PFbTagger.CombinedSecondaryVertexBJetTags
akPu4PFCombinedSecondaryVertexV2BJetTags = akPu4PFbTagger.CombinedSecondaryVertexV2BJetTags
akPu4PFJetBProbabilityBJetTags = akPu4PFbTagger.JetBProbabilityBJetTags
akPu4PFSoftPFMuonByPtBJetTags = akPu4PFbTagger.SoftPFMuonByPtBJetTags
akPu4PFSoftPFMuonByIP3dBJetTags = akPu4PFbTagger.SoftPFMuonByIP3dBJetTags
akPu4PFTrackCountingHighEffBJetTags = akPu4PFbTagger.TrackCountingHighEffBJetTags
akPu4PFTrackCountingHighPurBJetTags = akPu4PFbTagger.TrackCountingHighPurBJetTags
akPu4PFPatJetPartonAssociationLegacy = akPu4PFbTagger.PatJetPartonAssociationLegacy
akPu4PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akPu4PFImpactParameterTagInfos = akPu4PFbTagger.ImpactParameterTagInfos
akPu4PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu4PFJetProbabilityBJetTags = akPu4PFbTagger.JetProbabilityBJetTags

akPu4PFSecondaryVertexTagInfos = akPu4PFbTagger.SecondaryVertexTagInfos
akPu4PFSimpleSecondaryVertexHighEffBJetTags = akPu4PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu4PFSimpleSecondaryVertexHighPurBJetTags = akPu4PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu4PFCombinedSecondaryVertexBJetTags = akPu4PFbTagger.CombinedSecondaryVertexBJetTags
akPu4PFCombinedSecondaryVertexV2BJetTags = akPu4PFbTagger.CombinedSecondaryVertexV2BJetTags

akPu4PFSecondaryVertexNegativeTagInfos = akPu4PFbTagger.SecondaryVertexNegativeTagInfos
akPu4PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPu4PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu4PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPu4PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu4PFNegativeCombinedSecondaryVertexBJetTags = akPu4PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPu4PFPositiveCombinedSecondaryVertexBJetTags = akPu4PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPu4PFNegativeCombinedSecondaryVertexV2BJetTags = akPu4PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu4PFPositiveCombinedSecondaryVertexV2BJetTags = akPu4PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu4PFSoftPFMuonsTagInfos = akPu4PFbTagger.SoftPFMuonsTagInfos
akPu4PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu4PFSoftPFMuonBJetTags = akPu4PFbTagger.SoftPFMuonBJetTags
akPu4PFSoftPFMuonByIP3dBJetTags = akPu4PFbTagger.SoftPFMuonByIP3dBJetTags
akPu4PFSoftPFMuonByPtBJetTags = akPu4PFbTagger.SoftPFMuonByPtBJetTags
akPu4PFNegativeSoftPFMuonByPtBJetTags = akPu4PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPu4PFPositiveSoftPFMuonByPtBJetTags = akPu4PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPu4PFPatJetFlavourIdLegacy = cms.Sequence(akPu4PFPatJetPartonAssociationLegacy*akPu4PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPu4PFPatJetFlavourAssociation = akPu4PFbTagger.PatJetFlavourAssociation
# akPu4PFPatJetFlavourId = cms.Sequence(akPu4PFPatJetPartons*akPu4PFPatJetFlavourAssociation)

akPu4PFJetBtaggingIP = cms.Sequence(
    akPu4PFImpactParameterTagInfos *
    akPu4PFTrackCountingHighEffBJetTags +
    akPu4PFTrackCountingHighPurBJetTags +
    akPu4PFJetProbabilityBJetTags +
    akPu4PFJetBProbabilityBJetTags
    )

akPu4PFJetBtaggingSV = cms.Sequence(
    akPu4PFImpactParameterTagInfos *
    akPu4PFSecondaryVertexTagInfos *
    akPu4PFSimpleSecondaryVertexHighEffBJetTags +
    akPu4PFSimpleSecondaryVertexHighPurBJetTags +
    akPu4PFCombinedSecondaryVertexBJetTags +
    akPu4PFCombinedSecondaryVertexV2BJetTags
    )

akPu4PFJetBtaggingNegSV = cms.Sequence(
    akPu4PFImpactParameterTagInfos *
    akPu4PFSecondaryVertexNegativeTagInfos *
    akPu4PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPu4PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPu4PFNegativeCombinedSecondaryVertexBJetTags +
    akPu4PFPositiveCombinedSecondaryVertexBJetTags +
    akPu4PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPu4PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPu4PFJetBtaggingMu = cms.Sequence(
    akPu4PFSoftPFMuonsTagInfos *
    akPu4PFSoftPFMuonBJetTags +
    akPu4PFSoftPFMuonByIP3dBJetTags +
    akPu4PFSoftPFMuonByPtBJetTags +
    akPu4PFNegativeSoftPFMuonByPtBJetTags +
    akPu4PFPositiveSoftPFMuonByPtBJetTags
    )

akPu4PFJetBtagging = cms.Sequence(
    akPu4PFJetBtaggingIP
    * akPu4PFJetBtaggingSV
    # * akPu4PFJetBtaggingNegSV
    # * akPu4PFJetBtaggingMu
    )

akPu4PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPu4PFJets"),
    genJetMatch            = cms.InputTag("akPu4PFmatch"),
    genPartonMatch         = cms.InputTag("akPu4PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPu4PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPu4PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPu4PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPu4PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPu4PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPu4PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPu4PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPu4PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPu4PFJetBProbabilityBJetTags"),
        cms.InputTag("akPu4PFJetProbabilityBJetTags"),
        # cms.InputTag("akPu4PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPu4PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPu4PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPu4PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"),cms.InputTag("akPu4PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPu4PFJetID"),
    addBTagInfo = True,
    addTagInfos = True,
    addDiscriminators = True,
    addAssociatedTracks = True,
    addJetCharge = False,
    addJetID = False,
    getJetMCFlavour = True,
    addGenPartonMatch = True,
    addGenJetMatch = True,
    embedGenJetMatch = True,
    embedGenPartonMatch = True,
    # embedCaloTowers = False,
    # embedPFCandidates = True
    )

akPu4PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPu4PFJets"),
    R0  = cms.double(0.4)
    )

akPu4PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPu4PFNjettiness:tau1',
    'akPu4PFNjettiness:tau2',
    'akPu4PFNjettiness:tau3']

akPu4PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPu4PFpatJetsWithBtagging"),
    genjetTag = 'ak4HiSignalGenJets',
    rParam = 0.4,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
    trackTag = cms.InputTag("hiGeneralTracks"),
    fillGenJets = True,
    isMC = True,
    doSubEvent = True,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akPu4PF"),
    jetName = cms.untracked.string("akPu4PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak4GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak4HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak4HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak4HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak4GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak4GenJets","droppedBranches")
    )

akPu4PFJetSequence_mc = cms.Sequence(
    # akPu4PFclean
    # *
    akPu4PFmatch
    # *
    # akPu4PFmatchGroomed
    *
    akPu4PFparton
    *
    akPu4PFcorr
    # *
    # akPu4PFJetID
    *
    akPu4PFPatJetFlavourIdLegacy
    # *
    # akPu4PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPu4PFJetTracksAssociatorAtVertex
    *
    akPu4PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPu4PFNjettiness
    *
    akPu4PFpatJetsWithBtagging
    *
    akPu4PFJetAnalyzer
    )

akPu4PFJetSequence_data = cms.Sequence(
    akPu4PFcorr
    *
    # akPu4PFJetID
    # *
    akPu4PFJetTracksAssociatorAtVertex
    *
    akPu4PFJetBtagging
    *
    akPu4PFNjettiness
    *
    akPu4PFpatJetsWithBtagging
    *
    akPu4PFJetAnalyzer
    )

akPu4PFJetSequence_mb = cms.Sequence(
    akPu4PFJetSequence_mc)
akPu4PFJetSequence_jec = cms.Sequence(
    akPu4PFJetSequence_mc)

akPu4PFJetSequence = cms.Sequence(
    akPu4PFJetSequence_mc)
