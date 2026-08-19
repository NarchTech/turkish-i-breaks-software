# The Turkish İ Still Breaks Your Software (and Your AI Agents)

A short technical article on how the Turkish dotted **İ** / dotless **ı** — a
40-year-old known locale-casing issue — still breaks modern software stacks,
illustrated with five fresh 2026 measurements from one AI-agent fleet, plus a
portable reference implementation of locale-correct Turkish case folding.

**Authors:** Prof. Dr. Mustafa Melikoğlu · Yağız Deniz Altınbaş · Tayfun Tanrıöver
**Investigation & writing:** KAŞİF — an AI research identity in the narch ecosystem, reviewed with the ecosystem's upper-mind coordinator, Marcus. See the author's note inside each article; in keeping with scientific-publishing practice the humans above are the authors of record and the AI contribution is disclosed openly.

Status: **preprint v1.0** — a living, versioned record (this is our working ledger; we will revise). A formal venue (e.g. arXiv) may follow once it matures.

## Contents
| File | What |
|---|---|
| [`the-turkish-i-still-breaks-your-software.md`](the-turkish-i-still-breaks-your-software.md) | The article (English). |
| [`turkce-i-yazilimini-hala-bozuyor.md`](turkce-i-yazilimini-hala-bozuyor.md) | Turkish edition (adapted, not a literal translation). |
| [`CITATIONS.md`](CITATIONS.md) | The external sources, each with a live URL. |
| [`reference/turkish_fold.py`](reference/turkish_fold.py) | Standalone, dependency-free reference implementation of `tr_lower` / `tr_fold` / `contains_word`, with doctests. |

## The one-paragraph version
Python's `str.lower()` maps `İ` (U+0130) to **two** codepoints — `i` + `U+0307 COMBINING DOT ABOVE` — so `"İ".lower() != "i"`, and it *looks* identical on screen. Under the Turkish locale, `I`↔`ı` and `i`↔`İ`. Get this wrong and case-insensitive matching, deduplication, full-text search, PII redaction, terminal encoding, and even CSS `text-transform: uppercase` all fail — usually silently. Casing is a system-design concern, not a string-utility footnote.

## Cite this
Please cite the **concept DOI** (it always resolves to the latest version):

> _Concept DOI: added on first Zenodo release — see the repository's Zenodo record._

## License
- **Articles / text:** [CC BY 4.0](LICENSE).
- **Reference code (`reference/`):** [MIT](reference/LICENSE-CODE).

## Series
This is the first of a planned series, *"Turkish is not accented English."* Future notes cover locale-aware **tokenization and matching** — why `-maz` is at once a negation and Turkey's commonest surname ending, and why a naïve search for `Kaş` also finds `kasım`.
