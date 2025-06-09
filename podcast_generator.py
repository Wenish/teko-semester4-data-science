from gtts import gTTS

# Dein Podcast-Text
text = """
Willkommen zurück zu einer neuen Folge vom Python Quickcast! Heute geht’s um die Übungsserie 3 im Modul Data Science. 
Und das Ziel: Python lernen durch Praxis, mit echten Daten, echten Algorithmen – und ganz nebenbei lernst du auch die Grundlagen der Statistik.

Also: Kopfhörer rein, Kaffee in die Hand, los geht’s!

Aufgabe 1 – Daten generieren & visualisieren
Wir starten mit dem Klassiker: Zufallszahlen erzeugen.

Du verwendest die Methode np.random.normal(loc, scale, size) aus NumPy, einer Python-Bibliothek für mathematische Berechnungen.
Normal bedeutet, dass die Werte normalverteilt sind – das ist eine symmetrische Glockenkurve, bei der die meisten Werte nah am Mittelwert liegen.
loc ist der Mittelwert – also der Durchschnitt aller Werte.
scale ist die Standardabweichung – ein Maß dafür, wie stark die Werte streuen.
size ist die Anzahl der Zufallszahlen – in unserem Fall 1000.

Dann speicherst du diese Werte mit np.savetxt – das schreibt die Zahlen in eine Textdatei.
Später liest du sie wieder ein, rundest mit np.around – das heißt: Du beschränkst die Nachkommastellen auf eine Dezimalstelle.

Und jetzt wird gerechnet:
Minimum – der kleinste Wert,
Maximum – der größte Wert,
Spannweite – also wie breit die Daten gestreut sind,
Mittelwert – Durchschnitt,
Standardabweichung – wie „verstreut“ die Werte sind.

Zum Schluss kommt ein Histogramm mit plt.hist(). Ein Histogramm zeigt, wie häufig bestimmte Wertebereiche vorkommen – eine super Möglichkeit, Verteilungen zu sehen.

Aufgabe 2 – Datenanalyse mit Pandas
Jetzt nutzt du Pandas, eine Bibliothek für Datenanalyse.
Mit pd.read_csv liest du die Textdatei als sogenannte DataFrame ein – das ist wie eine Tabelle mit Zeilen und Spalten.

Der Unterschied zu NumPy: NumPy-Daten sind Arrays. Pandas-Daten sind strukturierter, mit Spaltennamen – ideal für Tabellen.

Dann fügst du eine Spaltenüberschrift hinzu – zum Beispiel: ZufallsZahl.

Mit .head() bekommst du die ersten fünf Zeilen. Mit .describe() gibt’s automatisch Statistik:
count – wie viele Datenpunkte es gibt,
mean – der Mittelwert,
std – Standardabweichung,
min, max – Minimum und Maximum,
25, 50, 75 Prozent – Quartile, sie zeigen, wie die Daten in Viertel aufgeteilt sind.

Ein weiteres Histogramm zeigt die Verteilung – mit der Faustregel für Klassenanzahl: die Wurzel aus der Anzahl Werte.
Dann speicherst du die Daten mit Punkt als Dezimalzeichen und Semikolon als Trennzeichen.

Aufgabe 3 – Sind deine Daten normalverteilt?
Hier kommt der Q-Q-Plot mit sm.qqplot.
Das ist ein Quantil-Quantil-Diagramm. Wenn die Punkte auf einer Linie liegen, ist die Verteilung normal.

Mit np.random.seed(0) stellst du sicher, dass die Zufallszahlen reproduzierbar sind.

Aufgabe 4 – Qualitätskontrolle bei Biscuits
Du bekommst eine Datei mit Gewichten von Biscuit-Packungen.
Zielgewicht: 100 g. Toleranz: ±3 g.

Du prüfst:
Wie viele Packungen gibt es?
Wie groß ist die Spannweite?
Welche sind außerhalb der Toleranz?

Ergebnisse speicherst du in zwei Dateien – eine mit den abweichenden, eine mit den guten Packungen.
Dann erstellst du Histogramme.

Aufgabe 5 – Pivotieren mit Schuhdaten
Du analysierst eine Excel-Datei mit Schuhdaten – mit openpyxl.
Pivoting bedeutet: Du sortierst Daten um. Zum Beispiel: Anzahl Schuhe pro Hersteller, Durchschnittspreis pro Marke.

Aufgabe 6 – Buchstabenhäufigkeit
Du liest Text, zählst Buchstaben – Groß- und Kleinschreibung ignorieren. Sonderzeichen weglassen.
Dann speicherst du das in einer Excel-Datei – mit Häufigkeiten. Und überprüfst: Handelt es sich um deutschen Text?

Aufgabe 7 – Würfeln
Fünf Personen haben gewürfelt.
Ein fairer Würfel zeigt eine Gleichverteilung: jede Augenzahl kommt gleich oft vor.
Wenn nicht – vielleicht ist der Würfel gezinkt?

Säulendiagramme helfen beim Vergleichen.

Das war’s für heute beim Python Quickcast!
Wir haben Statistik und Python vereint. Daten sind mächtig – wenn man weiß, wie man sie liest.

Bis zur nächsten Episode!
"""

# Erzeuge die Sprachdatei mit gTTS
tts = gTTS(text=text, lang='de')

# Speichere die Datei
tts.save("python_quickcast_uebungsserie3.mp3")
print("Podcast wurde gespeichert als: python_quickcast_uebungsserie3.mp3")
