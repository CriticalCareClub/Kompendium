---
status: final
---



:::{index} single: Markdown
:::
:::{index} single: Myst Markdown
:::

(MyST)=
(Markdown)=

# MyST-Markdown Kurzanleitung

## Was ist Klartext?

Klartext (Engl.: Plain text) ist Text, der ausschließlich aus lesbaren Zeichen besteht und *keine Formatierungen* oder eingebetteten Objekte enthält.
Er enthält *nur den eigentlichen textuellen Inhalt* (z. B. Buchstaben, Zahlen, Satzzeichen) ohne Informationen über Formatierungen wie Schriftart, Größe, Farbe oder Layout.

Auszeichnungssprachen
:   ... können *Befehle* definieren, um die Funktionalität von Klartext zu erweitern, z. B. um Hervorhebungen oder Ähnliches zu ermöglichen.

Semantik
:   Darunter versteht man den eigentlichen Inhalt bzw. Meta-Informationen ("Das ist eine Hervorhebung", "Das ist ein Produkname", ...)

Syntax
:   Definiert die erforderliche Schreibweise um ein bestimmtes Ergebnis zu Erhalten.

Kompilation
:   Für die eigentliche Formatierung ist ein zusätzlicher Schritt nötig, welcher aus dem Klartext die eigentlichen formatierten Produkte (PDF-Dateien, Webseiten etc.) herstellt (*Kompilation*).
    Dabei werden von einem Interpreter (Compiler) die Definitionen durch die Auszeichnungssprache im Dokument mit festgelegten *Layout- und Stil-Definitionen* verglichen und zu der eigentlichen, dem Ausgabeformat entsprechenden, Formatierung überführt.
    Dies ist sinnvoll, da die Formatierungsmöglichkeiten wesentlich von der gewünschten Zielplattform abhängen (Druck: z. B. "mache Hervorhebungen fett", Online: z. B.: "Mache Hervorhebungen fett und dunkelblau", ...).

    Der Compiler für dieses Projekt ist die {program}`Sphinx` Toolchain.
    Sie erlaubt das erstellen u. a. von druckfertigen PDFs, Webseiten und eBooks.



:::{figure} Kompilation.png

Kompilation: Aus dem Klartext erzeugt der Interpreter (Compiler) unter Zuhilfenahme der Stil-Definitionen die verschiedenen Ausgabeformate (Produkte).
:::



:::{admonition} Synopsis

-   Klartext erlaubt die Trennung von *Inhalt* und *Format*
-   Layout- und *Stildefintionen* definieren die Formatierung des Inhaltes für die unterschiedlichen Ausgabeformate.
-   Die *Kompilation* erstellt aus den Inhalten und den Stildefinitionen die formatierten Endprodukte.

Durch die Trennung von Inhalt und Formatierung können **aus dem gleichen Inhalt unterschiedliche Produkte** (Druck, Online, ...) erstellt werden.

:::



## Was ist Markdown?

**Markdown** (*MD*) ist eine Auszeichnungssprache, die entwickelt wurde, um Klartext mit einfacher, gut lesbarer Syntax zu formatieren.
Im Gegensatz zu komplexeren Formaten wie HTML oder LaTeX bleibt der Quelltext nahezu so lesbar wie der fertige Text.
Formatierungen wie Überschriften, Listen, Hervorhebungen oder Links werden durch wenige, intuitive Zeichen dargestellt (z. B. `#`, `*`, `[]()`).
Markdown wird häufig für Dokumentationen, Webseiten, wissenschaftliche Texte und Notebooks verwendet, da es einfach zu schreiben, plattformunabhängig und gut automatisierbar ist.
**MyST** (*Markedly Structured Text*) erweitert Markdown um Funktionen für wissenschaftliches und technisches Schreiben.
Es ergänzt Markdown um Direktiven, Rollen, Querverweise, Mathematik und strukturierte Metadaten.






