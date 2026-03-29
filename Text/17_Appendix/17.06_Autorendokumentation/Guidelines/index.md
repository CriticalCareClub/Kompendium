---
status: final
---


# Style Guide – MyST-Markdown

Dieser Style-Guide definiert verbindliche Formatierungs- und Strukturregeln für die Erstellung von Inhalten im Projekt.
Ziel ist eine konsistente, lehrbuchartige und technisch saubere Darstellung.

---

# 1. Allgemeine Prinzipien

- Ausgabe erfolgt **immer als Markdown-Code**.
- Stil: präzise, knapp, fachsprachlich korrekt.
- **Jeder Satz beginnt in einer neuen Zeile**.
- Begriffe aus der Überschrift werden im Fließtext **nicht erneut hervorgehoben**.
- Hervorhebungen:
  - *kursiv*: Fachbegriffe, zentrale Konzepte
  - **fett**: nur selektiv für starke Betonung

---

# 2. Überschriftenstruktur

Eine Überschrift besteht immer aus drei zusammengehörigen Elementen:

1. Indexeinträge
2. Label
3. Überschrift

Diese bilden eine **untrennbare Einheit**.

## Reihenfolge

```markdown
:::{index} single: Begriff
:::

(label)=

## Überschrift
```

## Abstand

- **5 Leerzeilen vor jeder Überschriftseinheit** (Index + Label + Überschrift)

---

# 3. Indexierung

- Syntax:
  ```markdown
  :::{index} single: Begriff
  :::
  ```
- Mehrere Einträge erlaubt
- Auch Unterkapitel erhalten eigene Indexeinträge
- Semantische Verknüpfungen möglich:
  ```markdown
  :::{index} single: Oberbegriff; Unterbegriff
  :::
  ```

---

# 4. Labels

- Syntax:
  ```markdown
  (label)=
  ```
- Steht **zwischen Index und Überschrift**
- Wird für Referenzen (`{ref}`) verwendet

---

# 5. Field Lists

## Grundsyntax

```markdown
Begriff
:   Definition
```

## Regeln

- **Keine Leerzeile zwischen Begriff und Definition**
- Einrückung: **genau 4 Spaces**
- Kein Tab-Mix

## Mehrzeilig

```markdown
Begriff
:   Erste Zeile
    Zweite Zeile
```

## Abstand

- **2 Leerzeilen vor und nach jedem Field-List-Block**

---

# 6. Typografie

- Abkürzungen: *Begriff* (*Abk1*, *Abk2*)
- Einheiten konsistent (µl, cm², g/dl)
- Zahlenbereiche mit Gedankenstrich (–)
- „z. B.“ korrekt schreiben

---

# 7. Hervorhebungen

- *kursiv*: Fachbegriffe
- **fett**: selten, nur bei Bedarf
- Keine Wiederholung von Überschriftenbegriffen

---

# 8. Fließtext

- Jeder Satz in neuer Zeile
- Prägnant, ohne Füllwörter
- Klinische Relevanz priorisieren

---

# 9. Ziel

- Konsistenz
- Lesbarkeit
- MyST-/Sphinx-Kompatibilität
