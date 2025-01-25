
:::{index} single: Blutgasanalyse
:::
:::{index} single: BGA
:::

(haemodynmonitoringbga)=
(GHDM-KP-BGA-haemodynamisch)=

# Blutgasanalyse (BGA): Hämodynamische Aussagen

Zwar ist das {ref}`respiratorische Monitoring das primäre Revier der BGA <RespMonitoringBGA>`, jedoch bieten aktuelle Geräte oft eine erweiterte Point-of-Care-Laborfunktion (PoC), welche die Bestimmung auch für den Kreislauf relevanter Laborwerte ermöglicht.
Darunter fallen der Laktatspiegel, sowie die O₂-Sättigungsbestimmung an unterschiedlichen Stationen des Kreislaufs (arteriell, zentralvenös, gemischtvenös).
Die {ref}`invasive arterielle Blutdruckmessung <IABP>` sorgt als Nebeneffekt für einen einfachen Zugangsweg zur Gewinnung von arteriellen Blutproben für eine arterielle Blutgasanalyse. 

:::{todo} {ticket-alt}`21` Bilder: BGAs
:::



:::{index} single: ScvO₂
:::
:::{index} single: SmvO₂
:::
:::{index} single: Sauerstoffsättigung; gemischtvenös
:::
:::{index} single: Sauerstoffsättigung; zentralvenös
:::
:::{index} single: Laktat
:::

## Messwerte

An unterschiedlichen Stellen (*x*) des Blutkreislaufes (**arteriell** (**a**), **venös** (**v**), **zentralvenös** (**cv**), **gemischtvenös** (**mv**)) können gemessen werden:

- Oxygenierung (p*x*O₂, p*x*CO₂)
- pH
- Sauerstoffträger (Hb)
- Sauerstoffsättigung (S*x*O₂)
- Laktat

## Indikationen

Bei vorhandenem Zugang kann die Indikation sehr liberal gestellt werden.

## Kontraindikationen

Bei vorhandenem Zugang grundsätzlich keine.

## Komplikationen

Abhängig von Entnahmestelle und -art.



:::{index} single: Sauerstoffausschöpfung
:::
:::{index} single: V̇O₂
:::
:::{index} single: SaO₂
:::
:::{index} single: ScvO₂
:::
:::{index} single: SmvO₂
:::
(scvo2-vo2)=
(VO2)=
(Q-GHDM-KP-24003)=

## Bestimmung der Sauerstoffausschöpfung V̇O₂: SaO₂ vs. SmvO₂

:::{note}
In der Literatur und sprachübergreifend sind die im Folgenden verwendeten Indices (v für venös, mv für gemischtvenös, cv für zentralvenös) nicht einheitlich geregelt.
Somit ist die jeweilige sprach- bzw. publikationsspezifische Konvention zu beachten.
:::

Betrachtet man den Körperkreislauf so kann man das *arterielle* Blut ($\rm\color{purple}a$) als *Startpunkt* und das *geschmischtvenöse* Blut ($\rm\color{violet}mv$, Blut im rechten Herzen, gemischt aus oberer und unterer Hohlvene) als *Endpunkt* sehen.
Dazwischen liegt das Kapillargebiet, aus welchem Sauerstoff abgegeben wird.

Vergleicht man nun den Sauerstoffgehalt des Blutes am *Startpunkt* ($\color{blue}\rm{C{\color{purple}a}O}_2$)[^cao2] mit dem des Blutes am *Endpunkt* ($\color{blue}\rm{C{\color{violet}mv}O}_2$)[^cvo2], so ist die *Differenz* der *"Verlust" an Sauerstoff*, also welcher an das Gewebe abgegeben wurde.
Da sowohl $\color{blue}\rm{Hb}$ als auch die Hüfner'sche Zahl am Start- und Endpunkt ident sind, ist die **Differenz der Sättigungswerte** interessant.
Verbunden mit dem $\color{red}\rm{CO}$ ergibt sich die **Sauerstoffausschöpfung** V̇O₂:

