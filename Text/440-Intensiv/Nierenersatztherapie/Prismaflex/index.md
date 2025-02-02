```{index} single: Prismaflex®; Kurzanleitung Therapieführung (Zitrat) pair: Prismaflex®; Zitrat
```
```{index} single: Kalzium; Prismaflex® single: Kalzium; CVVHDF
```
```{index} single: Ca; Prismaflex® single: Ca; CVVHDF
```

(prismaflexkurzanleitung)=

# Prismaflex®: Kurzanleitung (Zitrat)

:::{centered} eXeed Software 6.10 — Automatisierte Zitratantikoagulation mit integriertem Ca-Ausgleich
:::


:::{warning}
Achtung!

Diese Inhalte wurden noch nicht geprüft!
:::

## Therapiebeginn

```{eval-rst}
.. table:: Prismaflex® Starteinstellungen

    +-------------------+------------------------------+-----------------------+
    | Blutfluss         | freie Einstellung            | 100—150 mL / min      |
    +-------------------+------------------------------+-----------------------+
    | Zitrat            | Prismocitrat 18/0            | automatisch adaptiert |
    +-------------------+------------------------------+-----------------------+
    | Dialysatfluss     | Phoxilium, freie Einstellung | 500—2000 mL / h       |
    +-------------------+------------------------------+-----------------------+
    | Substitution post | Phoxilium, freie Einstellung | 500—2000 mL / h       |
    +-------------------+------------------------------+-----------------------+
    | Zitratdosis       | Start mit                    | 3 mmol / L            |
    +-------------------+------------------------------+-----------------------+
    | Ca-Ausgleich      | Start mit                    | 80%                   |
    +-------------------+------------------------------+-----------------------+
```

Die Prismaflex®-Software berechnet automatisch das Verhältnis von
Blutfluß zu PBP-Flussrate (Antikoagulanz).
Diese Verhältnis wird z. B.
bei Veränderung der Blutflussrate entsprechend der angegebenen
Zitratdosis automatisch angepasst.
Die PBP-Flussrate wird auch automatisch angepasst,
wenn die Zitratdosis verändert/korrigiert wird.
Prismaflex® regelt bei Veränderung von Flussraten den Ca⁺⁺-Ausgleich automatisch.
Der Ca⁺⁺-Ausgleich wird automatsich bei Beginn der Therapie gestartet
und beim Beenden der Therapie gestoppt.

## Laborkontrollen

```{eval-rst}
.. table::

    +--------------------------------+--------------------------+-----------------------------------------------------------+----------------+
    | Untersuchung                   | Werte                    | Zeit nach Therapiebeginn oder Änderung der Zitratdosis    | Regelintervall |
    +================================+==========================+===========================================================+================+
    | BGA extrakorporal, post-Filter | Ca⁺⁺                     | **20 min**                                                | 1x tgl.        |
    +--------------------------------+--------------------------+-----------------------------------------------------------+----------------+
    | BGA intrakorporal              | Ca⁺⁺, Na⁺, K⁺, SB-Status | Startwert vor Therapie, **60 min** nach Änderung          | alle 4—6 h     |
    +--------------------------------+--------------------------+-----------------------------------------------------------+----------------+
    | Gesamtlabor intrakorporal      | Gasamt-Ca, Magnesium     | \                                                         | 1x tgl.        |
    +--------------------------------+--------------------------+-----------------------------------------------------------+----------------+



```

## Korrektur der Parameter

:::{list-table} Korrekturen
:widths: 15 15 15 55

- - Wert
  - Ziel
  - Korrekturparameter
  - Korrektur
- - Ca⁺⁺ extrakorporal
  - 0,25—50 mmol / L
  - Zitratdosis
  - ```{eval-rst}

    :< 0,25 mmol / L: Reduktion um 0,5 mmol / L
    :> 0,45 mmol / L: Erhöhung um 0,5 mmol / L
    ```
