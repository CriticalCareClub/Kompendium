
# Gase

Der Aggregatzustand eines Stoffes ist abhängig von der Temperatur und dem Umgebungsdruck.
Man Unterscheidet zwischen festen, flüssigen und gasförmigen Phasen.

Der Schnittpunkt der drei Phasen wird *Trippelpunkt* genannt, für Wasser liegt er bei 273,16 K und 613 Pa.

:::{index} single: Gasgesetze
:::

## Gasgesetze

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



:::{index} single: R; Gaskonstante
:::
:::{index} single: Gaskonstante
:::
:::{index} single: Zustandsgleichung; ideale Gase
:::

## Zustandsgleichung *idealer* Gase

$$
p \cdot V = n \cdot R \cdot T
$$

Molzahl $n$, {index}`Gaskonstante` $R$ (8,314J/(mol K))



:::{index} Kohäsionsbinnendruck; Zustandsgleichung realer Gase
:::
:::{index} single: Zustandsgleichung; reales Gase
:::

## Zustandsgleichung *realer* Gase

*Reale* Gase: Moleküle haben Ausdehnung, Kräfte zwischen den Molekülen:

$$
\left(p + {\frac{a}{V^2}}\right) \cdot \left(V - {\color{green}b}\right) = n \cdot R \cdot T
$$

${{\frac{a}{V^2}}}$ Kohäsionsbinnendruck,
${\color{green}b}$ Eigenvolumen der Gasmoleküle



:::{index} single: Dampfdruck
:::

## Dampfdruck

:::{index} single: Henry-Gesetz
:::
:::{index} single: Gesetz, Henry-
:::
:::{index} single: Blut-Gas-Verteilungskoeffizient
:::
:::{index} single: BGV
:::

(henrygesetz)=
(henrykonstante)=

### Henry-Gesetz

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



:::{table} Blut-Gas-Verteilungskoeffizient (BGV) verschiedener Narkosegase

| Narkosegas | BGV  |                                          |
| ---------- | ---- | ---------------------------------------- |
| Ether      | 12,1 | hohe Löslichkeit, langsames Anfluten     |
| Chloroform | 8,4  |                                          |
| Halothan   | 2,3  |                                          |
| Lachgas    | 0,47 |                                          |
| Xenon      | 0,14 | niedrige Löslichkeit, schnelles Anfluten |
:::

Die Konzentration hängt laut dem Gesetz von William Henry vom  Partialdruck ab



:::{subfigure} AB
:subcaptions: below
:name: FIG-BS-
:class-grid: outline
:gap: 20px

Bilderserie: Konzentration, Partialdruck und das Henry'sche Gesetz \[₢ Johannes Schneider, {term}`ℓ CC-BY-SA 4.0`\]


![Die Konzentration an Teilchen in der flüssigen Phase (hier blau dargestellt) hängt vom Partialdruck ab. Eine ...](/Bilder/CC-BY-SA/Konzentrationsabhängigkeit_vom_Partialdruck_1.\*)

![Erhöhung des Außendrucks (hier durch Einpressen eines Kolbens dargestellt) führt zu einem höheren Partialdruck der Gasphase und folglich zu einer höheren Konzentration.](/Bilder/CC-BY-SA/Konzentrationsabhängigkeit_vom_Partialdruck_2.\*)

:::




Mit dem relativ einfachen Henry-Gesetz lässt sich die **Dekompressionserkrankung** {index}` <Dekompressionserkrankung>` bei Tauchern erklären.
Der Umgebungsdruck nimmt um etwa *1 bar pro 10 Meter* Wassertiefe zu. Mit zunehmendem Partialdruck löst sich mehr Stickstoff zunächst im Blut, das ihn in die Peripherie transportiert. Dort diffundiert er vorzugsweise in Kompartimente mit hohem Fettanteil. Erfolgt das Auftauchen zu schnell bzw. ohne die evtl. notwendigen Dekompressionspausen, so ist die Rückdiffusion von Stickstoff (Gewebe → Blut → Lunge →
Wasser) zu langsam, sodass er ausperlt. Findet dies im Gewebe statt, spricht man von Bends (Gelenkschmerzen), im Lungenkreislauf von Chokes (Atemproblemen) oder bei Blasenbildung in Arterien, die Hirn- oder Rückenmark versorgen, von Staggers (neurologischen Symptomen).

## Verdampfer

- Ventil zur Regulation des Gasflows
- vergrößerte Oberfläche
- erhitzen
