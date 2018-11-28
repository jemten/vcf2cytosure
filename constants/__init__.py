# constants

PROBE_SPACING = 100000
MAX_HEIGHT = 4
ABERRATION_HEIGHTS = {
	'DEL': -1.0,
	'DUP': +1.0,
	'TDUP': +1.5,
	'IDUP': +0.5,
	'INV': -0.5,
	'INS': -1.5,
	'BND': -2.0,
	'TRA': -2.0,
}

# Hard-coded data about GRCh37 follows.
# Whenever GRCh38 becomes relevant, use external .fai and .bed files instead.
CONTIG_LENGTHS = {
	'1':  249250621,
	'2':  243199373,
	'3':  198022430,
	'4':  191154276,
	'5':  180915260,
	'6':  171115067,
	'7':  159138663,
	'8':  146364022,
	'9':  141213431,
	'10': 135534747,
	'11': 135006516,
	'12': 133851895,
	'13': 115169878,
	'14': 107349540,
	'15': 102531392,
	'16':  90354753,
	'17':  81195210,
	'18':  78077248,
	'19':  59128983,
	'20':  63025520,
	'21':  48129895,
	'22':  51304566,
	'X':  155270560,
	'Y':   59373566,
}
# Intervals at which the reference contains N bases
N_INTERVALS = {
	'1': [
		(0, 10000),
		(177417, 227417),
		(267719, 317719),
		(471368, 521368),
		(2634220, 2684220),
		(3845268, 3995268),
		(13052998, 13102998),
		(13219912, 13319912),
		(13557162, 13607162),
		(17125658, 17175658),
		(29878082, 30028082),
		(103863906, 103913906),
		(120697156, 120747156),
		(120936695, 121086695),
		(121485434, 142535434),
		(142731022, 142781022),
		(142967761, 143117761),
		(143292816, 143342816),
		(143544525, 143644525),
		(143771002, 143871002),
		(144095783, 144145783),
		(144224481, 144274481),
		(144401744, 144451744),
		(144622413, 144672413),
		(144710724, 144810724),
		(145833118, 145883118),
		(146164650, 146214650),
		(146253299, 146303299),
		(148026038, 148176038),
		(148361358, 148511358),
		(148684147, 148734147),
		(148954460, 149004460),
		(149459645, 149509645),
		(205922707, 206072707),
		(206332221, 206482221),
		(223747846, 223797846),
		(235192211, 235242211),
		(248908210, 249058210),
		(249240621, 249250621),
	],
	'2': [
		(0, 10000),
		(3529312, 3579312),
		(5018788, 5118788),
		(16279724, 16329724),
		(21153113, 21178113),
		(31725939, 31726790),
		(33092197, 33093197),
		(33141692, 33142692),
		(87668206, 87718206),
		(89630436, 89830436),
		(90321525, 90371525),
		(90545103, 91595103),
		(92326171, 95326171),
		(110109337, 110251337),
		(149690582, 149790582),
		(234003741, 234053741),
		(239801978, 239831978),
		(240784132, 240809132),
		(243102476, 243152476),
		(243189373, 243199373),
	],
	'3': [
		(0, 60000),
		(66170270, 66270270),
		(90504854, 93504854),
		(194041961, 194047251),
		(197962430, 198022430),
	],
	'4': [
		(0, 10000),
		(1423146, 1478646),
		(8799203, 8818203),
		(9274642, 9324642),
		(31820917, 31837417),
		(32834638, 32840638),
		(40296396, 40297096),
		(49338941, 49488941),
		(49660117, 52660117),
		(59739333, 59789333),
		(75427379, 75452279),
		(191044276, 191154276),
	],
	'5': [
		(0, 10000),
		(17530657, 17580657),
		(46405641, 49405641),
		(91636128, 91686128),
		(138787073, 138837073),
		(155138727, 155188727),
		(180905260, 180915260),
	],
	'6': [
		(0, 60000),
		(58087659, 58137659),
		(58780166, 61880166),
		(62128589, 62178589),
		(95680543, 95830543),
		(157559467, 157609467),
		(157641300, 157691300),
		(167942073, 168042073),
		(170279972, 170329972),
		(171055067, 171115067),
	],
	'7': [
		(0, 10000),
		(232484, 282484),
		(50370631, 50410631),
		(58054331, 61054331),
		(61310513, 61360513),
		(61460465, 61510465),
		(61677020, 61727020),
		(61917157, 61967157),
		(74715724, 74765724),
		(100556043, 100606043),
		(130154523, 130254523),
		(139379377, 139404377),
		(142048195, 142098195),
		(142276197, 142326197),
		(143347897, 143397897),
		(154270634, 154370634),
		(159128663, 159138663),
	],
	'8': [
		(0, 10000),
		(7474649, 7524649),
		(12091854, 12141854),
		(43838887, 46838887),
		(48130499, 48135599),
		(86576451, 86726451),
		(142766515, 142816515),
		(145332588, 145432588),
		(146304022, 146364022),
	],
	'9': [
		(0, 10000),
		(39663686, 39713686),
		(39974796, 40024796),
		(40233029, 40283029),
		(40425834, 40475834),
		(40940341, 40990341),
		(41143214, 41193214),
		(41365793, 41415793),
		(42613955, 42663955),
		(43213698, 43313698),
		(43946569, 43996569),
		(44676646, 44726646),
		(44908293, 44958293),
		(45250203, 45350203),
		(45815521, 45865521),
		(46216430, 46266430),
		(46461039, 46561039),
		(47060133, 47160133),
		(47317679, 65467679),
		(65918360, 65968360),
		(66192215, 66242215),
		(66404656, 66454656),
		(66614195, 66664195),
		(66863343, 66913343),
		(67107834, 67207834),
		(67366296, 67516296),
		(67987998, 68137998),
		(68514181, 68664181),
		(68838946, 68988946),
		(69278385, 69328385),
		(70010542, 70060542),
		(70218729, 70318729),
		(70506535, 70556535),
		(70735468, 70835468),
		(92343416, 92443416),
		(92528796, 92678796),
		(133073060, 133223060),
		(137041193, 137091193),
		(139166997, 139216997),
		(141153431, 141213431),
	],
	'10': [
		(0, 60000),
		(17974675, 18024675),
		(38818835, 38868835),
		(39154935, 42354935),
		(42546687, 42596687),
		(46426964, 46476964),
		(47429169, 47529169),
		(47792476, 47892476),
		(48055707, 48105707),
		(49095536, 49195536),
		(51137410, 51187410),
		(51398845, 51448845),
		(125869472, 125919472),
		(128616069, 128766069),
		(133381404, 133431404),
		(133677527, 133727527),
		(135524747, 135534747),
	],
	'11': [
		(0, 60000),
		(1162759, 1212759),
		(50783853, 51090853),
		(51594205, 54694205),
		(69089801, 69139801),
		(69724695, 69774695),
		(87688378, 87738378),
		(96287584, 96437584),
		(134946516, 135006516),
	],
	'12': [
		(0, 60000),
		(95739, 145739),
		(7189876, 7239876),
		(34856694, 37856694),
		(109373470, 109423470),
		(121965036, 121965236),
		(122530623, 122580623),
		(123928080, 123928280),
		(132706992, 132806992),
		(133841895, 133851895),
	],
	'13': [
		(0, 19020000),
		(86760324, 86910324),
		(112353994, 112503994),
		(114325993, 114425993),
		(114639948, 114739948),
		(115109878, 115169878),
	],
	'14': [
		(0, 19000000),
		(107289540, 107349540),
	],
	'15': [
		(0, 20000000),
		(20894633, 20935075),
		(21398819, 21885000),
		(22212114, 22262114),
		(22596193, 22646193),
		(23514853, 23564853),
		(29159443, 29209443),
		(82829645, 82879645),
		(84984473, 85034473),
		(102521392, 102531392),
	],
	'16': [
		(0, 60000),
		(8636921, 8686921),
		(34023150, 34173150),
		(35285801, 46385801),
		(88389383, 88439383),
		(90294753, 90354753),
	],
	'17': [
		(296626, 396626),
		(21566608, 21666608),
		(22263006, 25263006),
		(34675848, 34725848),
		(62410760, 62460760),
		(77546461, 77596461),
		(79709049, 79759049),
	],
	'18': [
		(0, 10000),
		(15410898, 18510898),
		(52059136, 52209136),
		(72283353, 72333353),
		(75721820, 75771820),
		(78017248, 78077248),
	],
	'19': [
		(0, 60000),
		(7346004, 7396004),
		(8687198, 8737198),
		(20523415, 20573415),
		(24631782, 27731782),
		(59118983, 59128983),
	],
	'20': [
		(0, 60000),
		(26319569, 29419569),
		(29653908, 29803908),
		(34897085, 34947085),
		(61091437, 61141437),
		(61213369, 61263369),
		(62965520, 63025520),
	],
	'21': [
		(0, 9411193),
		(9595548, 9645548),
		(9775437, 9825437),
		(10034920, 10084920),
		(10215976, 10365976),
		(10647896, 10697896),
		(11188129, 14338129),
		(42955559, 43005559),
		(43226828, 43227328),
		(43249342, 43250842),
		(44632664, 44682664),
		(48119895, 48129895),
	],
	'22': [
		(0, 16050000),
		(16697850, 16847850),
		(20509431, 20609431),
		(50364777, 50414777),
		(51244566, 51304566),
	],
	'X': [
		(0, 60000),
		(94821, 144821),
		(231384, 281384),
		(1047557, 1097557),
		(1134113, 1184113),
		(1264234, 1314234),
		(2068238, 2118238),
		(7623882, 7673882),
		(10738674, 10788674),
		(37098256, 37148256),
		(49242997, 49292997),
		(49974173, 50024173),
		(52395914, 52445914),
		(58582012, 61682012),
		(76653692, 76703692),
		(113517668, 113567668),
		(115682290, 115732290),
		(120013235, 120063235),
		(143507324, 143557324),
		(148906424, 148956424),
		(149032062, 149082062),
		(152277099, 152327099),
		(155260560, 155270560),
	],
	'Y': [
		(0, 2649520),
		(8914955, 8964955),
		(9241322, 9291322),
		(10104553, 13104553),
		(13143954, 13193954),
		(13748578, 13798578),
		(20143885, 20193885),
		(22369679, 22419679),
		(23901428, 23951428),
		(28819361, 58819361),
		(58917656, 58967656),
		(59034049, 59373566),
	]
}

