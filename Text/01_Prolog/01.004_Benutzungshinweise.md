---
status: final
---

# Benutzungshinweise

## Im Text

*Betonte* Textteile sind kursiv, *Besonders stark betonte* sind fett gedruckt.
**Fachbegriffe**, welche an dieser Stelle erklärt werden, haben ebenfalls eine eigene Formatierung.
Normale Fußnoten [^footnote-1] beinhalten Hintergrundinformationen, die nicht uninteressant sind, aber den normalen Fließtext unnötig aufblähen würden.

[^footnote-1]: Ich bin eine normale Fußnote.



Wie jede Wissenschaft ist die Medizin ständigen Entwicklungen unterworfen.
Soweit fachliche Angaben gemacht werden, darf der Leser zwar darauf vertrauen, dass die Autoren große Sorgfalt darauf verwandt haben, dass diese Angaben dem Wissensstand bei Fertigstellung des Werkes entspricht.
Für Angaben, speziell bezüglich Dosierungen und Applikationsformen, kann jedoch keine Gewähr übernommen werden.

Jeder Leser ist angehalten, durch sorgfältige Prüfung der Literatur, der Lehrmeinung sowie der Beipackzettel der verwendeten Präparate und gegebenenfalls nach Konsultation eines Spezialisten festzustellen, ob die gegebene Aussage oder Empfehlung für Dosierungen oder die Beachtung von Kontraindikationen gegenüber der Angabe in diesem Werk abweicht.
Jede Dosierung oder Applikation erfolgt auf eigene Gefahr des Benutzers.

Die Herausgeber bitten jeden Leser, ihm aufgefallene Ungenauigkeiten und Fehler, sowie Anregungen und konstruktive Kritik mitzuteilen.

Geschützte Warennamen und Warenzeichen werden nicht durchgehend besonders kenntlich gemacht. Aus dem Fehlen eines solchen Hinweises kann also nicht geschlossen werden, dass es sich um einen freien Warennamen handelt.

Sofern nicht explizit angegeben, beziehen sich geschlechtsspezifische Bezeichnungen – soweit dies inhaltlich in Betracht kommt – auf Frauen und Männer in gleicher Weise.

