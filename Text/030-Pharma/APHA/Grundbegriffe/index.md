# Grundbegriffe

## Pharmakokinetik

Umfasst alles, was der Organismus mit dem Pharmakon macht.

Bioverfügbarkeit

: Anteil der in die systemische Zirkulation gelangt

  z. B. orale Bioverfügbarkeit = $\frac{\rm AUC_{\rm oral}}{\rm AUC_{\rm intravenös}}$

Verteilungsvolumen — Dosis/Plasmakonzentration

: beschreibt einen **virtuellen** Raum in dem sich das Arzneimittel verteilt

Plasmaclearence

: Plasmavolumen, welches pro Zeiteinheit durch Biotransformation oder Elimination befreit wird

Plasmahalbwertszeit

: Ist jene Zeit in der die Hälfte des Ausgangswertes erreicht ist, sie hängt von der *Clearence* und dem *Verteilungsvolumen* ab

  ${\rm Halbwertszeit}=\frac{\ln{2} \times {\rm Verteilungsvolumen}}{{\rm Clearence}}$

  Für die *Eliminiations-HWS* gilt, dass mehr als 4—5 HWZ abgewartet werden müssen, bis mehr als 93% einer Substanz ausgeschieden sind.

Initialdosis

: ${\rm Initialdosis}=\frac{{\rm Plasmavolumen} \times {\rm Verteilungsvolumen}}{{\rm Bioverfügbarkeit}}$

Erhaltungsdosis

: … ist abhängig von der Clearence:

  $\frac{{\rm Halbwertszeit}}{{\rm Zeit}}={\rm Plasmakonzentration} \times {\rm Clearence}$

Kompartmentmodell

<!--
:::{figure} ../Pictures/Kompartmentmodell.png
:width: 100%

`2DO-APHA-Graf-036` Kompartmentmodell
:::
-->

**Eigenschaften die Verteilung beeinflussen**

- Molekülgröße
- Ionisierungsgrad
- Lipidlöslichkeit
- Proteinbindung im Plasma
- Bindung an Gewebsproteine

## Pharmakodynamik

Umfasst alles, was ein Pharmakon mit dem Organismus macht

(APHA-VO-Rezeptoren)=

## Rezeptoren

Rezeptoren sind komplexe, große **(Protein-)Moleküle**, welche über Bindungsstellen eine **selektive** Anlagerung von Substanzen (**Liganden**, Agonisten) erlauben, welche über Wechselwirkungen eine **Signalübertragung** in die oder in der **Zelle** erlauben.
Die Bindung eines Liganden führt zu einer **Veränderung der räumlichen Anordnung** des Proteins (*Tertiär-* und *Quartärstruktur*) und damit zu einer **Veränderung des Funktionszustands** des Proteins.
Sie können sich sowohl in der Zellmembran als auch intrazellulär befinden.

:::{todo} Grafik: Rezeptor mit Ligand
:::



### Wirkungsprinzipien

| Wirkungsart  | Vorgang                    | Grundlage                    | Topografie                                  | Schwellendosis |
| ------------ | -------------------------- | ---------------------------- | ------------------------------------------- | -------------- |
| spezifisch   | Interaktion mit Rezeptoren | molekulare Passgenauigkeit   | abhängig von Rezeptorverteilung und -dichte | niedrig        |
| unspezifisch | Einlagerung in Membranen   | physikochemische Löslichkeit | ubiquitär im Organismus                     | hoch           |

### Art der Rezeptoren

Man unterscheidet:

- **Liganden**-gesteuerte Ionenkanäle
- **G-Protein** gesteuerte Rezeptoren

:::{todo} Grafik: Liganden-gesteuerter Ionenkanal

../Pictures/Liganden-gesteuerter-Ionenkanal.png
:width: 100%

:::



:::{todo} Grafik: G-Protein-gesteuerter Rezeptor

../Pictures/G-Protein-gesteuerter-Rezeptor.png
:width: 100%

:::



:::{list-table}
:header-rows: 1

