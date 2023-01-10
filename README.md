# UPNBuddit
**UPNBuddit** je zmogljivo orodje za množično urejanje seznama plačnikov za uvoz v orodje [IzpisUPNQR](https://www.zbs-giz.si/placilni-promet/).

Orodje za izpis UPN obrazcev s QR kodami [IzpisUPNQR](https://www.zbs-giz.si/placilni-promet/) je brezplačna aplikacija Združenja bank ki pomaga pri generiranju UPN obrazcev.

Omenjena aplikacija pa ne omogoča množičnega urejanja ter vnosa seznama plačnikov, kar je pri večjih količinah izpisov UPN problematično in časovno potratno.

V takšnem primeru lahko seznam plačnikov in konfiguracijo UPN vnesete v Excelovi datoteki ter z aplikacijo UPNBuddit podatke prevedete v ustrezen format za uvoz v orodje [IzpisUPNQR](https://www.zbs-giz.si/placilni-promet/).


## Navodila za uporabo
Opomba: Vsi dokumenti (`seznam.xls`, `config.xls` ter generiran `export.txt`) se privzeto nahajajo v korenski mapi projekta (`UPNBuddit/`).

### Namestitev grafičnega vmesnika

Grafični vmesnik se lahko brezplačno prenese [tukaj](https://github.com/CuAuPro/UPNBuddit/releases/latest). Potrebno je prenesti `UPNBuddit.zip` in ga na računalniku odpakirati (angl. ''unzip'').

### Predpriprava

1. V Excelovo tabelo `seznam.xls` vnesemo seznam članov/plačnikov.

| ![Konfiguracija](/docs/img/seznam.png) |
|:--:| 
| *Primer izseka sintetičnih podatkov.* |
    
2. V Excelovo tabelo `config.xls` vnesemo konfiguracijo UPN.

| ![Konfiguracija](/docs/img/config.png) |
|:--:| 
| *Primer konfiguracije UPN.* |


### Navodila za uporabo programa

Obstajata dve možnosti uporabe programa:
 - [a) Preko terminala](#terminal).
 - [b) Preko grafičnega vmesnika](#gui).

#### a) Preko terminala<a id='terminal'></a>

Prenesemo projekt in ga razširimo v mapo, nato namestimo ustrezne dodatne programske module:

```bash
pip install -r requirements.txt
```

##### Uporaba
```bash
usage: python .\main.py [-h] [-m] [-t TEMPLATE_PATH] [-i INPUT_PATH] [-o OUTPUT_PATH] [-c CONFIG_PATH]
```
##### Argumenti

|short|long|default|help|
| :--- | :--- | :--- | :--- |
|`-h`|`--help`||show this help message and exit|
|`-m`|`--manual-mode`||Tool mode (default: %(default)s)|
|`-t`|`--template-path`|`templates/`|Template folder path (default: %(default)s)|
|`-i`|`--input-path`|`seznam.xls`|Input file path (default: %(default)s)|
|`-o`|`--output-path`|`export.txt`|Output file path (default: %(default)s)|
|`-c`|`--config-path`|`config.xls`|Config file path (default: %(default)s)|


#### b) Preko grafičnega vmesnika <a id='gui'></a>

**Grafični vmesnik se zažene tako, da se odpre mapo, kjer je razširjen ter požene datoteko `launch.bat`**


Izgled grafičnega vmesnika je prikazan na spodnji sliki.
| ![GUI](/docs/img/gui_1.png) |
|:--:| 
| *Grafični vmesnik.* |

1. Pritisnemo na gumb Uvoz konfiguracije in izberemo datoteko `config.xls`. Izberemo Odpri.

| ![Konfiguracija](/docs/img/gui_config.png) |
|:--:| 
| *Izbira konfiguracije.* |
    
2. Pritisnemo na gumb Uvoz seznama in izberemo datoteko `seznam.xls`. Izberemo Odpri.

| ![Konfiguracija](/docs/img/gui_config.png) |
|:--:| 
| *Izbira seznama.* |

3. Pritisnemo na gumb Uvoz predlog in izberemo mapo, kjer se nahajajo predloge `templates/`. Izberemo Izberite mapo.

| ![Konfiguracija](/docs/img/gui_templates.png) |
|:--:| 
| *Izbira mape predlog.* |

4. Pritisnemo na gumb Uvoz seznama in izberemo poljubno ime izhodne datoteke s končnico `.txt`, npr. `export.txt`. Izberemo Shrani.

| ![Konfiguracija](/docs/img/gui_output_select.png) |
|:--:| 
| *Izbira izhodne datoteke.* |

5. Pritisnemo na gumb START. Če smo pravilno sledili navodilom, nas program obvesti o končanju in pot do generirane daoteke.

| ![Konfiguracija](/docs/img/gui_done.png) |
|:--:| 
| *Končni izpis.* |

### Uvoz v orodje [IzpisUPNQR](https://www.zbs-giz.si/placilni-promet/)

1. Odpremo program `IzpisUPNQR`.

2. Ustvarjanje nove mape.

| ![Uvoz v orodje IzpisUPNQR](/docs/img/IzvozUPNQR_1.png) |
|:--:| 
| *Ustvarjanje nove mape.* |


    2.1 Izberemo gumb Dodaj.

    2.2 Vpišemo ime mape.

    2.3 Izberemo gumb shrani.

3. Uvoz podatkov.

| ![Uvoz v orodje IzpisUPNQR](/docs/img/IzvozUPNQR_2.png) |
|:--:| 
| *Uvoz podatkov.* |


    3.1 Izberemo gumb Uvoz.

    3.2 Vpišemo ustrezni dokument, ki smo ga generirali s programom `UPNBuddit`.
    
    3.3 Izberemo gumb Odpri.

Če smo pravilno sledili navodilom, nas program obvesti, da so bili vnosi pravilno uvoženi.

## Kontakt

Kristjan Cuznar - [LinkedIn](https://www.linkedin.com/in/kristjan-cuznar/) - kristjancuznar0@gmail.com

Link projekta: [https://github.com/CuAuPro/UPNBuddit)

<p align="right">(<a href="#top">Na vrh</a>)</p>

