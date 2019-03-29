
*****************************************************
Sphinx-Schummelzettel
*****************************************************

:Info: See <http://docutils.sf.net/rst.html> for introductory docs.
:Author: David Goodger <goodger@python.org>

Struktur
=================

Überschirften sind mit Unterstrichen oder Unterstrichen mit Oberstrichen vesehen.

Body Elements
=============


"Listen-"Tabellen" (``.. list-table::``)
------------------------------------------------------------------------

Listen-Tabellen sind die einfachste Art um Tabellen zu erzeugen:

Die Direktive lautet ``.. list-table:: <Tabellentitel>``, 
``:widths:`` gibt die jeweiligen Spaltenbreiten (in Prozent) an,
``:header-rows:`` definiert wieviele Zeilen als Überschrift gerechnet werden,
``:stub-columns`` analog dazu, wie viele Spalten als Zeilentitel gerechnet werden.

::

    .. list-table:: Tabellenüberschrift
        :widths: 25 25 25 25
        :header-rows: 1
        :stub-columns: 1

        *   -   Erste Spalte, erste Zeile
            -   Zweite Spalte, erste Zeile 
            -   noch immer die erste Zeile 
            -   und die letzte (4.)Spalte der 1. Zeile
        *   -   jetzt geht es in die 2. Zeile
            -   usw. (2/2)
            -   usw. (3/2)
            -   usw. (4/2)
        *   -   (1/3)
            -   (2/3)
            -   (3/3)
            -   (4/3)

.. list-table:: Tabellenüberschrift
    :widths: 25 25 25 25
    :header-rows: 1
    :stub-columns: 1

    *   -   Erste Spalte, erste Zeile
        -   Zweite Spalte, erste Zeile 
        -   noch immer die erste Zeile 
        -   und die letzte (4.)Spalte der 1. Zeile
    *   -   jetzt geht es in die 2. Zeile
        -   usw. (2/2)
        -   usw. (3/2)
        -   usw. (4/2)
    *   -   (1/3)
        -   (2/3)
        -   (3/3)
        -   (4/3)

Tabelle mit Raster
-------------------

Raster-Tabellen sehen im Quelltext am schönsten aus, 
sind aber schwieriger zu erstellen bzw. auszubessern.
Allerdings ist hierbei das Zusammenführen von Zellen möglich.

.. code-block:: none
   
    +--------------------------------+-----------------------------------+
    | Ich bin eine Zelle             | Ich bin eine zusammengeführte     |
    |                                | Zelle (vertikal).                 |
    | Ich bin ein zweiter Absatz,    |                                   |
    | getrennt durch eine Leerzeile. | Auch hier kann es einen zweiten,  |
    +--------------------------------+ durch eine Leerzeile getrennten   |
    | Ich bin eine andere Zelle.     | Absatz geben.                     |
    |                                |                                   |
    |                                | Es kann auch:                     |
    |                                |                                   |
    |                                | -    Aufzählungen                 |
    |                                | -    andere **Formatierungen**    |
    |                                |                                   |
    |                                | geben.                            |
    +--------------------------------+-----------------------------------+
    | Ich bin eine horizontal zusammengeführte Zelle.                    |
    +--------------------------------------------------------------------+

+--------------------------------+-----------------------------------+
| Ich bin eine Zelle             | Ich bin eine zusammengeführte     |
|                                | Zelle (vertikal).                 |
| Ich bin ein zweiter Absatz,    |                                   |
| getrennt durch eine Leerzeile. | Auch hier kann es einen zweiten,  |
+--------------------------------+ durch eine Leerzeile getrennten   |
| Ich bin eine andere Zelle.     | Absatz geben.                     |
|                                |                                   |
|                                | Es kann auch:                     |
|                                |                                   |
|                                | -    Aufzählungen                 |
|                                | -    andere **Formatierungen**    |
|                                |                                   |
|                                | geben.                            |
+--------------------------------+-----------------------------------+
| Ich bin eine horizontal zusammengeführte Zelle.                    |
+--------------------------------------------------------------------+

Einfache Tabellen:
------------------

.. code-block:: none

  ==============    ==============
  Titel Spalte 1    Titel Spalte 2
  ==============    ==============
  Inhalt 11         Inhalt 21
  Inhalt 12         Inhalt 22
  Inhalt 13         Inhalt 23
  ==============    ==============



Listen
------

=======================  ==============================================================
Listenart                Beispiele                                               
=======================  ==============================================================
Nicht-mummerierte Liste  * items beginnt mit ``-``, ``+``, oder ``*``
Nummerierte Liste        1. items: Variation von       ``1.``, ``A)``, und ``(i)``
                         ``#.`` wird automatisch nummeriert
