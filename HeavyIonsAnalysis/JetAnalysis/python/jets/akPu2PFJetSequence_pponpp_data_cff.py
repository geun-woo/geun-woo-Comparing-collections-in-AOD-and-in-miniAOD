import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu2PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu2PFJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPu2PFmatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak2GenJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPu2PFparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu2PFJets"),
    matched = cms.InputTag("genParticles"))

akPu2PFcorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative','L2L3Residual'),
    src = cms.InputTag("akPu2PFJets"),
    payload = "AK2PF"
    )

akPu2PFJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPu2CaloJets'))

# akPu2PFclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak2GenJets'))

akPu2PFbTagger = bTaggers(
    "akPu2PF",
    0.2)

# create objects locally since they dont load properly otherwise
akPu2PFPatJetFlavourAssociationLegacy = akPu2PFbTagger.PatJetFlavourAssociationLegacy
akPu2PFPatJetPartons = akPu2PFbTagger.PatJetPartons
akPu2PFJetTracksAssociatorAtVertex = akPu2PFbTagger.JetTracksAssociatorAtVertex
akPu2PFJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu2PFSimpleSecondaryVertexHighEffBJetTags = akPu2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu2PFSimpleSecondaryVertexHighPurBJetTags = akPu2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu2PFCombinedSecondaryVertexBJetTags = akPu2PFbTagger.CombinedSecondaryVertexBJetTags
akPu2PFCombinedSecondaryVertexV2BJetTags = akPu2PFbTagger.CombinedSecondaryVertexV2BJetTags
akPu2PFJetBProbabilityBJetTags = akPu2PFbTagger.JetBProbabilityBJetTags
akPu2PFSoftPFMuonByPtBJetTags = akPu2PFbTagger.SoftPFMuonByPtBJetTags
akPu2PFSoftPFMuonByIP3dBJetTags = akPu2PFbTagger.SoftPFMuonByIP3dBJetTags
akPu2PFTrackCountingHighEffBJetTags = akPu2PFbTagger.TrackCountingHighEffBJetTags
akPu2PFTrackCountingHighPurBJetTags = akPu2PFbTagger.TrackCountingHighPurBJetTags
akPu2PFPatJetPartonAssociationLegacy = akPu2PFbTagger.PatJetPartonAssociationLegacy
akPu2PFPatJetPartonAssociationLegacy.partons = "myPartons"

akPu2PFImpactParameterTagInfos = akPu2PFbTagger.ImpactParameterTagInfos
akPu2PFImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu2PFJetProbabilityBJetTags = akPu2PFbTagger.JetProbabilityBJetTags

akPu2PFSecondaryVertexTagInfos = akPu2PFbTagger.SecondaryVertexTagInfos
akPu2PFSimpleSecondaryVertexHighEffBJetTags = akPu2PFbTagger.SimpleSecondaryVertexHighEffBJetTags
akPu2PFSimpleSecondaryVertexHighPurBJetTags = akPu2PFbTagger.SimpleSecondaryVertexHighPurBJetTags
akPu2PFCombinedSecondaryVertexBJetTags = akPu2PFbTagger.CombinedSecondaryVertexBJetTags
akPu2PFCombinedSecondaryVertexV2BJetTags = akPu2PFbTagger.CombinedSecondaryVertexV2BJetTags

