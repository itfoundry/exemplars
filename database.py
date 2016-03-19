#!/usr/bin/env python
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals

class _BaseObject(object):
    NAMES = []
    def __init__(self, name):
        self.name = name

    def key(self):
        return self.NAMES.index(self.name)

    def __repr__(self):
        return '<{} object: {}>'.format(self.__class__.__name__, self.name)

class Language(_BaseObject):
    NAMES = [
        'Sanskrit',
        'Hindi',
        'Marathi',
        'Nepali',
        'Gujarati',
        'Punjabi',
        'Bangla',
        'Assamese',
        'Odia',
        'Telugu',
        'Kannada',
        'Malayalam',
        'Tamil',
        'Sinhala',
    ]
    def __init__(self, name):
        super(Language, self).__init__(name)
        self.scripts = set()

class Script(_BaseObject):
    NAMES = [
        'Devanagari',
        'Gujarati',
        'Gurmukhi',
        'Bangla',
        'Odia',
        'Telugu',
        'Kannada',
        'Malayalam',
        'Tamil',
        'Sinhala',
    ]
    def __init__(self, name):
        super(Script, self).__init__(name)
        self.languages = set()

class UnicodeSet(set):
    def __init__(self, iterable):
        super(UnicodeSet, self).__init__(iterable)
        self.ordered = sorted(self, key=lambda i: iterable.index(i))

class ExemplarCharacters(object):

    @staticmethod
    def parse(string):
        if string:
            return UnicodeSet(''.join(string.split()))
        else:
            return UnicodeSet('')

    def __init__(self, main=None, auxiliary=None, index=None, punctuation=None):
        self.main = self.parse(main)
        self.auxiliary = self.parse(auxiliary)
        self.index = self.parse(index)
        self.punctuation = self.parse(punctuation)

class WritingSystem(_BaseObject):

    def __init__(self, language, script, name=None, exemplar_characters=None):

        self.language = language
        self.language.scripts.add(script)
        self.script = script
        self.script.languages.add(language)

        if not name:
            if self.script.name == self.language.name:
                name = self.language.name
            else:
                name = '{} in {}'.format(self.language.name, self.script.name)

        super(WritingSystem, self).__init__(name)

        self.exemplar_characters = ExemplarCharacters(**exemplar_characters)

    def key(self):
        return self.script.key(), self.language.key()

LANGUAGES = {name: Language(name) for name in Language.NAMES}

SCRIPTS = {name: Script(name) for name in Script.NAMES}