- - Liganden-gesteuerter Ionenkanal
  - G-Protein-gesteuerte Rezeptoren
- - - Acetylcholin Rezeptor vom Nikotin-Typ
    - Serotoninrezeptor vom 5-HT3-Subtyp
    - GABAA-Rezeptor
    - Glutamatrezeptor vom NMDA und Non-NMDA-Typ
    - Glycinrezeptor
    Einfacher Weg der Signalübertragung, rascher Anpassung
    - Spannungsabhängige Ionenkanäle – Nervenleitung
  - - Acetylcholin Rezeptor vom Muskarin-Typ
    - Adrenerge und dopaminergen Rezeptoren (α,β, D1/D2)
    - Serotoninrezeptoren außer 5-HT3-Subtyp
    - Histamin-,Adenosin-,Angiotensin-, Brandykinin-,Vasopressin- und
    - Prostaglandinrezeptoren
    - GABAB-Rezeptor
    - Opioidrezeptoren (µ,κ,δ)
    - Cannabinoidrezeptoren (CB1/CB2)
:::

| Steuerung                       | Axonale Konduktion                 | Synaptische Transmission      | Humorale Transduktion              |
| ------------------------------- | ---------------------------------- | ----------------------------- | ---------------------------------- |
| Spannungsabhängige Ionenkanäle  | Sehr schnelle Effekttransformation | 0                             | 0                                  |
| Liganden gesteuerte Ionenkanäle | 0                                  | Schnelle Effekttransformation | Langsame Effekttransformation      |
| G-Protein gesteuerte Rezeptoren | 0                                  | Langsame Effekttransformation | Langsame Effekttransformation      |
| Intrazelluläre Rezeptoren       | 0                                  | 0                             | Sehr langsame Effekttransformation |

```{eval-rst}
+--------------+---------------------+-----------------------------------------------------+----------------------------------+
| Hauptgruppe  | Untergruppe         | Mechanismus                                         | Relative intrisische Aktivität a |
+==============+=====================+=====================================================+==================================+
| Agonisten    | rein                | Rezeptor-spezifische Aktivierung                    | 1                                |
|              +---------------------+                                                     +----------------------------------+
|              | partiell            |                                                     | 0>a>1                            |
+--------------+---------------------+-----------------------------------------------------+----------------------------------+
| Antagonisten | partiell kompetitiv | Rezeptor-spezifische Inaktivierung                  | 0>a>                             |
|              +---------------------+-----------------------------------------------------+----------------------------------+
|              | nicht kompetitiv    | Allosterisch, effektbezogeneIrreversible Inhibierun | 0                                |
|              +---------------------+-----------------------------------------------------+                                  |
|              | funktionell         | Unterschiedliche Wirkort                            |                                  |
|              +---------------------+-----------------------------------------------------+                                  |
|              | physiologisch       | Gegenregulation durch Homöostase                    |                                  |
|              +---------------------+-----------------------------------------------------+                                  |
|              | chemisch            | Chemische Inaktivierung                             |                                  |
+--------------+---------------------+-----------------------------------------------------+----------------------------------+
```

### Überträger im autonomen Nervensystem

:::{todo} Grafik: Überträger im autonomen Nervensystem

../Pictures/Uebertraeger-autonomes-Nervensystem.png
:width: 100%
:::



(Q-APHA23001)=
(Q-APHA23002)=

#### Adrenerges System

Regulation des Gefäßtonus, Innervation des peripheren sympathischen Nervensystems

- **Noradrenalin**: Bildung im peripheren sympathischen Nervensystem aus Thyrosin, L-Dopa, Dopamin und dient als *Neurotransmitter*
- **Adrenalin**: Bildung in den **chromaffinen Zellen** des **Nebennierenmarks** aus *Noradrenalin*, wird von dort als Hormon in den Blutkreislauf abgegeben

