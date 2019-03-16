
##################
Benutzungshinweise
##################



*******
Im Text
*******

*Betonte* Textteile sind kursiv, *Besonders stark betonte* sind fett
gedruckt. :dfn:`Fachbegriffe`, welche an dieser
Stelle erklärt werden, haben ebenfalls eine eigene Formatierung.
Normale Fußnoten [1]_ beinhalten
Hintergrundinformationen, die nicht uninteressant sind, aber den
normalen Fließtext unnötig aufblähen würden.


.. [1]
   Ich bin eine normale Fußnote.

**************
Kompetenzlevel
**************

Die Kompetenzlevel des Zielpublikums der einzelnen Inhalte der AASS sind
wie in der folgenden Tabelle gegliedert:

.. table:: Kompetenzlevel

	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | **ID**   | **Level**   | **Titel**           | **Beschreibung**                                                                                                                            |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | 0        | *A*         | Laien, Ersthelfer   | Laienhelfer                                                                                                                                 |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | 1        | *B*         | First Responder     | First Responder (ohne Ausbildung nach SanG)                                                                                                 |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | 2        | *C*         | Basic               | *.at* Rettungssanitäter                                                                                                                     |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | 3        | *D*         | Intermediate        | *.at* Notfallsanitäter mit oder ohne Notfallkompetenz NKA; *.de* Rettungssanitäter                                                          |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | 4        | *E*         | Advanced            | Ärzte, diplomiertes Pflegepersonal; *.at* Notfallsanitäter mit Notfallkompetenz NKV oder NKI; *.de* Notfallsanitäter, Rettungsassistenten   |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
	   | 5        | *F*         | Expert              | Experten, Ärzte, Fachärzte, diplomiertes Pflegepersonal mit Zusatzausbildung                                                                |
	   +----------+-------------+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

***************************************************************
Aufbau eines Themas 
***************************************************************

Anatomische Struktur
====================

-	Überschrift

	``anatomische Nomenklaturen``

	-	Basics 
	
		*(inkl. Definition)*
	-	Umfassende Beschreibung

		-	Struktur
		-	Lage
		-	Histologie
		- 	... 
		
	-	Gefäßversorgung
	-	Innervation
	-	Physiologische Funktion

		- 	Basics
		-	Umfassende Beschreibung

	-	Besondere Anatomie

		- 	``Schnittbild``
		-	``Ultraschall``


Krankheitsbild
==============

-	Überschrift

	``ICD-Codes``

	-	Basics inkl. Definition
	-	Umfassende Beschreibung

	-	Symptome und Diagnostik

		``Vorbemerkungen, klassische Leitsymptome``
	
		-	ABCDE 
			
			*(Bei jedem Punkt jeweils zuerst Basics, dann erweiterte Diagnostik/Symptome)*
		-	SAMPLER
			
			*(Bei jedem Punkt jeweils zuerst Basics, dann Details)*
		-	Erweiterte Diagnostik

			-	``z. B. EKG``
			-	``z. B. Labor``
			-	``z. B. Bildgebung``
		
	-	Therapie
	
		-	Basics der Akuttherapie
		-	Erweiterte Akuttherapie
		
			-	Pharmakotherapie
			-	Interventionen
			-	...

		-	Weiterbehandlung
			
	-	Besonderheiten im präklinischen Setting
	
		-	Limitationen in Diagnostik und Therapie
		-	Prioritäten
		-	Transportziel


*********
Maßnahmen
*********

Maßnahmen im engeren Sinne sind festgelegte Handlungsempfehlungen,
vergleichbar mit Lehrmeinungen. Es wird zwischen allgemeinen, Standard-
und speziellen Maßnahmen unterschieden, siehe :ref:`Tafel-Massnahmentypen`.
Jede Maßnahme hat eine Kennung und eine Versionsnummer.

.. _Tafel-Massnahmentypen:

.. table:: Maßnahmentypen

	+----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| **ID**   | **Art**                  | **Beschreibung**                                                                                                                                                                                            |
	+----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| ALL      | *Allgemeine Maßnahmen*   | Allgemeine Maßnahmen beziehen sich auf eine Gruppe von Patienten mit einer Übergruppe bestimmter, verwandter Erkrankungen, wobei eine weiterführende Unterteilung mittels spezieller Maßnahmen existiert.   |
	+----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| STD      | *Standardmaßnahmen*      | Standardmaßnahmen treffen unter bestimmten Bedingungen auf eine große Gruppe unterschiedlicher Patienten mit unterschiedlichen Diagnosen zu.                                                                |
	+----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| SPZ      | *Spezielle Maßnahmen*    | Spezielle Maßnahmen treffen auf bestimmte Patienten mit einer bestimmten Diagnose oder einem bestimmten Zustand zu.                                                                                         |
	+----------+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


