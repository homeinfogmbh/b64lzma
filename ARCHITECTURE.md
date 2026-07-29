# b64lzma
Stand: 2026-07-29, geprüft gegen Commit d4fc64e

## Zweck
Kleine Utility-Bibliothek: repräsentiert beliebige Bytes als LZMA-komprimierte,
base64-kodierte Strings (und zurück). Dient dazu, Binärdaten kompakt und
textsicher (z. B. in JSON/DB/URLs) zu transportieren.

## Stack & Einstiegspunkte
Python 3, Single-Module-Package (`py_modules=["b64lzma"]`), `setuptools_scm`-
Versionierung. Kernlogik in `b64lzma.py`. Keine externen Laufzeit-Dependencies
(nutzt Standardbibliothek `lzma`/`base64`).

## Schnittstellen
### Konsumiert
- Nur Python-Standardbibliothek (`lzma`, `base64`).

### Bietet an
- Funktionen/Typ zum Kodieren (Bytes → LZMA → base64-String) und Dekodieren.
  Wird von anderen Homeinfo-Komponenten (`hwdb`, `ferengi`, `comcatlib` …) als
  Hilfsbaustein importiert.

## Deployment / Laufzeit
Reine Bibliothek; als Python-Package installiert und importiert. Kein Dienst,
kein CLI, keine DB. ⚠️ ANNAHME: kein eigenständiger Laufzeitbetrieb.

## Ersetzbarkeit
Kopplungsgrad: **niedrig**. Eigenständiges, zustandsloses Utility mit klarer,
schmaler API; leicht ersetzbar. Bei Änderung des Kodier-Formats müssten
allerdings alle Consumer, die so kodierte Daten gespeichert haben, berücksichtigt
werden.

## Weitere Doku
- `README.md` (Einzeiler zum Zweck).
- ⚠️ ANNAHME: Zentrales Repo `homeinfo-architektur` (Ordner `komponenten/`) noch
  nicht geprüft.