**Adrenerge Rezeptoren** sind G-Protein vermittelte Rezeptoren in der Membran vieler Zellen Klinische Relevanz besitzen **α1, α2, β1, β2**.
Weitere Subtypen weisen keine klinische Relevanz auf, da es keine spezifischen Pharmaka gibt.
Transmitter im sympathischen Nervensystem bilden Adrenalin und Noradrenalin.
Die Adrenalinbildung erfolgt im Nebennierenmark, Norarenalinbildung in den terminalen Endungen der sympathischen Nervenendigungen.

Alpha-1-Rezeptoren
: - Vasokonstriktion der Arteriolen der Haut, Nieren, Gastrointestinaltrakt und Venen

Alpha-2-Rezeptoren
: - Präsynaptisch lokalisiert, Stimulation hemmt Freisetzung von Noradrenalin
  - NO Freisetzung
  - Kontrakton glatter Gefäßmuskulatur

Beta-1-Rezeptoren
: - Steigerung der kardialen Kontraktilität (positiv inotrop), der Schlagfrequenz (positiv chronotrop), Steigerung der Erschlaffungsgeschwindigkeit (positiv lusitrop)
  - Überstimulation Apoptose und Nekrose von Herzmuskelzellen

Beta-2-Rezeptoren
: - Relaxierung der glatten Gefäßmuskulatur, Bronchien und Uterus, NO Freisetzung, geringe Konzentration auch im Herzen

:::{list-table} Affinität zu Rezeptoren
:header-rows: 1

- -
  - α1
  - α2
  - β1
  - β2
- - Noradrenalin

  - \+++

  - \+++

  - ++

  - (+)
- - Adrenalin

  - ++

  - ++

  - \+++

  - \+++
:::

Der Transmitter im **parasympathischen** Nervensystem ist **Acetylcholin**.



(Q-APHA23003-1)=

#### Kontraktion der Gefäßmuskulatur

Unter **Vasokonstriktion** versteht man die Kontraktion von Blutgefäßen und erfolgt durch die glatte Gefäßmuskulatur.
Das Gegenteil ist die **Vasodilatation**.
Substanzen, die eine Vasokonstriktion vermitteln, werden als Vasokonstriktoren oder **Vasopressoren** bezeichnet, Die Vasodilalation vermitteln **Vasodilatatoren**.


Die Vasokonstriktion wird vermittelt durch:

- viszeromotorische Fasern des vegetativen Nervensystems:
  **Sympathische Efferenzen** wirken neurogen vasokonstriktorisch, der vaskuläre *Basistonus* zwird zum *Ruhetonus* erhöht.
  Die Durchtrennung von sympathischen Fasern führt in der Peripherie zu einer Vasodilatation.
- verschiedene Botenstoffe wie
  - **Adrenalin**,
  - **Noradrenlin**,
  - **Vasopressin**,
  - **Angiotensin II** und
  - Endothelin, sowie durch
  - **synthetisch** hergestellte Stoffe

Der Mechanismus, der zur Vasokonstriktion führt, resultiert aus der erhöhten Konzentration von Kalzium in den glatten Gefäßmuskelzellen, die spezifischen Mechanismen hängen jedoch vom jeweiligen Vasokonstriktor ab.

Eine wesentliche Rolle spielen die **α₁-Adrenorezeptoren**, vgl. Tab. {ref}`Tab-Autonomes-Nervensystem-Rezeptoren`.
Über diesen erfolgt die vasopressorische Wirkung der Katecholamine Adrenalin und Noradrenalin.

:::{note}
Die höchste vasopressorische Wirkung wird über den α₁-Adrenorezeptore erzielt.

Zu den Stoffen mit der höchsten vasopressorischen Wirkung gehören Noradrenalin, Vasopressin und Adrenalin.
:::

<!--
:::{figure} ../Pictures/Kontraktion-Gefaessmuskulatur.png
:width: 100%

`2DO-APHA-Graf-029` Kontraktion der Gefäßmuskulatur
:::
-->

#### Signalwege der kardialen Kontraktion

Auch in der Steuerung der kardialen Kontraktion spielen Adrenorezeptoren eine wichtige Rolle, hier sind jedoch vor allem die **β₁-Rezeptoren** als Gegenspieler des muskarinergen M2-Rezeptors vorherrschend, vgl. Tab. {ref}`Tab-Autonomes-Nervensystem-Rezeptoren`.

