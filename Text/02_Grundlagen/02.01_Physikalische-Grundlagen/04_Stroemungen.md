---
status: final
---




# Strömungen




## Viskosität
**Viskosität** ist das Maß für die Zähigkeit einer Flüssigkeit.

- Dynamische Viskosität $\eta$: beschreibt den inneren Reibungswiderstand einer Flüssigkeit.
- Newtonsches Gesetz der inneren Reibung:
$$
F = \eta \cdot A \cdot \frac{dv}{dx}
$$

Blut hat eine nicht-Newtonsche Viskosität (abhängig von Scherung, Hämatokrit, Temperatur).

:::{rubric} Medizinische Bedeutung
:::
- Erhöhter Hämatokrit → erhöhte Viskosität → höherer Strömungswiderstand (z. B. Polyzythämie)
- Erniedrigte Viskosität bei Anämie
- Einfluss auf Durchblutung, Herzarbeit und Mikroperfusion



:::{index} single: Kontinuitätsgesetz
:::

## Kontinuitätsgesetz

Das **Kontinuitätsgesetz** ist ein Grundsatz der Strömungslehre.
Es besagt, dass die **Masse in einem abgeschlossenen System erhalten bleibt**.
Für eine Strömung bedeutet das: Was in ein Rohr hineinfließt, muss zeitgleich auch herausfließen.

Dies bedeutet, dass der Massenstrom eines Fluids (Flüssigkeit oder Gas) in einem Rohr unabhängig davon ist, wo er gemessen wird.
Für inkompressible Fluide gilt Kontinuität auch für den Volumenstrom.

:::{figure} ../../../Submodules/3134-medical-picture-collection/CC-BY-SA-3.0/FlowRate_gv52.png

Quelle: Wikipedia/Guy vandegrift, Lizenz: Creative Commons Attribution-Share Alike 3.0 Unported
:::



:::{index} single: Kontinuitätsgleichung
:::
:::{index} single: Kontinuitätsgesetz
:::

### Kontinuitätsgleichung

Die **Kontinuitätsgleichung** beschreibt den Zusammenhang von Strömungsgeschwindigkeit und Querschnittsfläche in einem Rohrsystem.
Sie basiert auf der Massenerhaltung:
Was in ein Rohr hineinfließt, muss auch wieder herausfließen.


:::{admonition} Gleichung: Kontinuitätsgleichung

... für inkompressible Flüssigkeiten:

$$
A_1 ⋅ v_1 = A_2 ⋅ v_2
$$
:::

:::{figure} ../../../Submodules/3134-medical-picture-collection/Gabriel-Sebastian/Sketches/Sketch-000002.\*
:::

Konsequenzen:
- Verengt sich der Querschnitt ($A$ kleiner), muss die Geschwindigkeit ($v$) steigen.
- Erweitert sich der Querschnitt, sinkt die Geschwindigkeit.


:::{rubric} Medizinische Bedeutung
:::
- **Blutgefäße:** Strömungsgeschwindigkeit nimmt in Stenosen (Gefäßverengungen) stark zu.
- **Herzklappen:** Bei Klappenstenosen verengt sich der Querschnitt → erhöhte Strömungsgeschwindigkeit
- **Doppler-Sonographie:** Misst Geschwindigkeiten und berechnet damit Druckgradienten.
- **Atemwege:** Verengungen (z. B. bei Asthma) führen zu erhöhter Strömungsgeschwindigkeit.
- **Infusionen:** Querschnitt von Kathetern bestimmt die Fließgeschwindigkeit.



(Bernoulli-Gleichung)=

## Bernoulli-Gleichung

Die **Bernoulli-Gleichung** beschreibt die Energieerhaltung in einer reibungsfreien Strömung.
Sie verbindet **Druck**, **Strömungsgeschwindigkeit** und **Höhenlage** eines Fluids.


:::{admonition} Gleichung: Bernoulli-Gleichung
$$
p_{\sum} = p_{ST} + p_h + p_d = \mathsf{konstant}
$$
:::

Die drei Terme entsprechen:
- **statischer Druck**
- **dynamischer Druck**
- **hydrostatischer Druck**

Die Summe aus dem *hydrostatischen*, *hydrodynamischen* und *Gesamtdruck* ist *konstant*.

Konsequenzen:
- Erhöht sich die Geschwindigkeit ($v$), sinkt der statische Druck ($p$).
- Druck, Geschwindigkeit und Höhe sind miteinander gekoppelt.

:::{figure} ../../../Submodules/3134-medical-picture-collection/Gabriel-Sebastian/Sketches/Sketch-000003.\*
:::



(Bernoulli-Prinzip)=

### Bernoulli-Prinzip

Das **Bernoulli-Prinzip** besagt:
**In einer strömenden Flüssigkeit nimmt der statische Druck ab, wenn die Strömungsgeschwindigkeit zunimmt.**
Durch die Differenz von statischen Drücken kommt es zum Auftrieb.

Konsequenzen:
- Tragflächenprofil: Luft strömt oben schneller → Druck sinkt → Auftrieb entsteht.
- {ref}`Venturi-Effekt <Effekt>`: Strömung durch Engstellen → Unterdruck → Ansaugen von Flüssigkeit oder Gas.



:::{figure} ../../../Submodules/3134-medical-picture-collection/Gabriel-Sebastian/Sketches/Sketch-000001.\*
:::

(Venturi-Effekt)=

### Venturi-Effekt

Fließt durch die **Venturi-Düse** ein *gasförmiges* oder *flüssiges* Medium, so ist *an der engsten Stelle* des Rohres *der dynamische Druck (Staudruck) maximal* und der *statische Druck minimal*.

