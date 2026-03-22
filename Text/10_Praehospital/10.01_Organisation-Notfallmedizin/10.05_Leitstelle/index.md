---
status: final
---






:::{index} single: Call Taking
:::
:::{index} single: Disposition
:::
:::{index} single: Disponent
:::

(AORG-VO-Rettungsleitstelle)=

# Die Rettungsleitstelle

:::{sidebar} Leitstelle
- *Call Taking*

  - Annahme & Abfrage von Notrufen & Alarmierungen
  - Erfassung im Einsatzleitsystem, Einteilung und Priorisierung nach
    Art und Dringlichkeit der Meldung, benötigtes Personal, etc.

- *Disposition*

  - Welche Einsatzmittel
  - Alarmierung der Einheiten
  - Übermittlung der Aufträge
  - Unterstützung, Koordination
  - Evtl. Zuteilung von Krankenhausbetten
  - Status-/Standort-Verwaltung

- Dokumentation
:::


Eine Leitstelle leitet den Betrieb einer oder mehrerer zugeordneter Organisationseinheiten.
Sie nimmt Informationen (Notrufe, Meldungen der Einheiten, …) entgegen, wertet sie aus und koordiniert die einzelnen, ihr zugeordneten Einheiten.

Eine Leitstelle kann sowohl organisationsübergreifend (eine Leitstelle ist für mehrere Organisationen zuständig, z. B. für Rettungsdienst *und* Feuerwehr) eingerichtet werden, es kann jedoch auch innerhalb einer Organisation verschiedene Leitstellen, getrennt nach Zuständigkeitsbereichen, geben (z. B. getrennte Leitstellen für Rettungs- und Krankentransport, Sonderleitstellen während Veranstaltungen, regionale Trennung, …).
Leitstellen sind meistens ortsfest eingerichtet, es gibt jedoch auch mobile Leitstellen, welche bei besonderen Ereignissen geplant oder ad-hoc zum Einsatz kommen können.

Zu den typischen **Aufgaben** einer Rettungsdienstleitstelle gehört die *Annahme und Abfrage von Notrufmeldungen* (Call Taking) oder sonstigen Alarmierungen, sowie deren *Erfassung* in einem Einsatzleitsystem durch einen *Call Taker*.
Die Meldungen unterlaufen eine *Einteilung und Priorisierung* nach Art und Dringlichkeit der Meldung.


:::{figure} ../../../../Submodules/3134-medical-picture-collection/Gabriel-Sebastian/Input/2010-06-25-DIF2010-IMG_2460_v2-quick00800-485.\*
:width: 50%

Call taker in einer Leitstelle

© Sebastian Gabriel {term}`ℓ MfG`
:::

Der Leitstelle obliegt die Entscheidung, *welche Einsatzmittel* eingesetzt werden, oft wird dazu nach einer Alarm- und **Ausrückordnung** vorgegangen.
Die *Alarmierung* der Einheiten erfolgt durch die Leitstelle über Sprech- oder Datenfunk, bzw. andere geeignete Hilfsmittel.
Sie *übermittelt die Einsatzaufträge* und unterstützt und koordiniert während des Einsatzes.

Die Einteilung, Alarmierung und Koordination der Einheiten wird **Disposition** genannt und erfolgt durch **Disponenten**.
In vielen Rettungsdienstbereichen ist die Leitstelle auch für die Zuteilung von Krankenhausaufnahmekapazitäten (*Bettenzuteilung*) zuständig.
Um einen Überblick über einsatzbereite Fahrzeuge etc. zu erhalten, sorgt die Leitstelle für eine *Status- und Standort-Verwaltung*: Es wird der jeweilige Status und – wenn möglich –
der Standort der Einheiten (einsatzbereit, Richtung Berufungsort, …) protokolliert und ausgewertet.

Eine sehr wichtige Aufgabe ist die *Dokumentation*: Es werden sowohl die Einsatzdaten wie z. B. Einsatzort, Einsatzursache und Zeiten protokolliert, als auch besondere Ereignisse.
Telefongespräche mit der Leitstelle werden i.d.R. aufgezeichnet und gespeichert.