:::{list-table} Markdown-Syntaxübersicht
:header-rows: 1
:stub-columns: 1
:widths: 20 40 40

*   -   Funktion
    -   Syntax
    -   Ergebnis

*   -   Einfache Hervorhebung
    -   ```
        Ich bin *hervorgehoben*
        ```
    -   Ich bin *hervorgehoben*

*   -   Starke Hervorhebung
    -   ```
        Ich bin **stark hervorgehoben**
        ```
    -   Ich bin **stark hervorgehoben**

*   -   Überschriften
    -   ```markdown
        # Überschrift Ebene 1

        ## Überschrift Ebene 2
        ```
    -
*   -   Liste
    -
        ```markdown
        -   Erster Punkt
        -   Zweiter Punkt
            -   Unterpunkt
            -   Noch einer
        -   Dritter Punkt
        ```
    -
        -   Erster Punkt
        -   Zweiter Punkt
            -   Unterpunkt
            -   Noch einer
        -   Dritter Punkt

*   -   Aufzählung
    -
        ```markdown
        1.  Erstens
            1.  Unterpunkt
            2.  Außerdem ...
        2.  Zweitens
        ```
    -
        1.  Erstens
            1.  Unterpunkt
            2.  Außerdem ...
        2.  Zweitens

*   -   Defintionsliste
    -
        ```markdown
        Begriff
        :   Die Erklärung
        ```
    -   Begriff
        :   Die Erklärung
*   -   Bild
    -   ```markdown
        ![Ein grün-gelbes Schachbrett](a.png)
        ```
    -   ![Ein grün-gelbes Schachbrett](a.png)
*   -   Bild mit Beschreibung
    -   ```markdown
        :::{figure} a.png

        Ein grün-gelbes Schachbrett
        :::
        ```
    -   :::{figure} a.png

        Ein grün-gelbes Schachbrett
        :::
