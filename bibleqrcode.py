"""Generate a QR code that opens the YouVersion Bible app on Android to any desired chapter and verse
"""

import pyqrcode
import argparse

"""
Returns an intent URI to load a book, chapter and verse from the Bible
@param book_name - Plaintext name of the desired bible book, e.g. 'Genesis' (required)
@param chapter - Integer chapter number (required)
@param verse_start - Integer verse number to start at (optional)
@param verse_end - Integer verse number to end at (optional)
@param version - Three leter version code, e.g. "KJV"
"""
def get_intent_url(book_name, chapter, verse_start=None, verse_end=None, version=None):

    # Sanity check - can't have verse end without verse start
    if verse_end is not None:
        if verse_start is None:
            verse_start = verse_end

    # URL template for www.bible.com
    url_template = "https://www.bible.com/en-GB/bible/{version_code}/{book_code}{chapter}{verse_start}{verse_end}"

    # Book name mappings for www.bible.com
    book_mappings = {
        "Genesis": "GEN",
        "Exodus": "EXO",
        "Leviticus": "LEV",
        "Numbers": "NUM",
        "Deuteronomy": "DEU",
        "Joshua": "JOS",
        "Judges": "JDG",
        "Ruth": "RUT",
        "1 Samuel": "1SA",
        "2 Samuel": "2SA",
        "1 Kings": "1KI",
        "2 Kings": "2KI",
        "1 Chronicles": "1CH",
        "2 Chronicles": "2CH",
        "Ezra": "EZR",
        "Nehemiah": "NEH",
        "Esther": "EST",
        "Job": "JOB",
        "Psalms": "PSA",
        "Proverbs": "PRO",
        "Ecclesiastes": "ECC",
        "Song of Solomon": "SNG",
        "Isaiah": "ISA",
        "Jeremiah": "JER",
        "Lamentations": "LAM",
        "Ezekiel": "EZK",
        "Daniel": "DAN",
        "Hosea": "HOS",
        "Joel": "JOL",
        "Amos": "AMO",
        "Obadiah": "OBA",
        "Jonah": "JON",
        "Micah": "MIC",
        "Nahum": "NAM",
        "Habakkuk": "HAB",
        "Zephaniah": "ZEP",
        "Haggai": "HAG",
        "Zechariah": "ZEC",
        "Malachi": "MAL",
        "Matthew": "MAT",
        "Mark": "MRK",
        "Luke": "LUK",
        "John": "JHN",
        "Acts": "ACT",
        "Romans": "ROM",
        "1 Corinthians": "1CO",
        "2 Corinthians": "2CO",
        "Galatians": "GAL",
        "Ephesians": "EPH",
        "Philippians": "PHP",
        "Colossians": "COL",
        "1 Thessalonians": "1TH",
        "2 Thessalonians": "2TH",
        "1 Timothy": "1TI",
        "2 Timothy": "2TI",
        "Titus": "TIT",
        "Philemon": "PHM",
        "Hebrews": "HEB",
        "James": "JAS",
        "1 Peter": "1PE",
        "2 Peter": "2PE",
        "1 John": "1JN",
        "2 John": "2JN",
        "3 John": "3JN",
        "Jude": "JUD",
        "Revelation": "REV"
    }

    # Look up the www.bible.com book code
    book_code = None
    if book_name in book_mappings:
        book_code = book_mappings[book_name]
    
    if book_code is None:
        raise ValueError("Unknown book name: '{0}'".format(book_name))

    # Check www.bible.com for version codes
    version_code = get_version_code(version)

    url = url_template.format(
        version_code = version_code,
        book_code = book_code,
        chapter = "." + str(chapter),
        verse_start = "" if (verse_start == None) else ("." + str(verse_start)),
        verse_end = "" if (verse_end == None) else ("-" + str(verse_end)),
    )

    return url


