---
status: final
---



:::{raw} latex
\clearpage
:::

:::{index} single: Blutgasanalyse
:::
:::{index} single: BGA
:::

(respmonitoringbga)=
(ARMO-KP-Blutgasanalyse)=
(Blutgasanalyse-respiratorisch)=

# Blutgasanalyse, respiratorischer Aspekt

```{toctree}
:caption: 'Inhalt:'
:maxdepth: 3
```

Syn.: *Astrup*, Abkz.: *BGA*; Engl: *Arterial Blood Gas Test* (*ABG*)

Die Blutgasanalyse ist ein Verfahren zur Messung von **Gas-Partialdrücken** sowie des pH-Wertes im Blut.
Basierend darauf können bestimmte Werte *berechnet* werden.
Darüber hinaus verfügen moderne BGA-Geräte oft auch über umfangreiche andere Mess- und Berechnungsmethoden im Sinne eines *Ponit-of-Care-Labors*, z. B. für *Hämoglobin*, Elektrolyte und Laktat.

*Gemessen* werden die Gas-*Partialdrücke* pO₂, pCO₂ und der pH[^bgamesselektroden].
*Berechnet* wird u. a. das *Standardbikarbonat*, *Basenüberschuss* (Base Excess, BE) und die *SpO₂*.

[^bgamesselektroden]: [Clark-Elektrode (pO₂), Serveringhaus-Elektrode(pCO₂), Glaselektrode (pH)]{.deep}

Abhängig davon, welches Blut untersucht wird (arteriell, venös, gemischt- oder zentralvenös) lassen sich unterschiedliche Aussagen treffen, vgl. {ref}`Hämodynamisches Monitoring / BGA <HaemodynMonitoringBGA>`.



:::{index} single: paO₂
:::
:::{index} single: paCO₂
:::
:::{index} single: HCO₃⁻
:::
:::{index} single: pH
:::
:::{index} single: H⁺
:::
:::{index} pair: Severinghaus; Elektrode
:::
:::{index} pair: Clark; Elektrode
:::
:::{index} pair: Glas; Elektrode
:::

(ARMO-KP-Partialdruecke)=

## Was fange ich mit den Messwerten an?

:::{list-table} BGA-Referenzbereiche (Erwachsene)
:stub-columns: 1

- - pH
  - 7,36--7,44
  -
  -
  -
- - paO₂
  - 75–97
  - mm Hg
  - 10–12,9
  - kPa
- - paCO₂
  - 35--**40**--45
  - mm Hg
  - 4,6–6,0
  - kPa
- - HCO₃⁻ (std)
  - 23--**24**--27
  - mmol/l
  -
  -
:::



:::{index} single: Sauerstoffgehalt
:::
:::{index} single: Sauerstoffträger
:::
:::{index} single: Sauerstoffkonzentration
:::
:::{index} single: CaO₂
:::

(ARMO-KP-CaO2)=

### Sauerstoffgehalt des Blutes

Sauerstoff wird im Blut an Hämoglobin **gebunden** und als Gas **physikalisch gelöst** transportiert.
Der physikalisch gelöste Anteil ist dabei verschwindend gering.
Die Sauerstoffkonzentration ${\color{blue}\rm{CaO}_2}$ berechnet sich dabei folgendermaßen:

$$
{\color{blue}\rm{CaO}_2} = ({\color{teal}\rm{Hb} \times 1,34 \times \rm{SaO}_2} + {\color{violet}\rm{paO}_2 \times 0,0031})
$$ (CaO₂)

:::{hlist}
- $\color{blue}\rm{Hb}$: Sauerstoffträger (Hämoglobin)
- $\color{blue}\rm{SaO}_2$: Sättigung des Sauerstoffträgers
- $\color{blue}1,34$: Hüfner'sche Zahl.
  Sie gibt an, wieviel Milliliter Sauerstoff als Absolutwert pro Gramm Hämoglobin gebunden und transportiert werden kann.
- $\color{violet}\rm{paO}_2$ in mm Hg
- Löslichkeitskoeffizient $\color{violet}0,0031$
:::

Somit stellt sich die Frage: *"Wenn der physkalisch gelöste Anteil verschwindend gering ist, wieso wird er gemessen?"*

:::{index} single: Sauerstoffbindungskurve
:::
:::{index} single: Bohr-Effekt
:::
:::{index} single: Effekt; Bohr-
:::

(Sauerstoffbindungskurve)=
(ARMO-KP-Sauerstoffbindungskurve)=