(AORG-VO-Meldealgorhithmen)=

## Standardisierte Dispatch-Systeme

In vielen Leitstellen wurden zertifizierte Abfragesysteme etabliert, eines der hierzulande bekannteren ist das *Advanced Medical Priority Dispatch System* (**AMPDS**).
Dies ist ein standardisiertes System zur Abfrage von Notrufmeldungen, Klassifizierung und Priorisierung der daraus resultierenden Einsätze, sowie zur telefonischen Hilfestellung bis zum Eintreffen der Einsatzkräfte.
Durch die systematisierte Abfrage wird ein 3-teiliger Code generiert, welcher den Auftrag klassifiziert und ihm eine Priorität zuweist.
- Der erste Teil ist eine Zahl von `1` bis `36` und weist auf eine Leit-Beschwerde oder ein spezifisches Protokoll des AMPDS hin.
- Die zweite Komponente, ein Buchstabe (`A` bis `E`, `Ω`), stellt die Priorität dar (`A` für niedrige, `E` für höchste Priorität, `Ω` für "sonstige Situation").
- Die dritte Komponente, eine Zahl, liefert spezifischere Informationen über den Zustand des Patienten.

Zum Beispiel:

| Code     | Bedeutung                                            |
| -------- | ---------------------------------------------------- |
| `9-E-1`  | Herz- oder Atemstillstand                            |
| `9-E-4`  | Herz- oder Atemstillstand aufgrund von Strangulation |
| `19-C-3` | Herzbeschwerden, Brustschmerzen > 35 Jahre           |
| `24-A-4` | Schlaflosigkeit                                      |
| `26-A-1` | Erkrankt, keine Notfallsymptome                      |
| `28-C-3` | Schlaganfall, Sprach- oder Bewegungsstörungen        |

Diese Einschätzungen und daraus resultierenden Codes sind zwar aufgrund der angewandten Systematik weitgehend reproduzierbar, jedoch haben sie erfahrungsgemäß mit der Realität mitunter wenig zu tun.
Dennoch, mittels dieser Diagnosecodes kann eine entsprechende **Ausrückordnung** für die unterschiedlichen Rettungsmittelkategorien erstellt werden, z. B.:
- `9-E-1` → NEF+RTW
- `28-C-3` → RTW



:::{index} single: Primäreinsatz
:::
:::{index} single: Sekundäreinsatz
:::

## Einsatztypen

:::{sidebar} Einsatztypen
Primäreinsatz
: - Erstes Glied der professionellen Versorgung

Sekundärtransport
: - Patient bereits versorgt
  - Überstellungen
:::

Beim **Primäreinsatz** ist der Rettungsdienst das *erste Glied* der professionellen Versorgung und wird präklinisch ("vor der Klinik") tätig.
Beim **Sekundärtransport** wird ein *bereits versorgter Patient* transportiert, z. B. zwischen unterschiedlichen Spitälern (Transferierung, *Überstellung*).

## Kommunikationswege

:::{index} single: Halbduplexbetrieb
:::
:::{index} single: Sprechfunk
:::
:::{index} single: Funkname
:::
:::{index} single: Rufnahme
:::

### Funk

:::{sidebar} Funk
- Sprechfunk
- Datenfunk
:::

Als Funk(technik) bezeichnet man allgemein die Methode, Informationen aller Art mit Hilfe elektromagnetischer Wellen im Radiofrequenzbereich (Radiowellen) drahtlos zu übertragen.

Das drahtlose Übertragen von *gesprochenen* Informationen wird als
**Sprechfunk** bezeichnet.
Dabei können Handfunkgeräte, Mobilfunkgeräte oder Feststationen zum Einsatz kommen.

