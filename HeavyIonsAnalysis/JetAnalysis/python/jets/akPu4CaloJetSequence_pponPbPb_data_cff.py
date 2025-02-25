import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch, patJetPartonMatch
from PhysicsTools.PatAlgos.recoLayer0.jetCorrFactors_cfi import patJetCorrFactors
from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import patJets

from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *

from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu4Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu4CaloJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPu4CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak4HiSignalGenJets"),
    matched = cms.InputTag("ak4HiSignalGenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.4
    )

akPu4Caloparton = patJetPartonMatch.clone(
    src = cms.InputTag("akPu4CaloJets"),
    matched = cms.InputTag("hiSignalGenParticles"))

akPu4Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
    levels   = cms.vstring('L2Relative'),
    src = cms.InputTag("akPu4CaloJets"),
    payload = "AK4PF"
    )

akPu4CaloJetID = cms.EDProducer(
    'JetIDProducer',
    JetIDParams,
    src = cms.InputTag('akPu4CaloJets'))

# akPu4Caloclean = heavyIonCleanedGenJets.clone(
#     src = cms.InputTag('ak4HiSignalGenJets'))

akPu4CalobTagger = bTaggers(
    "akPu4Calo",
    0.4)

# create objects locally since they dont load properly otherwise
akPu4CaloPatJetFlavourAssociationLegacy = akPu4CalobTagger.PatJetFlavourAssociationLegacy
akPu4CaloPatJetPartons = akPu4CalobTagger.PatJetPartons
akPu4CaloJetTracksAssociatorAtVertex = akPu4CalobTagger.JetTracksAssociatorAtVertex
akPu4CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu4CaloSimpleSecondaryVertexHighEffBJetTags = akPu4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu4CaloSimpleSecondaryVertexHighPurBJetTags = akPu4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu4CaloCombinedSecondaryVertexBJetTags = akPu4CalobTagger.CombinedSecondaryVertexBJetTags
akPu4CaloCombinedSecondaryVertexV2BJetTags = akPu4CalobTagger.CombinedSecondaryVertexV2BJetTags
akPu4CaloJetBProbabilityBJetTags = akPu4CalobTagger.JetBProbabilityBJetTags
akPu4CaloSoftPFMuonByPtBJetTags = akPu4CalobTagger.SoftPFMuonByPtBJetTags
akPu4CaloSoftPFMuonByIP3dBJetTags = akPu4CalobTagger.SoftPFMuonByIP3dBJetTags
akPu4CaloTrackCountingHighEffBJetTags = akPu4CalobTagger.TrackCountingHighEffBJetTags
akPu4CaloTrackCountingHighPurBJetTags = akPu4CalobTagger.TrackCountingHighPurBJetTags
akPu4CaloPatJetPartonAssociationLegacy = akPu4CalobTagger.PatJetPartonAssociationLegacy
akPu4CaloPatJetPartonAssociationLegacy.partons = "signalPartons"

akPu4CaloImpactParameterTagInfos = akPu4CalobTagger.ImpactParameterTagInfos
akPu4CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu4CaloJetProbabilityBJetTags = akPu4CalobTagger.JetProbabilityBJetTags

akPu4CaloSecondaryVertexTagInfos = akPu4CalobTagger.SecondaryVertexTagInfos
akPu4CaloSimpleSecondaryVertexHighEffBJetTags = akPu4CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu4CaloSimpleSecondaryVertexHighPurBJetTags = akPu4CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu4CaloCombinedSecondaryVertexBJetTags = akPu4CalobTagger.CombinedSecondaryVertexBJetTags
akPu4CaloCombinedSecondaryVertexV2BJetTags = akPu4CalobTagger.CombinedSecondaryVertexV2BJetTags