"""
Get version code from letter abbreviation
@param version - version abbreviation (required)
"""
def get_version_code(version):
    if version is None:
        # Version 1 is KJV
        return 1

    if version.isdigit():
        # Probably already is a version code
        return version

    versions = {
        "AMP": 1588,
        "AMPC": 8,
        "ASV": 12,
        "BOOKS": 31,
        "BSB": 3034,
        "CEB": 37,
        "CEV": 392,
        "CEVDCI": 303,
        "CEVUK": 294,
        "CJB": 1275,
        "CPDV": 42,
        "CSB": 1713,
        "DARBY": 478,
        "DRC1752": 55,
        "EASY": 2079,
        "ERV": 406,
        "ESV": 59,
        "FBV": 1932,
        "GNBDC": 416,
        "GNBDK": 431,
        "GNBUK": 296,
        "GNT": 68,
        "GNTD": 69,
        "GNV": 2163,
        "GW": 70,
        "GWC": 1047,
        "HCSB": 72,
        "ICB": 1359,
        "JUB": 1077,
        "KJV": 1,
        "KJVAAE": 546,
        "KJVAE": 547,
        "LEB": 90,
        "MEV": 1171,
        "MP1650": 1365,
        "MP1781": 3051,
        "MSG": 97,
        "NABRE": 463,
        "NASB1995": 100,
        "NASB2020": 2692,
        "NCV": 105,
        "NET": 107,
        "NIRV": 110,
        "NIV": 111,
        "NIVUK": 113,
        "NKJV": 114,
        "NLT": 116,
        "NMV": 2135,
        "NRSV": 2016,
        "NRSV-CI": 2015,
        "OJB": 130,
        "PEV": 2530,
        "RAD": 2753,
        "RSV": 2020,
        "RSV-CI": 2017,
        "RV1885": 477,
        "RV1895": 1922,
        "TEG": 3010,
        "TLV": 314,
        "TPT": 1849,
        "TS2009": 316,
        "WBMS": 2407,
        "WEB": 206,
        "WEBBE": 1204,
        "WMB": 1209,
        "WMBBE": 1207,
        "YLT98": 821,
    }

    version_code = None
    if version in versions:
        version_code = versions[version]

    if version_code is None:
        raise ValueError("Unknown version: '{0}'".format(version))

    return version_code


"""
Given a URI string and a filename, outputs a QR code that encodes the string
@param URI - String to encode in the QR barcode (required)
@param filename - Filename to save the QR code to (required)
@param scale - Integer scale to upsize the image (optional)
"""
def make_qr_code(URI, filename, scale=1):
    qr = pyqrcode.create(URI)
    qr.png(filename, scale=scale)


"""
Parse command line args and output help messages if needed
"""
def main():
    parser = argparse.ArgumentParser(description='Generates a QR code that opens a bible app to a specific location')
    parser.add_argument(
        '--output',
        '-o',
        dest='output',
        default='output.png',
        help='Output filename (with png extension)'
    )
    parser.add_argument(
        '--chapter',
        '-c',
        dest='chapter',
        default=1,
        help='Desired chapter'
    )
    parser.add_argument(
        '--start_verse',
        '-s',
        dest='start_verse',
        default=1,
        help='Starting verse'
    )
    parser.add_argument(
        '--end_verse',
        '-e',
        dest='end_verse',
        default=None,
        help='Ending verse'
    )
    parser.add_argument(
        '--version',
        '-v',
        dest='version',
        default="KJV",
        help='Three letter Bible version code (e.g. "KJV")'
    )
    parser.add_argument(
        '--zoom',
        '-z',
        dest='zoom',
        default=5,
        help='Scale factor to apply to the QR code'
    )
    parser.add_argument(
        'book',
        help='Desired book (e.g. "Genesis")'
    )

    args = parser.parse_args()

    intent_uri = get_intent_url(
        args.book,
        args.chapter,
        args.start_verse,
        args.end_verse,
        args.version
    )

    print("Generating QR code for intent URI:")
    print(intent_uri)
    make_qr_code(intent_uri, args.output, args.zoom)
    print("Saved {0}".format(args.output))


if __name__ == "__main__":
    main()