Der klassische Funkbetrieb wird im Wechselverkehr (*Halbduplexbetrieb*) abgewickelt, d. h. es kann nur ein Teilnehmer gleichzeitig senden und belegt dabei die Frequenz.[^vollduplexbetrieb]
Um einen geordneten Funkbetrieb zu ermöglichen, gibt es für jeden organisierten Funkbereich Vorschriften (Protokolle), wie der Funkverkehr abzuwickeln ist.

[^vollduplexbetrieb]: Beim {index}`Vollduplexbetrieb` kann man
    gleichzeitig empfangen und senden (z. B. Telefon).

#### Durchführung eines Funkspruchs

I. d. R. wird jede Funkstelle mit einem eigenen **Rufzeichen** bezeichnet und kann mit diesem gerufen werden.
Die Systematik der Benennung kann je nach Land, Organisation, Leitstellen- und Funkbereich sehr unterschiedlich sein.

Ein Funkgespräch wird mit Anrufen der Funkstelle begonnen.
Ein Funkspruch soll möglichst kurz und bündig sein, Höflichkeitsfloskeln sind nicht statthaft.
Das Ende eines Funkspruchs wird mit dem Wort *"kommen"* angezeigt, sodass die andere Funkstelle weiss dass sie nun antworten kann.
Das Funkgespräch wird mit dem Wort *"Ende!"* beendet.
Zum Buchstabieren werden genormte Buchstabieralphabete nach ÖNORM A 1081 oder DIN 5009 verwendet, in Englisch-sprachigen Konversationen (z. B. im Flugverkehr) das NATO-Alphabet, siehe Tabelle {ref}`Buchstabieralphabete`.

:::{note}
- Funken: *Denken* – *drücken* – *kurz und bündig sprechen*
:::

:::{tabularcolumns} CLLLCLLLCLL
:::

:::{list-table} Buchstabieralphabete nach ÖNORM A 1081, DIN 5009 und NATO
:header-rows: 1
:name: Buchstabieralphabete

- -
  - ÖNORM
  - DIN
  - NATO
  -
  - ÖNORM
  - DIN
  - NATO
  -
  -
  -
- - **A**
  - Anton
  - ←
  - Alpha
  - **O**
  - Otto
  - ←
  - Oscar
  - **0**
  - Null
  - Zero
- - **Ä**
  - Ärger
  - ←
  - —
  - **Ö**
  - Österreich
  - Ökonom
  - —
  - **1**
  - Eins
  - One
- - **B**
  - Berta
  - ←
  - Bravo
  - **P**
  - Paula
  - ←
  - Papa
  - **2**
  - Zwo
  - Two
- - **C**
  - Cäsar
  - ←
  - Charlie
  - **Q**
  - Quelle
  - ←
  - Quebec
  - **3**
  - Drei
  - Three
- - **Ch**
  - —
  - Charlotte
  - —
  - **R**
  - Richard
  - ←
  - Romeo
  - **4**
  - Vier
  - Fower
- - **D**
  - Dora
  - ←
  - Delta
  - **S**
  - Siegfried
  - Samuel
  - Sierra
  - **5**
  - Fünf
  - Five
- - **E**
  - Emil
  - ←
  - Echo
  - **Sch**
  - —
  - Schule
  - —
  - **6**
  - Sechs
  - Six
- - **F**
  - Friedrich
  - ←
  - Foxtrott
  - **ß**
  - Scharfes s
  - Eszett
  - —
  - **7**
  - Sieben
  - Seven
- - **G**
  - Gustav
  - ←
  - Golf
  - **T**
  - Theodor
  - ←
  - Tango
  - **8**
  - Acht
  - Eight
- - **H**
  - Heinrich
  - ←
  - Hotel
  - **U**
  - Ulrich
  - ←
  - Uniform
  - **9**
  - Neun
  - Niner
- - **J**
  - Julius
  - ←
  - Juliett
  - **V**
  - Viktor
  - ←
  - Victor
  - **.**
  - —
  - Stop
- - **K**
  - Konrad
  - Kaufmann
  - Kilo
  - **W**
  - Wilhelm
  - ←
  - Whiskey
  -
  -
  -