$$
{\dot{\rm V}\rm O}_2 \approx {\rm\color{red}CO} \times {\color{blue}{\rm Hb}\times 1,34 \times } ( {\color{teal}{\rm S{\color{purple}a}O_2} - {\rm S{\color{violet}mv}O_2}})
$$

[^cao2]: ${\color{blue}\rm{C{\color{purple}a}O}_2} \approx {\color{blue}\rm{Hb} \times 1,34 \times \rm{S{\color{purple}a}O}_2}$

[^cvo2]: ${\color{blue}\rm{C{\color{violet}mv}O}_2} \approx {\color{blue}\rm{Hb} \times 1,34 \times \rm{S{\color{violet}mv}O}_2}$

Das *geschmischtvenöse* Blut ($\rm\color{violet}mv$) ist jedoch einer routinemäßigen Messung schwer zugänglich.
Zu dessen Gewinnung würde man einen {ref}`Pulmonalarterienkatheter <PAC>` benötigen, welcher sehr risikobehaftet ist und nur bei speziellen Situationen indiziert ist.
Als *Surrogat* kann hierbei das *zentralvenöse Blut* ($\rm\color{violet}cv$) dienen, welches mittels eines zentralen Venenkatheters (*ZVK*) zugänglich ist, welcher sehr häufig bei Intensivpatienten als Gefäßzugang zum Einsatz kommt.

Es ist dabei festzuhalten, dass die Sauerstoff*ausschöpfung* *nicht* mit dem eigentlichen Sauerstoff*bedarf* des Körpers gleichzusetzen ist:
Nur Bereiche, welche *perfundiert* werden, haben überhaupt die Möglichkeit, Sauerstoff ausschöpfen.
Dies ist hinsichtlich dem Phänomen der *Zentralisation* ein wesentlicher Faktor.

Die V̇O₂ hat jedoch einen Haken:
Der *Cardiac Output* (CO) muss ermittelt werden um sie berechnen zu können.
Hat man dazu nicht die Möglichkeit, kann man jedoch auch die die Sättigungswerte isoliert betrachten.
Dies ist in der klinischen Routine bei Intensivpatienten mit den ohnehin vorhandenen Invasivitäten (ZVK, arterieller Zugang) oft problemlos und ohne großen Aufwand möglich. 
Da man hierbei nur die *relative* Sauerstoffausschöpfung beurteilt, kann man die *kardiale Komponente* als mögliche Ursache einer pathologischen Sauerstoffausschöpfung *nicht beurteilen*.

Der Normalbereich der **ScvO₂** liegt bei **70-75%**.
Es stellt sich nun die Frage:
*"Ist eine höhere zentralvenöse Sauerstoffausschöpfung gut oder schlecht?"*

Somit ergibt sich folgende Dynamik:

- Eine **hohe ScvO₂** kann für ein sehr **hohes O₂-Angebot** (guter Cardiac Output, viele O₂-Träger (Hb), gute Oxygenierung), **wenig Bedarf** *oder* **wenig Perfusion** sprechen.
  Alles, was eine Abgabe von O₂ an das Gewebe erschwert (Zentralisation, Anasarka, Hypothermie, Alkalose[^alkaloseo2abgabe]), kann die ScvO₂ erhöhen.
- Eine **niedrige ScvO₂** kann ein Zeichen für **erhöhte Nachfrage** und/oder ein **schlechtes Angebot** (wenig Cardiac Output, wenig O₂-Träger, schlechte Oxygenierung) sein.


[^alkaloseo2abgabe]: Hypothermie und Alkalose sorgen für eine höhere Affinität von O₂ zum Hämoglobin und erschweren daher die Abgabe (*Linksverschiebung* der **Sauerstoffbindungskurve**, vgl. {term}`Bohr-Effekt`)