Satz und Druckvorstufe
: [Sphinx Toolchain](https://sphinx-doc.com), LaTeX

Entwicklungsumgebung
: GNU Emacs, MS Visual Studio Code

Versionsverwaltung
: Git



<!--
## Kompetenzlevel

Die Kompetenzlevel des Zielpublikums der einzelnen Inhalte des Kompendiums des CCCA sind
wie in der folgenden Tabelle gegliedert:

```{eval-rst}
.. tabularcolumns:: cclL
```

:::{list-table} Kompetenzlevel
:class: tabulary
:header-rows: 1
:stub-columns: 1

- - ID
  - Level
  - Titel
  - Beschreibung
- - 0
  - A
  - Laien, Ersthelfer
  - Laienhelfer
- - 1
  - B
  - First Responder
  - First Responder (ohne Ausbildung nach SanG)
- - 2
  - C
  - Basic
  - *.at* Rettungssanitäter
- - 3
  - D
  - Intermediate
  - *.at* Notfallsanitäter mit oder ohne Notfallkompetenz NKA;
    *.de* Rettungssanitäter
- - 4
  - E
  - Advanced
  - Ärzte,
    diplomiertes Pflegepersonal;
    *.at* Notfallsanitäter mit Notfallkompetenz NKV oder NKI;
    *.de* Notfallsanitäter,
    Rettungsassistenten
- - 5
  - F
  - Expert
  - Experten,
    Ärzte,
    Fachärzte,
    diplomiertes Pflegepersonal mit Zusatzausbildung
:::

## Maßnahmen

Maßnahmen im engeren Sinne sind festgelegte Handlungsempfehlungen,
vergleichbar mit Lehrmeinungen. Es wird zwischen allgemeinen, Standard- und speziellen Maßnahmen unterschieden, siehe {ref}`Tafel-Massnahmentypen`.
Jede Maßnahme hat eine Kennung und eine Versionsnummer.

(tafel-massnahmentypen)=

```{eval-rst}
.. table:: Maßnahmentypen

        +----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | **ID**   | **Art**                  | **Beschreibung**                                                                                                                                                                                            |
        +----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | ALL      | *Allgemeine Maßnahmen*   | Allgemeine Maßnahmen beziehen sich auf eine Gruppe von Patienten mit einer Übergruppe bestimmter, verwandter Erkrankungen, wobei eine weiterführende Unterteilung mittels spezieller Maßnahmen existiert.   |
        +----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | STD      | *Standardmaßnahmen*      | Standardmaßnahmen treffen unter bestimmten Bedingungen auf eine große Gruppe unterschiedlicher Patienten mit unterschiedlichen Diagnosen zu.                                                                |
        +----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | SPZ      | *Spezielle Maßnahmen*    | Spezielle Maßnahmen treffen auf bestimmte Patienten mit einer bestimmten Diagnose oder einem bestimmten Zustand zu.                                                                                         |
        +----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


```

(table-versionstypen)=

```{eval-rst}
.. table:: Versionstypen. Es gibt sechs verschiedene Versionstypen, welche den Entwicklungsfortschritt einer Version angeben

           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | **Kennung**   | **Versionstyp**          | **Beschreibung**                                                                                                                                                                                                                                                                                                                                                               | **Beispiel**                     |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | *nightly*     | *Laufende Entwicklung*   | Es handelt sich dabei um eine Zwischenversion ohne formale Kriterien zur Fertigstellung. Die Versionstyp-spezifische Nummerierung ergibt sich aus dem Datum.                                                                                                                                                                                                                   | ``2.0.0.nightly.20140119164900`` |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | *alpha*       | *Zwischenversion*        | Version ohne wesentliche formale Kriterien zur Fertigstellung, gedacht als Version zu Demonstrations- oder speziellen Testzwecken. Eine Version, welche zu einem Review eingereicht wird, wäre auch eine Alpha Version. Die Versionstyp-spezifische Nummerierung ergibt sich aus dem Datum.                                                                                    | ``2.0.0.alpha.20140119164900``   |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | *beta*        | *Sprintversion*          | Version, welche nach einem Sprint (Entwicklungszyklus, Iteration) fertig gestellt wurde. Grundsätzlich wäre sie theoretisch nach formalen Gesichtspunkten einsetzbar, jedoch entspricht sie nicht den inhaltlichen Qualitätsstandards und ist auch nicht zum produktiven Einsatz gedacht. Die Versionstyp-spezifische Nummerierung ergibt sich aus der Nummer der Iteration.   | ``2.0.0.beta.44``                |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | *gamma*       | *Vorabversion*           | Version, welche für den produktiven Einsatz in kontrollierten Umgebungen (Partnerinstitutionen) gedacht ist. Die Versionstyp-spezifische Nummerierung ergibt sich aus einer fortlaufenden Nummerierung der Vorabversionen.                                                                                                                                                     | ``2.0.0.gamma.1``                |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | *delta*       | *Release Candidate*      | Für die Veröffentlichung eingereichte Version. Die Versionstyp-spezifische Nummerierung ergibt sich aus dem Zusatz RC und einer durch einen Bindestrich getrennten fortlaufenden Nummerierung (RC-1, …).                                                                                                                                                                       | ``2.0.0.delta.RC-1``             |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
           | *final*       | *Release*                | Es handelt sich hierbei um die endgültige Version, welche für den öffentlichen und produktiven Einsatz konzipiert wurde. Die finale Version hat keine Versionstyp-spezifische Nummerierung.                                                                                                                                                                                    | ``2.0.0``                        |
           +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

```

-->

:::{list-table} Entwicklungsfortschritt und Versionstypen
:header-rows: 1
:stub-columns: 1

*   -   Kennung
    -   Versionstyp
    -   Beschreibung
    -   Beispiel
*   -   *nightly*
    -   Laufende Entwicklung
    -   Es handelt sich dabei um eine Zwischenversion ohne formale Kriterien zur Fertigstellung.

        ``<last_tagged_version>+<commits_since>!DRAFT#B=<branch>.ID=<commit-id>``
    -   ``v4.0.0-alpha.388+9!DRAFT#B=master.ID=c7c92447``
*   -   alpha
    -   Entwicklungsversion
    -   Version ohne wesentliche formale Kriterien zur Fertigstellung, gedacht als Version zu Demonstrations- oder speziellen Testzwecken.
        Endversion eines Entwicklungszyklus (Sprint).
    -   ``4.0.0-alpha.359``
*   -   beta
    -   Vorabversion
    -   Version, welche theoretisch nach formalen Gesichtspunkten einsetzbar wäre, jedoch entspricht sie nicht den inhaltlichen Qualitätsstandards und ist auch nicht zum produktiven Einsatz gedacht.
    -   ``4.0.0-beta.44``
*   -   RC
    -   Release Candidate
    -   Für die Veröffentlichung eingereichte Version.
    -   ``4.0.0-RC.1``
*   -   final
    -   Release
    -   Veröffentlichte Version, welche für den öffentlichen und produktiven Einsatz konzipiert wurde.
    -   ``4.0.0``
:::

