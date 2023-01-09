#!/usr/bin/env python
""" UPNBuddit is a powerful tool for bulk editing of remittance slips.

With its advanced technology and efficient interface,
UPNBuddit makes it easy to quickly and accurately edit large numbers
of remittance slips. Whether you need to make changes to a single field
or update multiple fields at once, UPNBuddit has the tools you need to get
the job done. Its user-friendly interface allows even novice users to make
complex edits with ease, making it the ideal choice for businesses and
organizations that need to process large volumes of remittance slips.
Try UPNBuddit today and streamline your bulk remittance slip editing process!


This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Kristjan Cuznar"
__contact__ = "kristjancuznar0@gmail.com"
__copyright__ = ""
__credits__ = ["Coffee"]
__date__ = "2023/01/07"
__deprecated__ = False
__email__ =  "kristjancuznar0@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

import argparse
import pandas as pd
import os

def main(args):
    print("Verzija: {}".format(__version__))
    try:
        config = pd.read_excel(args.config_path)
    except:
        print("Konfiguracijske datoteke ni mogoce najti.")
        return -1
    try:     
        data = pd.read_excel(args.input_path)
    except:
        print("Vhodne datoteke ni mogoce najti.")
        return -1
    
    nr_members = data.shape[0]
    
    print("Zacetek izvoza.")
    try:
        
        with open(args.output_path, 'w', encoding="utf-16") as f:
            
            # Write heading
            f.write('<?xml version="1.0" encoding="utf-16"?>\n')
            f.write('<ArrayOfUPN xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n')
            
            for i in range(nr_members):
                f.write('  <UPN>\n')
                f.write('    <ID>' + str(i) + '</ID>\n')
                f.write('    <TipDokumenta>Nalog_za_plačilo</TipDokumenta>\n')
                f.write('    <BremeIBAN />\n')
                f.write('    <BremeModel />\n')
                f.write('    <BremeSklic />\n')
                f.write('    <BremeIme>' + data.iloc[i]['Ime'] + ' ' + data.iloc[i]['Priimek'] + '</BremeIme>\n')
                f.write('    <BremeUlica>'+ str(data.iloc[i]['Naslov']) + '</BremeUlica>\n')
                f.write('    <BremeKraj>'+ str(int(data.iloc[i]['Poštna številka'])) + ' ' + data.iloc[i]['Kraj'] + '</BremeKraj>\n')
                f.write('    <DobroIBAN>'+ config['IBAN prejemnika'].values[0] + '</DobroIBAN>\n')
                f.write('    <DobroModel>'+ config['Referenca model'].values[0] + '</DobroModel>\n')
                f.write('    <DobroSklic>'+ config['Referenca sklic'].values[0] + '</DobroSklic>\n')
                f.write('    <DobroIme>' + config['Ime prejemnika'].values[0] + '</DobroIme>\n')
                f.write('    <DobroUlica>' + config['Naslov prejemnika'].values[0] + '</DobroUlica>\n')
                f.write('    <DobroKraj>' + config['Kraj prejemnika'].values[0] + '</DobroKraj>\n')
                f.write('    <Znesek>' + ("%.2f" % round(float(config['Znesek'].values[0]), 2)) + '</Znesek>\n')
                f.write('    <DatumPlacila>' + pd.to_datetime(config['Datum placila'].values[0]).strftime('%d.%m.%Y') + '</DatumPlacila>\n')
                f.write('    <NamenPlacila>' + config['Namen'].values[0] + '</NamenPlacila>\n')
                f.write('    <KodaNamena>' + config['Koda namena'].values[0] + '</KodaNamena>\n')
                f.write('    <RokPlacila>' + pd.to_datetime(config['Rok placila'].values[0]).strftime('%d.%m.%Y') + '</RokPlacila>\n')
                f.write('    <RokPlacilaDni>0</RokPlacilaDni>\n')
                f.write('    <Nujno>' + str((config['Nujno'].values[0] == 'Da')).lower() + '</Nujno>\n')
                f.write('    <BrezZneska>' + str((config['Brez zneska'].values[0] == 'Da')).lower() + '</BrezZneska>\n')
                f.write('    <BrezPlacnika>' + str((config['Brez placnika'].values[0] == 'Da')).lower() + '</BrezPlacnika>\n')
                f.write('    <NatisniQR>' + str((config['QR'].values[0] == 'Da')).lower() + '</NatisniQR>\n')
                f.write('  </UPN>\n')
            
            f.write('</ArrayOfUPN>\n')
            return 0 
    except:
        print("Napaka pri izvozu. Struktura konfiguracijske ali vhodne datoteke ni pravilna.")
        os.remove(args.output_path)
        return -1
        




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Izvoz clanov za UPN')
    parser.add_argument("-i", "--input-path", type=str, default='seznam.xls',
                        help="Input file path (default: %(default)s)")
    parser.add_argument("-o", "--output-path", type=str, default='export.txt',
                        help="Output file path (default: %(default)s)")
    parser.add_argument("-c", "--config-path", type=str, default='config.xls',
                        help="Config file path (default: %(default)s)")
    args = parser.parse_args()

    ret = main(args)
    
    if ret == 0:
        print("Koncano. Hvala za uporabo programa.")
        print("Generiran dokument: {}".format(args.output_path))
        
    else:
        pass
    print("Avtor: {}".format(__author__))
    print("Kontakt: {}".format(__contact__))
