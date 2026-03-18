---
status: final
---

:::{index} single:: Pulskonturanalyse
:::
:::{index} single: Swing
:::
:::{index} single: pulse pressure variation
:::
:::{index} single: PPV
:::
:::{index} single: SVV
:::
:::{index} single: Stroke Volume Variation
:::
:::{index} single: Pulse Pressure Variation
:::
:::{index} single: Variation; Stroke Volume
:::
:::{index} single: Variation; Pulse Pressure
:::

(pulskonturanalyse)=
(GHDM-VO-Pulskonturanalyse)=
(GHDM-VO-PKThermo-Systeme)=
(PPV)=
(SVV)=

# Pulskonturanalyse und Thermodilution

## Pulskonturanalyse

Die {ref}`invasive arterielle Blutduckmessung <IABP>` erlaubt als Nebeneffekt auch die Interpretation der gemessenen und dargestellten Pulskurve.
Die Pulskonturanalyse ermöglicht zwei Dinge:

1. Beurteilung der Pulskurve an sich;

   - Variation der Minima- und Maxima-Werte v. a. während des Atemzyklus (Einfluss der intrathorakalen Druckverhältnisse auf den Pulsdruck): *"Swing"* {index}` <Swing>` der Arterienkurve
   - Variationen der Pulskontur der einzelnen Schläge, insbes. des *Area under the curve* (AUC; Fläche unter der Kurve).
     Daraus lässt sich die **Pulse Pressure Variation** (**PPV**) errechnen.

