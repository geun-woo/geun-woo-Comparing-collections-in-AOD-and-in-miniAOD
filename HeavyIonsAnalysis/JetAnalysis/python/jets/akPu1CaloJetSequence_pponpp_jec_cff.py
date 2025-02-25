import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu1Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu1CaloJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPu1CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak1GenJets"),
    matched = cms.InputTag("ak1GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.1
    )

akPu1Caloparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu1CaloJets"),
    matched = cms.InputTag("genParticles"))

akPu1Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPu1CaloJets"),
    payload = "AK4PF"
    )

akPu1CaloJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPu1CaloJets'))

# akPu1Caloclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak1GenJets'))

akPu1CalobTagger = bTaggers(
    "akPu1Calo",
    0.1)

# create objects locally since they dont load properly otherwise
akPu1CaloPatJetFlavourAssociationLegacy = akPu1CalobTagger.PatJetFlavourAssociationLegacy
akPu1CaloPatJetPartons = akPu1CalobTagger.PatJetPartons
akPu1CaloJetTracksAssociatorAtVertex = akPu1CalobTagger.JetTracksAssociatorAtVertex
akPu1CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu1CaloSimpleSecondaryVertexHighEffBJetTags = akPu1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu1CaloSimpleSecondaryVertexHighPurBJetTags = akPu1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu1CaloCombinedSecondaryVertexBJetTags = akPu1CalobTagger.CombinedSecondaryVertexBJetTags
akPu1CaloCombinedSecondaryVertexV2BJetTags = akPu1CalobTagger.CombinedSecondaryVertexV2BJetTags
akPu1CaloJetBProbabilityBJetTags = akPu1CalobTagger.JetBProbabilityBJetTags
akPu1CaloSoftPFMuonByPtBJetTags = akPu1CalobTagger.SoftPFMuonByPtBJetTags
akPu1CaloSoftPFMuonByIP3dBJetTags = akPu1CalobTagger.SoftPFMuonByIP3dBJetTags
akPu1CaloTrackCountingHighEffBJetTags = akPu1CalobTagger.TrackCountingHighEffBJetTags
akPu1CaloTrackCountingHighPurBJetTags = akPu1CalobTagger.TrackCountingHighPurBJetTags
akPu1CaloPatJetPartonAssociationLegacy = akPu1CalobTagger.PatJetPartonAssociationLegacy
akPu1CaloPatJetPartonAssociationLegacy.partons = "myPartons"

akPu1CaloImpactParameterTagInfos = akPu1CalobTagger.ImpactParameterTagInfos
akPu1CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu1CaloJetProbabilityBJetTags = akPu1CalobTagger.JetProbabilityBJetTags

akPu1CaloSecondaryVertexTagInfos = akPu1CalobTagger.SecondaryVertexTagInfos
akPu1CaloSimpleSecondaryVertexHighEffBJetTags = akPu1CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu1CaloSimpleSecondaryVertexHighPurBJetTags = akPu1CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu1CaloCombinedSecondaryVertexBJetTags = akPu1CalobTagger.CombinedSecondaryVertexBJetTags
akPu1CaloCombinedSecondaryVertexV2BJetTags = akPu1CalobTagger.CombinedSecondaryVertexV2BJetTags

akPu1CaloSecondaryVertexNegativeTagInfos = akPu1CalobTagger.SecondaryVertexNegativeTagInfos
akPu1CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPu1CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu1CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPu1CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu1CaloNegativeCombinedSecondaryVertexBJetTags = akPu1CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPu1CaloPositiveCombinedSecondaryVertexBJetTags = akPu1CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPu1CaloNegativeCombinedSecondaryVertexV2BJetTags = akPu1CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu1CaloPositiveCombinedSecondaryVertexV2BJetTags = akPu1CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu1CaloSoftPFMuonsTagInfos = akPu1CalobTagger.SoftPFMuonsTagInfos
akPu1CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu1CaloSoftPFMuonBJetTags = akPu1CalobTagger.SoftPFMuonBJetTags
akPu1CaloSoftPFMuonByIP3dBJetTags = akPu1CalobTagger.SoftPFMuonByIP3dBJetTags
akPu1CaloSoftPFMuonByPtBJetTags = akPu1CalobTagger.SoftPFMuonByPtBJetTags
akPu1CaloNegativeSoftPFMuonByPtBJetTags = akPu1CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPu1CaloPositiveSoftPFMuonByPtBJetTags = akPu1CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPu1CaloPatJetFlavourIdLegacy = cms.Sequence(akPu1CaloPatJetPartonAssociationLegacy*akPu1CaloPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPu1CaloPatJetFlavourAssociation = akPu1CalobTagger.PatJetFlavourAssociation
# akPu1CaloPatJetFlavourId = cms.Sequence(akPu1CaloPatJetPartons*akPu1CaloPatJetFlavourAssociation)

akPu1CaloJetBtaggingIP = cms.Sequence(
    akPu1CaloImpactParameterTagInfos *
    akPu1CaloTrackCountingHighEffBJetTags +
    akPu1CaloTrackCountingHighPurBJetTags +
    akPu1CaloJetProbabilityBJetTags +
    akPu1CaloJetBProbabilityBJetTags
    )

akPu1CaloJetBtaggingSV = cms.Sequence(
    akPu1CaloImpactParameterTagInfos *
    akPu1CaloSecondaryVertexTagInfos *
    akPu1CaloSimpleSecondaryVertexHighEffBJetTags +
    akPu1CaloSimpleSecondaryVertexHighPurBJetTags +
    akPu1CaloCombinedSecondaryVertexBJetTags +
    akPu1CaloCombinedSecondaryVertexV2BJetTags
    )

akPu1CaloJetBtaggingNegSV = cms.Sequence(
    akPu1CaloImpactParameterTagInfos *
    akPu1CaloSecondaryVertexNegativeTagInfos *
    akPu1CaloNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPu1CaloNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPu1CaloNegativeCombinedSecondaryVertexBJetTags +
    akPu1CaloPositiveCombinedSecondaryVertexBJetTags +
    akPu1CaloNegativeCombinedSecondaryVertexV2BJetTags +
    akPu1CaloPositiveCombinedSecondaryVertexV2BJetTags
    )

akPu1CaloJetBtaggingMu = cms.Sequence(
    akPu1CaloSoftPFMuonsTagInfos *
    akPu1CaloSoftPFMuonBJetTags +
    akPu1CaloSoftPFMuonByIP3dBJetTags +
    akPu1CaloSoftPFMuonByPtBJetTags +
    akPu1CaloNegativeSoftPFMuonByPtBJetTags +
    akPu1CaloPositiveSoftPFMuonByPtBJetTags
    )

akPu1CaloJetBtagging = cms.Sequence(
    akPu1CaloJetBtaggingIP
    * akPu1CaloJetBtaggingSV
    # * akPu1CaloJetBtaggingNegSV
    # * akPu1CaloJetBtaggingMu
    )

akPu1CalopatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPu1CaloJets"),
    genJetMatch            = cms.InputTag("akPu1Calomatch"),
    genPartonMatch         = cms.InputTag("akPu1Caloparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPu1Calocorr")),
    JetPartonMapSource     = cms.InputTag("akPu1CaloPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPu1CaloPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPu1CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPu1CaloSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPu1CaloSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPu1CaloCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPu1CaloCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPu1CaloJetBProbabilityBJetTags"),
        cms.InputTag("akPu1CaloJetProbabilityBJetTags"),
        # cms.InputTag("akPu1CaloSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPu1CaloSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPu1CaloTrackCountingHighEffBJetTags"),
        cms.InputTag("akPu1CaloTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPu1CaloImpactParameterTagInfos"),cms.InputTag("akPu1CaloSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPu1CaloJetID"),
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