akPu2PFSecondaryVertexNegativeTagInfos = akPu2PFbTagger.SecondaryVertexNegativeTagInfos
akPu2PFNegativeSimpleSecondaryVertexHighEffBJetTags = akPu2PFbTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu2PFNegativeSimpleSecondaryVertexHighPurBJetTags = akPu2PFbTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu2PFNegativeCombinedSecondaryVertexBJetTags = akPu2PFbTagger.NegativeCombinedSecondaryVertexBJetTags
akPu2PFPositiveCombinedSecondaryVertexBJetTags = akPu2PFbTagger.PositiveCombinedSecondaryVertexBJetTags
akPu2PFNegativeCombinedSecondaryVertexV2BJetTags = akPu2PFbTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu2PFPositiveCombinedSecondaryVertexV2BJetTags = akPu2PFbTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu2PFSoftPFMuonsTagInfos = akPu2PFbTagger.SoftPFMuonsTagInfos
akPu2PFSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu2PFSoftPFMuonBJetTags = akPu2PFbTagger.SoftPFMuonBJetTags
akPu2PFSoftPFMuonByIP3dBJetTags = akPu2PFbTagger.SoftPFMuonByIP3dBJetTags
akPu2PFSoftPFMuonByPtBJetTags = akPu2PFbTagger.SoftPFMuonByPtBJetTags
akPu2PFNegativeSoftPFMuonByPtBJetTags = akPu2PFbTagger.NegativeSoftPFMuonByPtBJetTags
akPu2PFPositiveSoftPFMuonByPtBJetTags = akPu2PFbTagger.PositiveSoftPFMuonByPtBJetTags
akPu2PFPatJetFlavourIdLegacy = cms.Sequence(akPu2PFPatJetPartonAssociationLegacy*akPu2PFPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPu2PFPatJetFlavourAssociation = akPu2PFbTagger.PatJetFlavourAssociation
# akPu2PFPatJetFlavourId = cms.Sequence(akPu2PFPatJetPartons*akPu2PFPatJetFlavourAssociation)

akPu2PFJetBtaggingIP = cms.Sequence(
    akPu2PFImpactParameterTagInfos *
    akPu2PFTrackCountingHighEffBJetTags +
    akPu2PFTrackCountingHighPurBJetTags +
    akPu2PFJetProbabilityBJetTags +
    akPu2PFJetBProbabilityBJetTags
    )

akPu2PFJetBtaggingSV = cms.Sequence(
    akPu2PFImpactParameterTagInfos *
    akPu2PFSecondaryVertexTagInfos *
    akPu2PFSimpleSecondaryVertexHighEffBJetTags +
    akPu2PFSimpleSecondaryVertexHighPurBJetTags +
    akPu2PFCombinedSecondaryVertexBJetTags +
    akPu2PFCombinedSecondaryVertexV2BJetTags
    )

akPu2PFJetBtaggingNegSV = cms.Sequence(
    akPu2PFImpactParameterTagInfos *
    akPu2PFSecondaryVertexNegativeTagInfos *
    akPu2PFNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPu2PFNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPu2PFNegativeCombinedSecondaryVertexBJetTags +
    akPu2PFPositiveCombinedSecondaryVertexBJetTags +
    akPu2PFNegativeCombinedSecondaryVertexV2BJetTags +
    akPu2PFPositiveCombinedSecondaryVertexV2BJetTags
    )

akPu2PFJetBtaggingMu = cms.Sequence(
    akPu2PFSoftPFMuonsTagInfos *
    akPu2PFSoftPFMuonBJetTags +
    akPu2PFSoftPFMuonByIP3dBJetTags +
    akPu2PFSoftPFMuonByPtBJetTags +
    akPu2PFNegativeSoftPFMuonByPtBJetTags +
    akPu2PFPositiveSoftPFMuonByPtBJetTags
    )

akPu2PFJetBtagging = cms.Sequence(
    akPu2PFJetBtaggingIP
    * akPu2PFJetBtaggingSV
    # * akPu2PFJetBtaggingNegSV
    # * akPu2PFJetBtaggingMu
    )

akPu2PFpatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPu2PFJets"),
    genJetMatch            = cms.InputTag("akPu2PFmatch"),
    genPartonMatch         = cms.InputTag("akPu2PFparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPu2PFcorr")),
    JetPartonMapSource     = cms.InputTag("akPu2PFPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPu2PFPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPu2PFJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPu2PFSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPu2PFSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPu2PFCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPu2PFCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPu2PFJetBProbabilityBJetTags"),
        cms.InputTag("akPu2PFJetProbabilityBJetTags"),
        # cms.InputTag("akPu2PFSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPu2PFSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPu2PFTrackCountingHighEffBJetTags"),
        cms.InputTag("akPu2PFTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPu2PFImpactParameterTagInfos"),cms.InputTag("akPu2PFSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPu2PFJetID"),
    addBTagInfo = True,
    addTagInfos = True,
    addDiscriminators = True,
    addAssociatedTracks = True,
    addJetCharge = False,
    addJetID = False,
    getJetMCFlavour = False,
    addGenPartonMatch = False,
    addGenJetMatch = False,
    embedGenJetMatch = False,
    embedGenPartonMatch = False,
    # embedCaloTowers = False,
    # embedPFCandidates = True
    )

akPu2PFNjettiness = Njettiness.clone(
    src = cms.InputTag("akPu2PFJets"),
    R0  = cms.double(0.2)
    )

akPu2PFpatJetsWithBtagging.userData.userFloats.src += [
    'akPu2PFNjettiness:tau1',
    'akPu2PFNjettiness:tau2',
    'akPu2PFNjettiness:tau3']

akPu2PFJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPu2PFpatJetsWithBtagging"),
    genjetTag = 'ak2GenJets',
    rParam = 0.2,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = False,
    isMC = False,
    doSubEvent = False,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akPu2PF"),
    jetName = cms.untracked.string("akPu2PF"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak2GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak2GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak2GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak2GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak2GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak2GenJets","droppedBranches")
    )

akPu2PFJetSequence_mc = cms.Sequence(
    # akPu2PFclean
    # *
    akPu2PFmatch
    # *
    # akPu2PFmatchGroomed
    *
    akPu2PFparton
    *
    akPu2PFcorr
    # *
    # akPu2PFJetID
    *
    akPu2PFPatJetFlavourIdLegacy
    # *
    # akPu2PFPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPu2PFJetTracksAssociatorAtVertex
    *
    akPu2PFJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPu2PFNjettiness
    *
    akPu2PFpatJetsWithBtagging
    *
    akPu2PFJetAnalyzer
    )

akPu2PFJetSequence_data = cms.Sequence(
    akPu2PFcorr
    *
    # akPu2PFJetID
    # *
    akPu2PFJetTracksAssociatorAtVertex
    *
    akPu2PFJetBtagging
    *
    akPu2PFNjettiness
    *
    akPu2PFpatJetsWithBtagging
    *
    akPu2PFJetAnalyzer
    )

akPu2PFJetSequence_mb = cms.Sequence(
    akPu2PFJetSequence_mc)
akPu2PFJetSequence_jec = cms.Sequence(
    akPu2PFJetSequence_mc)

akPu2PFJetSequence = cms.Sequence(
    akPu2PFJetSequence_data)