*************
Externe Teile
*************

Aus Kostengründen sind manchmal nicht alle Teile Bestandteil eines
Drucks. Dies betrifft besonders Teile des Appendix wie z. B. das
Literaturverzeichnis. Diese Teile sind online auf der AASS-Projektseite
im Download-Bereich verfügbar (http://www.aass.at/cms/download/aass/).

.. _Table-Versionstypen:

.. table:: Versionstypen. Es gibt sechs verschiedene Versionstypen, welche den Entwicklungsfortschritt einer Version angeben 
	   
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | **Kennung**   | **Versionstyp**          | **Beschreibung**                                                                                                                                                                                                                                                                                                                                                               | **Beispiel**                     |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | *nightly*     | *Laufende Entwicklung*   | Es handelt sich dabei um eine Zwischenversion ohne formale Kriterien zur Fertigstellung. Die Versionstyp-spezifische Nummerierung ergibt sich aus dem Datum.                                                                                                                                                                                                                   | ``2.0.0.nightly.20140119164900`` |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | *alpha*       | *Zwischenversion*        | Version ohne wesentliche formale Kriterien zur Fertigstellung, gedacht als Version zu Demonstrations- oder speziellen Testzwecken. Eine Version, welche zu einem Review eingereicht wird, wäre auch eine Alpha Version. Die Versionstyp-spezifische Nummerierung ergibt sich aus dem Datum.                                                                                    | ``2.0.0.alpha.20140119164900``   |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | *beta*        | *Sprintversion*          | Version, welche nach einem Sprint (Entwicklungszyklus, Iteration) fertig gestellt wurde. Grundsätzlich wäre sie theoretisch nach formalen Gesichtspunkten einsetzbar, jedoch entspricht sie nicht den inhaltlichen Qualitätsstandards und ist auch nicht zum produktiven Einsatz gedacht. Die Versionstyp-spezifische Nummerierung ergibt sich aus der Nummer der Iteration.   | ``2.0.0.beta.44``                |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | *gamma*       | *Vorabversion*           | Version, welche für den produktiven Einsatz in kontrollierten Umgebungen (Partnerinstitutionen) gedacht ist. Die Versionstyp-spezifische Nummerierung ergibt sich aus einer fortlaufenden Nummerierung der Vorabversionen.                                                                                                                                                     | ``2.0.0.gamma.1``                |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | *delta*       | *Release Candidate*      | Für die Veröffentlichung eingereichte Version. Die Versionstyp-spezifische Nummerierung ergibt sich aus dem Zusatz RC und einer durch einen Bindestrich getrennten fortlaufenden Nummerierung (RC-1, …).                                                                                                                                                                       | ``2.0.0.delta.RC-1``             |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   | *final*       | *Release*                | Es handelt sich hierbei um die endgültige Version, welche für den öffentlichen und produktiven Einsatz konzipiert wurde. Die finale Version hat keine Versionstyp-spezifische Nummerierung.                                                                                                                                                                                    | ``2.0.0``                        |
	   +---------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
	   

Eine Versionsnummer besteht aus

#. einem dreistelligen **Primärschlüssel**, bestehend aus

   #. der **Hauptversionsnummer** (*Major*) zur Kennzeichnung
      der **Hauptversionslinie**,

   #. der **Nebenversionsnummer** (*Minor*) zur Kennzeichnung
      von Update-Versionen der jeweiligen *Hauptversionslinie* und

   #. der **Revisionsnummer** für Fehlerbehebung;

#. dem **Versionstyp** und einer

#. nachgeordneten Versionstyp-spezifischen
   Nummerierung (*VSN*), welche die Eindeutigkeit der Versionskennung
   sicherstellen soll.

#. Die volle Versionskennungen beinhaltet noch die **Variantenbezeichnung**.

#. Sollte das Produkt einen Auszug des Gesamtwerkes darstellen, so wird
   noch eine **Auszugsbezeichnung** angefügt.

Die Bestandteile der Versionsbezeichnung werden durch Punkte getrennt.

    -  Schema der Versionsbezeichnung:
       ``<*Primärschlüssel*>.<*Versionstyp*>.<*VSN*>.<*Variante*>.<*Auszug*>``

Die 3 Stellen werden durch Punkte getrennt. In der Kurzschreibweise
können die Nebenversionsnummer und die Revisionsnummer weggelassen
werden, sofern die jeweilige und die dazu untergeordnete Stelle 0 ist
(z. B. ``2.1.0`` → ``2.1``, ``2.0.0`` → ``2``; ``2.0.1`` wird nicht abgekürzt).



