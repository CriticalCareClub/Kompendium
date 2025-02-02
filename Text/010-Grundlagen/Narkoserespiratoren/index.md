# Narkoserespiratoren und -systeme



## Grundlagen

Relevante Norm: EN 740

### Arten von Systemen

#### Offene Systeme

#### Halbgeschlossene Kreissysteme

```{eval-rst}
.. todo:: Grafik Schema Kreissystem

```

```{index} single: NIST-Anschluß single: DIN; Gasanschluß
```

### Gasversorgung

Wandversorgung

: Codierte Steckerkupplungen an der Versorgungsseite,
  Rückschlagventil, Farbcodierung

Flaschenversorgung

: Druckminderer, Drucküberwachung mit Manometer

Anschlußschlauch

: Farbcodiert

Geräteseitig
: - NIST-Anschluß:
    Dichtigkeit ist *ohne Kraftanstrengung* gewährleistet
  - DIN-Anschluß:
    Dichtigkeit ist nur *mit* Kraftanstrengung gewährleistet

```{eval-rst}
.. todo:: FOTO NIST-Anschluß
```

```{eval-rst}
.. todo:: FOTO DIN-Anschluß
```

:::{list-table} Farbcodes Gasversorgung
:header-rows: 1

- - Gas
  - Alte Kennfarbe
  - Neue Kennfarbe
- - Sauerstoff
  - Blau
  - Weiß
- - Lachgas
  - Gelb
  - Blau
- - Med. Luft
  - Grau
  - Schwarz/weiß
- - Vakuum
  - Weiß
  - Gelb
:::

#### Features

```{index} single: Sauerstoffmangelsignal
```

##### Sauerstoffmangelsignal

Akustisches Mangelsignal gem. EN 470 bei Unterschreitung eines
vom Hersteller angegebenen Mindestdrucks (i. d. R. 2,2 bar).
Es mussm indestens 7 Sekunden dauern und mind. 2 dB über weißem
Rauschen von 50 db liegen.
Das Signal muss *aus dem Sauerstoffversorgungsdruck*
abgeleitet werden.

```{index} single: Lachgassperre
```

##### Lachgassperre

Bei Ausfall von Suaerstoff muss die Zufuhr von Lachgas
automatisch unterbunden werden.

```{index} single: Sintermetallfilter
```

##### Gasdosierung: Pneumatisch mit Flowmeter

*Sintermetallfilter* (max. 0,1 mm) reduzieren den Gasdruck vom
Versorgungsdruck (ca. 5 bar) auf. ca 1,5 bar vor den Regelventilen.
Rotarmeter müssen im Betrieb rotieren, nur dann stimmt die Skalierung
mit dem Durchfluß überein.

```{index} single: ORC single: Oxygen Ratio Controller
```

##### Gasdosierung: Elektronisch

- Der Gesamtfrsichgasdruchfluß kann zwischen 0,2—18 L / min betragen.

- ORC-Funktion (Oxygen Ratio Controller) in Gasmischungen mit Lachgas

  - Pneumatisch: Der Fließdruck nach dem O₂-Regelventil regelt den Lachgasfluß derart,
    dass mindestens 25% O₂-Konzentration im Frischgas ins Kreissystem
    gelangen (Proportionalventil)
  - Elektronisch:
    Einfach Einstellung des Firschgasflows bei BEibehaltung der
    voreingestellten O₂-Konzentration von 25% bis zu einem
    Frischgasflow von 1 L / min.
    Wird der Frisschgasflow weiter reduziert ist ein Mindestfluß von
    250 mL / min O₂ garantiert.
    Ab 250 mL / min beträgt die O₂-Konzentration 100%
    Der minimale Frischgasflow beträgt 200 mL / min.

- Manuelle O₂-Notdosieurng, vorbereitet für inspiratorische
  O₂-Regelung, automatische Flowsteuerung

- Externer Frischgasausgang mit Druckmessung

Vor dem Frischgasventil befindet sich sich ein Mischgasreservoir mit 0,5 L.
Davor und nach dem Frischgasventil findet eine Flow- und Druckmessung statt.

```{eval-rst}
.. todo:: Sketch-4, Sketch-5
```

```{index} single: Frsichagsentkoppelung
```

##### Frischgasentkoppelung

```{eval-rst}
.. todo:: Bilder Frischgasentkoppelung
```

Während der Inspiration wird Frischgas in das Reservoir geleitet,
während der Exspiration wird es in das System eingeleitet.

