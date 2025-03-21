

### **Regole Dettagliate dell'Hexpawn**

**Hexpawn** è un gioco da tavolo strategico astratto basato su una versione ridotta degli scacchi, inventato da Martin Gardner nel 1962 per dimostrare il concetto di apprendimento delle macchine. Il gioco utilizza solo 3 pedine e una piccola scacchiera.

---

## **1\. Materiale Necessario**

* Una **scacchiera** di **3x3 caselle**.  
* **Tre pedine bianche** posizionate sulla prima fila (riga in basso per il Bianco).  
* **Tre pedine nere** posizionate sulla terza fila (riga in alto per il Nero).  
* Un sistema per registrare i diversi pesi associati alle mosse, se si vuole implementare l'apprendimento automatico.

---

## **2\. Obiettivo del Gioco**

Un giocatore vince se:

* Una delle sue pedine raggiunge la riga di fondo dell'avversario.  
* L'avversario non può effettuare mosse valide.  
* Sono state catturate tutte le pedine dell’avversario

---

## **3\. Movimento delle Pedine**

Le pedine si muovono **solo in avanti** (come i pedoni degli scacchi), con le seguenti regole:

* **Mossa avanti semplice**: una pedina può avanzare di **una casella** dritta in avanti se la casella è libera.  
* **Cattura diagonale**: una pedina può catturare una pedina avversaria che si trova diagonalmente **davanti a sinistra o a destra**.  
* **Non esiste la promozione**: le pedine non si trasformano in un pezzo superiore quando raggiungono l'ultima riga conseguendo la vittoria

---

## **4\. Turni di Gioco**

* I giocatori si alternano nei turni, iniziando sempre con il **Bianco**.  
* Ogni turno un giocatore deve eseguire **una mossa valida**.  
* Se un giocatore non ha mosse legali disponibili, **perde la partita**.

---

Hexpawn e AI (apprendimento automatico)

### **Meccanismo di Apprendimento Automatico in Hexpawn**

L'apprendimento automatico in **Hexpawn** si basa sulla rappresentazione fisica del processo di apprendimento di una macchina (realizzata mediante  carte o scatole di fiammiferi) che  acquisisce una sequenza di mosse vincenti, dopo partite ripetute, eliminando progressivamente le strategie che portano alla sconfitta. Il processo di eliminazione avviene penalizzando mosse perdenti e promuovendo quelle vincenti .

---

## **1\. Struttura della Macchina Apprendente**

### **Rappresentazione delle Mosse con Scatole e Fiammiferi**

* **Ogni posizione legale sulla scacchiera** ha una **carta** che rappresenta lo stato del gioco.  
* Sulla  carta è rappresentata una possibile mossa con un colore diverso.   
* Le mosse sono scelte **casualmente** mediante estrazione di una carta col colore corrispondente alla mossa

---

## **2\. Inizio dell’Apprendimento**

* La macchina inizia a giocare in modo completamente casuale.  
* A ogni turno, sceglie **una mossa a caso** dalla carta  corrispondente allo stato attuale: le carte sono contraddistinte dal livello di mossa e dalla mossa giocata dall’avversario   
* La partita si svolge secondo le regole esposte prima  finché uno dei giocatori non vince.

---

## **3\. Apprendimento Attraverso la Penalizzazione**

Dopo ogni partita, il sistema modifica la sua strategia **eliminando le mosse che hanno portato alla sconfitta**:

### **Caso 1: La macchina (Nero) perde**

* Si rivede la sequenza di mosse fatte dalla macchina.  
* **L’ultima mossa della macchina viene penalizzata**, rimuovendo il colore corrispondente dal retro della carta dello stato in cui è stata giocata.  
* Se quella mossa non era l'unica disponibile, non verrà mai più scelta.  
* Se una carta  rimane vuota, significa che **quella posizione porterà sempre alla sconfitta**, e quindi la macchina eviterà di arrivarci.

### **Caso 2: La macchina (Nero) vince**

* La sequenza di mosse che ha portato alla vittoria viene **rafforzata**.  
* Questo può avvenire **aggiungendo identificativi di colori  extra** per quelle mosse, aumentando la probabilità che vengano scelte in futuro.

---

## **4\. Evoluzione dell'Apprendimento**

Dopo diverse partite:

* **Le mosse perdenti saranno state eliminate.**  
* **Le mosse vincenti avranno una maggiore probabilità di essere selezionate.**  
* Alla fine, la macchina avrà una strategia che **garantisce la vittoria o il pareggio**, se il Bianco gioca perfettamente.

---

## **5\. Riferimenti** 

*  [https://medium.com/@pavelanni/machine-learning-with-matchboxes-436e98edd929](https://medium.com/@pavelanni/machine-learning-with-matchboxes-436e98edd929) un articolo che descrive una versione analoga del gioco con scatole di fiammiferi per ogni stato  
* Le istruzioni dettagliate per realizzarlo [https://www.instructables.com/Matchbox-Mini-Chess-Learning-Machine/](https://www.instructables.com/Matchbox-Mini-Chess-Learning-Machine/)  
* La prima rappresentazione di un processo analogico che dimostra l’uso del reinforcement learning per apprendere il gioco del filetto (noughts and crosses o tic-tac-toe) è il MENACE (Matchbox Educable Noughts and Crosses Engine ) [https://en.wikipedia.org/wiki/Matchbox\_Educable\_Noughts\_and\_Crosses\_Engine](https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine)  
* Stand-up Maths [https://youtu.be/R9c-\_neaxeU?si=oLbdkC\_L9Miexrxq](https://youtu.be/R9c-_neaxeU?si=oLbdkC_L9Miexrxq)   
* Gioco online [https://www.mrozilla.cz/lab/hexapawn/](https://www.mrozilla.cz/lab/hexapawn/)   
  