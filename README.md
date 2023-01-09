# UPNBuddit
UPNBuddit je zmogljivo orodje za množično urejanje seznama plačnikov za uvoz v orodje [IzpisUPNQR](https://www.zbs-giz.si/placilni-promet/).

## Navodila za uporabo
Opomba: Vsi dokumenti (`seznam.xls`, `config.xls` ter generiran `export.txt`) se privzeto nahajajo v korenski mapi projekta (`UPNBuddit/`).

### Predpriprava

1. V Excelovo tabelo `seznam.xls` vnesemo seznam članov/plačnikov.

![Konfiguracija](/docs/img/seznam.png)*: Primer izseka sintetičnih podatkov.*
    
2. V Excelovo tabelo `config.xls` vnesemo konfiguracijo UPN.

![Konfiguracija](/docs/img/config.png)*: Primer konfiguracije UPN.*

### Navodila za uporabo programa

#### Preko terminala

Namestimo ustrezne dodatne programske module:

```bash
pip install -r requirements.txt
```

##### Uporaba:
```bash
usage: python .\main.py [-h] [-i INPUT_PATH] [-o OUTPUT_PATH] [-c CONFIG_PATH]
```
##### Argumenti

|short|long|default|help|
| :--- | :--- | :--- | :--- |
|`-h`|`--help`||show this help message and exit|
|`-i`|`--input-path`|`seznam.xls`|Input file path.|
|`-o`|`--output-path`|`export.txt`|Output file path.|
|`-c`|`--config-path`|`config.xls`|Config file path.|




### Uvoz v orodje [IzpisUPNQR](https://www.zbs-giz.si/placilni-promet/)

1. Odpremo program `IzpisUPNQR`.

2. Ustvarjanje nove mape.

![Uvoz v orodje IzpisUPNQR](/docs/img/IzvozUPNQR_1.png)*: Ustvarjanje nove mape.*

    2.1 Izberemo gumb Dodaj.

    2.2 Vpišemo ime mape.

    3.2 Izberemo gumb shrani.

3. Uvoz podatkov.

![Uvoz v orodje IzpisUPNQR](/docs/img/IzvozUPNQR_2.png)*: Uvoz podatkov.*

    3.1 Izberemo gumb Uvoz.

    3.2 Vpišemo ustrezni dokument, ki smo ga generirali s programom `UPNBuddit`.
    
    3.2 Izberemo gumb Odpri.

Če smo pravilno sledili navodilom, nas program obvesti, da so bili vnosi pravilno uvoženi.

## Kontakt

Kristjan Cuznar - [LinkedIn](https://www.linkedin.com/in/kristjan-cuznar/) - kristjancuznar0@gmail.com

Link projekta: [https://github.com/CuAuPro/UPNBuddit)

<p align="right">(<a href="#top">Na vrh</a>)</p>