- - Ca⁺⁺ intrakorporal
  - 1,0—1,2 mmol / L
  - Ca⁺⁺-Ausgleich
  - ```{eval-rst}

    :< 0,8:         +20%
    :0,8--0,9:      +10%
    :0,9--0,99:     +5%
    :1--1,19:       keine Veränderung
    :1,2--1,25:     -5%
    :1,26--1,33:    -10%
    :> 1,33:        -20%
    ```
- - Bikarbonat

  - 22—26 mmol / L

  - Dialysat-Flussrate

  - „neue“ Zitratbeutel 18/0

    Alkalose

    : Erhöhung auf > 1500 ml / h

      Evtl. zusätzlich Erniedrigung der Zitratdosis um
      0,5 mmol / L

    Azidose

    : Reduktion auf 250--500 mL

      Eventuell zusätzlich Erhöhung der Zitratdosis um
      0,5 mmol / L, wird mehr Bikarbonat benötigt,
      Ausgleich durch Kurzinfusion (50--100 mL)
- - Kalium
  - 3,5—5 mmol / L
  - Kalium
  - nach internem Standard
- - Magnesium
  - 0,7—1,6 mmol / L
  - Magnesium
  - nach internem Standard
:::

% Ca⁺⁺ extrakorporal
% ========================================================================
%
% Ziel: **0,25—50 mmol / L**
%
% .. table:: Extrakorporales Ca⁺⁺ und Korrektur der Zitratdosis
%
%     +-----------------+---------------------------+
%     | iCa⁺⁺           | Korrektur Zitratdosis     |
%     +=================+===========================+
%     | < 0,25 mmol / L | Reduktion um 0,5 mmol / L |
%     +-----------------+---------------------------+
%     | > 0,45 mmol / L | Erhöhung um 0,5 mmol / L  |
%     +-----------------+---------------------------+
%
%
%
% Ca⁺⁺ intrakorporal
% ========================================================================
%
% Ziel:  **1,0—1,2 mmol / L**
%
% Initialer Ausgleich über Prisamflex-Spritzenpumpe 40—200%
%
% .. table:: Intrakorporales Ca⁺⁺ und Ca⁺⁺-Ausgleich
%
%     +------------------+----------------------------+
%     | iCa⁺⁺ art. (BGA) | Veränderung Ca⁺⁺-Ausgleich |
%     +==================+============================+
%     | < 0,8            |                       +20% |
%     +------------------+----------------------------+
%     | 0,8--0,9         |                       +10% |
%     +------------------+----------------------------+
%     | 0,9--0,99        |                        +5% |
%     +------------------+----------------------------+
%     | 1--1,19          |          keine Veränderung |
%     +------------------+----------------------------+
%     | 1,2--1,25        |                        -5% |
%     +------------------+----------------------------+
%     | 1,26--1,33       |                       -10% |
%     +------------------+----------------------------+
%     | > 1,33           |                       -20% |
%     +------------------+----------------------------+
%
% Alternativ kann der Ca⁺⁺-Ausgleich auch im Status Bildschirm in
% mL / h abgelesen werden
%
%
%
% Bikarbonat
% ========================================================================
%
% Ziel: **22—26 mmol / L**, „neue“ Zitratbeutel 18/0
%
% Alkalose
%     Erhöhung der Dialysat-Flussrate aus > 1500 ml / h
%
%     Evtl. zusätzlich Erniedrigung der Zitratdosis um
%     0,5 mmol / L
%
% Azidose
%     Reduktion der Dialysat-Flussrate auf 250--500 mL
%
%     Eventuell zusätzlich Erhöhung der Zitratdosis um
%     0,5 mmol / L, wird mehr Bikarbonat benötigt,
%     Ausgleich durch Kurzinfusion (50--100 mL)
%
% Kalium
% ========================================================================
%
% Ziel: **3,5—5 mmol / L**
%
% Kalium wird nach Standard des Klinikums substituiert
%
% Magnesium
% ========================================================================
%
% Ziel: **0,7—1,6 mmol / L**
%
% Kalium wird nach Standard des Klinikums substituiert
