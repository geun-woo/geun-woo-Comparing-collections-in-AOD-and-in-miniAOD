import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu2Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu2CaloJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPu2CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak2GenJets"),
    matched = cms.InputTag("ak2GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.2
    )

akPu2Caloparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu2CaloJets"),
    matched = cms.InputTag("genParticles"))

akPu2Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPu2CaloJets"),
    payload = "AK4PF"
    )

akPu2CaloJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPu2CaloJets'))

# akPu2Caloclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak2GenJets'))

akPu2CalobTagger = bTaggers(
    "akPu2Calo",
    0.2)

# create objects locally since they dont load properly otherwise
akPu2CaloPatJetFlavourAssociationLegacy = akPu2CalobTagger.PatJetFlavourAssociationLegacy
akPu2CaloPatJetPartons = akPu2CalobTagger.PatJetPartons
akPu2CaloJetTracksAssociatorAtVertex = akPu2CalobTagger.JetTracksAssociatorAtVertex
akPu2CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu2CaloSimpleSecondaryVertexHighEffBJetTags = akPu2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu2CaloSimpleSecondaryVertexHighPurBJetTags = akPu2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu2CaloCombinedSecondaryVertexBJetTags = akPu2CalobTagger.CombinedSecondaryVertexBJetTags
akPu2CaloCombinedSecondaryVertexV2BJetTags = akPu2CalobTagger.CombinedSecondaryVertexV2BJetTags
akPu2CaloJetBProbabilityBJetTags = akPu2CalobTagger.JetBProbabilityBJetTags
akPu2CaloSoftPFMuonByPtBJetTags = akPu2CalobTagger.SoftPFMuonByPtBJetTags
akPu2CaloSoftPFMuonByIP3dBJetTags = akPu2CalobTagger.SoftPFMuonByIP3dBJetTags
akPu2CaloTrackCountingHighEffBJetTags = akPu2CalobTagger.TrackCountingHighEffBJetTags
akPu2CaloTrackCountingHighPurBJetTags = akPu2CalobTagger.TrackCountingHighPurBJetTags
akPu2CaloPatJetPartonAssociationLegacy = akPu2CalobTagger.PatJetPartonAssociationLegacy
akPu2CaloPatJetPartonAssociationLegacy.partons = "myPartons"

akPu2CaloImpactParameterTagInfos = akPu2CalobTagger.ImpactParameterTagInfos
akPu2CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu2CaloJetProbabilityBJetTags = akPu2CalobTagger.JetProbabilityBJetTags

akPu2CaloSecondaryVertexTagInfos = akPu2CalobTagger.SecondaryVertexTagInfos
akPu2CaloSimpleSecondaryVertexHighEffBJetTags = akPu2CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu2CaloSimpleSecondaryVertexHighPurBJetTags = akPu2CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu2CaloCombinedSecondaryVertexBJetTags = akPu2CalobTagger.CombinedSecondaryVertexBJetTags
akPu2CaloCombinedSecondaryVertexV2BJetTags = akPu2CalobTagger.CombinedSecondaryVertexV2BJetTags

