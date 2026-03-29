---
status: final
---



:::{index} single: Druck
:::
:::{index} single: p
:::
:::{index} single: Pascal
:::
:::{index} single: Pa
:::
:::{index} single: Bar
:::
:::{index} single: Torr
:::
:::{index} single: mm Hg
:::
:::{index} single: atm
:::

(druck)=

# Druck

Druck ist eine fundamentale physikalische Größe, die beschreibt, wie viel Kraft auf eine bestimmte Fläche wirkt.
Die SI-Einheit ist **Pascal** (**Pa**), 1 Pascal (Pa) ist definiert als 1 N / m².

Mathematisch wird Druck als Kraft pro Fläche beschrieben:

:::{math} Druck
:name: EQ-Druck

p=\frac{F}{A}
:::


:::{table} Druckeinheiten

| Druckeinheit   | Wert in Pascal (Pa)     |
|----------------|--------------------------|
| 1 atm          | 101 325 Pa               |
| 1 bar          | 100 000 Pa               |
| 1 mbar         | 100 Pa                   |
| 1 cmH₂O        | 98.0665 Pa               |
| 1 mmHg         | 133.322 Pa               |
| 1 Torr         | 133.322 Pa               |
| 1 psi          | 6 894.76 Pa              |
| 1 Pa           | 1 Pa                     |
| 1 kPa          | 1 000 Pa                 |
| 1 MPa          | 1 000 000 Pa             |
:::




## Drücke in Flüssigkeiten

Der Druck in strömenden Medien besteht aus einem statischen und einem dynamischen Anteil. Beide Teile sind von der Dichte abhängig. Sie unterscheiden sich dadurch, dass der statische Druck (bei konstanter Dichte) *linear* mit der Höhe $h$ der Flüssigkeitssäule steigt und von der (Erd-)beschleunigung $g$ abhängig ist. Der dynamische Anteil wächst dagegen *quadratisch* mit der Strömungsgeschwindigkeit des Fluids.



:::{index} single: Druck, hydrostatischer
:::
:::{index} single: hydrostatischer Druck
:::
:::{index} single: Paradoxon; hydrostatisches
:::

(hydrostatischerdruck)=
(hydrostatischesparadoxon)=

### Hydrostatischer Druck $p_h$

Der **hydrostatische Druck** ist der Druck, der in einer ruhenden Flüssigkeit durch die Gewichtskraft der Flüssigkeitssäule entsteht.
Er nimmt mit der Tiefe zu, da mehr Flüssigkeit darüber lastet.
Der hydrostatische Druck in einer Tiefe $h$ unterhalb der Oberfläche einer Flüssigkeit mit Dichte $\rho$ ist:

$$
p_h = \rho \cdot g \cdot h ( + p_0)
$$

- $p_h$ = hydrostatischer Druck (Pa)
- $ρ$ Dichte der Flüssigkeit (kg/m³)
- $g$ Erdbeschleunigung (9,81 m / s²)
- $h$ Höhe der Flüssigkeitssäule (m)
- $p_0$ Druck an der Flüssigkeitsoberfläche (z. B. Atmosphärendruck): Der Gesamtdruck in der Tiefe $h$ ergibt sich aus Umgebungsdruck plus hydrostatischem Druck.


Das **hydrostatische Paradoxon** beschreibt ein scheinbares Paradoxon in der Hydrostatik:
Der **Druck am Boden eines Gefäßes** hängt nur von der **Höhe der Flüssigkeitssäule** ab,
**nicht** von der Form oder vom Volumen des Gefäßes.

:::{admonition} Hydrostatisches Paradoxon

- Zwei Gefäße mit **gleicher Flüssigkeitshöhe** üben am Boden den **gleichen Druck** aus,
  auch wenn ihre Formen und ihr Flüssigkeitsvolumen völlig unterschiedlich sind.
:::

:::{rubric} Medizinische Anwendungen
:::

- Die Einheit **Millimeter Quecksilbersäule** (mm Hg) kommt aus der Zeit, als Drücke mit **Quecksilber-Manometern** gemessen wurden, welche eine mit Quecksilber gefüllte Säule als Skala verwendeten.
  Diese Skala verwendete das Prinzip des hydrostatischen Drucks um den Druck zu ermitteln und den Wert anzuzeigen.
  Nach dem gleichen Prinzip funktioniert auch die Einheit *Zentimeter Wassersäule* (*cm H₂O*).
- **Blutdruck in Gefäßen:** In abhängigen Körperregionen (z. B. Beine im Stehen) erhöht sich der Druck durch die hydrostatische Säule des Blutes.
- **Orthostatische Dysregulation:** Blut versackt in den Beinen → zu geringer Druck im Gehirn → Schwindel oder Ohnmacht.
- **Infusionen:** Tropfbehälter über Patientenhöhe erzeugen durch hydrostatischen Druck den Fluss.
- **Liquordruckmessung:** Der Druck in der Lumbalpunktion hängt von der Höhe der Liquorsäule ab.
- **Tauchmedizin:** Zunahme des Außendrucks auf den Körper mit Tiefe im Wasser.




:::{todo} {issue}`6` GRAFIK: Hydrostatisches_Paradox: unterschiedliche Gefäße  on4.svg
:::




:::{index} single: Druck; hydrodynamischer
:::
:::{index} single: Staudruck
:::
:::{index} single: p\ :sub:`d`
:::

(hydrodynamischerdruck)=

### Hydrodynamischer Druck

Der **hydrodynamische Druck** $P_\text{dyn}$ (auch: Staudruck) ist ein Druckanteil, der durch die Bewegung einer Flüssigkeit entsteht.
Er ergibt sich aus der **Bewegungsenergie pro Volumeneinheit** eines strömenden Mediums.


$$
p_\text{dyn} = \frac{\rho \cdot v^2}{2}
$$

- $\rho$ = Dichte der Flüssigkeit (kg/m³)
- $v$ = Geschwindigkeit der Strömung (m/s)

$p_\text{dyn}$ beschreibt die Fähigkeit einer Strömung, **Kraft auf eine Oberfläche** auszuüben.
Je höher die Geschwindigkeit, desto größer der hydrodynamische Druck.

:::{attention}
Der hydrodynamische Druck $p_\text{dyn}$ wächst **quadratisch** mit der Flußgeschwindigkeit.
:::

:::{rubric} Medizinische Anwendungen
:::
- **Blutdruck und Hämodynamik:** Der Blutstrom in Gefäßen erzeugt neben dem statischen Druck auch einen hydrodynamischen Druckanteil.
- **Herzklappen:** Strömungsgeschwindigkeit des Blutes bestimmt Druckdifferenzen über Herzklappen (z. B. bei Stenosen).
- **Doppler-Sonographie:** Berechnet Strömungsgeschwindigkeiten und damit Druckgradienten in Gefäßen.
- **Ventilationstherapie:** Strömungsgeschwindigkeiten von Atemgasen beeinflussen Druckverhältnisse in den Atemwegen.



## Gesamtdruck einer Strömung

Nach der **Bernoulli-Gleichung** setzt sich der Gesamtdruck $p_\text{ges}$ in einer Strömung aus drei Komponenten zusammen:

$$
p_\text{ges} = p_\text{stat} + p_\text{dyn} + p_\text{hyd}
$$

- $p_\text{stat}$ = statischer Druck (ruhende Flüssigkeit, Umgebungsdruck)
- $p_\text{dyn}$ = **dynamischer Druck** (hydrodynamischer Druck)
- $p_\text{hyd}$ = Schweredruck (durch Höhe im Gravitationsfeld)
