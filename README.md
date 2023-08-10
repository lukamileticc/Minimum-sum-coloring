# Minimum sum coloring :memo:

**Problem bojenja minimalne sume (The Minimum Sum Coloring Problem (MSCP)) je NP-težak problem koji su 1989. godine otkrili Kubicka and Schwenk. Kao široko proučavan problem bojenja grafa (Graph Coloring Problem (GCP)) MSCP se takođe sastoji u dodeljivanju jedne boje svakom ćvoru datog grafa G poštujući poštujući ograničenja susedstva.**


## Opis problema: :wrench:

link: https://www.csc.kth.se/~viggo/wwwcompendium/node16.html

* INSTANCA: Graf $G=\left(V,E\right)$.
* RESENJE: Obojiti graf G, podeliti skup cvorova V u disjunktne podskupove $V_1,V_2,\ldots,V_k$ takve da za svako $V_i$ vazi da nema istu boju kao $V_j (i \ne j$).
* Metrika: Suma bojenja, $\sum_{1\le i\le k}\sum_{v\in V_i} i.$


## Metode koje smo razvili: :dart:
* Tehnika grube sile (Brute force algorithm)
* Lokalna pretraga (Local search)
* Simulirano kaljenje (Simulated annealing)
* Metoda promenljivih okolina (VNS - Variable Neighborhood Search)
* Genetski algoritam (Genetic algorithm)
* Hibridni algoritam (Hybrid - Genetic algorithm + Simulated annealing)

## Dodatno: :selfie:

U direktorijumu **our_graph_instances** se nalaze grafovi koje smo mi generisali, i koji mogu da se testiraju iz svake metode ponaosob(fajla)
ili pokretanjem programa **main.py** koji pokrece svaku metodu redom.

U direktorijumu **graph_instances** se nalaze primeri grafova iz prakse podeljeni u dve grupe. Grupu 1 cine grafovi koji imaju manje od 100 cvorova, a
grupu 2 cine grafovi koji imaju vise od 100 cvorova. Testiranje je izvrseno u programu **instances_test.py** koji redom svaku metodu pokrece nad zadatim grafom(prosledjujemo putanju do tog grafa u dimacs formatu). Svaka metoda se pokrece 5 puta i resenje(grafik) se smesta u direktorijum **graphic_results**
gde se moze videti vreme izvrsavanja tih 5 iteracija, prosecna vrednost koju je metoda dobila kao i najbolje resenje koje je metoda pronasla (predstavljeno u vidu grafika).

U direktorijumu **our_graph_instances** se nalaze dva primera grafa koje smo mi generisali,i to **random_graph.txt** koji ima 50 cvorova, i **small_random_graph.txt** koji ima 12 cvorova. Nad njima je takodje sprovedeno testiranje metoda a rezultati u vodu plot grafika su sacuvani u istom direktorijumu.Pokretanjem programa **main.py** se generise novi random graf od 12 cvorova i pokrecu se sve metode redom nad tim grafom.

Kao detaljan prikaz opisa problema, nacina resavanja istog, detalja implementacije i prikaz razultata ekspermentalnog testiranja procitati 
pdf dokumentaciju: fajl - **Minimum sum coloring.pdf**


## Primer prevodjenja i pokretanja programa iz terminala:
``` 
$ cd ./Minimum-sum-coloring
$ python3 main.py (za pokretanje svih metoda redom nad nasim grafovima)
$ python3 instances_test.py (za pokretanje svih metoda nad grafovima iz prakse)
```
## Ove testove mozete pokrenuti takodje preko pyCharm okruzenja, kako ga instalirati:
```
$ sudo apt-get update 
$ sudo snap install pycharm-community --classic
OR
$ sudo snap install pycharm-professional --classic
OR
$ sudo snap install pycharm-educational --classic
```


## Članovi tima :punch:

- [Marija Papović, 63/2019](https://github.com/Marija63) :girl:
- [Luka Miletić, 91/2017](https://github.com/lukamileticc) :boy:
