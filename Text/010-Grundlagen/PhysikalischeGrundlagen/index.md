# Physikalische Grundlagen



```{index} single: Druck
```
```{index} single: p
```

(druck)=

## Druck

$$
p=\frac{F}{A}
$$

```{index} single: Pascal
```
```{index} single: Pa
```
```{index} single: Bar
```
```{index} single: Torr
```
```{index} single: mm Hg
```
```{index} single: atm
```

### Druckeinheiten

> 1 Pascal (Pa) = 1 N / m²
>
> 1 Bar = 10⁵ Pa
>
> 1 Pa = 133,3 Torr
>
> 1 Torr = 1 mm Hg
>
> 1 atm ≈ 1 Bar

```{index} single: Temperatur
```
```{index} single: Kelvin
```

## Temperatur

Maßeinheit *Kelvin* (**K**). Absoluter Nullpunkt: **273,15** °C.

Die Temperatur $T$ ist proportional zur mittleren kinetischen Energie der Moleküle:

$$
T \propto \langle E_{\mbox{kin}} \rangle
$$

```{index} single: Gasgesetze
```

## Gase — Gasgesetze

Drei Variablen:

- Volumen $V$,
- Temperatur $T$,
- Druck $p$

Es gilt:

$$
p \propto \frac{1}{V} \quad \ldots T~\mbox{konstant}

V \propto T \quad \ldots p~\mbox{konstant}

P \propto T \quad \ldots V~\mbox{konstant}
$$

```{index} single: R; Gaskonstante Gaskonstante Zustandsgleichung; ideale Gase
```

### Zustandsgleichung *idealer* Gase

$$
p \cdot V = n \cdot R \cdot T
$$

Molzahl $n$, {index}`Gaskonstante` $R$ (8,314J/(mol K))

```{index} Kohäsionsbinnendruck; Zustandsgleichung realer Gase Zustandsgleichung; reales Gase
```

### Zustandsgleichung *realer* Gase

*Reale* Gase: Moleküle haben Ausdehnung, Kräfte zwischen den Molekülen:

$$
\left(p + {\frac{a}{V^2}}\right) \cdot \left(V - {\color{green}b}\right) = n \cdot R \cdot T
$$

${{\frac{a}{V^2}}}$ Kohäsionsbinnendruck,
${\color{green}b}$ Eigenvolumen der Gasmoleküle

## Drücke in Flüssigkeiten

Der Druck in strömenden Medien besteht aus einem statischen und einem dynamischen Anteil. Beide Teile sind von der Dichte abhängig. Sie unterscheiden sich dadurch, dass der statische Druck (bei konstanter Dichte) *linear* mit der Höhe $h$ der Flüssigkeitssäule steigt und von der (Erd-)beschleunigung $g$ abhängig ist. Der dynamische Anteil wächst dagegen *quadratisch* mit der Strömungsgeschwindigkeit des Fluids.

```{index} single: Druck, hydrostatischer
```
```{index} single: hydrostatischer Druck
```

(hydrostatischerdruck)=

### Hydrostatischer Druck $p_h$

$$
p_h = \rho \cdot g \cdot h + p_0
$$

$ρ$ Dichte,
$g$ Erdbeschleunigung (9,81 m / s²),
$h$ Höhe \[m\],
$p_0$ Luftdruck auf Flüssigkeitsoberfläche

```{index} single: Paradoxon; hydrostatisches
```

(hydrostatischesparadoxon)=

#### Hydrostatisches Paradoxon

```{eval-rst}
.. todo::   ?? Bild unterschiedliche Gefäße  Hydrostatisches_Paradoxon4.svg
```

Auch bei unterschiedlich geformten Gefäßen ist der hydrostatische Druck am Boden überall gleich groß (*hydrostatisches Paradoxon*;
Wandkräfte; gilt nur für Flüssigkeiten!).

~~~{index} single: Druck; hydrodynamischer
```
```{index} single: Staudruck
```
```{index} single: p\ :sub:`d`
~~~

(hydrodynamischerdruck)=

### Hydrodynamischer Druck

Hydrodynamischer Druck $P_d$, auch: Staudruck

$$
p_d = \frac{\rho \cdot v^2}{2}
$$

:::{attention}
Der hydrodynamische Druck $p_d$ wächst **quadratisch** mit der Flußgeschwindigkeit.
:::

## Strömungen

```{index} single: Kontinuitätsgesetz
```

### Kontinuitätsgesetz

