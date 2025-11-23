---
status: final
---

:::{index} single: PICCO
:::
:::{index} single: Puls Contour Cardiac Output
:::

(picco)=

# PICCO (Puls Contour Cardiac Output) = Pulskontur Herzzeitvolumen

Das PiCCO-System (PULSION Medical Systems AG, München, Deutschland) führt nun die Prinzipien der Thermodilution und der Pulskonturanalyse zusammen:
Es errechnet kontinuierlich ein Cardiac Output durch Analyse der arteriellen Druckwellenform.
Dabei wird die Thermodilution verwendet, um eine Kalibrierung und Zuordnung von Druckkurve zu Fluss zu bewerkstelligen.
Eine regelmäßige **Kalibrierung**, anfangs sowie nach Änderungen der Patientenposition oder anderer Variablen etc., ist notwendig.

Klappenvitien führen zu einer Änderung der Druck-Volumen-Kurve beim PICCO (AS+AI)!



:::{index} single: Thermodilution; transpulmonale
:::

(GHDM-KP-Transpulm-Thermodil)=

## *Transpulmonale* Thermodilution und Pulskonturanalyse

Als Kalibriertechnik wird die *transpulmonale* {ref}`Thermodilution <Thermodilution>` angewandt.
Diese verwendet grundsätzlich das Stewart-Hamilton-Prinzip, allerdings wird die Temperaturänderungen **von einem zentral-venösen** Zugang zu einem **zentralen arteriellen Zugang**, z. B. in der A. femoralis, erfasst.
Somit wird auch die Lungenstrombahn miterfasst, die Herzkammern und die Lunge mit dem extravaskulären Lungenwasser sind die Mischkammern für den kalten Bolus.

:::{todo} {issue}`130` Grafik: ../Bilder/Picco-Kreislauf.png

:alt: Bild
:width: 100%

Die kalte Bolusgabe erfolgt über einen ZVK, die anschließende Messung über einen speziellen arteriellen Katheter in zentraler Lage
:::

Mittlere Transitzeit (MTt)

: Die MTt ist definiert als die Zeit, die im Mittel vergeht bis der Indikator (das gekühlte Injektat) am Sensor ankommt.

Downsloapzeit (DSt)

: Die DSt definiert die Zeit zwischen den beiden Messpunkten 75% und 25% des Maximums der Indikatorverdünnungskurve nach Stewart-Hamilton-Methode





:::{todo} {issue}`130` Grafik: ../Bilder/Thermodilution-Downsloap.png


:alt: Bild
:width: 100%

Thermodilution-Downsloap
:::

Die aus der Thermodilution mit kalter Kochsalzlösung abgeleitete Kurve wird verwendet, um die arterielle Kontur zu kalibrieren und eine kontinuierliche Überwachung zu ermöglichen.
Der PiCCO-Algorithmus ist abhängig von der Morphologie der Blutdruckwellenform (mathematische Analyse der Wellenform).
Die transpulmonale Thermodilution umfasst das rechte Herz, den Lungenkreislauf und das linke Herz, was eine weitere mathematische Analyse der Thermodilutionskurve ermöglicht und Messungen des *Herzfüllvolumens* (Globales End-Diastolisches Volumen/-Index, *GEDV*, *GEDI*), des *intrathorakalen Blutvolumens* (Volumen in den Kammern des Herzens und des Lungenkreislaufs, *ITBV*) und des *extravaskulären Lungenwassers* (ELW, *ELWI*) und den pulmonalvaskulären Permeabilitätsindex (*PVPI*) liefert.
Die Zusammenschau von ELWI und PVPI ermöglicht die Unterscheidung der Ursache eines Lungenödems hinsichtlich Capillar leak oder eines Hydrostatisches Ödems.

dPmax: indirekte Messung über die Steilheit des Druckanstiegs in der Aorta

Die transpulmonale Thermodilution ermöglicht eine weniger invasive Kalibrierung, ist jedoch weniger genau als die pulmonalarterielle Thermodilution und erfordert einen zentralvenösen und arteriellen Zugang mit den damit verbundenen Infektionsrisiken.


:::{list-table} PiCCO: Messwerte und deren Bedeutung
:header-rows: 1

* - Vorlastparameter
  - Inotropie
  - Nachlastparameter
  - Global, sonstige
* - - GEDI
    - ITBV

    Flüssigkeit:
    - SVV
    - PPV
    - ELWI
    - PVPI
  - - dpmax
  - - SVRI
  - - CI
:::





Vorteile des PICCO
: - wenig invasiv,
  - wenig Komplikationen,
  - kontinuierliche HZV-Messung,
  - GEDV besser als ZVD (Volumen vs. Druckmessung),
  - ITBV korreliert gut mit SVI und CI

Nachteil
: - Vitien beeinflussen die Ergebnisse;
  - SVV nicht messbar bei spontaner Atmung und Vorhofflimmern.
  - regelmäßige Kalibrierung notwendig
  - spezieller arterieller Katheter notwendig (Thermistor)