### Die Sauerstoffbindungskurve

Tatsächlich besteht ein Zusammenhang zwischen dem Sauerstoff-Partialdruck und der Sauerstoffsättigung (welche einen Faktor für die Menge des gebundenen Sauerstoffs darstellt):
Die **Sauerstoffbindungskurve**.
Sie verläuft S-förmig und flacht bei einem pO₂ von 90 mm Hg deutlich ab: Ab diesem Plateau bilden sich Veränderungen des pO₂ kaum mehr in der Sauerstoffsättigung (SO₂) ab.
Die Lage der Kurve ist nicht fixiert:
Diverse *Einflussfaktoren*, insbesonders der **pH**, haben Auswirkungen auf die Bindungsaffinität des Sauerstoffs an Hämoglobin. Es kommt zu einer **Rechts-** oder **Linksverschiebung**.
Dieses Phänomen wird als **Bohr-Effekt** bezeichnet.

Dadurch ergibt sich, dass bei einer *Alkalose* O₂ zwar *leichter ins Blut* aufgenommen, aber *im Gewebe schlechter* wieder gelöst, d. h. abgegeben, wird.
Umgekehrt ist die O₂-Aufnahme bei einer Azidose reduziert, das bereits aufgenommene O₂ wird aber bereitwillig an das Gewebe abgegeben.

:::{subfigure} AB
:subcaptions: below
:name: Fig-BS-Sauerstoffbindungskurve
:class-grid: outline
:gap: 10px

