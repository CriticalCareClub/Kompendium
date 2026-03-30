---
status: final
---




# MyST-Markdown Kurzanleitung

## Was ist Markdown?

**Markdown** (*MD*) ist eine Auszeichnungssprache, die entwickelt wurde, um Text mit einfacher, gut lesbarer Syntax zu formatieren.
Im Gegensatz zu komplexeren Formaten wie HTML oder LaTeX bleibt der Quelltext nahezu so lesbar wie der fertige Text.
Formatierungen wie Überschriften, Listen, Hervorhebungen oder Links werden durch wenige, intuitive Zeichen dargestellt (z. B. `#`, `*`, `[]()`).
Markdown wird häufig für Dokumentationen, Webseiten, wissenschaftliche Texte und Notebooks verwendet, da es einfach zu schreiben, plattformunabhängig und gut automatisierbar ist.
**MyST** (*Markedly Structured Text*) erweitert Markdown um Funktionen für wissenschaftliches und technisches Schreiben.
Es ergänzt Markdown um Direktiven, Rollen, Querverweise, Mathematik und strukturierte Metadaten.




:::{list-table} Markdown-Syntaxübersicht
:header-rows: 1
:widths: 19 27 27 27

*   -   Funktion
    -   Syntax
    -   Alternative
    -   Ergebnis

*   -   Einfache Hervorhebung
    -   `*Italic*`
    -
    -   *Italic*

*   -   Starke Hervorhebung
    -   `**Bold**`
    -
    -   **Bold**

*   -   Überschrift Ebene 1
    -   `# Heading 1`
    -
    -   # Heading 1

*   -   Überschrift Ebene 2
    -   `## Heading 2`
    -
    -   ## Heading 2

*   -   Link
    -   `[Link](http://a.com)`
    -
    -   [Link](http://a.com)


*   -   Zitat
    -   `>   Blockquote`
    -
    -
        >   Blockquote

*   -   Liste
    -
        ```
        -   List
        -   List
        -   List
        ```
    -
    -
        -   List
        -   List
        -   List

*   -   Aufzählung
    -
        ```
        1.   One
        2.   Two
        3.   Three
        ```
    -
    -
        1.   One
        2.   Two
        3.   Three

*   -   Defintionsliste
    -
        ```
        Begriff
        :   Die Erklärung
        ```
    -
    -   Begriff
        :   Die Erklärung
*   -   Horizontale Linie
    -   `---`
    -
    -   ***

*   -   Inline-Code
    -   `` `Inline code` ``
    -
    -   `Inline code`

*   -   Bild
    -   `![Image](a.png)`
    -   ```
        :::{image} a.png
        :::
        ```
    -   ![Image](a.png)
*   -   Bild mit Beschreibung
    -
    -   ```
        :::{figure} a.png

        Beschreibung
        :::
        ```
    -   :::{figure} a.png

        Beschreibung
        :::
*   -   Mathematik
    -
        ```
        $I = \frac{U}{R}$
        ```
    -   ```
        {math}`I = \frac{U}{R}`
        ```
    -   $I = \frac{U}{R}$

:::






## Basis-Markdown

::::::{admonition} Beispiel: Basis-Markdown

::::markdown
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

Rollen erweitern die Inline-Syntax.
Sie werden innerhalb einer Zeile verwendet.

Allgemeine Syntax:

::::markdown
Text {rollenname}`Inhalt`
::::

:::{list-table} Beispiele für Rollen
:header-rows: 1
:stub-columns: 1

*   -   Funktion
    -   Rolle
    -   Beispiel
*   -   Abkürzung
    -   abbr
    -   ``` {abbr}`MRT (Magnetresonanztomographie)` ```
*   -   Querverweis
    -   ref
    -   ``` {ref}`Beschreibung <label>` ```
*   -   Verweis auf Term
    -   term
    -   ``` {term}`term` ```
*   -   Bild
    -   image
    -   ``` {image}`a.png` ```
*   -   Mathematik
    -   math
    -   ``` {math}`E = mc^2` ```
*   -
    -
    -   ```  ```

:::







## Direktiven (Block-Elemente)

Direktiven sind strukturierte Blockelemente.
Sie beginnen meist mit einem Fence und einem Namen in geschweiften Klammern.

Allgemeine Syntax:

::::markdown
:::{name} Argument
:Option1: Wert
:Option2: Wert

Inhalt
:::
::::

Häufig verwendete Direktiven sind:

-   image
-   figure
-   math
-   admonition

::::::{admonition} Beispiel: Abbildung

::::markdown
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


::::markdown
Begriff
:   Definition
::::


::::::{admonition} Beispiel: Definition List

::::markdown
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

::::markdown
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

::::markdown
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






## Querverweise

Mit Labels können Abschnitte, Abbildungen oder Gleichungen referenziert werden.

### Label vor Überschrift setzen


Erzeugt das Label `Reanimation` vor der eigentlichen Überschrift:

::::markdown

(Referenz-erzeugen)=

# Referenz erzeugen
::::



### Direktive (z.B. Bild) benennen


::::markdown
:::{figure} a.png
:label: fig-beispiel

Bildunterschrift
:::
::::





(Referenz-erzeugen)=

### Referenz erzeugen

::::markdown
Siehe {ref}`Referenz-erzeugen`, oder siehe {ref}`Beipiel zum Erzeugen einer Referenz <Referenz-erzeugen>`.
::::

::::::{admonition} Beispiel: Querverweis

::::markdown
Siehe {ref}`Referenz-erzeugen`, oder siehe {ref}`Beipiel zum Erzeugen einer Referenz <Referenz-erzeugen>`.
::::

Siehe {ref}`Referenz-erzeugen`, oder siehe {ref}`Beipiel zum Erzeugen einer Referenz <Referenz-erzeugen>`.

::::::





## Mathematik

Mathematik kann inline oder als Block dargestellt werden.

### Inline

::::markdown
$E = mc^2$
::::

### Block

::::markdown
```{math}
E = mc^2
```
::::

::::::{admonition} Beispiel: Mathematik

::::markdown
:::{math}
E = mc^2
:::
::::

:::{math}
E = mc^2
:::
::::::

## Fußnoten

::::markdown
Text mit Fußnote[^Bezeichner]

[^Bezeichner]: Das ist die Fußnote.
::::

::::::{admonition} Beispiel: Fußnote

::::markdown
Text mit Fußnote[^Bezeichner]

[^Bezeichner]: Erklärung
::::

Text mit Fußnote[^Bezeichner]

[^Bezeichner]: Erklärung

::::::

## Frontmatter

Frontmatter enthält Metadaten und steht am Anfang der Datei.


::::::{admonition} Beispiel: Frontmatter

::::yaml
---
title: Mein Dokument
authors:
  - name: Max Mustermann
date: 2025-03-30
status: final
---
::::
::::::

