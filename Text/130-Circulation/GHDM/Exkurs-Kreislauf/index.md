
:::{index} single: Kreislauf
:::
:::{index} single: Hämodynamik
:::
:::{index} single: Oxygenierung
:::
(GHDM-VO-Kreislauf-O2-Transport)=

# Exkurs: Kreislauf und Hämodynamik

:::{rubric} Oxygenation ist das Ziel der Hämodynamik
:::

Der Zweck des Kreislaufs ist die zelluläre Oxygenierung.
Für eine optimale Sauerstoffversorgung auf zellulärer Ebene müssen die Makro- und Mikrozirkulation sowie der pulmonale Gasaustausch sowie das Gewebemilieu ausgeglichen sein.
Der Kreislauf übernimmt mit dem Blut als Transportmedium den Transport von Sauerstoff von den Lungenkapillaren in das Gewebe der Endorgane.

:::{figure} ../Bilder/LungeZuZelle.png
:alt: Bild
:width: 100%

Von der Lunge zur Zelle: Der Kreislauf ist die *"Sauerstoffspedition"*
:::



:::{index} single: Sauerstoffangebot
:::
:::{index} single: DO₂
:::

## Das Sauerstoffangebot DO₂

Das Sauerstoffangebot **DO₂** an den Körper wird dabei bestimmt durch den Cardiac Output $\color{red}\rm{CO}$ und den Sauerstoffgehalt des oxygenierten Blutes $\color{blue}\rm{CaO}_2$:

$$
\rm{DO}_2 = {\color{red}\rm{CO}} \times {\color{blue}\rm{CaO}_2}
$$

Blickt man nun etwas genauer ...

$$
\rm{DO}_2  \approx {\color{red}\rm{CO}} \times {\color{blue}\rm{Hb} \times 1,34 \times \rm{SaO}_2}
$$

... und noch genauer[^physgelo2] ...

$$
\rm{DO}_2  \approx {\color{red}{\rm{SV}} \times f} \times {\color{blue}\rm{Hb} \times 1,34 \times \rm{SaO}_2}
$$

… so sieht man, dass das Sauerstoffangebot von folgenden Faktoren abhängig ist:

- **Cardiac Output**

  - $\color{red}\rm{SV}$: Stroke Volume (Schlagvolumen)
  - $\color{red}f$: (mechanische) Herzfrequenz

- **Sauerstoffgehalt**

  - $\color{blue}\rm{Hb}$: Sauerstoffträger (Hämoglobin)
  - $\color{blue}\rm{SaO}_2$: Sättigung des Sauerstoffträgers
  - $\color{blue}1,34$: Hüfner'sche Zahl.
    Sie gibt an, wieviel Milliliter Sauerstoff als Absolutwert pro Gramm Hämoglobin gebunden und transportiert werden kann[^huefnerschezahl].

[^physgelo2]: Aufmerksamen Lesern wird aufgefallen sein, dass ${\color{blue}\rm{Hb} \times 1,34 \times \rm{SaO}_2}$ nur den über Hämoglobin gebundenen, aber nicht den physikalisch gelösten Sauerstoff berücksichtigt. Letzterer macht einen verschwinden geringen Anteil am Sauerstoffgehalt (CaO₂, \< 2%) aus und wird daher in der Praxis vernachlässigt.

    Wer es genau wissen will (paO₂ in mm Hg, Löslichkeitskoeffizient 0,0031):

    $$
    {\color{blue}\rm{CaO}_2} = ({\color{teal}\rm{Hb} \times 1,34 \times \rm{SaO}_2} + {\color{violet}\rm{paO}_2 \times 0,0031})
    $$

    Somit ergibt sich:

    $$
    \rm{DO}_2 = {\color{red}\rm{CO}} \times {\color{blue}\rm{CaO}_2} = {\color{red}\rm{CO}} \times ({\color{teal}\rm{Hb} \times 1,34 \times \rm{SaO}_2}+ {\color{violet}\rm{paO}_2 \times 0,0031})
    $$

[^huefnerschezahl]: Der rechnerisch maximale Wert der Hüfner'schen Zahl beträgt 1,39 ml O₂ / g Hb.
    Dieser in-vitro-Wert wird in vivo jedoch nicht erreicht, u. a. weil Hämoglobin physiologisch in geringen Mengen auch als Methämoglobin oder CO-Hämoglobin vorliegt.
    Gase, welche mit Sauerstoff in Konkurrenz um die Bindekapazität stehen, reduzieren die Sauerstoffbindekapazität.
    Ein extremes Beispiel dafür ist Kohlenmonoxid.

% .. figure::  ../Bilder/LungeZumMitochondrium.png
%     :alt: Bild
%     :width: 100%
%
%     Oxygen Absorption: Lungs →
%     Oxygen Transportation: Blood →
%     Oxygen Delivery: Tissues  →
%     Oxygen Utilisation: Cells / Microchondria

% .. figure::  ../Bilder/LungeZurZelle-DO2.png
%     :alt: Bild
%     :width: 100%
%
%     LungeZurZelle

% .. figure::  ../Bilder/DO2Vo2.png
%     :alt: Bild
%     :width: 100%
%
%     DO2Vo2



:::{index} single: 
:::
:::{index} single: 
:::

(GHDM-VO-Cardiac-Output)=

## Cardiac Output



:::{index} single: Herzauswurf
:::
:::{index} single: Volumen
:::
:::{index} single: Inotropie
:::
:::{index} single: Kontraktilität
:::
:::{index} single: Frank-Starling-Mechanismus
:::
:::{index} single: Mechanismus; Frank-Starling-
:::
:::{index} single: Nachlast
:::
:::{index} single: Widerstand; systemisch-vaskulären 
:::
:::{index} single: SVR
:::
:::{index} single: Dyn
:::
:::{index} single: Druck; ≠ Fluss
:::
### Was Sie schon immer über den Herzauswurf wissen wollten …



