---
status: final
---


:::{index} single: Versionierung
:::

# Versionierung

Eine Versionsnummer besteht aus einem dreistelligen **Primärschlüssel**, bestehend aus:

1. der **Hauptversionsnummer** (*Major*) zur Kennzeichnung
  der **Hauptversionslinie**,
2. der **Nebenversionsnummer** (*Minor*) zur Kennzeichnung
  von Update-Versionen der jeweiligen *Hauptversionslinie* und
3. der **Revisionsnummer** für Fehlerbehebungen ohne inhaltliche Änderungen;





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



::::{admonition} Versionsverwaltung (Git-Archiv)

```{eval-rst}
.. git_changelog::
    :revisions: 1
```

```{eval-rst}
.. git_commit_detail::
    :branch:
    :commit:
    :uncommitted:
    :untracked:
```
::::


