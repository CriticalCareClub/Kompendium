---
substitutions:
  StdMVitBedPat: "Standardma\xDFnahmen f\xFCr vital bedrohte Patienten"
---

(thema-rst)=

# ResctructuredText: Das Textformat

Basierend auf  \<<http://docutils.sf.net/rst.html>>
und
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>.
Dank an Tibs (<mailto:tibs@tibsnjoan.co.uk>) and David Goodger (<mailto:goodger@python.org>)

reStructuredText (ReST, RST) ist eine vereinfachte Auszeichnungssprache
für Textdateien mit dem Ziel,
in der reinen Textform besonders lesbar zu sein.

```{index} single: * single: ** single: Markup
```
```{index} single: Absatz
```
```{index} single: Einrückung
```
```{index} single: Hervorhebung
```
```{index} single: Hervorhebung; starke
```
```{index} single: Web-Link
```
```{index} single: Backslash
```
```{index} single: \
```

## Grundlagen und einfache Formatierungen ("Markup")

Ein **Absatz** ist der grundlegendste Block in einem Dokument.
Absätze sind Textabschnitte,
die durch eine oder mehrere Leerzeilen voneinander getrennt sind.
Die **Einrückung** ist in RST von Bedeutung,
daher müssen alle Zeilen desselben Absatzes linksbündig
auf die *gleiche Einrückungsebene* ausgerichtet sein.
Eingerückte Absätze haben einen Bezug zum obigen nicht-
(oder weniger-) eingerückten Text.

Eine *Hervorhebung* erfolgt mittels eines Sterns (`*`) wie `*Hervorherbung*`,
eine **starke Hervorhebung** mit 2 Sternen (`**` ), also
z. B. `**starke Hervorhebung**`. Web-Links werden normalerweise
automatisch erkannt, z. B. ergibt `http://www.criticalcareclub.at`
<http://www.criticalcareclub.at>.

Beachte:

- Verschachtelungen sind *nicht* möglich

- Der Text muss unmittelbar dem beginnendem Markup-Zeichen folgen
  bzw. das beendente Markup-Zeichen muss unmittelbar dem Text
  folgen:
  `* Text*` wäre falsch