*   -   Link
    -   ```markdown
        [Link zu Example GmbH](https://example.com)
        ```
    -   [Link zu Example GmbH](https://example.com)


*   -   Zitat
    -   ```markdown
        >   Blockquote
        ```
    -
        >   Blockquote

*   -   Trennlinie
    -   ```markdown
        ---
        ```
    -   ![alt text](HR.png)

*   -   Code
    -   ```
        Die Barcodenummer ist `123123`!
        ```
    -   Die Barcodenummer ist `123123`!

*   -   Mathematik
    -
        ```markdown
        $I = \frac{U}{R}$
        ```
        oder
        ```markdown
        {math}`I = \frac{U}{R}`
        ```
    -   $I = \frac{U}{R}$

        Anm.: Die Syntax folgt der [LaTeX-Mathematik-Syntax](https://www.grund-wissen.de/informatik/latex/mathematischer-formelsatz.html).

:::





## Basis-Markdown

::::::{admonition} Beispiel: Basis-Markdown

::::{code} markdown

# Überschrift Ebene 1
## Überschrift Ebene 2
### Überschrift Ebene 3

*hervorgehoben*
**stark hervorgehoben**

-   Liste
-   Liste

1.  Aufzählung
2.  Aufzählung

[Link](https://example.com)
::::

::::::





## Rollen (Inline-Elemente)

Rollen dienen zur erweiterten Formatierung *innerhalb einer Zeile*, bzw. können spezielle *Funktionen* haben wie z. B. das Einfügen eines Querverweises.


Allgemeine Syntax
:   ::::{code} markdown

    Text {rollenname}`Inhalt`

    ::::

:::{list-table} Beispiele für Rollen
:header-rows: 1
:stub-columns: 1

*   -   Funktion
    -   Rolle
    -   Beispiel
*   -   Abkürzung
    -   `{abbr}`
    -   ``` {abbr}`MRT (Magnetresonanztomographie)` ```
*   -   Querverweis
    -   `{ref}`
    -   ``` {ref}`Beschreibung <label>` ```
*   -   Nummerierter Querverweis
    -   `{numref}`
    -   ``` {numref}`Beschreibung <label>` ```
*   -   Verweis auf Term
    -   `{term}`
    -   ``` {term}`term` ```
*   -   Verweis auf Formel
    -   `{eq}`
    -   ``` {eq}`FormelEinstein` ```
*   -   Bild
    -   `{image}`
    -   ``` {image}`a.png` ```
*   -   Mathematik
    -   `{math}`
    -   ``` {math}`E = mc^2` ```
*   -
    -
    -   ```  ```

:::





## Direktiven (Block-Elemente)

Direktiven dienen der Formatierung von abgesetzten *Blöcken* und haben meistens spezielle *Funktionen* (Textboxen, Einfügen von Bildern oder Tabellen etc.).
Sie beginnen mit einem Fence (`:::`) und einem Namen in geschweiften Klammern und enden in einer der folgenden Zeilen wiederum mit `:::`.
Alles was zwischen den Fences steht wird von der Direktive erfasst.
Direktiven können auch ineinander *verschachtelt* werden, dabei erhöht sich die Anzahl der `:` der jeweiligen Direktive damit es eindeutig bleibt, welcher Fence welche Direktive beendet.
Direktiven können ein *Argument* und darüber hinaus mehrere *Optionen* haben.



Allgemeine Syntax
:   ::::{code} markdown

    :::{name} Argument
    :Option1: Wert
    :Option2: Wert

    Inhalt
    :::

::::

Häufig verwendete Direktiven sind:

-   `image` ... für unbeschriftete Bilder
-   `figure` ... für beschriftete Bilder
-   `math` ... für Formeln
-   `admonition` ... für Boxen

::::::{admonition} Beispiel: Abbildung

::::{code} markdown

:::{figure} a.png
:align: center
:width: 50%

Bildunterschrift
:::
::::

:::{figure} a.png
:align: center
:width: 50%

Bildunterschrift
:::

::::::



## Definitionslisten

Definitionslisten dienen zur Darstellung von Begriffen mit zugehörigen Definitionen.
Sie eignen sich besonders für *Glossare*, Verzeichnisse oder *strukturierte Erklärungen*.
Eine Definitionsliste besteht aus einem **Begriff** (*Term*) und einer oder mehreren **Definitionen**:


::::{code} markdown

Begriff
:   Definition

::::


::::::{admonition} Beispiel: Definition List

::::{code} markdown

Reanimation
:   Wiederbelebungsmaßnahmen zur Wiederherstellung von Atmung und Kreislauf

Hypoxie
:   Sauerstoffmangel im Gewebe
::::

Reanimation
:   Wiederbelebungsmaßnahmen zur Wiederherstellung von Atmung und Kreislauf

Hypoxie
:   Sauerstoffmangel im Gewebe

::::::


::::::{admonition} Beispiel: Mehrzeilige Definition

::::{code} markdown

Sepsis
:   Lebensbedrohliche Organdysfunktion infolge einer dysregulierten Immunantwort auf eine Infektion.
    Sie kann verschiedene Ursachen haben.

    Man kann ihr auch einen weiteren Absatz widmen.
::::

Sepsis
:   Lebensbedrohliche Organdysfunktion infolge einer dysregulierten Immunantwort auf eine Infektion.
    Sie kann verschiedene Ursachen haben.

    Man kann ihr auch einen weiteren Absatz widmen.

::::::


::::::{admonition} Beispiel: Mehrere Definitionen

::::{code} markdown

Schock
:   Lebensbedrohlicher Zustand mit unzureichender Gewebeperfusion
:   Psychische Reaktion auf belastendes Ereignis
::::

Schock
:   Lebensbedrohlicher Zustand mit unzureichender Gewebeperfusion
:   Psychische Reaktion auf belastendes Ereignis

::::::


Hinweise:

-   Der Begriff steht in einer eigenen Zeile
-   Die Definition beginnt mit `:   `
-   Einrückung ist entscheidend für die Struktur
-   Mehrere Definitionen sind möglich





(Referenz-erzeugen)=

## Querverweise

Mit Labels können Abschnitte, Abbildungen oder Gleichungen referenziert werden.

:::{list-table} Rollen für Querverweise
:header-rows: 1
:stub-columns: 1

*   -   Funktion
    -   Rolle
    -   Beispiel
*   -   Querverweis
    -   `{ref}`
    -   ``` {ref}`Beschreibung <label>` ```
*   -   Nummerierter Querverweis
    -   `{numref}`
    -   ``` {numref}`Beschreibung <label>` ```
*   -   Verweis auf einen Term in einem Glossar
    -   `{term}`
    -   ``` {term}`term` ```
*   -   Verweis auf Formel
    -   `{eq}`
    -   ``` {eq}`FormelEinstein` ```

:::


1.  **Marke** (Label) **setzen**:
    Dies ist abhängig davon, *was* referenziert werden soll (Überschrift, Bild, Tabelle etc.)

    -   *Label vor Überschrift* setzen mittels `(Labelname)=`


        Erzeugt das Label `Reanimation` vor der eigentlichen Überschrift:

        ::::{code} markdown


        (Referenz-erzeugen)=

        # Referenz erzeugen
        ::::

    -   *Direktiven* (z.B. Bild, Tabelle, Formel) benennen:
        Dies geschieht mittels der Option `:label:` innerhalb der Direktive:

        ::::{code} markdown

        :::{figure} a.png
        :label: fig-beispiel

        Bildunterschrift
        :::
        ::::


2.  **Verweis erzeugen**

    ::::{code} markdown

    Siehe {ref}`Referenz-erzeugen`, oder siehe {ref}`Beipiel zum Erzeugen einer Referenz <Referenz-erzeugen>`.
    ::::



::::::{admonition} Beispiel: Querverweis

::::{code} markdown

Siehe {ref}`Referenz-erzeugen`, oder siehe {ref}`Beipiel zum Erzeugen einer Referenz <Referenz-erzeugen>`.
::::

Siehe {ref}`Referenz-erzeugen`, oder siehe {ref}`Beipiel zum Erzeugen einer Referenz <Referenz-erzeugen>`.

::::::





## Mathematik

Mathematik kann in der Zeile (inline) oder als abgesetzter Block dargestellt werden:

1.  **In der Zeile**:

    ::::{code} markdown

    $E = mc^2$
    ::::

2.  Als **Block**:

    ::::{code} markdown

    ```{math}
    E = mc^2
    ```
    ::::

::::::{admonition} Beispiel: Mathematik

::::{code} markdown

:::{math}
:label: FormelEinstein

E = mc^2
:::

Der Vorteil des Blocks ist, dass die Formel benannt und mit der Rolle `{eq}}` referenziert (siehe Formel {eq}`FormelEinstein`) werden kann.
::::

:::{math}
:label: FormelEinstein

E = mc^2
:::

Der Vorteil des Blocks ist, dass die Formel benannt und mit der Rolle `{eq}` referenziert (siehe Formel {eq}`FormelEinstein`) werden kann.

::::::






## Fußnoten



::::::{admonition} Beispiel: Fußnote

::::{code} markdown

Text mit Fußnote[^Bezeichner]

[^Bezeichner]: Text der Fußnote
::::

Text mit Fußnote[^Bezeichner]

[^Bezeichner]: Text der Fußnote

::::::

## Frontmatter

Frontmatter enthält Metadaten und steht am Anfang der Datei.


::::::{admonition} Beispiel: Frontmatter

::::{code} yaml

---
title: Mein Dokument
authors:
  - name: Max Mustermann
date: 2025-03-30
status: final
---

Hier beginnt dann der eigentliche Text des Dokuments ...
::::
::::::