- - **L**
  - Ludwig
  - ←
  - Lima
  - **X**
  - Xaver
  - Xanthippe
  - X-ray
  -
  -
  -
- - **M**
  - Martha
  - ←
  - Mike
  - **Y**
  - Ypsilon
  - ←
  - Yankee
  -
  -
  -
- - **N**
  - Nordpol
  - ←
  - November
  - **Z**
  - Zürich
  - Zacharias
  - Zulu
  -
  -
  -
:::

### Digitalfunk, Datenfunk und TETRA

Unter dem Begriff *Datenfunk* versteht man die *automatisierte*, drahtlose Übertragung von codierten *Daten* mittels analoger oder digitaler Funktechnik.
I.d.R. erfolgt dies mittels EDV-gestützter Systeme, welche sich um die Codierung und anwendungsgerechte Darstellung (Monitor, Fahrzeugdisplays, etc.) der Daten kümmern.
Der Vorteil des Datenfunkes ist, dass Informationen nur einmal eingegeben werden müssen, und von den Systemen der Empfangsstationen (Fahrzeugdisplays, elektronische Dokumentationssysteme, etc.) automatisiert weiterverwendet werden können.
Am Markt haben sich eine Vielzahl von Produkten fest etabliert und lösen den Sprechfunk als Kommunikationsmedium immer mehr ab.
In vielen Ländern hat der Digitalfunk analoge Funksysteme für die Behördenkommunikation abgelöst.

In Österreich wurde beinahe flächendeckend das System **TETRA** (Terrestrial Trunked Radio) eingeführt.
Dies ist ein Standard für digitalen Bündelfunk, mit dem sich Universalnetze für unterschiedliche Mobilfunkdienste (Sprechfunk, Telefonie, Datenfunk) realisieren lassen.
Mittels TETRA ist einerseits die direkte Kommunikation zwischen Endgeräten möglich, die Stärke liegt jedoch in der Anbindung an eine Netzinfrastruktur durch eine Basisstation ähnlich einer Mobilfunkstation.

:::{subfigure} AB
:subcaptions: below
:name: Fig-BS-TETRA
:class-grid: outline
:gap: 20px

TETRA Funkgeräte \[© Sebastian Gabriel  {term}`ℓ MfG`\]


![TETRA Handfunkgerät](../../../../Submodules/3134-medical-picture-collection/Gabriel-Sebastian/Vehicles/NEF/Noe/IMG_172313.001341px.jpg)

![TETRA Fahrzeugfunkgerät](../../../../Submodules/3134-medical-picture-collection/Gabriel-Sebastian/Vehicles/NEF/Noe/IMG_172239.001341px.jpg)
:::

### Telefon

Das Telefon oder Mobiltelefon hat sich in der täglichen Routine etabliert.
Nachteil dieses Systems ist, dass man auf die zivile Infrastruktur angewiesen ist.
Ist diese z. B. in Folge von Überlastung gestört, ist dieser Kommunikationsweg nicht mehr zuverlässig nutzbar und man muss mit den Einsatzorganisationen vorbehaltenen Kommunikationswegen auskommen.

(Q-AORG23003)=

#### Notrufnummern

Neben der internen Kommunikation der Einsatzkräfte hat das Telefon einen großen Stellenwert hinsichtlich der Durchführung von Notrufen.
Dazu stehen in Österreich folgende Nummern zur Verfügung:

:::{list-table} Notrufnummern in Österreich
:header-rows: 1
:stub-columns: 1

- - Nr.
  - Beschreibung
  - Anmerkungen
- - 122
  - Feuerwehr
  -
- - 133
  - Polizei
  -
- - 144
  - Rettungsdienst
  -
- - 141
  - Ärztenotdienst
  -
- - 112
  - Euro-Notruf
  - läuft in Österreich bei der Polizei auf
- - 140
  - Bergrettung
  -
- - 1450
  - telefonische Gesundheitsberatung
  -
:::