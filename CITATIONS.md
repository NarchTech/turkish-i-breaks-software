# External sources

Every external claim in the article is backed by a live source that was fetched
during research. Listed here for transparency.

1. **Unicode casing under the Turkish/Azeri locale** — Unicode Character Database, `SpecialCasing.txt` (v17.0.0). Under the header *"I and i-dotless; I-dot and i are case pairs in Turkish and Azeri"*: `I` (U+0049) → `ı` (U+0131) and `i` (U+0069) → `İ` (U+0130) under `tr`.
   <https://www.unicode.org/Public/17.0.0/ucd/SpecialCasing.txt>

2. **Java — `String.toLowerCase()` is locale-sensitive; use `Locale.ROOT`.** The Javadoc note (reproduced in the mirrored documentation) warns of "unexpected results" for identifiers, keys, and HTML tags, giving `"TITLE".toLowerCase()` → `"tıtle"` in a Turkish locale.
   <https://learn.microsoft.com/en-us/dotnet/api/java.lang.string.tolowercase>
   SEI CERT Oracle Coding Standard for Java, rule **STR02-J** (the `"script"` → `"SCRİPT"` XSS-filter example):
   <https://cmu-sei.github.io/secure-coding-standards/sei-cert-oracle-coding-standard-for-java/rules/characters-and-strings-str/str02-j>

3. **.NET — culture-sensitive `ToLower/ToUpper`; the "Turkish-I problem"; the `FILE:` bypass.** Microsoft's *Best Practices for Comparing Strings in .NET* recommends `StringComparison.Ordinal`/`OrdinalIgnoreCase` for non-linguistic strings.
   <https://learn.microsoft.com/en-us/dotnet/standard/base-types/best-practices-strings>

4. **A real CVE — CVE-2024-38827 (Spring Security, Nov 2024):** "The usage of `String.toLowerCase()` and `String.toUpperCase()` has some `Locale` dependent exceptions that could potentially result in authorization rules not working properly."
   <https://spring.io/security/cve-2024-38827>

5. **"The Turkey Test"** — the long-standing name for testing software against the Turkish locale (the Moserware blog, 2008).
   <https://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html>
