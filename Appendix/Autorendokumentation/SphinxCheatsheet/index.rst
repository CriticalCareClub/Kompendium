
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

Tabelle mit Raster:
-------------------

.. code-block:: none
   
  +--------------------------------+-----------------------------------+
  | Paragraphs are flush-left,     | Literal block, preceded by "::":: |
  | separated by blank lines.      |                                   |
  |                                |     Indented                      |
  |     Block quotes are indented. |                                   |
  +--------------------------------+ or::                              |
  | >>> print 'Doctest block'      |                                   |
  | Doctest block                  | > Quoted                          |
  +--------------------------------+-----------------------------------+
  | | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
  | |     Useful for addresses, verse, and adornment-free lists; long  |
  |       lines can be wrapped with continuation lines.                |
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

