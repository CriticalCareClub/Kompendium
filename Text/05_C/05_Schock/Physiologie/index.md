---
status: final
---



:::{raw} latex
\clearpage
:::


(GSCH-SE-Schock-Physiologie)=

# Physiologie des Kreislaufs und der Hämodynamik

Um die Pathophysiologie des Schocks zu verstehen, muss man die Physiologie der Hämodynamik kennen.

:::{rubric} Oxygenation ist das Ziel der Hämodynamik
:::

Der Zweck des Kreislaufs ist die zelluläre Oxygenierung.
Für eine optimale Sauerstoffversorgung auf zellulärer Ebene müssen die Makro- und Mikrozirkulation sowie der pulmonale Gasaustausch sowie das Gewebemilieu ausgeglichen sein.
Der Kreislauf übernimmt mit dem Blut als Transportmedium den Transport von Sauerstoff von den Lungenkapillaren in das Gewebe der Endorgane.

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



### Cardiac Output

#### Ohne *Volumen* keine Füllung und kein Auswurf

Das Vorhandensein eines ausreichenden Volumens um die Gefäße zu füllen ist die Grundvoraussetzung um dieses Volumen zirkulieren zu lassen.

Voraussetzung für einen Herzauswurf ist freilich auch die vorherige Füllung des Herzens.
Abgesehen von dieser banalen Feststellung hat aber auch das *Ausmaß* der Füllung großen Einfluss auf die …



####  *Inotropie* pumpt

Die Inotropie ist die Kontraktionsfähigkeit der Herzmuskulatur, die **myokardiale Kontraktilität**.
Neben der Funktionalität des Myokards im engeren Sinne wird sie auch wesentlich von der **Füllung** über den *Frank-Starling-Mechanismus* und damit über die Vorlast (Preload) beeinflusst.



#### Gefäße sind flexibel

Dabei muss beachtet werden, dass das erforderliche Volumen, anders als z. B. in einem Heizungskreislauf mit starren Rohren, keine Fixgröße ist, sondern durch die Elastizität und **Kontraktilität** der Gefäßmuskulatur (“Enger- und Weiterstellen”) maßgeblich beeinflusst wird.
Durch Ihre Kontraktilität können sie einen Druck aufbauen, welcher auf das Herz wie ein Widerstand, gegen welches es pumpen muss, wirkt: Die **Nachlast** (*Afterload*).
Diese Nachlast steht in Verbindung mit dem durch die Gefäße aufgebauten **systemisch-vaskulären Widerstand** (*systemic vascular resistance*, *SVR*).

% Die SVR wird in dynes s / cm⁵ angegeben. Dyn ist eine alte Einheit für Kraft, 1 dyn entspricht 0,00001 Newton.



####  *Druck* ≠ Fluss — Aber ohne Druck fließt nichts

Doch Druck ist nicht unbedingt etwas Schlechtes:
Die treibende Kraft für einen Fluss ist ein *Druckunterschied* (Gradient).
Der Druck an sich garantiert jedoch an sich noch keinen Fluss, so kann die Passage z. B. durch Vasokonstriktion, Embolie o. ä. versperrt und die kapilläre Perfusion beeinträchtigt sein.



### Das Triumvirat des Schlagvolumens: *Preload*, *Inotropie*, *Afterload*

Aus dem vorangegangen Gesagten ergeben sich nun drei wesentliche Faktoren, welche das Schlagvolumen bestimmen:

- Vorlast (**Preload**) als Ausdruck der Füllung vor der Systole und mit dem *Frank-Starling-Mechanismus* im Hintergrund
- Kontraktilität (**Inotropie**)
- Nachlast (**Afterload**)

### Frequenz

Da das Herz im Kreislauf die Funktion einer *Pulsationspumpe* inne hat, ist die *Frequenz* ein entscheidender Faktor, der den Auswurf im Zeitverlauf bestimmt.
Vorteilhaft ist hierbei, dass eine Frequenzänderung sehr *rasch* einsetzen und das Herzzeitvolumen (HZV, CO) an die aktuellen Erfordernisse anpassen kann.
Dies ist jedoch nur in gewissen Grenzen möglich, da das Herz auch ausreichend Zeit benötigt um ausreichend vor einem Schlag gefüllt zu sein.
Bei einer Herzfrequenzerhöhung *verkürzt* sich vor allem die *Diastole* und damit die Füllzeit.

:::{attention}
Somit ist die Herzfrequenz einerseits ein **eigenständiger Faktor** für das Herzzeitvolumen, nimmt aber auch durch den **Einfluss auf die Füllung** Einfluss auf das Schlagvolumen.
:::

## Die Sauerstoffausschöpfung V̇O₂ und der Sauerstoffbedarf

Betrachtet man den Körperkreislauf, so kann man das arterielle Blut ($\rm{\color{purple}a}$) als Startpunkt und das zentralvenöse Blut ($\rm{\color{violet}cv}$, Blut in den Hohlvenen) als Endpunkt sehen.
Dazwischen liegt das Kapillargebiet, aus welchem Sauerstoff abgegeben wird.