akPu1CaloNjettiness = Njettiness.clone(
    src = cms.InputTag("akPu1CaloJets"),
    R0  = cms.double(0.1)
    )

akPu1CalopatJetsWithBtagging.userData.userFloats.src += [
    'akPu1CaloNjettiness:tau1',
    'akPu1CaloNjettiness:tau2',
    'akPu1CaloNjettiness:tau3']

akPu1CaloJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPu1CalopatJetsWithBtagging"),
    genjetTag = 'ak1GenJets',
    rParam = 0.1,
    matchJets = cms.untracked.bool(False),
    matchTag = 'patJetsWithBtagging',
    pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
    trackTag = cms.InputTag("generalTracks"),
    fillGenJets = True,
    isMC = True,
    doSubEvent = True,
    useHepMC = cms.untracked.bool(False),
    genParticles = cms.untracked.InputTag("genParticles"),
    eventInfoTag = cms.InputTag("generator"),
    doLifeTimeTagging = cms.untracked.bool(True),
    doLifeTimeTaggingExtras = cms.untracked.bool(False),
    bTagJetName = cms.untracked.string("akPu1Calo"),
    jetName = cms.untracked.string("akPu1Calo"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
    doSubJets = cms.untracked.bool(False),
    doGenSubJets = cms.untracked.bool(False),
    subjetGenTag = cms.untracked.InputTag("ak1GenJets"),
    doGenTaus = cms.untracked.bool(False),
    genTau1 = cms.InputTag("ak1GenNjettiness","tau1"),
    genTau2 = cms.InputTag("ak1GenNjettiness","tau2"),
    genTau3 = cms.InputTag("ak1GenNjettiness","tau3"),
    doGenSym = cms.untracked.bool(False),
    genSym = cms.InputTag("ak1GenJets","sym"),
    genDroppedBranches = cms.InputTag("ak1GenJets","droppedBranches")
    )

akPu1CaloJetSequence_mc = cms.Sequence(
    # akPu1Caloclean
    # *
    akPu1Calomatch
    # *
    # akPu1CalomatchGroomed
    *
    akPu1Caloparton
    *
    akPu1Calocorr
    # *
    # akPu1CaloJetID
    *
    akPu1CaloPatJetFlavourIdLegacy
    # *
    # akPu1CaloPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPu1CaloJetTracksAssociatorAtVertex
    *
    akPu1CaloJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPu1CaloNjettiness
    *
    akPu1CalopatJetsWithBtagging
    *
    akPu1CaloJetAnalyzer
    )

akPu1CaloJetSequence_data = cms.Sequence(
    akPu1Calocorr
    *
    # akPu1CaloJetID
    # *
    akPu1CaloJetTracksAssociatorAtVertex
    *
    akPu1CaloJetBtagging
    *
    akPu1CaloNjettiness
    *
    akPu1CalopatJetsWithBtagging
    *
    akPu1CaloJetAnalyzer
    )

akPu1CaloJetSequence_mb = cms.Sequence(
    akPu1CaloJetSequence_mc)
akPu1CaloJetSequence_jec = cms.Sequence(
    akPu1CaloJetSequence_mc)

akPu1CaloJetSequence = cms.Sequence(
    akPu1CaloJetSequence_jec)
akPu1CaloJetAnalyzer.genPtMin = cms.untracked.double(1)
akPu1CaloJetAnalyzer.jetPtMin = cms.double(1)
