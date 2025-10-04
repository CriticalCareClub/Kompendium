
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

Die Konzentration hängt laut dem Gesetz von William Henry vom  Partialdruck ab.


:::{subfigure} AB
:subcaptions: below
:name: FIG-BS-Henry
:class-grid: outline
:gap: 20px

Bilderserie: Konzentration, Partialdruck und das Henry'sche Gesetz. [₢ Johannes Schneider, {term}`ℓ CC-BY-SA 4.0`]

![Die Konzentration an Teilchen in der flüssigen Phase (hier blau dargestellt) hängt vom Partialdruck ab.](../../Bilder/CC-BY-SA/Konzentrationsabhaengigkeit_vom_Partialdruck_1.\*)

![Eine Erhöhung des Außendrucks (hier durch Einpressen eines Kolbens dargestellt) führt zu einem höheren Partialdruck der Gasphase und folglich zu einer höheren Konzentration.](../../Bilder/CC-BY-SA/Konzentrationsabhaengigkeit_vom_Partialdruck_2.\*)

:::




Mit dem relativ einfachen Henry-Gesetz lässt sich die **Dekompressionserkrankung** {index}` <Dekompressionserkrankung>` bei Tauchern erklären.
Der Umgebungsdruck nimmt um etwa *1 bar pro 10 Meter* Wassertiefe zu. Mit zunehmendem Partialdruck löst sich mehr Stickstoff zunächst im Blut, das ihn in die Peripherie transportiert. Dort diffundiert er vorzugsweise in Kompartimente mit hohem Fettanteil. Erfolgt das Auftauchen zu schnell bzw. ohne die evtl. notwendigen Dekompressionspausen, so ist die Rückdiffusion von Stickstoff (Gewebe → Blut → Lunge →
Wasser) zu langsam, sodass er ausperlt. Findet dies im Gewebe statt, spricht man von Bends (Gelenkschmerzen), im Lungenkreislauf von Chokes (Atemproblemen) oder bei Blasenbildung in Arterien, die Hirn- oder Rückenmark versorgen, von Staggers (neurologischen Symptomen).



:::{index} single: Verdampfer
:::

## Verdampfer

Ein Verdampfer ist ein Gerät, das eine Flüssigkeit gezielt in die Gasphase überführt.
Dazu nutzt er verschiedene Prinzipien, um die Verdampfung zu unterstützen und zu steuern.

- Über ein **Ventil** wird der Gasfluss reguliert, sodass die Menge des verdampften Stoffes kontrolliert dosiert werden kann.
- Eine **vergrößerte Oberfläche** (z. B. durch spezielle Strukturen oder Einsätze) erleichtert die Verdampfung, da mehr Flüssigkeit gleichzeitig in Kontakt mit der Umgebungsluft oder Heizfläche steht.
- Durch **Erhitzen** wird zusätzliche Energie zugeführt, wodurch die Flüssigkeit schneller in die Gasphase übergeht.

:::{rubric} Medizinische Bedeutung
:::
In der Medizin werden Verdampfer vor allem in der **Anästhesie** eingesetzt, um flüchtige Anästhetika (z. B. Sevofluran, Isofluran, Desfluran) kontrolliert zu verdampfen und mit dem Atemgasstrom zu vermischen.
Dadurch lässt sich die Konzentration des Narkosemittels präzise einstellen.

<!--

# Markdown-Vorgaben

## Allgemeine Formatierung

1. Es wird Myst-Markdown verwendet.
2. Es wird colon-fencing verwendet (":::" statt "```")
3. Jeder Satz beginnt im Markdown-Quelltext in einer neuen Zeile.
4. Begriffe werden im ersten Satz nicht hervorgehoben, wenn sie bereits die Überschrift darstellen.
5. Die Tab size beträgt 2 Leerzeichen.

## Index-Einträge

Für wichtige Termini werden Index-Einträge vor Überschriften gesetzt.

Beispiel:

::::
:::{index} single: Term
:::

## Term
Der Term wird hier erklärt.
::::

## Einheiten
Einheiten werden mit einem schmalen geschützten Leerzeichen (Unicode 202F) abgetrennt.

Beispiele:

:::
10 mm
2 mg / kg
120 mm Hg
::::

## Tabellen
Tabellen werden mit der MyST-Direktive `list-table` erstellt.

Beispiel:

::::
:::{list-table} Beispiel-Tabelle
:header-rows: 1

* - Begriff
  - Formel
  - Einheit
* - Druck
  - $p = \frac{F}{A}$
  - Pa (N / m²)
:::
 -->::::