Das Kontinuitätsgesetz besagt (in integraler Form), dass der Massenstrom eines Fluids (Flüssigkeit oder Gas) in einem Rohr unabhängig davon ist, wo er gemessen wird. Für inkompressible Fluide gilt Kontinuität auch für den Volumenstrom.

:::{figure} /Bilder/WikipediaCcBySa/FlowRate_gv52.png

Quelle: Wikipedia/Guy vandegrift, Lizenz: Creative Commons Attribution-Share Alike 3.0 Unported
:::

```{index} single: Kontinuitätsgleichung
```
```{index} single: Kontinuitätsgesetz
```

#### Kontinuitätsgleichung

:::{admonition} Gleichung: Kontinuitätsgleiuchung
$$
A_1 ⋅ v_1 = A_2 ⋅ v_2
$$
:::

:::{figure} /Bilder/Sketches/Sketch-000002.\*
:::

#### Bernoulli-Gleichung

:::{admonition} Gleichung: Bernoulli-Gleichung
$$
p_{\sum} = p_{ST} + p_h + p_d = \mathsf{konstant}
$$
:::

Die Summe aus dem hydrostatischen,

hydrodynamischen und

Gesamtdruck ist konstant.

:::{figure} /Bilder/Sketches/Sketch-000003.\*
:::

#### Bernoulli-Prinzip

Durch die Differenz von statischen Drücken kommt es zum Auftrieb.

:::{figure} /Bilder/Sketches/Sketch-000001.\*
:::

### Venturi-Prinzip

Fließt durch die Venturi-Düse ein gasförmiges oder flüssiges Medium, so ist an der engsten Stelle des Rohres der dynamische Druck (Staudruck) maximal und der statische Druck minimal. Die Geschwindigkeit des fließenden Gases (bzw. der Flüssigkeit) steigt im Verhältnis der Querschnitte beim Durchströmen des eingeschnürten Teils an, weil überall dieselbe Menge durchfließt. Gleichzeitig sinkt der Druck im Abnahmerohr, das genau im engen Teil sitzt. Damit entsteht ein Differenzdruck, der dann in verschiedenen Messgeräten oder zum Ansaugen von Flüssigkeiten oder Gasen benutzt wird.

Die Druckdifferenz ist bei Flüssigkeiten (inkompressibel und ohne Reibung) durch die Bernoulli-Gleichung gegeben. Bei idealen Gasen gilt die erweiterte Bernoulli-Gleichung.

```{eval-rst}
.. todo:: ?? Venturirohr.jpg

```

```{index} single: Strömungswiderstand 
```
```{index} pair: Gleichung; Strömungswiderstand
```

### Strömungswiderstand

Der Strömungswiderstand ist die physikalische Größe, die in der Fluiddynamik die Kraft bezeichnet, die das Fluid als Medium einer Bewegung entgegensetzt. Ein Körper, der sich relativ zu einem gasförmigen oder flüssigen Medium bewegt, erfährt einen Strömungswiderstand, eine der Relativgeschwindigkeit entgegengesetzt wirkende Kraft. Bewegt sich eine Person (z. B.
ein Jogger) oder ein Gegenstand (z. B. ein Flugzeug) an der Luft oder durch die Luft, so spricht man auch vom Luftwiderstand oder von der Luftreibung, bei hydrodynamischen Problemen im Wasser von Wasserwiderstand.

:::{admonition} Gleichung: Strömungswiderstand
$$
R = \frac{\Delta p}{\dot{V}}
$$

$\Delta p$

: Druckunterschied;
  ergibt sich aus $\Delta p = p_1 - p_2$,
  wobei $p_1$ und $p_2$ die jeweiligen Drücke am Anfang
  und am Ende des Weges sind.

$\dot{V}$

: Volumsstromstärke.
:::

Das entspricht dem aus der Elektrik bekannten $R=\frac{U}{I}$.

```{index} single: Hagen-Poiseuille-Gleichung
```
```{index} single: Gleichung; Hagen-Poiseuille
```

### Hagen-Poiseuille-Gleichung

bei *laminaren* Strömungen:

:::{admonition} Formel: Hagen-Poiseuille-Gleichung
$$
\dot{V} = \frac{\pi \cdot r^4 \cdot \Delta p}{8 \cdot \eta \cdot l} = \frac{\Delta p}{R}
$$

- $\dot{V}$  Volumsstromstärke,
- $r$                  Radius,
- $\Delta p$                  Druckunterschied,
- $η$                  Viskosität,
- $l$                 Länge.
:::

```{index} single: Reynolds-Zahl
```

### Turbulent oder laminar? Die Reynolds-Zahl

:::{admonition} Gleichung: Reynolds-Zahl
$$
\mathrm{Re} = \frac{v \cdot \rho \cdot r}{\eta}
$$

