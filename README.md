# BDEA_MapReduce-LambdArchitecture
Das Ziel dieser Übung ist die Entwicklung einer auf Lambda-Architektur basierenden Applikation zur Erstellung von TagClouds, die 
folgende Funktionalitäten unterstützen sollte:

- Upload von Text-Dateien über eine Web-Schnittstelle und Speicherung im Dateisystem (hier wurde das HDFS verwendet)
- Direkte Erzeugung einer TagCloud pro hochgeladener Datei
- Auswahl einer TagCloud aus einer Liste aller hochgeladenen Dateien und Anzeige der TagCloud im Browser
- Per Hand(=Klick) auslösbarer M/R-WordCount, der eine normalisierte TagCloud für den gesamten Dokumentenbestand erzeugt
- Erzeugung einer normaliserten TagCloud für ein Dokument

