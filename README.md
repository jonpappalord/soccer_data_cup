Materiale per i partecipanti dell'evento Soccer Data Cup.

Lo strumento che utilizzeremo per l'analisi dei dati è Jupyter, per seguire blocchi di codice python e visualizzare e creare plot.

Per installare jupyter e tutte le librerie necessarie:

- Windows: installare Anaconda, che contiene jupyter e le librerie python più comuni. https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe
installare quindi plotly, la libreria per la creazione e visualizzazione dei plot dentro jupyter. Per l'isntallazione di plotly, basta aprire il terminale e digitare il comando: pip install plotly

- Linux: scaricare ed eseguire l'installer da https://www.anaconda.com/distribution/#linux

installare quindi plotly tramite il comando da terminale: sudo pip install plotly (verrà richiesta la password dell'utente amministratore di sistema)

I dati che verranno forniti, per ogni partita dei quarti di finale, sono di due tipi:

- match events: dati forniti da wyscout, al termine della loro analisi video. Ogni evento legato alla palla viene registrato e fornito in formato json. La documentazione degli eventi forniti è fornita qui: https://apidocs.wyscout.com/

- tracking data: i giocatori indosseranno una pettorina, con cui vengono registrati i dati di posizionamento di ogni giocatore. Da questi dati si calcolano le distanze percorse, le velocità medie, le accelerazioni, l'occupazione del campo e la struttura della squadra.

Contenuti delle cartelle:

python_training: notebook con un un'introduzione a python e pandas, incluso un dataset di esempio su cui eseguire i primi test. Pandas è una libreria molto utile per la manipolazione/aggregazione rapida dei dati. Risorse ulteriori: video-tutorial jupyter notebook https://www.youtube.com/watch?v=KDA6MKh03bw

python-abc https://pythonitalia.github.io/python-abc/

pandas tutorial https://pandas.pydata.org/pandas-docs/version/0.22/tutorials.html

- match_events: notebook con alcuni esempi di analisi dei dati di una partita. .

- tracking_data: notebook con esempi di visualizzazione e aggregazione dei dati di tracking. 

I dati da utilizzare sono forniti nella cartella condivisa su drive. Nella cartella troverete le stesse due cartelle (match_events e tracking_data), con dentro una sottocartella example_match contenente i dati relativi. Dovrete copiare la cartella example_match all'interno della relativa cartella madre.
I dati delle partite del torneo vi verranno forniti allo stesso modo, tramite la stessa cartella su drive.