#### Ohne *Volumen* keine Füllung und kein Auswurf

Das Vorhandensein eines ausreichenden Volumens um die Gefäße zu füllen ist die Grundvoraussetzung um dieses Volumen zirkulieren zu lassen.

Voraussetzung für einen Herzauswurf ist freilich auch die vorherige Füllung des Herzens.
Abgesehen von dieser banalen Feststellung hat aber auch das *Ausmaß* der Füllung großen Einfluss auf die …



#### *Inotropie* pumpt

Die Inotropie ist die Kontraktionsfähigkeit der Herzmuskulatur, die **myokardiale Kontraktilität**.
Neben der Funktionalität des Myokards im engeren Sinne wird sie auch wesentlich von der **Füllung** über den *Frank-Starling-Mechanismus* und damit über die Vorlast (Preload) beeinflusst.



#### Gefäße sind flexibel

Dabei muss beachtet werden, dass das erforderliche Volumen, anders als z. B. in einem Heizungskreislauf mit starren Rohren, keine Fixgröße ist, sondern durch die Elastizität und **Kontraktilität** der Gefäßmuskulatur (“Enger- und Weiterstellen”) maßgeblich beeinflusst wird.
Durch Ihre Kontraktilität können sie einen Druck aufbauen, welcher auf das Herz wie ein Widerstand, gegen welches es pumpen muss, wirkt: Die **Nachlast** (*Afterload*).
Diese Nachlast steht in Verbindung mit dem durch die Gefäße aufgebauten **systemisch-vaskulären Widerstand** (*systemic vascular resistance*, *SVR*).
Die SVR wird in dynes s / cm⁵ angegeben.
Dyn ist eine alte Einheit für Kraft, 1 dyn entspricht 0,00001 Newton.



#### *Druck* ≠ Fluss — Aber ohne Druck fließt nichts

Doch Druck ist nicht unbedingt etwas Schlechtes:
Die treibende Kraft für einen Fluss ist ein *Druckunterschied* (*Gradient*).
Der Druck an sich garantiert jedoch noch keinen Fluss, so kann die Passage z. B. durch Vasokonstriktion, Embolie o. ä. versperrt und die kapilläre Perfusion beeinträchtigt sein.



:::{index} single: Preload
:::
:::{index} single: Inotropie
:::
:::{index} single: Afterload
:::
:::{index} single: Vorlast
:::
:::{index} single: Kontraktilität
:::
:::{index} single: Nachlast
:::

### Das Triumvirat des Schlagvolumens: *Preload*, *Inotropie*, *Afterload*

Aus dem vorangegangen Gesagten ergeben sich nun drei wesentliche Faktoren, welche das Schlagvolumen bestimmen:

- Vorlast (**Preload**) als Ausdruck der Füllung vor der Systole und mit dem *Frank-Starling-Mechanismus* im Hintergrund
- Kontraktilität (**Inotropie**)
- Nachlast (**Afterload**)



:::{index} single: Frequenz
:::

### Frequenz

Da das Herz im Kreislauf die Funktion einer Pulsationspumpe inne hat, ist die Frequenz ein entscheidender Faktor der den Auswurf im Zeitverlauf bestimmt.
Vorteilhaft ist hierbei, dass eine Frequenzänderung sehr rasch einsetzen und das Herzzeitvolumen (HZV) an die aktuellen Erfordernisse anpassen kann.
Dies ist jedoch nur in gewissen Grenzen möglich, da das Herz auch ausreichend Zeit benötigt um ausreichend vor einem Schlag gefüllt zu sein.
Bei einer Herzfrequenzerhöhung verkürzt sich vor allem die Diastole und damit die Füllzeit.

:::{attention}
Somit ist die Herzfrequenz einerseits ein **eigenständiger Faktor** für das Herzzeitvolumen, nimmt aber auch durch den Einfluss auf die Füllung Einfluss auf das Schlagvolumen.
:::



:::{index} single: Indizes
:::
:::{index} single: cardiac output
:::
:::{index} single: CO
:::
:::{index} single: cardiac index
:::
:::{index} single: index; cardiac
:::
:::{index} single: CI
:::
:::{index} single: stroke volume
:::
:::{index} single: SV
:::
:::{index} single: stroke volume index
:::
:::{index} single: index; stroke volume
:::
:::{index} single: SVI
:::
:::{index} single: SVR
:::
:::{index} single: index; systemic vascular resistance
:::
:::{index} single: SVRI
:::
:::{index} single: Körperoberfläche
:::
(cardiac-index)=

## Indizes erlauben die Vergleichbarkeit

Absolutwerte von Messwerten wie z. B. dem Cardiac Output sind individuell und zwischen verschiedenen Patienten nicht sinnvoll vergleichbar.
Deswegen werden viele Messwerte gegen Maße die die Physiognomie einer Person widerspiegeln normalisiert und Indizes  gebildet.
Häufig wird als Bezugswert die Körperoberfläche herangezogen, z. B.:

:::{list-table}
:header-rows: 1

- - Absolutwert
  -
  - Einheit
  - Indizierter Wert
  -
  - Einheit
- - Cardiac Output
  - CO
  - L/min
  - Cardiac *Index*
  - CI
  - L/min/m² KÖF
- - Stroke Volume
  - SV
  - ml / b (b steht für "beat")
  - Stroke Volume *Index*
  - SVI
  - ml / b / m² KÖF
- - system. vask. Widerstand
  - SVR
  - dyne · s / cm⁵
  - system. vask. Widerstands-*Index*
  - SVRI
  - dyne · s / cm⁵ / m²
:::