Vergleicht man nun den Sauerstoffgehalt des Blutes am Startpunkt ($\color{blue}\rm{C{\color{purple}a}O}_2$)[^cao2] mit dem des Blutes am Endpunkt ($\color{blue}\rm{C{\color{violet}v}O}_2$)[^cvo2], so ist die Differenz der Verlust" an Sauerstoff, also welcher an das Gewebe abgegeben wurde.
Da sowohl $\color{blue}\rm{Hb}$ als auch die Hüfner'sche Zahl am Start- und Endpunkt ident sind, ist die Differenz der Sättigungswerte interessant.
Verbunden mit dem $\color{red}\rm{CO}$ ergibt sich die Sauerstoffausschöpfung ${\dot{\rm V}\rm O}_2$:

$$
{\dot{\rm V}\rm O}_2 \approx {\rm\color{red}CO} \times {\color{blue}{\rm Hb}\times 1,34 \times } ( {\color{teal}{\rm S{\color{purple}a}O_2} - {\rm S{\color{violet}cv}O_2}})
$$

[^cao2]: ${\color{blue}\rm{C{\color{purple}a}O}_2} \approx {\color{blue}\rm{Hb} \times 1,34 \times \rm{S{\color{purple}a}O}_2}$

[^cvo2]: ${\color{blue}\rm{C{\color{violet}cv}O}_2} \approx {\color{blue}\rm{Hb} \times 1,34 \times \rm{S{\color{violet}cv}O}_2}$

Es ist dabei festzuhalten, dass die Sauerstoffausschöpfung nicht mit dem eigentlichen Sauerstoffbedarf des Körpers gleichzusetzen ist:
Nur Bereiche, welche *perfundiert* werden, haben überhaupt die Möglichkeit, Sauerstoff auszuschöpfen.
Dies ist hinsichtlich dem Phänomen der *Zentralisation* ein wesentlicher Faktor.

% Die V̇O₂ hat jedoch einen Haken:
% Der Cardiac Output muss ermittelt werden um sie berechnen zu können.
% Hat man dazu nicht die Möglichkeit, kann man auch die die Sättigungswerte isoliert betrachten.
% Dies ist in der klinischen Routine bei Intensivpatienten mit den ohnehin vorhandenen Invasivitäten (ZVK, arterieller Zugang) oft problemlos und ohne großen Aufwand möglich
% Da man hierbei nur die *relative* Sauerstoffausschöpfung beurteit, kann man die *kardiale Komponente* als mögliche Ursache einer pathologischen Sauerstoffausschöpfung *nicht beurteilen*.
%
% Der Normalbereich der ScvO₂ liegt bei 70-75%
%
% Es stellt sich nun die Frage:
% *"Ist eine höhere zentralvenöse Sauerstoffausschöpfung gut oder schlecht?"*
%
%
% Somit ergibt sich folgende Dynamik:
%
% -   Eine hohe ScvO₂ kann für ein sehr hohes O₂-Angebot (guter Cardiac Output, viele O₂-Träger (Hb), gute Oxygenierung), wenig Bedarf oder wenig Perfusion sprechen.
% -   Eine niedrige ScvO₂ kann ein Zeichen für erhöhte Nachfrage und/oder ein schlechtes Angebot (wenig Cardiac Output, wenig O₂-Träger, schlechte Oxygenierung) sein.
% -   Alles was eine Abgabe von O₂ an das Gewebe erschwert (Zentralisation, Anasarka, Hypothermie, Alkalose\ [#AlkaloseO2Abgabe]_)
%
% .. [#AlkaloseO2Abgabe]
%     Hypothermie und Alkalose sorgen für eine höhere Affinität von O₂ zum Hämoglobin und erschweren daher die Abgabe (*Linksverschiebung* der **Sauerstoffbindungskurve**, vgl. {term}`Bohr-Effekt`)
%
% .. note::
%
%     -   Wenn die Sauerstoffversorgung nicht ausreicht, um den Stoffwechselbedarf des Gewebes zu decken, ergibt sich ein erniedrigter ScvO₂-Wert. Verminderte Perfusion (Zentralisation!) kann dies verschleiern.
%     -   Die ScvO₂ ist abhängig von Oxygenierung, Sauerstoffzufuhr und Sauerstoffextraktion, differenziert aber nicht.
%     -   Der tatsächliche Bedarf wird durch die Sauerstoffextraktion nur indirekt und mitunter falsch angezeigt.
%
% Als orientierende Untersuchung ist daher die isolierte Betrachtung der ScvO₂ einfach und nützlich, zur weiteren Differenzierung bedarf es aber oft der Ermittlung des Cardiac Outputs mittels anderer Methoden, um die relative und absolute Sauerstoffausschöpfung zu ermitteln.
