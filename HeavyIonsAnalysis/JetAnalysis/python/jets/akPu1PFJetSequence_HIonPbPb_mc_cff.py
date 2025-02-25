import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu1PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu1PFJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPu1PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak1HiSignalGenJets"),
    matched = cms.InputTag("ak1HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPu1PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu1PFJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akPu1PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPu1PFJets"),
    payload = "AKPu1PF_offline"
    )

akPu1PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPu1CaloJets'))

# akPu1PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1HiSignalGenJets'))

akPu1PFbTagger = bTaggers(
    "akPu1PF",
    0.1)

# create objects locally since they dont load properly otherwise
akPu1PFPatJetFlavourAssociationLegacy = akPu1PFbTagger.PatJetFlavourAssociationLegacy
akPu1PFPatJetPartons = akPu1PFbTagger.PatJetPartons
akPu1PFJetTracksAssociatorAtVertex = akPu1PFbTagger.JetTracksAssociatorAtVertex
akPu1PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu1PFSimpleSecondaryVertexHighEffBJetTags = akPu1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu1PFSimpleSecondaryVertexHighPurBJetTags = akPu1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu1PFCombinedSecondaryVertexBJetTags = akPu1PFbTagger.CombinedSecondaryVertexBJetTags
akPu1PFCombinedSecondaryVertexV2BJetTags = akPu1PFbTagger.CombinedSecondaryVertexV2BJetTags
akPu1PFJetBProbabilityBJetTags = akPu1PFbTagger.JetBProbabilityBJetTags
akPu1PFSoftPFMuonByPtBJetTags = akPu1PFbTagger.SoftPFMuonByPtBJetTags
akPu1PFSoftPFMuonByIP3dBJetTags = akPu1PFbTagger.SoftPFMuonByIP3dBJetTags
akPu1PFTrackCountingHighEffBJetTags = akPu1PFbTagger.TrackCountingHighEffBJetTags
akPu1PFTrackCountingHighPurBJetTags = akPu1PFbTagger.TrackCountingHighPurBJetTags
akPu1PFPatJetPartonAssociationLegacy = akPu1PFbTagger.PatJetPartonAssociationLegacy
akPu1PFPatJetPartonAssociationLegacy.partons = "signalPartons"

akPu1PFImpactParameterTagInfos = akPu1PFbTagger.ImpactParameterTagInfos
akPu1PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu1PFJetProbabilityBJetTags = akPu1PFbTagger.JetProbabilityBJetTags

akPu1PFSecondaryVertexTagInfos = akPu1PFbTagger.SecondaryVertexTagInfos
akPu1PFSimpleSecondaryVertexHighEffBJetTags = akPu1PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu1PFSimpleSecondaryVertexHighPurBJetTags = akPu1PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu1PFCombinedSecondaryVertexBJetTags = akPu1PFbTagger.CombinedSecondaryVertexBJetTags
akPu1PFCombinedSecondaryVertexV2BJetTags = akPu1PFbTagger.CombinedSecondaryVertexV2BJetTags