<!--
:::{figure} ../Pictures/Signalwege-kardiale-Kontraktion.png
:width: 100%

`2DO-APHA-Graf-030` Signalwege der kardialen Kontraktion
:::
 -->

## Wirkungen Autonomes Nervensystem

```{eval-rst}
.. table:: Rezeptoren im Autonomen Nervensystem
    :name: Tab-Autonomes-Nervensystem-Rezeptoren

    +------------------+-----------------------+--------------+-----------------------+--------------+
    |                  |   Parasympathikus     |   Rezeptor   |   Sympathikus         |   Rezeptor   |
    +==================+=======================+==============+=======================+==============+
    | Sinusknoten      | Negativ Chronotop     | M2           | Positiv Chronotrop    | β1           |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | AV Knoten        | Negativ Chronotop     | M2           | Positiv Chronotrop    | β1           |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | Blutgefäße       | Dilatation            |              | Konstriktion          | α1, α2       |
    |                  |                       |              +-----------------------+--------------+
    |                  |                       |              | Dilatation            | β2           |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | Bronchien        | Konstriktion          | M3           | Dilatation            | β2           |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | Bronchialdrüsen  | Sekretions-steigerung | M3           | Sekretionshemmung     | α1           |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | Speicheldrüsen   | Viel dünner Speichel  | M3           | Wenig dicker Speichel | α1           |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | Magen-Darm-Trakt | Motilitätssteigerung  | M3           | Motilitätshemmung     | β2, α1       |
    +------------------+-----------------------+--------------+-----------------------+--------------+
    | Stoffwechsel     | Anabol                |              | Katabol               |              |
    +------------------+-----------------------+--------------+-----------------------+--------------+
```

## Parasympatholytika

**Parasympatholytika** sind Substanzen, die die Erregungsübertragung durch kompetetiven Antagonismus zu Acetylcholin an muskarinartigen Rezeptoren des parasympathischen Nervensystems unterbrechen.

- **Tertiäre Amine**
- **Quartäre Amine**: keine Passage der Blut-Hirn-Schranke

Klinische Wirkung
: - **Peripher**: Herzfrequenzsteigerung, Bronchodilatation, Antisalvation, Spasmolyse im Gastrointestinal und Urogenitaltrakt
  - **Zentral**: Bewusstseins und psychische Veränderungen

Indikationen
: - Akute bradykarde Rhythmusstörung
  - Verhinderung reflektorischer Bradykardien
  - Verhinderung von Nebenwirkung (Bradykardien) bei Verwendung von Cholinesterasehmmern zur Antagonisierung der Muskelrelaxierung
  - Antisalvation

:::{list-table}
:header-rows: 1
:stub-columns: 1

- -
  - Atropin
  - Glycopyrulat
  - Ipratropium
  - Scopalamin
- - Handelsname
  -
  - Robinul
  - Itrop
  -
- - Struktur
  - Tertiäres Amin
  - Quartäres Amin
  - Quartäres Amin
  - Tertiäres Amin
- - ZNS
  - Geringe Stimulation
  - keine
  - keine
  - Sedierung, Amnesie
:::

## Vasopressoren

- Steigerung des Blutdrucks über direkte Erhöhung des peripheren Gefäßwiderstandes: Direkte α1-Wirkung
- Direkte oder indirekte Sympathomimetika — entweder direkte Wirkung auf adrenerge Rezeptoren oder durch Erhöhung der Noradreanalin Konzentration.

|                       | Etilefrin         | Ephedrin          | Phenylephrin |
| --------------------- | ----------------- | ----------------- | ------------ |
| Arterieller Blutdruck | ↑↑                | ↑↑                | ↑↑↑          |
| Herzfrequenz          | ↑↑                | ↑                 | 0            |
| Wirkmechanismus       | Direkt > Indirekt | Indirekt > Direkt | Direkt       |
| Rezeptoren            | α, β              | α, β              | α            |