$v$

: Geschwindigkeit

$ρ$

: Dichte

$r$

: Radius

$η$

: Viskosität
:::

Cut-off: $Re$ = 1200, darüber eher turbulent, darunter eher laminar.

```{eval-rst}
.. todo:: Bild Kerze ??
```

## Dämpfe

Der Aggregatzustand eines Stoffes ist abhängig von der Temperatur und dem Umgebungsdruck.
Man Unterscheidet zwischen festen, flüssigen und gasförmigen Phasen.

Der Schnittpunkt der drei Phasen wird *Trippelpunkt* genannt, für Wasser liegt er bei 273,16 K und 613 Pa.

```{index} single: Dampfdruck
```

### Dampfdruck

```{index} single: Henry-Gesetz
```
```{index} single: Gesetz, Henry- 
```
```{index} single: Blut-Gas-Verteilungskoeffizient
```
```{index} single: BGV
```

(henrygesetz)=
(henrykonstante)=

#### Henry-Gesetz

Das *Henry-Gesetz* besagt, dass der Partialdruck eines Gases über einer Flüssigkeit direkt proportional ist zur Konzentration des Gases in der Flüssigkeit. Die Proportionalität wird ausgedrückt durch die Henry-Konstante $H^{cp}$.

:::{admonition} Gleichung: Henry-Gesetz
$$
c = H^{cp} \cdot p
$$

$c$

: Gaskonzentration (im Blut)

$H^{cp}$

: Henry-Löslichkeitskonstante

$p$

: Partialdruck des Gases
:::

Die dimensionslose *Henry-Löslichkeitskonstante* $H^{cc}$
wird auch als {dfn}`Blut-Gas-Verteilungskoeffizient` *BGV* bezeichnet:

$$
\mathsf{BGV} = H^{cc} = \frac{c_{\mathsf{Blut}}}{\cdot c_{\mathsf{Gas}}}
$$

```{eval-rst}
.. table:: BGV

      +--------------+--------+--------------------------------------------+
      | e. g.        | BGV    |                                            |
      +==============+========+============================================+
      | Ether        | 12,1   | hohe Löslichkeit, langsames Anfluten       |
      +--------------+--------+--------------------------------------------+
      | Chloroform   | 8,4    |                                            |
      +--------------+--------+--------------------------------------------+
      | Halothan     | 2,3    |                                            |
      +--------------+--------+--------------------------------------------+
      | Lachgas      | 0,47   |                                            |
      +--------------+--------+--------------------------------------------+
      | Xenon        | 0,14   | niedrige Löslichkeit, schnelles Anfluten   |
      +--------------+--------+--------------------------------------------+
```

Die Konzentration hängt laut dem Gesetz von William Henry vom  Partialdruck ab

:::{figure} /Bilder/WikipediaCcBySa/Konzentrationsabhängigkeit_vom_Partialdruck_1.\*

Die Konzentration an Teilchen in der flüssigen Phase (hier blau dargestellt) hängt vom Partialdruck ab. Eine ...
:::

:::{figure} /Bilder/WikipediaCcBySa/Konzentrationsabhängigkeit_vom_Partialdruck_2.\*

Erhöhung des Außendrucks (hier durch Einpressen eines Kolbens dargestellt) führt zu einem höheren Partialdruck der Gasphase und folglich zu einer höheren Konzentration.
:::

Mit dem relativ einfachen Henry-Gesetz lässt sich die **Dekompressionserkrankung** {index}`\ <Dekompressionserkrankung>` bei Tauchern erklären.
Der Umgebungsdruck nimmt um etwa *1 bar pro 10 Meter* Wassertiefe zu. Mit zunehmendem Partialdruck löst sich mehr Stickstoff zunächst im Blut, das ihn in die Peripherie transportiert. Dort diffundiert er vorzugsweise in Kompartimente mit hohem Fettanteil. Erfolgt das Auftauchen zu schnell bzw. ohne die evtl. notwendigen Dekompressionspausen, so ist die Rückdiffusion von Stickstoff (Gewebe → Blut → Lunge →
Wasser) zu langsam, sodass er ausperlt. Findet dies im Gewebe statt, spricht man von Bends (Gelenkschmerzen), im Lungenkreislauf von Chokes (Atemproblemen) oder bei Blasenbildung in Arterien, die Hirn- oder Rückenmark versorgen, von Staggers (neurologischen Symptomen).

### Verdampfer

- Ventil zur Regulation des Gasflows
- vergrößerte Oberfläche
- erhitzen