Sauerstoffbindungskurve [₢ [Michał Komorniczak](https://commons.wikimedia.org/wiki/User:M.Komorniczak) {term}`ℓ CC BY 3.0`]

![Die Sauerstoffbindungskurve. Bemerke: Die Kurve verläuft S-förmig und flacht bei einem pO₂ von 90 mm Hg deutlich ab: Ab diesem Plateau bilden sich Veränderungen des pO₂ kaum mehr in der Sauerstoffsättigung (SO₂) ab.](../../../../Submodules/3134-medical-picture-collection/CC-BY-SA-3.0/HbA_saturation_edited.*)

![Bohr-Effekt:Diverse Einflussfaktoren, insbesonders der pH, haben Auswirkungen auf die Bindungsaffinität des Sauerstoffs an Hämoglobin. Es kommt zu einer Rechts- oder Linksverschiebung.](../../../../Submodules/3134-medical-picture-collection/CC-BY-SA-3.0/Hb-saturation-Bohr-Effect_edited.*)

:::


:::{admonition} Dictum
Der Sauerstoffpartialdruck hat über die Beziehung der Sauerstoffbindungskurve eine große Aussagekraft hinsichtlich des Sauerstoffgehalts ${\rm{CaO}_2}$ des Blutes.
:::

(ARMO-KP-SB-Haushalt)=
% Bikarbonat bei erhöhtem etCO₂:
(Q-ARMO23004-2)=
% BGA und metabolische Azidose
(Q-ARMO23005)=

### CO₂ und der Säure-Basen-Haushalt

Weiters spielt das **pCO₂** eine wichtige Rolle:
Die H⁺-Konzentration wird durch das Gleichgewicht zwischen pCO₂ und HCO₃⁻ bestimmt.
Eine Änderung der H⁺-Konzentration, also des pH-Wertes, ist auf eine Änderung von pCO₂ oder der HCO₃⁻-Konzentration zurückzuführen, Stichwort **Bikarbonat-Puffer**:

$$
\rm  {\color{brown} Bikarbonat } + {\color{red} Säure } \rightleftarrows {\color{purple} CO₂ } + {\color{blue} Wasser }

\rm {\color{brown} HCO_3^- } + {\color{red} H^+ } \rightleftarrows {\color{gray} H_2CO_3 } \rightleftarrows {\color{purple} CO_2 } + {\color{blue} H_2O }
$$ (Bikarbonatpuffer)

Dies ist die konkrete Ableitung der Henderson-Hasselbalch’schen
Puffergleichung für den Bikarbonatpuffer.

Das CO₂ wird normalerweise über die Lunge abgeatmet.
Daraus folgt:

- **Hypoventilation**:
  Atmet der Patient nicht (genug), *staut* sich das CO₂ auf der rechten Seite der Gleichung und Säure wird auf der anderen Seite *nicht abgebaut*.
  Es entsteht eine *respiratorische Azidose*.
- **Hyperventilation**:
  Atmet der Patient zu viel ($V_\text{min}$ ↑: zu schnell und zu tief!), wird zu viel CO₂ abgeatmet und das Reaktionsgleichgewicht verschiebt sich.
  Es wird vermehrt H⁺ mit Bikarbonat zu CO₂ umgewandelt.
  Da nun Säure *fehlt*,
  kommt es zu einer **respiratorischen Alkalose**.
- Umgekehrt können **metabolische Prozesse** Einfluss auf die Atmung haben:
  Fällt zu viel Säure im Körper an (metabolisch bedingte Azidose),
  wird es zu CO₂ (und Wasser) umgewandelt und stimuliert dadurch den Atemantrieb.
  Das *CO₂ wird abgeatmet* und es kann zu einer *tiefen, schnellen Atmung* kommen (*Kussmaul'sche Atmung*).

:::{admonition} Dictum
CO₂, pH und Bikarbonat stehen in einer engen Verbindung.
Sowohl respiratorische, als auch metabolische Faktoren können diese beeinflussen.
:::

## Beurteilung

Wir haben gesehen, dass sowohl respiratorische, als auch metabolische Faktoren unsere BGA beieinflussen können.
Es ist nun wichtig die Ursache einer Störung zuordnen zu können.

% .. rubric:: Basendefizit geschätzt
%
% neg. BE . kg / 3

```{index} single: Säure-Basen-Haushalt
```
```{index} single: SB-Haushalt
```
```{index} single: Azidose
```
```{index} single: Alkalose
```
```{index} single: Blutgasanalyse
```

(bga-respiratorische-alkalose)=



```{index} single: Stufenanalyse (SB-Haushalt)
```

(Q-ARMO23001)=

### Analyse hinsichtlich SB-Haushalt

:::{todo} {issue}`135` BGA

SCHINNERL: So hab ich die BGA noch nie betrachtet…
Mir fehlen Begriffe wie
„metabolisch kompensierte resp. Azidose“
(Kann man dann in allen 4 Varianten spielen)
:::

Zuerst erfolgt die Identifizierung der primären SB-Störung, anschließend der sekundären Antworten um andere Einflüsse abzugrenzen und zwischen einer akuten und chronischen Störung zu unterscheiden.
Bedenke: Neben dem *schnellen* Bikarbonatpuffer hat auch die *Niere* einen großen, aber zeitverzögerten, Einfluss auf den Säure-Basen.Haushalt.

1. Eine SB-Störung liegt vor, wenn paCO₂ *oder* pH-Wert ausserhalb der Norm liegen

2. Weichen *sowohl* paCO₂ *als auch* pH ab, untersucht man die Richtung der Veränderung:

   1. **Richtungsgleiche** Veränderung von paCO₂ und pH: primär **metabolische** Störung (*"metabolisch miteinander"*)[^anionenluecke].
      Sekundäre Antworten:

      - Ist die paCO₂ höher als erwartet, liegt zudem eine sekundäre respiratorische Azidose vor;
      - Ist die paCO₂ niedriger aus als erwartet, besteht eine sekundäre respiratorische Alkalose.

   2. **Gegenläufige** Veränderung von paCO₂ und pH: primär **respiratorische** Störung

      Interessant sind nun die sekundären Antworten um eine akute von einer chronischen Störung zu unterscheiden und metabolische Einflüsse aufzuzeigen:
      - Eine *normale HCO₃⁻-Konzentration* gilt als Hinweis für eine **akute** Störung.
      - Bei **HCO₃⁻-Abweichung** soll die erwartete HCO₃⁻-Konzentration bestimmt werden.

        - Chronische respiratorische *Azidose*:
          - Ist das HCO₃⁻ niedriger als erwartet, ist die *renale Antwort unvollständig*,
          - ist es höher, liegt eine **sekundäre metabolische Alkalose** vor.

        - Chronische respiratorische *Alkalose*:
          - Ist das HCO₃⁻ **>** erwartet, dann ist *renale Antwort unvollständig*;
          - wenn **\<** erwartet, dann **sekundäre metabolische Azidose**.

3. Weicht *nur eine* der beiden Komponenten von der Norm ab, handelt es sich um eine **gemischt** *metabolisch-respiratorische* Störung.
   Ist dabei der pH im Normbereich, spricht man von einer durch den Konterpart **kompensierten** Störung.

   1. Weicht nur der paCO₂ ab, lassen sich die Art der respiratorischen Störung und die entgegengesetzte metabolische Störung anhand der Veränderung des paCO₂ identifizieren.
   2. Weicht nur der pH-Wert ab, lassen sich analog die metabolische Störung und die gegenläufige respiratorische Störung durch die Richtungsänderung des pH identifizieren (z. B. niedriger pH: metabolische Azidose).

:::{note}
*"Metabolisch miteinander"* (paCO₂ und pH)
:::

[^anionenluecke]: Der Vollständigkeit halber sei die Beurteilung einer metabolischen Azidose anhand der **Anionenlücke** erwähnt: Na⁺ - (Cl⁻ + HCO₃⁻). Zu einer erhöhten Anionenlücke kommt es durch einem vermehrten Anfall von Säuren, z. B. durch Ketoazidose, Urämie, Salicylsäure, Methanol, Aethylenglykol, Laktat.

(Q-ARMO23002)=

### Analyse hinsichtlich Oxygenation und Gasaustausch

Die Aussagekraft hinsichtlich der Respiration der BGA:

- Respiratorische Beeinflussung des Säure-Basen-Haushalts, s. o.
- Beeinflussung des Säure-Basen-Haushalts auf die Respiration, s. o.

- Unterscheidung zwischen:
  - **hypoxische** Insuffizienz:
    Die pO₂ is erniedrigt, die pCO₂ normal (oder erniedrigt; **Partialinsuffizienz**)
  - **hyperkapnische** Insuffizienz:
    pO₂ ist erniedrigt und pCO₂ erhöht(**Globalinsuffizienz**)

- Beurteilung des Gasaustausches (**Diffusionsstörung**) in Abhängigkeit von der inspiratorischen Sauerstoffkonzentration (FiO₂; Horovitz-Index).

  Eine Diffusionsstörung ist anzunehmen, wenn das Verhältnis zwischen der Luft-Gaskonzentration (FiO₂, aber auch etCO₂, vgl. {ref}`Kapnometrie <Kapnometrie>`) zu den korrespondierenden Blutgasen gestört ist.
  Beachte: Eine Diffusionsstörung kann auch sekundär durch eine Perfusions- oder Ventilationsstörung bedingt sein!

```{index} single: Horovitz-Quotient
```
```{index} single: Quotient; Horovitz
```
```{index} single: Index; Horovitz
```
(Horovitz-Quotient)=
(Q-ARMO23002-2)=

#### Horovitz-Quotient

:::{margin} Horowitz-Quotient
$$
\rm \frac{p_{a}O_2 [mm\,Hg]}{FiO_2}
$$

450—300 normal

\< 300 leichte, \< 200 mittelschwere, \< 100 schwere Lungenschädigung
:::

Der Horovitz-Quotient oder Horovitz-Index ist das Verhältnis von  paO₂ und der eingeatmeten Sauerstoffkonzentration (FiO₂).
Er zeigt eine primäre oder sekundäre Diffusionsstörung an und ist nützlich, um das Ausmaß einer Lungenschädigung zu beurteilen und den Sauerstoffbedarf zu quantifizieren.

$$
\rm Horovitz-Quotient = \frac{p_{a}O_2 [mm\,Hg]}{FiO_2}
$$ (HorivitzQuotient)

Z. B. Gesunder Patient mit paO₂ = 100 mm Hg bei Raumluft:

$$
{\rm Horovitz-Quotient} = \frac{100}{0,21} \approx 476
$$ (HorivitzQuotientBeispiel)

Bei Gesunden ist der Horovitz-Index altersabhängig und liegt zwischen 350 und 450. Ein Wert unter 300 gilt als Schwelle für eine leichte Lungenschädigung, unter 200 weist er auf eine mittelschwere, unter 100 auf eine schwere Lungenschädigung hin.

:::{todo} {issue}`136` BGA: Bild bearbeiten (FiO₂ rot markieren)
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/IMG_223832_001342px.jpg
:width: 100%

BGAs in Serie

Patient mit  COVID-19-Pneumonie und schwerer Oxygenationsstörung in Bauchlage (BL) und nach Zurückdrehen in Rückenlage (RL).
Der Horovitzkoeffizient ist zuletzt 45.

₢ GaSe  {term}`ℓ MfG`
:::


:::{raw} latex
\begin{minipage}{\linewidth+\marginparwidth+\marginparsep}
:::

:::{figure} ../../../Bilder/Metavision/MV_ICU-Intubation-bei-resp-Verschlechterung-Stundenuebersicht.png

Patient mit respiratorischer Verschlechterung
:::

:::{raw} latex
\end{minipage}
:::
