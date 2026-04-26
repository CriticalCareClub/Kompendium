---
status: final
---

:::{raw} latex
\clearpage
:::

:::{index} pair: Code; Guidelines
:::

# Style Guide – MyST-Markdown (Medizinisches Kompendium)



## Allgemeine Prinzipien

-   Ausgabe erfolgt **immer als Markdown-Code**.
-   Stil: **präzise, knapp, fachsprachlich korrekt**.
-   Fokus: **klinische Entscheidungsunterstützung**.
-   Jeder Satz beginnt in einer neuen Zeile.
-   Jeder Abschnitt muss klinisch verwertbar sein.



## Einrückung

-   Einrückungen folgen einem **Tab-Stop von 4 Zeichenpositionen**.
-   Listen werden entsprechend ausgerichtet: `-   Text`
-   Unterpunkte werden um eine weitere Ebene eingerückt:


    ::::{code} markdown

    -   Punkt
        -   Unterpunkt
    ::::





## Überschriften

Eine Überschriftseinheit besteht aus:

1.  Indexeinträgen
2.  Label
3.  Überschrift


:::::{admonition} Beispiel
:class: example

::::{code} markdown

:::{index} single: Begriff
:::

(label)=

## Überschrift

::::
:::::


Vor Überschriftseinheiten stehen **5 Leerzeilen**, ausgenommen unmittelbar davor steht eine Überschrift ohne Text dazwischen.





## Field Lists

Vor und nach jedem Field-List-Block stehen **2 Leerzeilen**.

::::{code} markdown

Begriff
:   Text


Mehrzeilig:


Begriff
:   Erste Zeile.
    Zweite Zeile.

::::





## Listen

-   Listenpunkte verwenden das Format `-   Text`.
-   Verschachtelung erfolgt mit einer weiteren Einrückungsebene.
-   Kein Fließtext als Pseudo-Liste.





## List-Tables

::::{code} markdown

:::{list-table} Titel
:header-rows: 1

*   -   Spalte 1
    -   Spalte 2
*   -   Wert A
    -   Wert B
:::
::::





## Admonitions

Synopsis-Boxen verwenden eine eigene Klasse:

:::::{admonition} Beispiel

::::{code} markdown

:::{admonition} Synopsis
:class: synopsis

-   Punkt
:::
::::
:::::

Keine Verwendung von `tip`, `warning` oder `info` für Synopsis-Boxen.





## Referenzen

-   Alles mit eigenem Kapitel wird referenziert.
-   Begriff und Abkürzung dürfen beide referenziert werden.


:::::{admonition} Beispiel

{ref}`Elektrokardiogramm <EKG>` ({ref}`EKG <EKG>`)

:::::





## Hervorhebungen

-   *kursiv*: Fachbegriffe, Parameter, Konzepte
-   **fett**: zentrale klinische Aussagen
-   Begriffe aus der Überschrift werden im Fließtext nicht erneut hervorgehoben.





## Typografie

-   „z. B.“ und „d. h.“ mit "protected thin space" (Unicode U+202f) schreiben.
-   Zahlenbereiche mit Gedankenstrich (EM-Dash).
-   Einheiten  mit "protected thin space" (Unicode U+202f) trennen  (z. B. 90 mm Hg)
-   Doppelte Leerzeichen vermeiden.