2. Herleitung des Schlagvolumens durch Zuhilfenahme der {ref}`Thermodilutionstechnik <thermodilution>`. Dies erlaubt die Ermittlung von:

   - **Variation des Schlagvolumens** während des Atemzyklus: **Stroke Volume Variation** (**SVV**)
     Die Technik beruht auf dem Prinzip, dass ein erhöhter intrathorakaler Druck im Inspirationszyklus mechanischer Beatmungsgeräte den venösen Rückfluss und damit das Herzzeitvolumen verringert.
     Diese Abnahme wird durch Berechnung des Herzzeitvolumens während Inspiration (Abnahme) und Exspiration (SVV) bestimmt.

     Der positive Druck der Beatmung wirkt sich umso mehr aus ("die Varianz ist größer"), je geringer der Druck im Ventrikel ist und dagegen wirkt („leerer Ventrikel").
   - Kontinuierliche Berechnung des **Cardiac Outputs** (**CO**)

%
%
%
%
% Das berechnete Herzzeitvolumen bezieht sich normalerweise auf eine vorherige Messung des Herzzeitvolumens unter Verwendung einer transpulmonalen Verdünnungstechnik.
%
% Das Flo trac™-System verwendet einen proprietären Algorithmus zur Berechnung des Herzzeitvolumens mithilfe der Pulswellenformanalyse, ohne dass eine Kalibrierung erforderlich ist (auf Kosten der Genauigkeit).
%
% Die Differenz zwischen Pulsdruck (PPV) oder systolischem Druck (SPV) wird ebenfalls als Surrogatmarker verwendet, wodurch die Notwendigkeit einer Messung des Herzzeitvolumens entfällt.

:::{todo} {issue}`130` Grafik: PPV ../Bilder/PPV.jpg


:alt: Bild
:width: 100%

Die Änderungen der intrathorakalen Druckverhältnisse während der In- und Exspiration beeinflussen den venösen Rückstrom und folglich die Blutdruckamplitude.
Dies zeigt sich an der Druckkurve einerseits durch schwankende Minima und Maxima, als auch durch eine Amplituden- und Flächenvarianz.
:::

:::{todo} {issue}`130` Grafik: SVV ../Bilder/SVV-1.png


:alt: Bild
:width: 100%

Varianz der Area under the curve (AUC)
:::

Doch wie kann man von einer Druckkurve auf ein Flussvolumen schließen?
Dazu benötigt man folgende Voraussetzungen:

- Alle möglichen Störgrößen müssen so gut es geht ausgeschlossen werden:

  - Der Pulsschlag muss regelmäßig sein
  - Die Atmung des Patienten muss sowohl was die Frequenz, als auch das Volumen betrifft regelmäßig sein (d. h. kontrolliert beatmet).

- Ist dies gegeben wird die Druckkurve zu einem Herzauswurf in Beziehung gesetzt. Dies kann geschehen durch:

  - **Messung**: Der Cardiac Output wird mittels {ref}`Thermodilution <Thermodilution>` *gemessen* und gleichzeitig die Pulskontur aufgezeichnet. Ein Beispiel dafür ist das System {ref}`PiCCO <PiCCO>`.
  - **Statistik und Mathematik**: Anhand diverser Parameter (Alter, Geschlecht, Körperoberfläche, …) ermittelt ein Algorithmus aus der Druckkurve ein wahrscheinliches Auswurfsvolumen. Beispiele solcher Systeme *Vigeleo™* oder *FloTrac™* der Firma Edwards Lifesciences™[^flotracalgorithmus].
    Die Aussagekraft und  Nutzen dieser Systeme ist umstritten ({term}`🗎 Marqué 2013`, {term}`🗎 Oh 2022`, {term}`🗎 Su 2012`).

[^flotracalgorithmus]: Der FloTrac-Algorithmus analysiert die Druckwellenform hundertmal pro Sekunde.
    Diese Datenpunkte werden zusammen mit den demografischen Informationen des Patienten verwendet, um die Standardabweichung des arteriellen Drucks ($\sigma_{\rm AP}$) zu berechnen.

    Die Umrechnung von ($\sigma_{\rm AP}$ in ml/Schlag erfolgt durch Multiplikation mit dem Umrechnungsfaktor ${\rm Khi}(x)$.
    Dieser ist eine multivariate Polynomgleichung, die den Einfluss des sich ständig ändernden Gefäßtonus $x$ auf den Pulsdruck bewertet, indem die Pulsfrequenz des Patienten, der   mittlere arterielle Druck, die Standardabweichung des mittleren arteriellen Drucks, die Compliance der großen Gefäße — *wie anhand der Patientendemografie geschätzt (!)* — sowie die Schiefe und Kurtosis der arteriellen Wellenform analysiert werden. {term}`🗎 FloTrac 2020`

:::{figure} ../../../Bilder/Gabriel-Sebastian-CCCA/IMG_082107.001341px.jpg

Tachykardie mit deutlichem Swing in der Arterienkurve
:::



:::{index} single: Thermodilution
:::
:::{index} single: Stewart-Hamilton-Gleichung
:::
:::{index} single: Gleichung; Stewart-Hamilton
:::

(thermodilution)=
(GHDM-VO-Thermodilutionstechnik)=
(ghdm-vo-thermodilutionstechnik-co)=

## Flussmessung durch *Thermodilution*

Wenn man eine bekannte Menge einer Substanz (Marker) stromaufwärts injiziert, hängt die Änderung der Konzentration stromabwärts von der Strömungsgeschwindigkeit ab.
Der Fluss über die Zeit ergibt das Herzzeitvolumen.
Dies beschreibt die **Stewart-Hamilton-Gleichung**:

$$
{\rm CO} = \frac{\rm Dosis}{C t}
$$

$C t$: *Area under the concentration curve* über die Zeit.

Dies gilt nicht nur für Stoffe als Marker, sondern sinngemäß auch für Temperaturänderungen, dies wird bei der Thermodilutionsmethode angewendet.
Injiziert man einen Bolus mit kalter Lösung, ist die Geschwindigkeit des Blutflusses umgekehrt proportional zur zeitlichen Temperaturänderung, somit ist die mittlere Temperaturabnahme umgekehrt proportional zum Herzzeitvolumen.

Die messbaren Kurven sind je nach CO unterschiedlich.
Je höher das Herzzeitvolumen, desto schneller der Blutfluss und desto kürzer, kleiner und steiler ist die Thermodilutionskurve.
Bei niedrigem CO ist die Kurve träge, mit einer großen Fläche unter der Kurve (AUC).

:::{todo} {issue}`130` Grafik: ../Bilder/Thermodilution_Injektion_Verlauf.png


:alt: Bild
:width: 100%

Beispiel Thermodilutionskurve: Temperaturänderungen, die von einer peripheren Arterie aufgezeichnet wurden
:::