Die Geschwindigkeit des fließenden Gases (bzw. der Flüssigkeit) steigt im Verhältnis der Querschnitte beim Durchströmen des eingeschnürten Teils an, weil überall dieselbe Menge durchfließt.
Gleichzeitig sinkt der Druck im Abnahmerohr, das genau im engen Teil sitzt.
Damit entsteht ein **Differenzdruck**, der dann in verschiedenen Messgeräten oder zum *Ansaugen* von Flüssigkeiten oder Gasen benutzt wird.

Die Druckdifferenz ist bei Flüssigkeiten (inkompressibel und ohne Reibung) durch die {ref}`Bernoulli-Gleichung <Bernoulli-Gleichung>` gegeben.
Bei idealen Gasen gilt die erweiterte Bernoulli-Gleichung.



:::{index} single: Strömungswiderstand
:::
:::{index} pair: Gleichung; Strömungswiderstand
:::

(Stroehmungswiderstand)=

## Strömungswiderstand

Der Strömungswiderstand ist die physikalische Größe, die in der Fluiddynamik die Kraft bezeichnet, die das Fluid als Medium einer Bewegung *entgegensetzt* ("durch Reibung gehemmt wird").
Ein Körper, der sich relativ zu einem gasförmigen oder flüssigen Medium bewegt, erfährt einen Strömungswiderstand, eine der Relativgeschwindigkeit entgegengesetzt wirkende Kraft.
Bewegt sich eine Person (z. B. ein Jogger) oder ein Gegenstand (z. B. ein Flugzeug) an der Luft oder durch die Luft, so spricht man auch vom Luftwiderstand oder von der Luftreibung, bei hydrodynamischen Problemen im Wasser von Wasserwiderstand.

:::{admonition} Gleichung: Strömungswiderstand
$$
R = \frac{\Delta p}{\dot{V}} =  \frac{p_1 - p_2}{\dot{V}}
$$

- $\Delta p$: Druckunterschied;
  ergibt sich aus $\Delta p = p_1 - p_2$, wobei $p_1$ und $p_2$ die jeweiligen Drücke am Anfang und am Ende des Weges sind.
- $\dot{V}$: Volumenstrom = Fluss[^Fluss] $\approx I$
:::

[^Fluss]: Im medizinischen Alltag meint "**Fluss**" (engl. *flow*) fast immer den **Volumenstrom**.
    {index}` <Beweis; Mediziner sind keine echten Naturwissenschaftler>`
    Streng genommen kann "Fluss" für Volumenfluss (Volumenstrom), Massenfluss ($\dot{m}$) oder Teilchenfluss (z. B. Ionenfluss durch Membranen) stehen.

Die Druckdifferenz $\Delta p = p_1 - p_2$ ist in anderen Worten ein Druck*gradient*, was im Prinzip einer *Spannung* ($U$) entspricht.
Versteht man nun den Volumenstrom als Fluss[^Fluss] bzw. Strom ($I$), so entspricht die Formel des Strömungswiderstandes dem aus der Elektrik bekannten {ref}`Ohm'schen Gesetz <Ohmsches-Gesetz>` ($R=\frac{U}{I}$).
Die Welt ist klein.




:::{index} single: Hagen-Poiseuille-Gleichung
:::
:::{index} single: Gleichung; Hagen-Poiseuille
:::

### Gesetz von Hagen-Poiseuille für *laminare* Strömungen



:::{admonition} Formel: Hagen-Poiseuille-Gleichung
$$
\dot{V} = \frac{\pi \cdot r^4 \cdot \Delta p}{8 \cdot \eta \cdot l} = \frac{\Delta p}{R}
$$

- $\dot{V}$: Volumenstromstärke
- $r$: Radius
- $\Delta p$: Druckunterschied
- $\eta$: Viskosität
- $l$: Länge
:::

Der Widerstand steigt mit der *vierten Potenz* der Gefäßverengung.

:::{rubric} Medizinische Bedeutung
:::
- Vasokonstriktion und Stenosen → drastische Zunahme des Widerstands
- Blutdruckregulation
- Atemwegswiderstand bei Asthma oder COPD



:::{index} single: Reynolds-Zahl
:::

### Die Reynolds-Zahl: Turbulent oder laminar?

Die **Reynolds-Zahl** (Re) ist eine dimensionslose Kennzahl der Strömungsmechanik.
Sie beschreibt das Verhältnis von Trägheitskräften zu Zähigkeitskräften (viskosen Kräften) einer Strömung.


:::{admonition} Gleichung: Reynolds-Zahl
$$
\mathrm{Re} = \frac{v \cdot \rho \cdot r}{\eta}
$$

- $v$: Geschwindigkeit
- $\rho$: Dichte
- $r$: Radius
- $\eta$: Viskosität
:::



:::{rubric}  Bedeutung
:::
- Re < 2300: **laminare Strömung** (geordnet, Schichtströmung)
- 2300 < Re < 4000: Übergangsbereich
- Re > 4000: **turbulente Strömung** (verwirbelt, unregelmäßig)


:::{rubric} Medizinische Bedeutung
:::
- **Blutströmung**: In großen Arterien (z. B. Aorta) können hohe Reynolds-Zahlen auftreten → Turbulenzen, Strömungsgeräusche.
- **Herzgeräusche**: Turbulente Strömungen bei Klappenfehlern (Stenosen, Insuffizienzen).
- **Doppler-Sonographie**: Strömungsform (laminar vs. turbulent) beeinflusst Messungen.
- **Infusionen/Atemwege**: Strömungsverhalten in Schläuchen und Kathetern.