akPu4CaloSecondaryVertexNegativeTagInfos = akPu4CalobTagger.SecondaryVertexNegativeTagInfos
akPu4CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPu4CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu4CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPu4CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu4CaloNegativeCombinedSecondaryVertexBJetTags = akPu4CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPu4CaloPositiveCombinedSecondaryVertexBJetTags = akPu4CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPu4CaloNegativeCombinedSecondaryVertexV2BJetTags = akPu4CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu4CaloPositiveCombinedSecondaryVertexV2BJetTags = akPu4CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu4CaloSoftPFMuonsTagInfos = akPu4CalobTagger.SoftPFMuonsTagInfos
akPu4CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu4CaloSoftPFMuonBJetTags = akPu4CalobTagger.SoftPFMuonBJetTags
akPu4CaloSoftPFMuonByIP3dBJetTags = akPu4CalobTagger.SoftPFMuonByIP3dBJetTags
akPu4CaloSoftPFMuonByPtBJetTags = akPu4CalobTagger.SoftPFMuonByPtBJetTags
akPu4CaloNegativeSoftPFMuonByPtBJetTags = akPu4CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPu4CaloPositiveSoftPFMuonByPtBJetTags = akPu4CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPu4CaloPatJetFlavourIdLegacy = cms.Sequence(akPu4CaloPatJetPartonAssociationLegacy*akPu4CaloPatJetFlavourAssociationLegacy)
# Not working with our PU sub, but keep it here for reference
# akPu4CaloPatJetFlavourAssociation = akPu4CalobTagger.PatJetFlavourAssociation
# akPu4CaloPatJetFlavourId = cms.Sequence(akPu4CaloPatJetPartons*akPu4CaloPatJetFlavourAssociation)

akPu4CaloJetBtaggingIP = cms.Sequence(
    akPu4CaloImpactParameterTagInfos *
    akPu4CaloTrackCountingHighEffBJetTags +
    akPu4CaloTrackCountingHighPurBJetTags +
    akPu4CaloJetProbabilityBJetTags +
    akPu4CaloJetBProbabilityBJetTags
    )

akPu4CaloJetBtaggingSV = cms.Sequence(
    akPu4CaloImpactParameterTagInfos *
    akPu4CaloSecondaryVertexTagInfos *
    akPu4CaloSimpleSecondaryVertexHighEffBJetTags +
    akPu4CaloSimpleSecondaryVertexHighPurBJetTags +
    akPu4CaloCombinedSecondaryVertexBJetTags +
    akPu4CaloCombinedSecondaryVertexV2BJetTags
    )

akPu4CaloJetBtaggingNegSV = cms.Sequence(
    akPu4CaloImpactParameterTagInfos *
    akPu4CaloSecondaryVertexNegativeTagInfos *
    akPu4CaloNegativeSimpleSecondaryVertexHighEffBJetTags +
    akPu4CaloNegativeSimpleSecondaryVertexHighPurBJetTags +
    akPu4CaloNegativeCombinedSecondaryVertexBJetTags +
    akPu4CaloPositiveCombinedSecondaryVertexBJetTags +
    akPu4CaloNegativeCombinedSecondaryVertexV2BJetTags +
    akPu4CaloPositiveCombinedSecondaryVertexV2BJetTags
    )

akPu4CaloJetBtaggingMu = cms.Sequence(
    akPu4CaloSoftPFMuonsTagInfos *
    akPu4CaloSoftPFMuonBJetTags +
    akPu4CaloSoftPFMuonByIP3dBJetTags +
    akPu4CaloSoftPFMuonByPtBJetTags +
    akPu4CaloNegativeSoftPFMuonByPtBJetTags +
    akPu4CaloPositiveSoftPFMuonByPtBJetTags
    )

akPu4CaloJetBtagging = cms.Sequence(
    akPu4CaloJetBtaggingIP
    * akPu4CaloJetBtaggingSV
    # * akPu4CaloJetBtaggingNegSV
    # * akPu4CaloJetBtaggingMu
    )

