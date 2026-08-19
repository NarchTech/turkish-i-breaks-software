"""turkish_fold.py — locale-correct case folding for Turkish (tr) / Azeri (az).

Reference implementation accompanying the article
"The Turkish İ Still Breaks Your Software (and Your AI Agents)".

Why this exists
---------------
Python's built-in ``str.lower()`` / ``str.casefold()`` apply the Unicode
*default* case mapping. Under it, "İ" (U+0130) lowercases to TWO codepoints —
"i" + U+0307 COMBINING DOT ABOVE — so ``"İ".lower() != "i"``, and the result
*looks* identical on screen. And "I" lowercases to "i", never to the Turkish
dotless "ı". For matching identifiers, keys, names, districts, and search terms
in Turkish text you must fold the six Turkish letter-pairs *before* the generic
lowercase, and compare on word boundaries rather than by naive substring.

Dependency-free (standard library only). MIT licensed (see reference/LICENSE-CODE).
"""

import re
import unicodedata

# Fix ONLY the dotted/dotless i's before a generic .lower(); keep other TR letters.
_TR_LOWER = str.maketrans({"İ": "i", "I": "ı"})

# ASCII-fold map — applied BEFORE NFKD so the dotless "ı" is not silently dropped.
_TR_ASCII = str.maketrans({
    "ı": "i", "İ": "I", "ğ": "g", "Ğ": "G", "ü": "u", "Ü": "U",
    "ş": "s", "Ş": "S", "ö": "o", "Ö": "O", "ç": "c", "Ç": "C",
})


def tr_lower(value: str) -> str:
    """Turkish-safe lowercase that PRESERVES Turkish letters.

    Use for case-insensitive comparison of Turkish-keyed data (roles, categories)
    where you want to keep ç/ğ/ı/ö/ş/ü but fix the İ/I dotted/dotless mapping.

    >>> tr_lower("İSDEMİR") == tr_lower("İsdemir")
    True
    >>> "İ".lower() == "i"          # the bug this avoids
    False
    """
    return value.translate(_TR_LOWER).lower()


def tr_fold(value: str) -> str:
    """Reduce Turkish text to an ASCII lowercase matching key.

    ASCII-folds the six letter-pairs BEFORE lowercasing, so the result is pure
    ASCII and can't sprout a combining dot. Use as the single join key for
    name / district / label matching (put the SAME fold on both sides).

    >>> tr_fold("Kaş")
    'kas'
    >>> tr_fold("İstanbul") == tr_fold("ISTANBUL")
    True
    """
    folded = value.translate(_TR_ASCII)
    return unicodedata.normalize("NFKD", folded).encode("ascii", "ignore").decode("ascii").lower()


def contains_word(haystack: str, needle: str) -> bool:
    """Word-boundaried search: "kas" (Kaş) does NOT match inside "kasım".

    Both arguments are assumed already ``tr_fold()``-ed. A naive
    ``needle in haystack`` produces silent false positives for short names.

    >>> contains_word(tr_fold("kasım ayı"), tr_fold("Kaş"))
    False
    >>> contains_word(tr_fold("Kaş Antalya"), tr_fold("Kaş"))
    True
    """
    if not needle:
        return False
    return re.search(rf"(?<![0-9a-z]){re.escape(needle)}(?![0-9a-z])", haystack) is not None


if __name__ == "__main__":
    import doctest

    fails, tests = doctest.testmod(verbose=False)
    print(f"{tests - fails}/{tests} doctests passed")
