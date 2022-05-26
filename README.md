# github_to_telegram
Questo progetto è una dimostrazione di come impostare un Webhook per inviare messaggi su un gruppo Telegram.

1) Create un file .env, con questo contenuto:
  TELEGRAM_BOT_TOKEN= Token del Bot Telegram
  CHAT_ID=- Id Della chat Telegram destinataria
  PROJECT_NAME= Nome del progetto in cui state lavorando

Per collegare il nostro server a GitHub, dobbiamo avere un repository. Questo può essere un nuovo repository o uno esistente. Se si vuole creare un nuovo repository, navigare su https://github.new per creare un nuovo repository.

Per impostare i webhook, andare alla scheda Impostazioni del repository e selezionare la sezione Webhook. Premere il pulsante Aggiungi webhook per aggiungere un nuovo webhook. Vi verrà chiesto di inserire la vostra password GitHub.

Una volta fatto, aggiungere l'URL ricevuto da ngrok (non dimenticare di aggiungere /hook come suffisso all'URL), o dall'url hostato, poiché questo è il nostro endpoint per ricevere i webhook. Cambiare il tipo di contenuto in application/json. Quindi, selezionare gli eventi webhook che si desidera ricevere. Nel nostro caso, abbiamo bisogno degli eventi  push. Infine, salvare le modifiche.