:::{note}
- Wenn die Sauerstoffversorgung nicht ausreicht, um den Stoffwechselbedarf des Gewebes zu decken, ergibt sich ein erniedrigter ScvO₂-Wert. Verminderte Perfusion (Zentralisation!) kann dies verschleiern.
- Die ScvO₂ ist abhängig von Oxygenierung, Sauerstoffzufuhr und Sauerstoffextraktion, differenziert aber nicht.
- Der tatsächliche *Bedarf* wird durch die Sauerstoffextraktion nur indirekt und mitunter falsch angezeigt.
:::

Als *orientierende Untersuchung* ist daher die isolierte Betrachtung der ScvO₂ einfach und nützlich, zur weiteren *Differenzierung* bedarf es aber oft der Ermittlung des Cardiac Outputs mittels anderer Methoden, um die relative und absolute Sauerstoffausschöpfung zu ermitteln.



:::{index} single: gemischtvenöse Sättigung
:::
:::{index} single: Sättigung; gemischtvenöse 
:::
:::{index} single: SmvO₂
:::
(ghdm-vo-pac-smvo2)=

### Gemischtvenöse Sättigung SmvO₂

Die venöse Sättigung kann zentralvenös (große Hohlvenen über ZVK) oder **gemischtvenös** (Formelzeichen $\rm mv$, *Zusammenfluss* beider Hohlvenen: **rechter Vorhof** bzw. **rechte Kammer**) mittels eines {ref}`Pulmonalarterienkatheters <Pulmonalarterienkatheter>` gemessen werden.
Dabei muss bedacht werden, dass das Einzugsgebiet der oberen und der unteren Hohlvene unterschiedliche Organe mit unterschiedlichem Sauerstoffbedarf versorgt (Hirn durch die obere Hohlvene, Stamm und untere Extremität durch die untere Hohlvene).

:::{margin} ScvO₂ und SmvO₂
Normal, in Ruhe: ScvO₂ < SmvO₂

Schock: ScvO₂ > SmvO₂
:::

Bei *normalen* Patienten ist die ScvO₂ *in Ruhe* etwas *niedriger* als die SmvO₂, weil der untere Körperteil weniger Sauerstoff entzieht als der obere.
Im *Schockzustand* kann es jedoch zu Veränderungen des regionalen Blutflusses (*Zentralisation!*) und der Sauerstoffentnahme kommen.
Es kommt dann zu einer Abnahme der mesenterialen und renalen Blutversorgung (mit einer Zunahme der O₂-Extraktion) und einer *Umverteilung* des Blutflusses zum Gehirn.
Somit sind die absoluten Zahlenwerte von ScvO₂ und SmvO₂ nicht vergleichbar, allerdings verlaufen die Trends parallel zueinander, weshalb oft der **Trend der ScvO₂** als Verlaufsparameter berücksichtigt wird.
Bei kritischen Erkrankungen ist die ScvO₂ etwas *höher* als die SmvO₂.
{term}`🗎 Shanmukhappa 2022`



:::{index} single: Laktat
:::
:::{index} single: Stoffwechsel, anaerober
:::
:::{index} single: Glykolyse; anaerobe
:::

(Laktat)=

## Laktat

Laktat wird im Rahmen des **anaeroben Stoffwechsels** von den Zellen produziert (anaerobe Glykolyse).
Es ist somit mit einer erhöhten Gewebehypoxie, Azidose und einer verringerten myokardialen Sauerstoffversorgung verbunden.
Der Abbau findet vor allem in der Leber durch Gluconeogenese statt.

Ursachen eines erhöhten Laktatspiegels können sein:

- alles was zur Gewebshypoxie führt (Oxygenationsstörungen, Herzinsuffizienz, Kreislaufversagen bzw. Schock, Anämie, lokale und systemische Minderperfusion (Organischämie), erhöhter Bedarf (Belastung, Krampfgeschehen etc.), …)
- Flüssigkeitsmangel bzw. Hypovolämie
- Leberinsuffizienz (verminderter Abbau)
- Medikamente (klassisch: perioperative Laktatazidose bei Metformin)