akPu2CaloSecondaryVertexNegativeTagInfos = akPu2CalobTagger.SecondaryVertexNegativeTagInfos
akPu2CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPu2CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu2CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPu2CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu2CaloNegativeCombinedSecondaryVertexBJetTags = akPu2CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPu2CaloPositiveCombinedSecondaryVertexBJetTags = akPu2CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPu2CaloNegativeCombinedSecondaryVertexV2BJetTags = akPu2CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu2CaloPositiveCombinedSecondaryVertexV2BJetTags = akPu2CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu2CaloSoftPFMuonsTagInfos = akPu2CalobTagger.SoftPFMuonsTagInfos
akPu2CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu2CaloSoftPFMuonBJetTags = akPu2CalobTagger.SoftPFMuonBJetTags
akPu2CaloSoftPFMuonByIP3dBJetTags = akPu2CalobTagger.SoftPFMuonByIP3dBJetTags
akPu2CaloSoftPFMuonByPtBJetTags = akPu2CalobTagger.SoftPFMuonByPtBJetTags
akPu2CaloNegativeSoftPFMuonByPtBJetTags = akPu2CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPu2CaloPositiveSoftPFMuonByPtBJetTags = akPu2CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPu2CaloPatJetFlavourIdLegacy = cms.Sequence(akPu2CaloPatJetPartonAssociationLegacy*akPu2CaloPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPu2CaloPatJetFlavourAssociation = akPu2CalobTagger.PatJetFlavourAssociation
# akPu2CaloPatJetFlavourId = cms.Sequence(akPu2CaloPatJetPartons*akPu2CaloPatJetFlavourAssociation)

akPu2CaloJetBtaggingIP = cms.Sequence(
    akPu2CaloImpactParameterTagInfos *
    akPu2CaloTrackCountingHighEffBJetTags +
    akPu2CaloTrackCountingHighPurBJetTags +
    akPu2CaloJetProbabilityBJetTags +
    akPu2CaloJetBProbabilityBJetTags
    )

akPu2CaloJetBtaggingSV = cms.Sequence(
    akPu2CaloImpactParameterTagInfos *
    akPu2CaloSecondaryVertexTagInfos *
    akPu2CaloSimpleSecondaryVertexHighEffBJetTags +
    akPu2CaloSimpleSecondaryVertexHighPurBJetTags +
    akPu2CaloCombinedSecondaryVertexBJetTags +
    akPu2CaloCombinedSecondaryVertexV2BJetTags
    )

akPu2CaloJetBtaggingNegSV = cms.Sequence(
    akPu2CaloImpactParameterTagInfos *
    akPu2CaloSecondaryVertexNegativeTagInfos *
    akPu2CaloNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPu2CaloNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPu2CaloNegativeCombinedSecondaryVertexBJetTags +
    akPu2CaloPositiveCombinedSecondaryVertexBJetTags +
    akPu2CaloNegativeCombinedSecondaryVertexV2BJetTags +
    akPu2CaloPositiveCombinedSecondaryVertexV2BJetTags
    )

akPu2CaloJetBtaggingMu = cms.Sequence(
    akPu2CaloSoftPFMuonsTagInfos *
    akPu2CaloSoftPFMuonBJetTags +
    akPu2CaloSoftPFMuonByIP3dBJetTags +
    akPu2CaloSoftPFMuonByPtBJetTags +
    akPu2CaloNegativeSoftPFMuonByPtBJetTags +
    akPu2CaloPositiveSoftPFMuonByPtBJetTags
    )

akPu2CaloJetBtagging = cms.Sequence(
    akPu2CaloJetBtaggingIP
    * akPu2CaloJetBtaggingSV
    # * akPu2CaloJetBtaggingNegSV
    # * akPu2CaloJetBtaggingMu
    )

akPu2CalopatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPu2CaloJets"),
    genJetMatch            = cms.InputTag("akPu2Calomatch"),
    genPartonMatch         = cms.InputTag("akPu2Caloparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPu2Calocorr")),
    JetPartonMapSource     = cms.InputTag("akPu2CaloPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPu2CaloPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPu2CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPu2CaloSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPu2CaloSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPu2CaloCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPu2CaloCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPu2CaloJetBProbabilityBJetTags"),
        cms.InputTag("akPu2CaloJetProbabilityBJetTags"),
        # cms.InputTag("akPu2CaloSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPu2CaloSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPu2CaloTrackCountingHighEffBJetTags"),
        cms.InputTag("akPu2CaloTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPu2CaloImpactParameterTagInfos"),cms.InputTag("akPu2CaloSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPu2CaloJetID"),
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

akPu2CaloNjettiness = Njettiness.clone(
    src = cms.InputTag("akPu2CaloJets"),
    R0  = cms.double(0.2)
    )

akPu2CalopatJetsWithBtagging.userData.userFloats.src += [
    'akPu2CaloNjettiness:tau1',
    'akPu2CaloNjettiness:tau2',
    'akPu2CaloNjettiness:tau3']

akPu2CaloJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPu2CalopatJetsWithBtagging"),
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
    bTagJetName = cms.untracked.string("akPu2Calo"),
    jetName = cms.untracked.string("akPu2Calo"),
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

akPu2CaloJetSequence_mc = cms.Sequence(
    # akPu2Caloclean
    # *
    akPu2Calomatch
    # *
    # akPu2CalomatchGroomed
    *
    akPu2Caloparton
    *
    akPu2Calocorr
    # *
    # akPu2CaloJetID
    *
    akPu2CaloPatJetFlavourIdLegacy
    # *
    # akPu2CaloPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPu2CaloJetTracksAssociatorAtVertex
    *
    akPu2CaloJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPu2CaloNjettiness
    *
    akPu2CalopatJetsWithBtagging
    *
    akPu2CaloJetAnalyzer
    )

akPu2CaloJetSequence_data = cms.Sequence(
    akPu2Calocorr
    *
    # akPu2CaloJetID
    # *
    akPu2CaloJetTracksAssociatorAtVertex
    *
    akPu2CaloJetBtagging
    *
    akPu2CaloNjettiness
    *
    akPu2CalopatJetsWithBtagging
    *
    akPu2CaloJetAnalyzer
    )

akPu2CaloJetSequence_mb = cms.Sequence(
    akPu2CaloJetSequence_mc)
akPu2CaloJetSequence_jec = cms.Sequence(
    akPu2CaloJetSequence_mc)

akPu2CaloJetSequence = cms.Sequence(
    akPu2CaloJetSequence_data)
