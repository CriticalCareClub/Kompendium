---
status: final
maintainer: GABRIEL Sebastian
last-update: 2026-04-25
---


:::{raw} latex
\clearpage
:::

:::{index} single: Design
:::
:::{index} single: Guidelines; Design
:::

(Design-Guidelines)=

# Design Guidelines


## Farben

Das Farbschema basiert auf dem [Solarized-Farbschema](https://ethanschoonover.com/solarized/) von Ethan Schoonover.
Es ist ein Farbkonzept für Texteditoren und Benutzeroberflächen und basiert auf einer bewusst reduzierten, harmonischen Farbpalette mit definierten Kontrastverhältnissen und unterstützt einen Hell- und Dunkelmodus (Light mode, Dark mode).


Eigenschaften
:   -   16 gezielt abgestimmte Farben
    -   Einheitliche Farblogik (Farben haben feste semantische Rollen)
    -   Gleiche Palette für Light- und Dark-Modus (nur invertiert genutzt)
    -   Fokus auf reduzierte Helligkeitskontraste statt reiner Schwarz-Weiß-Kontraste


Vorteile
:   -   Reduzierte Augenbelastung bei längerer Bildschirmarbeit
    -   Gute Lesbarkeit durch ausgewogene Kontrastverhältnisse
    -   Flexibler Wechsel zwischen Light- und Dark-Mode


Zusätzlich wurde die Farbpalette um Farben für spezielle Anwendungen ergänzt (*Ergänzungsfarben*).
Diese sollen nur unter bestimmten Umständen zum Einsatz kommen.


:::{list-table} Solarized-Farben (+ Ergänzungsfarben)
:header-rows: 1

*   -   Farbton
    -   Vorschau
    -   RGB (dezimal)
    -   HEX
    -   CMYK
    -   Anmerkungen

*   -   Base03
    -   ![](Solarized-Base03.png)
    -   0, 43, 54
    -   #002b36
    -   1.00, 0.21, 0.00, 0.79
    -   Hintergrund dunkel (Primär)

*   -   Base02
    -   ![](Solarized-Base02.png)
    -   7, 54, 66
    -   #073642
    -   0.91, 0.18, 0.00, 0.74
    -   Hintergrund dunkel (Kontrast)

*   -   Base01
    -   ![](Solarized-Base01.png)
    -   88, 110, 117
    -   #586e75
    -   0.25, 0.07, 0.00, 0.54
    -   Text auf hellem Hintergrund

*   -   Base00
    -   ![](Solarized-Base00.png)
    -   101, 123, 131
    -   #657b83
    -   0.23, 0.06, 0.00, 0.49
    -   Standardtext

*   -   Base0
    -   ![](Solarized-Base0.png)
    -   131, 148, 150
    -   #839496
    -   0.13, 0.03, 0.00, 0.41
    -   Sekundärer Text

*   -   Base1
    -   ![](Solarized-Base1.png)
    -   147, 161, 161
    -   #93a1a1
    -   0.09, 0.00, 0.00, 0.37
    -   Text auf dunklem Hintergrund

*   -   Base2
    -   ![](Solarized-Base2.png)
    -   238, 232, 213
    -   #eee8d5
    -   0.00, 0.03, 0.10, 0.07
    -   Hintergrund hell (Kontrast)

*   -   Base3
    -   ![](Solarized-Base3.png)
    -   253, 246, 227
    -   #fdf6e3
    -   0.00, 0.03, 0.10, 0.01
    -   Hintergrund hell (Primär)

*   -   Yellow
    -   ![](Solarized-Yellow.png)
    -   181, 137, 0
    -   #b58900
    -   0.00, 0.25, 1.00, 0.29
    -   Gedämpftes Gelb

*   -   Yellow-Bright
    -   ![](Solarized-Yellow-Bright.png)
    -   255, 234, 0
    -   #ffea00
    -   0.00, 0.08, 1.00, 0.00
    -   *Ergänzung.* Highlight

*   -   Yellow-Custom
    -   ![](Solarized-Yellow-Custom.png)
    -   241, 196, 15
    -   #f1c40f
    -   0.00, 0.18, 0.94, 0.06
    -   *Ergänzung.* Kräftige Zwischenstufe

*   -   Orange
    -   ![](Solarized-Orange.png)
    -   203, 75, 22
    -   #cb4b16
    -   0.00, 0.63, 0.89, 0.20
    -   Warnfarbe

*   -   Red
    -   ![](Solarized-Red.png)
    -   220, 50, 47
    -   #dc322f
    -   0.00, 0.77, 0.79, 0.14
    -   Alarm

*   -   Custom-1
    -   ![](Solarized-Custom-1.png)
    -   148, 38, 0
    -   #942600
    -   0.00, 0.75, 1.00, 0.42
    -   *Ergänzung.* Dunkler Rotton

*   -   Magenta
    -   ![](Solarized-Magenta.png)
    -   211, 54, 130
    -   #d33682
    -   0.00, 0.74, 0.38, 0.17
    -   Akzent

*   -   Violet
    -   ![](Solarized-Violet.png)
    -   108, 113, 196
    -   #6c71c4
    -   0.45, 0.42, 0.00, 0.23
    -   Sekundärakzent

*   -   Blue
    -   ![](Solarized-Blue.png)
    -   38, 139, 210
    -   #268bd2
    -   0.82, 0.34, 0.00, 0.18
    -   Primärfarbe

*   -   Blue-Light
    -   ![](Solarized-Blue-Light.png)
    -   227, 242, 251
    -   #e3f2fb
    -   0.10, 0.04, 0.00, 0.02
    -   Heller Hintergrund

*   -   Cyan
    -   ![](Solarized-Cyan.png)
    -   42, 161, 152
    -   #2aa198
    -   0.74, 0.00, 0.06, 0.37
    -   Info

*   -   Green
    -   ![](Solarized-Green.png)
    -   133, 153, 0
    -   #859900
    -   0.13, 0.00, 1.00, 0.40
    -   Status (gedämpft)

*   -   Green-Bright
    -   ![](Solarized-Green-Bright.png)
    -   0, 200, 83
    -   #00c853
    -   1.00, 0.00, 0.58, 0.22
    -   *Ergänzung.* Aktiver Status
:::





## Schriftarten

Als Basisschriftart kommt die **Lexend**-Schriftfamilie zum Einsatz.

*Lexend* ist eine moderne Sans-Serif-Schriftfamilie, die gezielt zur *Verbesserung der Lesbarkeit* entwickelt wurde, indem sie auf Erkenntnissen der *Lesbarkeitsforschung* basiert und die visuelle sowie kognitive Verarbeitung von Text optimiert.

Sie wurde von *Dr. Bonnie Shaver-Troup* (Educational Therapist und Begründerin des Lexend-Projekts) gemeinsam mit dem Typedesigner *Thomas Jockin* entwickelt.
Die Entwicklung begann aus der Forschung zur Leseflüssigkeit heraus und wurde später in Zusammenarbeit mit **Google Fonts** als frei verfügbare Schriftfamilie umgesetzt.


Eigenschaften
:   -   Variable Buchstabenabstände und Proportionen
    -   Große x-Höhe und offene, gut unterscheidbare Zeichenformen
    -   Klare Differenzierung ähnlicher Glyphen (z. B. l, I, 1)
    -   Mehrere Varianten mit unterschiedlicher Laufweite (z. B. Deca, Mega, Zetta)
    -   Optimiert für Bildschirmdarstellung


Lesbarkeit
:   Die Lesbarkeit wird durch mehrere typografische Mechanismen verbessert.
    Größere Buchstabenabstände reduzieren das visuelle „Verschmieren“ von Zeichen und erleichtern die Orientierung im Text.
    Offene Formen und eine große x-Höhe verbessern die Erkennbarkeit einzelner Buchstaben.
    Gleichzeitig sorgt die geringere visuelle Dichte für weniger „Textblock-Effekt“ und eine bessere Strukturwahrnehmung.

    Auf kognitiver Ebene führt dies zu stabileren Fixationen, weniger Rücksprüngen im Text und insgesamt flüssigerem Lesen.
    Die visuelle und mentale Belastung beim Lesen wird dadurch reduziert.


Vorteile
:   -   Erhöhte Lesegeschwindigkeit und besseres Textverständnis
    -   Reduzierte visuelle Ermüdung
    -   Verbesserte Lesbarkeit bei langen Texten und auf Bildschirmen
    -   Besonders geeignet für Personen mit Dyslexie oder erhöhter visueller Belastung


Weiterführende Links
:   -   Offizielle Seite: https://www.lexend.com
    -   Google Fonts: https://fonts.google.com/specimen/Lexend


:::{admonition} Synopsis

Lexend zielt *nicht auf typografische Eleganz*, sondern auf **maximale Lesbarkeit und kognitive Entlastung**.
:::