akPu4CalopatJetsWithBtagging = patJets.clone(
    jetSource = cms.InputTag("akPu4CaloJets"),
    genJetMatch            = cms.InputTag("akPu4Calomatch"),
    genPartonMatch         = cms.InputTag("akPu4Caloparton"),
    jetCorrFactorsSource   = cms.VInputTag(cms.InputTag("akPu4Calocorr")),
    JetPartonMapSource     = cms.InputTag("akPu4CaloPatJetFlavourAssociationLegacy"),
    JetFlavourInfoSource   = cms.InputTag("akPu4CaloPatJetFlavourAssociation"),
    trackAssociationSource = cms.InputTag("akPu4CaloJetTracksAssociatorAtVertex"),
    useLegacyJetMCFlavour  = True,
    discriminatorSources   = cms.VInputTag(
        cms.InputTag("akPu4CaloSimpleSecondaryVertexHighEffBJetTags"),
        cms.InputTag("akPu4CaloSimpleSecondaryVertexHighPurBJetTags"),
        cms.InputTag("akPu4CaloCombinedSecondaryVertexBJetTags"),
        cms.InputTag("akPu4CaloCombinedSecondaryVertexV2BJetTags"),
        cms.InputTag("akPu4CaloJetBProbabilityBJetTags"),
        cms.InputTag("akPu4CaloJetProbabilityBJetTags"),
        # cms.InputTag("akPu4CaloSoftPFMuonByPtBJetTags"),
        # cms.InputTag("akPu4CaloSoftPFMuonByIP3dBJetTags"),
        cms.InputTag("akPu4CaloTrackCountingHighEffBJetTags"),
        cms.InputTag("akPu4CaloTrackCountingHighPurBJetTags"),
        ),
    tagInfoSources = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"),cms.InputTag("akPu4CaloSecondaryVertexTagInfos")),
    jetIDMap = cms.InputTag("akPu4CaloJetID"),
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

akPu4CaloNjettiness = Njettiness.clone(
    src = cms.InputTag("akPu4CaloJets"),
    R0  = cms.double(0.4)
    )

akPu4CalopatJetsWithBtagging.userData.userFloats.src += [
    'akPu4CaloNjettiness:tau1',
    'akPu4CaloNjettiness:tau2',
    'akPu4CaloNjettiness:tau3']

akPu4CaloJetAnalyzer = inclusiveJetAnalyzer.clone(
    jetTag = cms.InputTag("akPu4CalopatJetsWithBtagging"),
    genjetTag = 'ak4HiSignalGenJets',
    rParam = 0.4,
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
    bTagJetName = cms.untracked.string("akPu4Calo"),
    jetName = cms.untracked.string("akPu4Calo"),
    genPtMin = cms.untracked.double(5),
    hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
    doTower = cms.untracked.bool(False),
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

akPu4CaloJetSequence_mc = cms.Sequence(
    # akPu4Caloclean
    # *
    akPu4Calomatch
    # *
    # akPu4CalomatchGroomed
    *
    akPu4Caloparton
    *
    akPu4Calocorr
    # *
    # akPu4CaloJetID
    *
    akPu4CaloPatJetFlavourIdLegacy
    # *
    # akPu4CaloPatJetFlavourId # Use legacy algo till PU implemented
    *
    akPu4CaloJetTracksAssociatorAtVertex
    *
    akPu4CaloJetBtagging
    *
    # No constituents for calo jets in pp. Must be removed for pp calo jets but
    # I'm not sure how to do this transparently (Marta)
    akPu4CaloNjettiness
    *
    akPu4CalopatJetsWithBtagging
    *
    akPu4CaloJetAnalyzer
    )

akPu4CaloJetSequence_data = cms.Sequence(
    akPu4Calocorr
    *
    # akPu4CaloJetID
    # *
    akPu4CaloJetTracksAssociatorAtVertex
    *
    akPu4CaloJetBtagging
    *
    akPu4CaloNjettiness
    *
    akPu4CalopatJetsWithBtagging
    *
    akPu4CaloJetAnalyzer
    )

akPu4CaloJetSequence_mb = cms.Sequence(
    akPu4CaloJetSequence_mc)
akPu4CaloJetSequence_jec = cms.Sequence(
    akPu4CaloJetSequence_mc)

akPu4CaloJetSequence = cms.Sequence(
    akPu4CaloJetSequence_data)