Definitionsliste         Term is flush-left : optional classifier
                         Definition is indented, no blank line between
Feld-Liste               ``:field name: field body``
Optionsliste             ``-o  at least 2 spaces between option & description``
=======================  ==============================================================

Markup
------

===================  ================================================================
Explicit Markup      Beispiele                                   
===================  ================================================================
Fußnote              ``.. [1] Manually numbered`` or ``[#] auto-numbered``
                     (even ``[#labelled]``) or ``[*] auto-symbol``
Literaturzitat       ``.. [CIT2002] A citation.``
Hyperlink 1          ``.. _reStructuredText: http://docutils.sf.net/rst.html``
2                    ``.. _indirect target: reStructuredText_``
3                    ``.. _internal target:``
4                    ``__ http://docutils.sf.net/docs/ref/rst/restructuredtext.html``
Directive ("::")     ``.. image:: images/biohazard.png``
Ersätzung Definiion  ``.. |substitution| replace:: like an inline directive``
Kommentar            ``.. is anything else``
Kommentar            (``..`` on a line by itself, with blank lines before & after,
                     used to separate indentation contexts)
===================  ================================================================

Inline Markup
=============

::

   *Hervorhebung*;

   **starke Hervorhebung**;

   `interpreted text`;

   `interpreted text with role`:emphasis:;

   ``inline literal text``;

   standalone hyperlink, http://docutils.sourceforge.net;

   named reference, reStructuredText_;
   
   `anonymous reference`__;
   
   footnote reference, [1]_;
   
   citation reference, [CIT2002]_;

   |substitution|; _`inline internal target`.

Direktiven
=========================
See <http://docutils.sf.net/docs/ref/rst/directives.html> for full info.


attention         
    Specific admonition; also 

admonition        
    Generische "Box"

    ::

        .. admonition:: Das ist ein Titel

            Das ist der Text in der Box 

    .. admonition:: Das ist ein Titel

        Das ist der Text in der Box 
    
    Neben der generischen Box gibt es spezielle Boxen: 
    -   "caution", 
    -   "danger",
    -   "error", 
    -   "hint", 
    -   "important", 
    -   "note", 
    -   "tip", 
    -   "warning"

    ::

        .. danger:: 

            Das ist eine Gefahr! 

    .. danger:: 

        Das ist eine Gefahr! 

image             
    ``.. image:: /Pfad/zu/dem/Bild.jpg``

figure            
    Wie "image", aber mit (optionaler) Legende und Nummerierung

topic             
    ``.. topic:: Title``; like a mini section

sidebar           
    ``.. sidebar:: Title``; like a mini parallel document

parsed-literal    
    A literal block with parsed inline markup

rubric            
    ``.. rubric:: Informal Heading``

epigraph          
    Block quote with class="epigraph"

highlights        
    Block quote with class="highlights"

pull-quote        
    Block quote with class="pull-quote"

compound          
    Compound paragraphs [0.3.6]

container         
    Generic block-level container element [0.3.10]

table             
    Create a titled table [0.3.1]

list-table        
    Create a table from a uniform two-level bullet list [0.3.8]

csv-table         
    Create a table from CSV data [0.3.4]

contents          
    Generate a table of contents

sectnum           
    Automatically number sections, subsections, etc.

header, footer    
    Create document decorations [0.3.8]

target-notes      
    Create an explicit footnote for each external target

math              
    Mathematical notation (input in LaTeX format)

meta              
    HTML-specific metadata

include           
    Read an external reST file as if it were inline

raw               
    Non-reST data passed untouched to the Writer

replace           
    Replacement text for substitution definitions

unicode           
    Unicode character code conversion for substitution defs

date              
    Generates today's date; for substitution defs

class             
    Set a "class" attribute on the next element

role              
    Create a custom interpreted text role [0.3.2]

default-role      
    Set the default interpreted text role [0.3.10]

title             
    Set the metadata document title 



Interpreted Text Role Quick Reference
=====================================
See <http://docutils.sf.net/docs/ref/rst/roles.html> for full info.

================  ============================================================
Role Name         Description
================  ============================================================
emphasis          Equivalent to *emphasis*
literal           Equivalent to ``literal`` but processes backslash escapes
math              Mathematical notation (input in LaTeX format)
PEP               Reference to a numbered Python Enhancement Proposal
RFC               Reference to a numbered Internet Request For Comments
raw               For non-reST data; cannot be used directly (see docs) [0.3.6]
strong            Equivalent to **strong**
sub               Subscript
sup               Superscript
title             Title reference (book, etc.); standard default role
================  ============================================================