Exspiratorisch:
Über die Gaseinlassventile werden die Gase AIRS/O₂ bzw. N2O/O₂ in den
Mischtank geleitet.
Die Ventile werden zeitgesteuert nacheinander geöffnet und geschlossen.
Flow und Druck der einströmenden Gase werden überwacht,
sodass der Mischer unabhängig von Versorgungsdrücken ist.
Der Gesamt-Frischgasflow wird mit Hilfe eines *Proportionalventils*
(Flowdosierventil)
gesteuert und **nur in der Exspirationsphase** in das Kreisystem geleitet.

#### Inhalationsanästhetika

##### Verdunster

Geeignet für: Halothane, Enflurane, Isuflurane, Sevoflurane;
*nicht* für Desflurane.

Die  Konzentrationseinstellung erfolgt durch Varaition
des Querschnitts in der Verdunstungsleitung.

$$
\mathsf{Sättigungskonzentration} = \frac{\mathsf{Dampfdruck}}{\mathsf{Luftdruck}}
$$

:::{list-table} Sättigungskonzentrationen bei 20°C
- - Halothane
  - 32%
- - Enflurane
  - 23%
- - Isoflurane
  - 30%
- - Sevoflurane
  - 21%
- - Desflurane
  - **87%**
:::

```{index} single: Desflurane; Verdampfer
```

##### Desflurane-Verdampfer

100% Desflurane-Dampf wird dem Frischgas zudosiert.

```{index} single: DIVA™ single: Direct Injection of Volatile Anaesthetics
```

##### DIVA™: Direct Injection of Volatile Anaesthetics

- Kontrolle der expiratorischen Anästhesiemittel-Konzentration
- Minimaler Verbrauch
- Schnelles Ein- und Auswachen
- Verbrauchskalkulation
- Anzeige des Füllstandes
- Befüllung während Betrieb möglich

```{index} single: Atemkalk single: Absorberkalk single: Absorber single: Calciumhydroxid single: Ca(OH)₂ single: Natriumhydroxid single: NaOH single: Kaliumhydroxid single: KOH single: Bariumhydroxid single: Ba(OH)₂
```

### Atemkalk

Atemkalk dient in Kreislaufsystemen zur Elimination von CO₂ durch
Bindung des in der Ausatemluft enthaltenem Kohlenstoffdioxid.
In der
Medizin und beim Tauchen wird eine Mischung aus **Calciumhydroxid**
Ca(OH)₂ und **Natriumhydroxid** NaOH verwendet, früher auch
*Kaliumhydroxid* KOH und *Bariumhydroxid* Ba(OH)₂.
Atemkalk zur
chemischen Bindung von Kohlenstoffdioxid wurde 1924 von Ralf Waters
eingeführt. 100 g Natriumhydroxid können bis zu 23 Liter
Kohlenstoffdioxid binden. Durchschnittliche Absorber können 10—15
Liter pro 100 g absorbieren.
Dem Atemkalk ist ein pH-Indikator
beigemischt, der bei niedrigem pH-Wert seine Farbe von weiß nach
violett ändert und damit (unzuverlässig) anzeigt, dass der Absorber
verbraucht ist.

> CO₂ + H₂O ⇌ H₂CO₃
>
> H₂CO₃ + 2 NaOH ⇌ Na₂CO₃ + 2 H₂O
>
> Na₂CO₃ + Ca(OH)₂ ⇌ CaC=3 + 2 NaOH

## Datex Ohmeda und GE

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_115001-01341px.\*
GE Monitormodule
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150324_124348-01341px.\*
Nachfüllen eines GE-Sevofluran-Vapors.
:::

### Aespire

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20140402_161636-01341px.jpg
Frontansicht
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20140402_161645-01341px.jpg
Mittig die Druckanzeigen für die VErsorgungsdrücke. Links oben die Ventile zur Regulation der Frischgase.
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20140402_161717-01341px.jpg
Externe Monitoreinheit (oben) und Beatmungseinheit (unten)
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20140402_161729-01341px.jpg
Externe Beatmungseinheit Typ 7100.
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20140403_080248-01341px.jpg
Die xterne Beatmungseinheit Typ 7100 ermöglicht die volumskontrollierte Beatmung
:::

### Datex Ohmeda AS/5

Datex Ohmeda AS/5 Narkosemaschine

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_114945-01341px.jpg
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_115142-00640px.jpg
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_115016-00640px.jpg
:::

bestückt

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_115024-00640px.jpg
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150212_091242-00640px.jpg
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_115125-00640px.jpg
:::

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150217_115119-00640px.jpg
:::

### Aisys

:::{figure} /Bilder/Gabriel-Sebastian-CCCA/N-5/IMG_20150213_114233-01341px.jpg
:::

## Dräger

### Primus
