

:::{raw} latex
\clearpage
:::


# Exkurs: Dosierung

## Konzentrationen

Prüfungsrelevanz
: ☑ **Praktikum** | ☑ **Schriftliche Prüfung** | ☑ **PJ-Reife / OSCE** 

Es ist sinnvoll die Konzentration eines flüssigen Arzneimittels in mg / ml umzurechnen.
Bei Konzentrationsangaben in Prozent zeigt sich, dass Mediziner mit Naturwissenschaften eigentlich nicht soviel am Hut haben; man postuliert einfach, dass ein Liter einem Kilogramm entspricht[^SI-Kilogramm-Liter].


[^SI-Kilogramm-Liter]: Beachte: Die "umgangssprachlichen" SI-Grundeinheiten für Masse und Volumen unterscheiden sich in der Größenordnung von 10³ (*Kilo*gramm, aber Liter)

:::{table} Typische Konzentrationen

|                | Konz. per ml         |
| -------------- | --------------------------: |
| 1%             | 10 mg / ml                  |
| 1 mg / 50 ml   | 0,020 mg / ml =  20 µg / ml |
| 5 mg / 50 ml   | 0,100 mg / ml = 100 µg / ml |
| 10 mg / 50 ml  | 0,200 mg / ml = 200 µg / ml |
:::

Viele Arzneimittel werden unter dem gleichen Markennamen, aber mit deutlich unterschiedlicher Konzentration vertrieben, {numref}`Tab-Gleicher-Wirkstoff-unterschiedliche-Konzentrationen` zeigt einige bekannte Beispiele.

:::{table} Fallen: Gleicher Wirkstoff, unterschiedliche Konzentrationen
:name: Tab-Gleicher-Wirkstoff-unterschiedliche-Konzentrationen

| Produkt   | Wirkstoff | Präparation    | Konz. per ml |
| --------- | --------: | -------------- | ------------ |
| Propofol  | Propofol  | 1%             | 10 mg / ml   |
| Propofol  | Propofol  | 2%             | 20 mg / ml   |
| Dormicum™ | Midazolam | 5 mg / 1 ml    | 5 mg / ml    |
| Dormicum™ | Midazolam | 5 mg / 5 ml    | 1 mg / ml    |
| Dormicum™ | Midazolam | 15 mg / 3 ml   | 5 mg / ml    |
| Ketanest™ | S-Ketamin | 25 mg / 5 ml   | 5 mg / ml    |
| Ketanest™ | S-Ketamin | 250 mg / 10 ml | 25 mg / ml   |
:::

## Dosisrate

:::{sidebar} Dosisrate

- µg / kg / min: *\"Gamma\"*
:::

Dosierungen für die Langzeitgabe von hochpotenten Medikamenten wie Opioide oder Katecholamine werden zwecks Vergleichbarkeit in **µg / kg / min** angegeben, umgangssprachlich wird dies oft als *"Gamma"* bezeichnet.



## Flussrate

:::{sidebar} Flussrate

- Flussrate [ml / h]:

  $$\frac{\text{Dosisrate [µg / kg / min]}\times\text{Gewicht [kg]}\times 60}{\text{Konz. [µg / ml]}}$$
:::

Abhängig von der Zubereitung und Konzentration der Infusionslösung und des Patientengewichts kann man eine **Flussrate** errechnen, die man z. B. auf Spritzenpumpen einstellen kann (bzw. muss):

:::{math}
\text{Flußrate [ml / h]} = \frac{\text{Dosisrate [µg / kg / min]}\times\text{Gewicht [kg]}\times 60}{\text{Konzentration [µg / ml]}}
:::

| Wirkstoff    | Dosisrate                  | Bsp. Zubereitung | Konzentration | Flußrate  (70 kg) |
| ------------ | --------------------------: | ----------------: | -------------: | -----------------: |
| Remifentanil | initial 0,1µ / kg / min    | 5 mg / 50 ml     | 100 µg / ml   | 4,2 ml / h         |
| Morphium     | 2 µg / kg / min            | 100 mg / 50 ml   | 2 mg / ml     | 4,2 ml / h         |
| Sufentanil   | initial 0,04 µg / kg / min | 2500 µg / 50 ml  | 50 µg / ml    | 3,36 ml / h         |



:::{caution}

Die tatsächlich erforderliche Dosierung ist sehr individuell und von der Schmerzintensität sowie der gewünschten Sedierungstiefe abhängig!
:::