CHROM_RENAME = {'X': '23', 'Y': '24'}

CGH_TEMPLATE = u"""
<data formatVersion="2">
<pgdData><pgdDataEntry key="SPECIMEN_TYPE" value="BLASTOMERE"/></pgdData>
<noResults>
</noResults>
<pgd_reagents/>
<cgh mother="-1" father="-1" genomeBuild="hg19" softwareVersion="4.8.32" batched="false">
  <submission design="031035" feFile="dummy.txt" cghFile="dummy.cgh" scanDate="1462520414000" barcode="253103511677_1_3" sampleCy3="true">
  <notes/>
  <sample sampleId="{}" male="{}"><phenotype/></sample>
  <reference sampleId="Promega {}" male="{}"><phenotype/></reference>
  <extra>
    <datum category="Nanodrop" type="Sample DNA (ng)" dataType="Float"/>
    <datum category="Sample Extraction" type="Sample Arrival Date" dataType="Date"/>
    <datum category="Sample Extraction" type="Specimen Type" dataType="List">Blood</datum>
    <datum category="Labelling" type="Lab User" dataType="String"/>
    <datum category="Hyb &amp; Wash" type="Cot1 Batch" dataType="String"/>
    <datum category="Sample Extraction" type="Extraction Method" dataType="String"/>
    <datum category="General" type="Reference Concentration" dataType="Float"/>
    <datum category="Sample Extraction" type="A260/A280" dataType="Float"/>
    <datum category="General" type="Assigned Technologist" dataType="String">MF</datum>
    <datum category="Nanodrop" type="Reference DNA (pmoles)" dataType="Float"/>
    <datum category="Labelling" type="Columns Used" dataType="List">Qiagen</datum>
    <datum category="Nanodrop" type="Sample DNA (A260/A280)" dataType="Float"/>
    <datum category="Labelling" type="Column Batch No" dataType="String"/>
    <datum category="Sample Extraction" type="Extracted By" dataType="String"/>
    <datum category="Hyb &amp; Wash" type="Hyb Protocol" dataType="String"/>
    <datum category="Labelling" type="Experiment Date" dataType="Date"/>
    <datum category="General" type="Case Status" dataType="List"/>
    <datum category="Labelling" type="Lab Notes" dataType="Text"/>
    <datum category="Hyb &amp; Wash" type="Hyb Buffer Batch" dataType="String"/>
    <datum category="Nanodrop" type="Reference DNA (A260/A280)" dataType="Float"/>
    <datum category="Labelling" type="Labelling Reagent Batch No" dataType="String"/>
    <datum category="Hyb &amp; Wash" type="Wash Protocol" dataType="String"/>
    <datum category="Labelling" type="Labelling Protocol" dataType="List">Enzo</datum>
    <datum category="Nanodrop" type="Reference DNA (ng)" dataType="Float"/>
    <datum category="Nanodrop" type="Sample DNA (pmoles)" dataType="Float"/>
  </extra>
</submission>
<excludedRegions>
</excludedRegions>
<qc>
<aqf key="SPIKES" value="null"/>
<aqf key="DLRSPREAD" value="0.1"/>
<aqf key="RED_SIGNAL_INTENSITY" value="1000.0"/>
<aqf key="GREEN_SIGNAL_INTENSITY" value="1000.0"/>
<aqf key="BG_NOISE_RED" value="5.0"/>
<aqf key="BG_NOISE_GREEN" value="5.0"/>
<aqf key="RED_SNR" value="100.0"/>
<aqf key="GREEN_SNR" value="100.0"/>
<aqf key="COMPARATIVE_SIGNAL_INTENSITY" value="0.11111111111"/>
<aqf key="REPRODUCIBILITY_GREEN" value="0.1111111"/>
<aqf key="REPRODUCIBILITY_RED" value="0.1111111"/>
<aqf key="NEG_CONTROL_RED" value="1.1111111"/>
<aqf key="NEG_CONTROL_GREEN" value="1.1111111"/>
<aqf key="FLAG_PERC" value="0.00722363"/>
<aqf key="SAT_PERC" value="0.0"/>
<aqf key="WAVINESS" value="0.0011111"/>
<aqf key="SNP_TROUGH_PEAK_RATIO" value="null"/>
<aqf key="SNP_GREY_AREA" value="null"/>
<aqf key="SNP_Red_Signal_Intensity" value="NaN"/>
<aqf key="SNP_Green_Signal_Intensity" value="NaN"/>
<aqf key="SNP_Ratio_Separation" value="0.0"/>
xoxoxo<aqf key="Percentage_Homozygosity" value="NaN"/>
<aqf key="SD" value="0.111111"/>
</qc>
<probes></probes>
<segmentation type="NORMALIZED"></segmentation>
</cgh>
</data>
"""