WRITING_SYSTEMS = {
    'Sanskrit in Devanagari': WritingSystem(
        LANGUAGES['Sanskrit'], SCRIPTS['Devanagari'],
        exemplar_characters = {
            'main': '''
                अआइईउऊ ऋॠऌॡ एऐओऔ
                \N{DEVANAGARI VOWEL SIGN AA}
                \N{DEVANAGARI VOWEL SIGN I}
                \N{DEVANAGARI VOWEL SIGN II}
                \N{DEVANAGARI VOWEL SIGN U}
                \N{DEVANAGARI VOWEL SIGN UU}
                \N{DEVANAGARI VOWEL SIGN VOCALIC R}
                \N{DEVANAGARI VOWEL SIGN VOCALIC RR}
                \N{DEVANAGARI VOWEL SIGN VOCALIC L}
                \N{DEVANAGARI VOWEL SIGN VOCALIC LL}
                \N{DEVANAGARI VOWEL SIGN E}
                \N{DEVANAGARI VOWEL SIGN AI}
                \N{DEVANAGARI VOWEL SIGN O}
                \N{DEVANAGARI VOWEL SIGN AU}
                कखगघङ चछजझञ टठडढण तथदधन पफबभम यरलव शषसह
                \N{DEVANAGARI SIGN ANUSVARA}
                \N{DEVANAGARI SIGN VISARGA}
                \N{DEVANAGARI SIGN VIRAMA}
                \N{DEVANAGARI SIGN AVAGRAHA}
            ''',
        },
    ),
    'Hindi': WritingSystem(
        LANGUAGES['Hindi'], SCRIPTS['Devanagari'],
        name = 'Hindi',
        exemplar_characters = {
            'main': '''
                अआइईउऊ ऋ एऐओऔ
                \N{DEVANAGARI VOWEL SIGN AA}
                \N{DEVANAGARI VOWEL SIGN I}
                \N{DEVANAGARI VOWEL SIGN II}
                \N{DEVANAGARI VOWEL SIGN U}
                \N{DEVANAGARI VOWEL SIGN UU}
                \N{DEVANAGARI VOWEL SIGN VOCALIC R}
                \N{DEVANAGARI VOWEL SIGN E}
                \N{DEVANAGARI VOWEL SIGN AI}
                \N{DEVANAGARI VOWEL SIGN O}
                \N{DEVANAGARI VOWEL SIGN AU}
                कखगघङ चछजझञ टठडढण तथदधन पफबभम यरलव शषसह
                \N{DEVANAGARI SIGN ANUSVARA}
                \N{DEVANAGARI SIGN VIRAMA}
            ''',
        },
    ),
    'Marathi': WritingSystem(
        LANGUAGES['Marathi'], SCRIPTS['Devanagari'],
        name = 'Marathi',
        exemplar_characters = {
            'main': '''
                अआइईउऊ ऋ एऐओऔ
                \N{DEVANAGARI VOWEL SIGN AA}
                \N{DEVANAGARI VOWEL SIGN I}
                \N{DEVANAGARI VOWEL SIGN II}
                \N{DEVANAGARI VOWEL SIGN U}
                \N{DEVANAGARI VOWEL SIGN UU}
                \N{DEVANAGARI VOWEL SIGN VOCALIC R}
                \N{DEVANAGARI VOWEL SIGN E}
                \N{DEVANAGARI VOWEL SIGN AI}
                \N{DEVANAGARI VOWEL SIGN O}
                \N{DEVANAGARI VOWEL SIGN AU}
                कखगघङ चछजझञ टठडढण तथदधन पफबभम यरलव शषसह ळ
                \N{DEVANAGARI SIGN ANUSVARA}
                \N{DEVANAGARI SIGN VIRAMA}
            ''',
        },
    ),
    'Gujarati': WritingSystem(
        LANGUAGES['Gujarati'], SCRIPTS['Gujarati'],
        exemplar_characters = {
            'main': '''
                અઆઇઈઉઊ ઋ એઐઓઔ
                \N{GUJARATI VOWEL SIGN AA}
                \N{GUJARATI VOWEL SIGN I}
                \N{GUJARATI VOWEL SIGN II}
                \N{GUJARATI VOWEL SIGN U}
                \N{GUJARATI VOWEL SIGN UU}
                \N{GUJARATI VOWEL SIGN VOCALIC R}
                \N{GUJARATI VOWEL SIGN E}
                \N{GUJARATI VOWEL SIGN AI}
                \N{GUJARATI VOWEL SIGN O}
                \N{GUJARATI VOWEL SIGN AU}
                કખગઘઙ ચછજઝઞ ટઠડઢણ તથદધન પફબભમ યરલવ શષસહ ળ
                \N{GUJARATI SIGN ANUSVARA}
                \N{GUJARATI SIGN VIRAMA}
            ''',
        },
    ),
    'Punjabi in Gurmukhi': WritingSystem(
        LANGUAGES['Punjabi'], SCRIPTS['Gurmukhi'],
        exemplar_characters = {
            'main': '''
                ਅਆਇਈਉਊ ਏਐਓਔ ੲੳ
                \N{GURMUKHI VOWEL SIGN AA}
                \N{GURMUKHI VOWEL SIGN I}
                \N{GURMUKHI VOWEL SIGN II}
                \N{GURMUKHI VOWEL SIGN U}
                \N{GURMUKHI VOWEL SIGN UU}
                \N{GURMUKHI VOWEL SIGN EE}
                \N{GURMUKHI VOWEL SIGN AI}
                \N{GURMUKHI VOWEL SIGN OO}
                \N{GURMUKHI VOWEL SIGN AU}
                ਕਖਗਘਙ ਚਛਜਝਞ ਟਠਡਢਣ ਤਥਦਧਨ ਪਫਬਭਮ ਯਰਲਵ ਸਹ ੜ
                \N{GURMUKHI SIGN BINDI}
                \N{GURMUKHI TIPPI}
                \N{GURMUKHI SIGN VIRAMA}
                \N{GURMUKHI ADDAK}
            ''',
        },
    ),
    'Bangla': WritingSystem(
        LANGUAGES['Bangla'], SCRIPTS['Bangla'],
        exemplar_characters = {
            'main': '''
                অআইঈউঊ ঋ এঐওঔ
                \N{BENGALI VOWEL SIGN AA}
                \N{BENGALI VOWEL SIGN I}
                \N{BENGALI VOWEL SIGN II}
                \N{BENGALI VOWEL SIGN U}
                \N{BENGALI VOWEL SIGN UU}
                \N{BENGALI VOWEL SIGN VOCALIC R}
                \N{BENGALI VOWEL SIGN E}
                \N{BENGALI VOWEL SIGN AI}
                \N{BENGALI VOWEL SIGN O}
                \N{BENGALI VOWEL SIGN AU}
                \N{BENGALI AU LENGTH MARK}
                কখগঘঙ চছজঝঞ টঠডঢণ তথদধন পফবভম যরল শষসহ
                \N{BENGALI SIGN ANUSVARA}
                \N{BENGALI SIGN VIRAMA}
            ''',
        },
    ),
    'Assamese': WritingSystem(
        LANGUAGES['Assamese'], SCRIPTS['Bangla'],
        name = 'Assamese',
        exemplar_characters = {
            'main': '''
                অআইঈউঊ ঋ এঐওঔ
                \N{BENGALI VOWEL SIGN AA}
                \N{BENGALI VOWEL SIGN I}
                \N{BENGALI VOWEL SIGN II}
                \N{BENGALI VOWEL SIGN U}
                \N{BENGALI VOWEL SIGN UU}
                \N{BENGALI VOWEL SIGN VOCALIC R}
                \N{BENGALI VOWEL SIGN E}
                \N{BENGALI VOWEL SIGN AI}
                \N{BENGALI VOWEL SIGN O}
                \N{BENGALI VOWEL SIGN AU}
                \N{BENGALI AU LENGTH MARK}
                কখগঘঙ চছজঝঞ টঠডঢণ তথদধন পফবভম যৰলৱ শষসহ
                \N{BENGALI SIGN ANUSVARA}
                \N{BENGALI SIGN VIRAMA}
            ''',
        },
    ),
    'Odia': WritingSystem(
        LANGUAGES['Odia'], SCRIPTS['Odia'],
        exemplar_characters = {
            'main': '''
                ଅଆଇଈଉଊ ଋ ଏଐଓଔ
                \N{ORIYA VOWEL SIGN AA}
                \N{ORIYA VOWEL SIGN I}
                \N{ORIYA VOWEL SIGN II}
                \N{ORIYA VOWEL SIGN U}
                \N{ORIYA VOWEL SIGN UU}
                \N{ORIYA VOWEL SIGN VOCALIC R}
                \N{ORIYA VOWEL SIGN E}
                \N{ORIYA VOWEL SIGN AI}
                \N{ORIYA VOWEL SIGN O}
                \N{ORIYA VOWEL SIGN AU}
                \N{ORIYA AI LENGTH MARK}
                \N{ORIYA AU LENGTH MARK}
                କଖଗଘଙ ଚଛଜଝଞ ଟଠଡଢଣ ତଥଦଧନ ପଫବଭମ ଯୟରଳଲ ଶଷସହ
                \N{ORIYA SIGN ANUSVARA}
                \N{ORIYA SIGN VIRAMA}
            ''',
        },
    ),
    'Telugu': WritingSystem(
        LANGUAGES['Telugu'], SCRIPTS['Telugu'],
        exemplar_characters = {
            'main': '''
                అఆఇఈఉఊ ఋ ఎఏఐఒఓఔ
                \N{TELUGU VOWEL SIGN AA}
                \N{TELUGU VOWEL SIGN I}
                \N{TELUGU VOWEL SIGN II}
                \N{TELUGU VOWEL SIGN U}
                \N{TELUGU VOWEL SIGN UU}
                \N{TELUGU VOWEL SIGN VOCALIC R}
                \N{TELUGU VOWEL SIGN E}
                \N{TELUGU VOWEL SIGN EE}
                \N{TELUGU VOWEL SIGN AI}
                \N{TELUGU VOWEL SIGN O}
                \N{TELUGU VOWEL SIGN OO}
                \N{TELUGU VOWEL SIGN AU}
                \N{TELUGU AI LENGTH MARK}
                కఖగఘఙ చఛజఝఞ టఠడఢణ తథదధన పఫబభమ యరలవ ళ శషసహ ఱ
                \N{TELUGU SIGN ANUSVARA}
                \N{TELUGU SIGN CANDRABINDU}
                \N{TELUGU SIGN VIRAMA}
            ''',
        },
    ),
    'Kannada': WritingSystem(
        LANGUAGES['Kannada'], SCRIPTS['Kannada'],
        exemplar_characters = {
            'main': '''
                ಅಆಇಈಉಊ ಋ ಎಏಐಒಓಔ
                \N{KANNADA VOWEL SIGN AA}
                \N{KANNADA VOWEL SIGN I}
                \N{KANNADA VOWEL SIGN II}
                \N{KANNADA VOWEL SIGN U}
                \N{KANNADA VOWEL SIGN UU}
                \N{KANNADA VOWEL SIGN VOCALIC R}
                \N{KANNADA VOWEL SIGN E}
                \N{KANNADA VOWEL SIGN EE}
                \N{KANNADA VOWEL SIGN AI}
                \N{KANNADA VOWEL SIGN O}
                \N{KANNADA VOWEL SIGN OO}
                \N{KANNADA VOWEL SIGN AU}
                \N{KANNADA LENGTH MARK}
                \N{KANNADA AI LENGTH MARK}
                ಕಖಗಘಙ ಚಛಜಝಞ ಟಠಡಢಣ ತಥದಧನ ಪಫಬಭಮ ಯರಲವ ಶಷಸಹ ಳ
                \N{KANNADA SIGN ANUSVARA}
                \N{KANNADA SIGN VIRAMA}
            ''',
        },
    ),
    'Malayalam': WritingSystem(
        LANGUAGES['Malayalam'], SCRIPTS['Malayalam'],
        exemplar_characters = {
            'main': '''
                അആഇഈഉഊ ഋ എഏഐഒഓഔ
                \N{MALAYALAM VOWEL SIGN AA}
                \N{MALAYALAM VOWEL SIGN I}
                \N{MALAYALAM VOWEL SIGN II}
                \N{MALAYALAM VOWEL SIGN U}
                \N{MALAYALAM VOWEL SIGN UU}
                \N{MALAYALAM VOWEL SIGN VOCALIC R}
                \N{MALAYALAM VOWEL SIGN E}
                \N{MALAYALAM VOWEL SIGN EE}
                \N{MALAYALAM VOWEL SIGN AI}
                \N{MALAYALAM VOWEL SIGN O}
                \N{MALAYALAM VOWEL SIGN OO}
                \N{MALAYALAM VOWEL SIGN AU}
                \N{MALAYALAM AU LENGTH MARK}
                കഖഗഘങ ചഛജഝഞ ടഠഡഢണ തഥദധന പഫബഭമ യരലവ ശഷസഹ ളഴറ
                \N{MALAYALAM SIGN ANUSVARA}
                \N{MALAYALAM SIGN VIRAMA}
            ''',
        },
    ),
    'Tamil': WritingSystem(
        LANGUAGES['Tamil'], SCRIPTS['Tamil'],
        exemplar_characters = {
            'main': '''
                அஆஇஈஉஊ எஏஐஒஓஔ
                \N{TAMIL VOWEL SIGN AA}
                \N{TAMIL VOWEL SIGN I}
                \N{TAMIL VOWEL SIGN II}
                \N{TAMIL VOWEL SIGN U}
                \N{TAMIL VOWEL SIGN UU}
                \N{TAMIL VOWEL SIGN E}
                \N{TAMIL VOWEL SIGN EE}
                \N{TAMIL VOWEL SIGN AI}
                \N{TAMIL VOWEL SIGN O}
                \N{TAMIL VOWEL SIGN OO}
                \N{TAMIL VOWEL SIGN AU}
                \N{TAMIL AU LENGTH MARK}
                கங சஞ டண தந பம யரலவ ழளறன ஐ ஷஸஹ
                \N{TAMIL SIGN VIRAMA}
            ''',
        },
    ),
    'Sinhala': WritingSystem(
        LANGUAGES['Sinhala'], SCRIPTS['Sinhala'],
        exemplar_characters = {
            'main': '''
                අආඇඈඉඊඋඌ ඍ එඒඔඕ
                \N{SINHALA VOWEL SIGN AELA-PILLA}
                \N{SINHALA VOWEL SIGN KETTI AEDA-PILLA}
                \N{SINHALA VOWEL SIGN DIGA AEDA-PILLA}
                \N{SINHALA VOWEL SIGN KETTI IS-PILLA}
                \N{SINHALA VOWEL SIGN DIGA IS-PILLA}
                \N{SINHALA VOWEL SIGN KETTI PAA-PILLA}
                \N{SINHALA VOWEL SIGN DIGA PAA-PILLA}
                \N{SINHALA VOWEL SIGN GAETTA-PILLA}
                \N{SINHALA VOWEL SIGN KOMBUVA}
                \N{SINHALA VOWEL SIGN DIGA KOMBUVA}
                \N{SINHALA VOWEL SIGN KOMBUVA HAA AELA-PILLA}
                \N{SINHALA VOWEL SIGN KOMBUVA HAA DIGA AELA-PILLA}
                කඛගඝඞ ඟ චඡජඣඤ ටඨඩඪණ ඬ තථදධන ඳ පඵබභම ඹ යරලව ළ ශෂසහ ෆ
                \N{SINHALA SIGN ANUSVARAYA}
                \N{SINHALA SIGN AL-LAKUNA}
            ''',
        },
    ),
}

with open('README.md', 'w') as f:

    lines = [
        '# Exemplars',
        '',
        'This "README" is generated by `database.py`.',
    ]

    for ws in sorted(WRITING_SYSTEMS.values(), key=lambda i: i.key()):

        lines.append('')

        lines.append('## {}'.format(ws.name))

        lines.append('')

        lines.append('- Language: {}'.format(ws.language.name))

        line_about_script = '- Script: {}'.format(ws.script.name)
        if len(ws.script.languages) > 1:
            line_about_script += ' (also used for {})'.format(
                ', '.join(
                    i.name for i
                    in sorted(ws.script.languages, key=lambda j: j.key())
                    if i is not ws.language
                )
            )
        lines.append(line_about_script)

        lines.append(
            '- Exemplar set "main": [{}]'.format(
                ' '.join(ws.exemplar_characters.main.ordered)
            )
        )

    f.writelines((line + '\n').encode('UTF-8') for line in lines)