- Es muss durch "Nicht-Wort-Zeichen" vom umgebenden Text getrennt
  werden. Verwenden Sie einen umgekehrten Schrägstrich mit
  Leerzeichen (`\`), um dies zu
  umgehen: `Dasist\ **ein**\ Wort` ergibt Dasist**ein**Wort.

  Ohne dieser Trennung wird die Hervorhebung nicht erkannt:
  `Dasist**ein**Wort`: Dasist\*\*ein\*\*Wort

RST verwendet **Backslashes** (`\`),
um die spezielle Bedeutung von Markup-Zeichen zu überschreiben
und die Literalzeichen selbst abzurufen.
Verwenden Sie einen Escape-Backslash ("\\"),
um einen Backslash zu erhalten.

```{index} single: Überschirften
```
```{index} single: Gliederungsebenen
```

## Überschriften und Gliederung

Überschriften werden mit speziellen Zeichen unterstrichen
(oder über- und unterstrichen),
ähnlich wie bei einem Schreibmaschinentext.
Möglich sind die Zeichen {literal}`= - : ' " ~ ^ _ * + # < >`.
Welches Zeichen für welche Gliederungebene verwendet wird
ist grundsätztlich egal
und wird,
sofern über ein Dokument konsequent
das gleiche Zeichen für die gleiche Gliederungebene verwendet wird,
von Sphinx automatisch erkannt.
Empfohlen ist jedoch folgende Abfolge:

```
###############################
Gliederungsebene 1 (z. B. Teil)
###############################

**********************************
Gliederungsebene 2 (z. B. Kapitel)
**********************************

Gliederungsebene 3 (z. B. Abschnitt)
====================================

Gliederungsebene 4 (z. B. Unterabschnitt)
-----------------------------------------

Gliederungsebene 5
^^^^^^^^^^^^^^^^^^

Gliederungsebene 6
""""""""""""""""""
```

Die Unterstreichung / Überstreichung muss mindestens so lang sein wie der Titeltext.

```{index} single: Listen
```

## Listen

### Nicht-nummerierte Liste

Aufzählungszeichen sind `-`, `*` oder `+`.
Der fortlaufende Text muss am Aufzählungszeichen plus Einrückung ausgerichtet sein.

Eine Leerzeile vor dem ersten und nach dem
letzten Punkt einer Gliederungsebene erforderlich,
sowie optional zwischen den Elementen möglich.

:::{admonition} Beispiel: Nicht-nummerierte Liste
```
-   Dies ist Punkt 1
-   Dies ist Punkt 2
-   Punkt 3 ist deutlich länger

    Er umfasst auch einen zweiten Absatz,
    welcher entsprechend eingerückt ist.

    -   Punkt 4 zeigt, dass man durch
        Einrückung die Gliederungsebene
        beeinflussen kann.
```

ergibt:

> - Dies ist Punkt 1
>
> - Dies ist Punkt 2
>
> - Punkt 3 ist deutlich länger
>
>   Er umfasst auch einen zweiten Absatz,
>   welcher entsprechend eingerückt ist.
>
>   - Punkt 4 zeigt, dass man durch
>     Einrückung die Gliederungsebene
>     beeinflussen kann.
:::

### Nummerierte Listen

Enumeratoren sind arabische Zahlen,
einzelne Buchstaben
oder römische Ziffern,
sowie {literal}`#.` um automatisch zu nummerieren.
Listenelemente sollten fortlaufend nummeriert sein,
müssen jedoch nicht bei 1 beginnen
(obwohl nicht alle Ausgabeprogramme den ersten Index berücksichtigen).

:::{admonition} Beispiel:
```
3. Dies ist der erste Punkt
4. Dies ist der zweite Punkt
#. Dieser Punkt wird automatisch nummeriert
```

3. Dies ist der erste Punkt
4. Dies ist der zweite Punkt
5. Dieser Punkt wird automatisch nummeriert
:::

### Definitions- und Feldlisten

Definitionslisten verknüpfen einen Begriff mit einem Inhalt.

Der Begriff ist ein einzeiliger Ausdruck,
und die Definition besteht aus einem oder mehreren Absätzen oder Textelementen,
die relativ zum Begriff eingerückt sind.
Leerzeilen zwischen Begriff und Definition sind nicht zulässig.

:::{admonition} Beispiel: Defintionsliste
```
Begriff
    Erklärung

Anderer Begriff
    Eine längere Erklärung.

    Sie beinhaltet sogar einen weiteren Absatz.
    Und sodar eine Aufzählung ist möglich:

    1. Erstens
    2. Zweitens
    3. Drittens
```

Begriff

: Erklärung

Anderer Begriff

: Eine längere Erklärung.

  Sie beinhaltet sogar einen weiteren Absatz.
  Und sodar eine Aufzählung ist möglich:

  1. Erstens
  2. Zweitens
  3. Drittens
:::

Feldlisten ähneln Definitionlisten.
Sie werden vor allem intern zur Angabe von Optionen bei Direktiven verwendet.

:::{admonition} Beispiel: Feldliste
```
:Feld:
    Inhalt

:Autoren:
    Hinz, Kunz

    Weiters danken wir:

    1. Erna
    2. Resi
    3. Zenzi
```

```{eval-rst}

:Autoren:
    Hinz, Kunz

    Weiters danken wir:

    1. Erna
    2. Resi
    3. Zenzi
```
:::

## Exkurs: *Rollen* und *Direktiven*

Neben den bereits vorgestellten einfachen Formatierungsanweisungen (Markup)
gibt es noch sog. *Rollen* und *Direktiven*.
Im Prinzip handelt es sich bei beiden Varianten um Befehle,
die die Möglichkeiten von RST deutlich erweitern.
Wichtig ist das Verständnis des grundsätzlichen Schemas dieser Befehle:

```{index} single: Rollen
```

(rollen)=

### Rollen

Rollen sind im Prinzip Befehle die *im Textverlauf* angewendet werden.
Der Befehl steht zwischen Doppelpunkten (`:`),
das Argument zwischen jeweils einem **Accent grave** (`` ` ``).

{samp}`:{Befehl}:\`{Argument}\`` bzw. {samp}`:{Befehl}:\`{Optionales Argument}
<{Argument}>\``. Z. b. ein Querverweis: `` :ref:`Beispiel-Verweis` ``.

:::{important}
Der Accent grave (Gravis, `` ` ``) ist ein eigenständiges
Zeichen und nicht mit einem Anführungsstrich bzw. Apostroph
gleichzusetzen!

Auf deutschen Tastaturen befindet er sich zwischen der {kbd}`ß`-
und {kbd}`Backspace`-Taste, über dem Akut (`´`, {kbd}`Shift + ´`).
:::

```{index} single: Direktiven
```

(direktiven)=

### Direktiven

Direktiven erlauben mehr Optionen
und werden im
Prinzip wie Absätze verwendet.

Sie beginnen mit einem `..` gefolgt
von einem Leerzeichen, gefolgt von einem einem Befehl und schliessen mit einem
doppelten Doppelpunkt ab, danach kann ein Argument folgen:

```
.. Befehl:: Argument
```

Ein konkretes Beospiel wäre z. B.
`.. figure:: /Pfad/zu/einem/Bild.jpg`.
Weitere Optionen oder
Argumente können *eingerückt* als *Feldliste* in den nächsten Zeilen
Folgen, weiters können -- durch eine Leerzeile getrennt --
entsprechend eingerückte Absätze folgen:

```
.. Befehl:: Argument
    :Option1: Wert
    :Option2: Anderer Wert

    Dies ist ein Absatz
```

Ein konkretes Beispiel wäre:

```
.. figure:: /Pfad/zu/einem/Bild.jpg
    :scale: 50 %
    :alt: Alternativer Titel

    Das ist der Titel des Bildes

    Die weiteren Absätze sind Teil der Bild-Legende.

    Sie kann auch mahrere Absätze geben usw.
```

```{index} single: Tabellen
```

## Tabellen

### Tabelle mit Raster

Raster-Tabellen sehen im Quelltext am schönsten aus,
sind aber schwieriger zu erstellen bzw. auszubessern.
Allerdings ist hierbei das Zusammenführen von Zellen möglich.

Im Prinzip werden sie durch "Zeichnen" mit `+`, `|`, `-` und
`=` erzeugt:

:::{admonition} Beispiel: Tabelle mit Raster
```none
+--------------------------------+-------------------------------+
| Überschrift 1                  | Überschrift 2                 |
+================================+===============================+
| Ich bin eine Zelle             | Ich bin eine zusammen-        |
|                                | geführte Zelle (vertikal).    |
| Ich bin ein zweiter Absatz,    |                               |
| getrennt durch eine Leerzeile. | Auch hier kann es einen       |
+--------------------------------+ zweiten, durch eine Leerzeile |
| Ich bin eine andere Zelle.     | getrennten Absatz geben.      |
|                                |                               |
|                                | Es kann auch:                 |
|                                |                               |
|                                | -   Aufzählungen              |
|                                | -   andere **Formatierungen** |
|                                |                               |
|                                | geben.                        |
+--------------------------------+-------------------------------+
| Ich bin eine horizontal zusammengeführte Zelle.                |
+----------------------------------------------------------------+
```

```{eval-rst}
+--------------------------------+-----------------------------------+
| Überschrift 1                  | Überschrift 2                     |
+================================+===================================+
| Ich bin eine Zelle             | Ich bin eine zusammengeführte     |
|                                | Zelle (vertikal).                 |
| Ich bin ein zweiter Absatz,    |                                   |
| getrennt durch eine Leerzeile. | Auch hier kann es einen zweiten,  |
+--------------------------------+ durch eine Leerzeile getrennten   |
| Ich bin eine andere Zelle.     | Absatz geben.                     |
|                                |                                   |
|                                | Es kann auch:                     |
|                                |                                   |
|                                | -    Aufzählungen                 |
|                                | -    andere **Formatierungen**    |
|                                |                                   |
|                                | geben.                            |
+--------------------------------+-----------------------------------+
| Ich bin eine horizontal zusammengeführte Zelle.                    |
+--------------------------------------------------------------------+
```
:::

### Tabelle mit Liste

Listen-Tabellen sind die einfachste Art um Tabellen zu erzeugen:

Die Direktive lautet {samp}`.. list-table:: {Tabellentitel}`, als Optionen
sind möglich:

```{eval-rst}

gibt die jeweiligen Spaltenbreiten (in Prozent) an,
:``header-rows``:
    definiert wieviele Zeilen als Überschrift
    gerechnet werden,
:``stub-columns``:
    analog dazu, wie viele Spalten als Zeilentitel gerechnet werden.
```

Eine neue Zeile wird mittels Stern `*` begonnen,
eine eingerückte, nicht-nummerierte Liste definiert die Spalten.

```
.. list-table:: Tabellenüberschrift
    :widths: 25 25 25 25
    :header-rows: 1
    :stub-columns: 1

    *   -   Erste Spalte, erste Zeile
        -   Zweite Spalte, erste Zeile
        -   noch immer die erste Zeile
        -   und die letzte (4.)Spalte der 1. Zeile
    *   -   jetzt geht es in die 2. Zeile
        -   usw. (2/2)
        -   usw. (3/2)
        -   usw. (4/2)
    *   -   (1/3)
        -   (2/3)
        -   (3/3)
        -   (4/3)
```

:::{list-table} Tabellenüberschrift
:header-rows: 1
:stub-columns: 1
:widths: 25 25 25 25

- - Erste Spalte, erste Zeile
  - Zweite Spalte, erste Zeile
  - noch immer die erste Zeile
  - und die letzte (4.)Spalte der 1. Zeile
- - jetzt geht es in die 2. Zeile
  - usw. (2/2)
  - usw. (3/2)
  - usw. (4/2)
- - (1/3)
  - (2/3)
  - (3/3)
  - (4/3)
:::

### Einfache Tabellen:

```none
==============    ==============
Titel Spalte 1    Titel Spalte 2
==============    ==============
Inhalt 11         Inhalt 21
Inhalt 12         Inhalt 22
Inhalt 13         Inhalt 23
==============    ==============
```

```{index} single: Bilder
```

## Bilder

Bei Bildern unetrscheidet man zwischen dem einfachen Bild
und dem Bild mit Beschriftung.

(image)=

### Einfaches Bild (image)

Der Befehl `.. image::` bindet ein einfaches Bild ein:

```
.. image:: /Pfad/zu/dem/Bild.jpg
```

Der Pfad für die Bildquelldatei wird als Argument angegeben.
Optional können weitere Optionen angegeben werden, z. B.:

```
.. image:: /Pfad/zu/dem/Bild.jpg
   :height: 30000px
   :width: 500 px
   :scale: 50 %
   :alt: Alternativer Titel
   :align: center
```

Folgende Optionen sind typisch:

````{eval-rst}
.. rst:directive:: .. image:: Pfad

    .. rst:directive:option:: alt: alternativer Text
        :type: Text

        **Alternativer Text**. Eine kurze Beschreibung des Bildes, die von
        Anwendungen angezeigt wird, die keine Bilder anzeigen können, oder
        von Anwendungen für Benutzer mit Sehbehinderung gesprochen wird.

    .. rst:directive:option:: height
        :type: integer or no value

        Dient zum Reservieren von Speicherplatz oder zum vertikalen
        Skalieren des Bildes. Wenn die Option "scale" ebenfalls angegeben
        ist, werden sie kombiniert. Zum Beispiel entspricht eine Höhe von
        200px und eine Skala von 50 einer Höhe von 100px ohne Skala.

    .. rst:directive:option:: width
        :type: Länge oder Verhältnis (%) zur aktuellen Zeilenbreite

        Die **Breite** des Bildes. Wird verwendet, um Platz zu reservieren
        oder das Bild horizontal zu skalieren. Wie bei "height" oben
        werden sie kombiniert, wenn die Option "scale" ebenfalls angegeben
        wird.

    .. rst:directive:option:: scale
        :type: ganzzahliger Prozentsatz (das Symbol ``%`` ist optional)

        Der einheitliche **Skalierungsfaktor** des Bildes.
        Die Standardeinstellung ist ``100%``, d. H. Keine Skalierung.

    .. rst:directive:option:: align
        :type:  ``top``, ``middle``, ``bottom``, ``left``, ``center`` oder ``right``

        Die **Ausrichtung** des Bildes.

        Die Werte ``top``, ``middle`` und
        ``bottom`` steuern die vertikale Ausrichtung eines Bildes (relativ
        zur Textbasislinie).
        Sie sind nur für Inline-Bilder (Ersetzungen)
        nützlich.

        Die Werte ``left``, ``center`` und ``right`` steuern die
        horizontale Ausrichtung eines Bildes, sodass das Bild schweben
        kann und der Text darum herum fließt. Das spezifische Verhalten
        hängt vom verwendeten Browser oder Exporter ab.


    .. rst:directive:option:: target
        :type: Text (URI oder Referenzname)

        Macht das Bild zu einer Hyperlink-Referenz ("anklickbar"). Das
        Optionsargument kann eine URL (relativ oder absolut) oder ein
        "Referenzname" mit einem Unterstrichsuffix (z. B. ```ein Name`_``)
        sein.






````

(figure)=

### Bild mit Beschriftung (figure)

Eine `.. figure::` ist im Prizip ein `.. image::`, jedoch mit zusätzlicher
optionaler *Beschreibung* (Titel) und *Legende*.
`.. figure::` unterstützt alle Optionen von `.. image::`.
Vor dem Beschreibungs-Absatz und vor der Legende müssen Leerzeilen
stehen.

```
.. figure:: /Pfad/zu/einem/Bild.jpg
    :scale: 50 %
    :alt: Alternativer Titel

    Das ist der Titel des Bildes

    Die weiteren Absätze sind Teil der Bild-Legende.

    Sie kann auch mahrere Absätze geben usw.
```

```{index} single: Boxen
```

## Boxen

Mittels `.. admonition::` können Textboxen erzeugt werden, z. B.:

::::{admonition} Besipiel: Textbox mittels admonition
```
.. admonition:: Das ist ein Titel

    Das ist der Text in der Box
```

:::{admonition} Das ist ein Titel
Das ist der Text in der Box
:::
::::

Neben der generischen Box gibt es spezielle Boxen:

- "caution",
- "danger",
- "error",
- "hint",
- "important",
- "note",
- "tip",
- "warning"

::::{admonition} Beispiel: "Danger"
```
.. danger::

    Das ist eine Gefahr!
```

:::{danger}
Das ist eine Gefahr!
:::
::::

## Fußnoten, Verweise und Spezielles

```{index} single: Fußnoten
```

### Fußnoten

Fußnoten werden in eckigen Klammern gesetzt, beginnen mit einem `#`
gefolgt von einem Namen; nach der schließenden eckigen Klammer folgt
ein Unterstrich: (`[#Name]_`).
Die Nummerierung erfolgt automatisch.
In dem Dokuemnt müssen Fußnoten dann auch mittels `.. [#Name]`
definiert werden.
Zwecks Übersichtlichkeit empfiehlt es sich,
die Fußnoten unmittelbar nach dem Absatz zu definieren.

:::{admonition} Beispiel: Fußnote
```
Das ist ein Absatz mit einer Fußnote [#Beispiel-Fussnote]_.

.. [#Beispiel-Fussnote] Und hier erfolgt die Definition der Fußnote.
```

Das ist ein Absatz mit einer Fußnote [^beispiel-fussnote].

[^beispiel-fussnote]: Und hier erfolgt die Definition der Fußnote.
:::

```{index} single: Querverweise
```

(beispiel-querverweis)=

### Verweise

Zuerst muss ein Querverweisziel *vor einer Überschrift* gesetzt werden:

```
.. _Beispiel-Querverweis:

Verweise
========

Zuerst muss ein Querverweisziel *vor einer Überschrift* gesetzt werden:
```

Anschließend kann darauf ein Verweis erfolgen:

```
Ein Querverweisziel sieht man unter :ref:`Beispiel-Querverweis`.
```

Ein Querverweisziel sieht man unter {ref}`Beispiel-Querverweis`.

Möchte man einen bestimmten Verweistext angezeigt bekommen, anstatt
der zum Verweis gehördenen Überschrift, setzt man den Querverweis
zwischen `<` und `>` und gibt davor den gewünschten Text an:

```
Ein Querverweisziel sieht man in diesem :ref:`Abschnitt <Beispiel-Querverweis>`.
```

Ein Querverweisziel sieht man in diesem {ref}`Abschnitt <Beispiel-Querverweis>`.

```{index} single: Literaturreferenzen
```

### Literaturreferenzen

```{eval-rst}
.. rst:role:: cite

   Literaturzitat mittels eines BibTeX-Schlüssels einfügen:

   :samp:`:cite:\`BibTex-ID\``
```

```{index} single: Kommentar
```

### Kommentare

Jeder Text,
der mit `..` ohne einer folgenden gültigen Anweisung
mit Leerzeilen davor und danach
beginnt, ist ein Kommentar.

```{index} single: Ersetzung
```

### Ersetzungen

Substitutionen sind Zeichenfolgen innerhalb zweier
`|`-Zeichen. Andernorts kann für eine Substitution ein
Ersetzungetext definiert werden.

:::{admonition} Beispiel: Feldliste
```
Es werden die |StdMVitBedPat| durchgeführt.
Die |StdMVitBedPat| beinhalten fünf verschiedene Maßnahmen.

.. |StdMVitBedPat| replace:: Standardmaßnahmen für vital bedrohte Patienten
```

Es werden die {{ StdMVitBedPat }} durchgeführt.
Die {{ StdMVitBedPat }} beinhalten fünf verschiedene Maßnahmen.
:::

## Weitere Kommandos ("Rollen")

Eine vollständige Auflistung findet sich unter \<<http://docutils.sf.net/docs/ref/rst/roles.html>>.

### Wichtige und interessante Unicode-Glyphen

| UCODE  | NAME                                       | SYMBOL |
| ------ | ------------------------------------------ | ------ |
| U+0391 | GREEK CAPITAL LETTER ALPHA                 | Α      |
| U+0392 | GREEK CAPITAL LETTER BETA                  | Β      |
| U+0393 | GREEK CAPITAL LETTER GAMMA                 | Γ      |
| U+0394 | GREEK CAPITAL LETTER DELTA                 | Δ      |
| U+0395 | GREEK CAPITAL LETTER EPSILON               | Ε      |
| U+0396 | GREEK CAPITAL LETTER ZETA                  | Ζ      |
| U+0397 | GREEK CAPITAL LETTER ETA                   | Η      |
| U+0398 | GREEK CAPITAL LETTER THETA                 | Θ      |
| U+0399 | GREEK CAPITAL LETTER IOTA                  | Ι      |
| U+039A | GREEK CAPITAL LETTER KAPPA                 | Κ      |
| U+039B | GREEK CAPITAL LETTER LAMDA                 | Λ      |
| U+039C | GREEK CAPITAL LETTER MU                    | Μ      |
| U+039D | GREEK CAPITAL LETTER NU                    | Ν      |
| U+039E | GREEK CAPITAL LETTER XI                    | Ξ      |
| U+039F | GREEK CAPITAL LETTER OMICRON               | Ο      |
| U+03A0 | GREEK CAPITAL LETTER PI                    | Π      |
| U+03A1 | GREEK CAPITAL LETTER RHO                   | Ρ      |
| U+03A3 | GREEK CAPITAL LETTER SIGMA                 | Σ      |
| U+03A4 | GREEK CAPITAL LETTER TAU                   | Τ      |
| U+03A5 | GREEK CAPITAL LETTER UPSILON               | Υ      |
| U+03A6 | GREEK CAPITAL LETTER PHI                   | Φ      |
| U+03A7 | GREEK CAPITAL LETTER CHI                   | Χ      |
| U+03A8 | GREEK CAPITAL LETTER PSI                   | Ψ      |
| U+03A9 | GREEK CAPITAL LETTER OMEGA                 | Ω      |
| U+03B1 | GREEK SMALL LETTER ALPHA                   | α      |
| U+03B2 | GREEK SMALL LETTER BETA                    | β      |
| U+03B3 | GREEK SMALL LETTER GAMMA                   | γ      |
| U+03B4 | GREEK SMALL LETTER DELTA                   | δ      |
| U+03B5 | GREEK SMALL LETTER EPSILON                 | ε      |
| U+03B6 | GREEK SMALL LETTER ZETA                    | ζ      |
| U+03B7 | GREEK SMALL LETTER ETA                     | η      |
| U+03B8 | GREEK SMALL LETTER THETA                   | θ      |
| U+03B9 | GREEK SMALL LETTER IOTA                    | ι      |
| U+03BA | GREEK SMALL LETTER KAPPA                   | κ      |
| U+03BB | GREEK SMALL LETTER LAMDA                   | λ      |
| U+03BC | GREEK SMALL LETTER MU                      | μ      |
| U+03BD | GREEK SMALL LETTER NU                      | ν      |
| U+03BE | GREEK SMALL LETTER XI                      | ξ      |
| U+03BF | GREEK SMALL LETTER OMICRON                 | ο      |
| U+03C0 | GREEK SMALL LETTER PI                      | π      |
| U+03C1 | GREEK SMALL LETTER RHO                     | ρ      |
| U+03C2 | GREEK SMALL LETTER FINAL SIGMA             | ς      |
| U+03C3 | GREEK SMALL LETTER SIGMA                   | σ      |
| U+03C4 | GREEK SMALL LETTER TAU                     | τ      |
| U+03C5 | GREEK SMALL LETTER UPSILON                 | υ      |
| U+03C6 | GREEK SMALL LETTER PHI                     | φ      |
| U+03C7 | GREEK SMALL LETTER CHI                     | χ      |
| U+03C8 | GREEK SMALL LETTER PSI                     | ψ      |
| U+03C9 | GREEK SMALL LETTER OMEGA                   | ω      |
| U+FE4D | DASHED LOW LINE                            | ﹍      |
| U+2011 | NON-BREAKING HYPHEN                        | ‑      |
| U+2014 | EM DASH                                    | —      |
| U+2E3A | TWO-EM DASH                                | ⸺      |
| U+2E3B | THREE-EM DASH                              | ⸻      |
| U+0609 | ARABIC-INDIC PER MILLE SIGN                | ؉      |
| U+060A | ARABIC-INDIC PER TEN THOUSAND              | ؊      |
| U+00B1 | PLUS-MINUS SIGN                            | ±      |
| U+00D7 | MULTIPLICATION SIGN                        | ×      |
| U+00F7 | DIVISION SIGN                              | ÷      |
| U+2190 | LEFTWARDS ARROW                            | ←      |
| U+2191 | UPWARDS ARROW                              | ↑      |
| U+2192 | RIGHTWARDS ARROW                           | →      |
| U+2193 | DOWNWARDS ARROW                            | ↓      |
| U+2194 | LEFT RIGHT ARROW                           | ↔      |
| U+21D2 | RIGHTWARDS DOUBLE ARROW                    | ⇒      |
| U+21D4 | LEFT RIGHT DOUBLE ARROW                    | ⇔      |
| U+21F5 | DOWNWARDS ARROW LEFTWARDS OF UPWARDS ARROW |        |
| U+2195 | UP DOWN ARROW                              | ↕      |
| U+2196 | NORTH WEST ARROW                           | ↖      |
| U+2197 | NORTH EAST ARROW                           | ↗      |
| U+2198 | SOUTH EAST ARROW                           | ↘      |
| U+2199 | SOUTH WEST ARROW                           | ↙      |
| U+21BA | ANTICLOCKWISE OPEN CIRCLE ARROW            | ↺      |
| U+21BB | CLOCKWISE OPEN CIRCLE ARROW                | ↻      |
| U+21C4 | RIGHTWARDS ARROW OVER LEFTWARDS ARROW      | ⇄      |
| U+21C5 | UPWARDS ARROW LEFTWARDS OF DOWNWARDS ARROW | ⇅      |
| U+21C6 | LEFTWARDS ARROW OVER RIGHTWARDS ARROW      | ⇆      |
| U+21C7 | LEFTWARDS PAIRED ARROWS                    | ⇇      |
| U+21C8 | UPWARDS PAIRED ARROWS                      | ⇈      |
| U+21C9 | RIGHTWARDS PAIRED ARROWS                   | ⇉      |
| U+21CA | DOWNWARDS PAIRED ARROWS                    | ⇊      |
| U+2200 | FOR ALL                                    | ∀      |
| U+2208 | ELEMENT OF                                 | ∈      |
| U+2209 | NOT AN ELEMENT OF                          | ∉      |
| U+2140 | DOUBLE-STRUCK N-ARY SUMMATION              | ⅀      |
| U+2211 | N-ARY SUMMATION                            | ∑      |
| U+221D | PROPORTIONAL TO                            | ∝      |
| U+221E | INFINITY                                   | ∞      |
| U+2227 | LOGICAL AND                                | ∧      |
| U+2228 | LOGICAL OR                                 | ∨      |
| U+222B | INTEGRAL                                   | ∫      |
| U+2245 | APPROXIMATELY EQUAL TO                     | ≅      |
| U+2246 | APPROXIMATELY BUT NOT ACTUALLY EQUAL TO    | ≆      |
| U+2247 | NEITHER APPROXIMATELY NOR ACTUALLY EQUAL T | ≇      |
| U+2248 | ALMOST EQUAL TO                            | ≈      |
| U+2249 | NOT ALMOST EQUAL TO                        | ≉      |
| U+2260 | NOT EQUAL TO                               | ≠      |
| U+2261 | IDENTICAL TO                               | ≡      |
| U+2262 | NOT IDENTICAL TO                           | ≢      |
| U+2263 | STRICTLY EQUIVALENT TO                     | ≣      |
| U+2264 | LESS-THAN OR EQUAL TO                      | ≤      |
| U+2265 | GREATER-THAN OR EQUAL TO                   | ≥      |
| U+2266 | LESS-THAN OVER EQUAL TO                    | ≦      |
| U+2267 | GREATER-THAN OVER EQUAL TO                 | ≧      |
| U+2268 | LESS-THAN BUT NOT EQUAL TO                 | ≨      |
| U+2269 | GREATER-THAN BUT NOT EQUAL TO              | ≩      |
| U+226A | MUCH LESS-THAN                             | ≪      |
| U+226B | MUCH GREATER-THAN                          | ≫      |
| U+211E | PRESCRIPTION TAKE                          | ℞      |
| U+2325 | OPTION KEY                                 | ⌥      |
| U+2387 | ALTERNATIVE KEY SYMBOL                     | ⎇      |
| U+23F0 | ALARM CLOCK                                | ⏰      |
| U+23F1 | STOPWATCH                                  | ⏱      |
| U+23F2 | TIMER CLOCK                                | ⏲      |
| U+23F3 | HOURGLASS WITH FLOWING SAND                | ⏳      |
| U+23FB | POWER SYMBOL                               | ⏻      |
| U+23FC | POWER ON-OFF SYMBOL                        | ⏼      |
| U+2620 | SKULL AND CROSSBONES                       | ☠      |
| U+2621 | CAUTION SIGN                               | ☡      |
| U+2622 | RADIOACTIVE SIGN                           | ☢      |
| U+2623 | BIOHAZARD SIGN                             | ☣      |
| U+2640 | FEMALE SIGN                                | ♀      |
| U+2641 | EARTH                                      | ♁      |
| U+2642 | MALE SIGN                                  | ♂      |
| U+267F | WHEELCHAIR SYMBOL                          | ♿      |
| U+2690 | WHITE FLAG                                 | ⚐      |
| U+2691 | BLACK FLAG                                 | ⚑      |
| U+2692 | HAMMER AND PICK                            | ⚒      |
| U+2693 | ANCHOR                                     | ⚓      |
| U+2694 | CROSSED SWORDS                             | ⚔      |
| U+2695 | STAFF OF AESCULAPIUS                       | ⚕      |
| U+2696 | SCALES                                     | ⚖      |
| U+2697 | ALEMBIC                                    | ⚗      |
| U+26A0 | WARNING SIGN                               | ⚠      |
| U+26A1 | HIGH VOLTAGE SIGN                          | ⚡      |
| U+26D4 | NO ENTRY                                   | ⛔      |
| U+26D5 | ALTERNATE ONE-WAY LEFT WAY TRAFFIC         | ⛕      |
| U+26F3 | FLAG IN HOLE                               | ⛳      |
| U+2706 | TELEPHONE LOCATION SIGN                    | ✆      |
| U+2707 | TAPE DRIVE                                 | ✇      |
| U+2708 | AIRPLANE                                   | ✈      |
| U+2709 | ENVELOPE                                   | ✉      |
| U+2713 | CHECK MARK                                 | ✓      |
| U+2714 | HEAVY CHECK MARK                           | ✔      |
| U+2715 | MULTIPLICATION X                           | ✕      |
| U+2716 | HEAVY MULTIPLICATION X                     | ✖      |