akPu1PFSecondaryVertexNegativeTagInfos = akPu1PFbTagger.SecondaryVertexNegativeTagInfos
akPu1PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPu1PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu1PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPu1PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu1PFNegativeCombinedSecondaryVertexBJetTags = akPu1PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPu1PFPositiveCombinedSecondaryVertexBJetTags = akPu1PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPu1PFNegativeCombinedSecondaryVertexV2BJetTags = akPu1PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu1PFPositiveCombinedSecondaryVertexV2BJetTags = akPu1PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu1PFSoftPFMuonsTagInfos = akPu1PFbTagger.SoftPFMuonsTagInfos
akPu1PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu1PFSoftPFMuonBJetTags = akPu1PFbTagger.SoftPFMuonBJetTags
akPu1PFSoftPFMuonByIP3dBJetTags = akPu1PFbTagger.SoftPFMuonByIP3dBJetTags
akPu1PFSoftPFMuonByPtBJetTags = akPu1PFbTagger.SoftPFMuonByPtBJetTags
akPu1PFNegativeSoftPFMuonByPtBJetTags = akPu1PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPu1PFPositiveSoftPFMuonByPtBJetTags = akPu1PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPu1PFPatJetFlavourIdLegacy = cms.Sequence(akPu1PFPatJetPartonAssociationLegacy*akPu1PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPu1PFPatJetFlavourAssociation = akPu1PFbTagger.PatJetFlavourAssociation
# akPu1PFPatJetFlavourId = cms.Sequence(akPu1PFPatJetPartons*akPu1PFPatJetFlavourAssociation)

akPu1PFJetBtaggingIP = cms.Sequence(
    akPu1PFImpactParameterTagInfos *
    akPu1PFTrackCountingHighEffBJetTags +
    akPu1PFTrackCountingHighPurBJetTags +
    akPu1PFJetProbabilityBJetTags +
    akPu1PFJetBProbabilityBJetTags
    )

akPu1PFJetBtaggingSV = cms.Sequence(
    akPu1PFImpactParameterTagInfos *
    akPu1PFSecondaryVertexTagInfos *
    akPu1PFSimpleSecondaryVertexHighEffBJetTags +
    akPu1PFSimpleSecondaryVertexHighPurBJetTags +
    akPu1PFCombinedSecondaryVertexBJetTags +
    akPu1PFCombinedSecondaryVertexV2BJetTags
    )

akPu1PFJetBtaggingNegSV = cms.Sequence(
    akPu1PFImpactParameterTagInfos *
    akPu1PFSecondaryVertexNegativeTagInfos *
    akPu1PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPu1PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPu1PFNegativeCombinedSecondaryVertexBJetTags +
    akPu1PFPositiveCombinedSecondaryVertexBJetTags +
    akPu1PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPu1PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPu1PFJetBtaggingMu = cms.Sequence(
    akPu1PFSoftPFMuonsTagInfos *
    akPu1PFSoftPFMuonBJetTags +
    akPu1PFSoftPFMuonByIP3dBJetTags +
    akPu1PFSoftPFMuonByPtBJetTags +
    akPu1PFNegativeSoftPFMuonByPtBJetTags +
    akPu1PFPositiveSoftPFMuonByPtBJetTags
    )

akPu1PFJetBtagging = cms.Sequence(
    akPu1PFJetBtaggingIP
    * akPu1PFJetBtaggingSV
    # * akPu1PFJetBtaggingNegSV
    # * akPu1PFJetBtaggingMu
    )

akPu1PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPu1PFJets"),
    genJetMatch            = cms.InputTag("akPu1PFmatch"),
    genPartonMatch         = cms.InputTag("akPu1PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPu1PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPu1PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPu1PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPu1PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPu1PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPu1PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPu1PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPu1PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPu1PFJetBProbabilityBJetTags"),
        cms.InputTag("akPu1PFJetProbabilityBJetTags"),
        # cms.InputTag("akPu1PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPu1PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPu1PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPu1PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPu1PFImpactParameterTagInfos"),cms.InputTag("akPu1PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPu1PFJetID"),
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

akPu1PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPu1PFJets"),
    R0  = cms.double(0.1)
    )

akPu1PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPu1PFNjettiness:tau1',
    'akPu1PFNjettiness:tau2',
    'akPu1PFNjettiness:tau3']

akPu1PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPu1PFpatJetsWithBtagging"),
    genjetTag = 'ak1HiSignalGenJets',
    rParam = 0.1,
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
    bTagJetName = cms.untracked.string("akPu1PF"),
    jetName = cms.untracked.string("akPu1PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(True),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak1GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak1HiGenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak1HiGenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak1HiGenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak1GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak1GenJets","droppedBranches")
    )

akPu1PFJetSequence_mc = cms.Sequence(
    # akPu1PFclean
    # *
    akPu1PFmatch
    # *
    # akPu1PFmatchGroomed
    *
    akPu1PFparton
    *
    akPu1PFcorr
    # *
    # akPu1PFJetID
    *
    akPu1PFPatJetFlavourIdLegacy
    # *
    # akPu1PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPu1PFJetTracksAssociatorAtVertex
    *
    akPu1PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPu1PFNjettiness
    *
    akPu1PFpatJetsWithBtagging
    *
    akPu1PFJetAnalyzer
    )

akPu1PFJetSequence_data = cms.Sequence(
    akPu1PFcorr
    *
    # akPu1PFJetID
    # *
    akPu1PFJetTracksAssociatorAtVertex
    *
    akPu1PFJetBtagging
    *
    akPu1PFNjettiness
    *
    akPu1PFpatJetsWithBtagging
    *
    akPu1PFJetAnalyzer
    )

akPu1PFJetSequence_mb = cms.Sequence(
    akPu1PFJetSequence_mc)
akPu1PFJetSequence_jec = cms.Sequence(
    akPu1PFJetSequence_mc)

akPu1PFJetSequence = cms.Sequence(
    akPu1PFJetSequence_mc)
