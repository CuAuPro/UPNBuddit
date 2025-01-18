import pandas as pd
import os
from jinja2 import Environment, FileSystemLoader

def run(args):
    try:
        config = pd.read_excel(args.config_path)
    except:
        print("Konfiguracijske datoteke ni mogoce najti.")
        return -1
    try:     
        data = pd.read_excel(args.input_path)
    except:
        print("Vhodne datoteke ni mogoce najti.")
        return -2
    
    nr_members = data.shape[0]
    print(f"Stevilo vseh: {nr_members}")
    
    if args.only_adults:
        try:
            date_today = pd.Timestamp.now().normalize()
            data['Rojstni dan'] = pd.to_datetime(data['Rojstni dan'])
            data['Age'] = (date_today - data['Rojstni dan']).dt.days / 365.25 
            # Filter the data where the age is greater than or equal to 18
            data = data[data['Age'] >= 18]
            nr_members = data.shape[0]
            print(f"Stevilo vseh starejsih od 18 let: {nr_members}")
        except:
            return -5
            
    encoding = 'utf-16'
    environment = Environment(loader=FileSystemLoader(args.template_path))
    print("Zacetek izvoza.")
    try:
        
        with open(args.output_path, 'w', encoding=encoding) as f:
            template = environment.get_template("header.txt")
            content = template.render(
                encoding=encoding,
            )
            # Write heading
            f.write(content)
            document_type =  config['Tip dokumenta'].values[0].replace(' ','_')
            for i in range(nr_members):
                try:
                    template = environment.get_template("body.txt")
                except:
                    print("Mape s predlogami ni mogoce najti.")
                    return -3
                content = template.render(
                    id = str(i),
                    TipDokumenta = document_type,
                    BremeIme = data.iloc[i]['Ime'] + ' ' + data.iloc[i]['Priimek'],
                    BremeUlica = str(data.iloc[i]['Naslov']),
                    BremeKraj = str(int(data.iloc[i]['Poštna številka'])) + ' ' + data.iloc[i]['Kraj'],
                    DobroIBAN = config['IBAN prejemnika'].values[0],
                    DobroModel = config['Referenca model'].values[0],
                    DobroSklic = str(data.iloc[i]['ID Člana']),
                    DobroIme = config['Ime prejemnika'].values[0],
                    DobroUlica = config['Naslov prejemnika'].values[0],
                    DobroKraj = config['Kraj prejemnika'].values[0],
                    Znesek = ("%.2f" % round(float(config['Znesek'].values[0]), 2)),
                    DatumPlacila = pd.to_datetime(config['Datum placila'].values[0]).strftime('%d.%m.%Y'),
                    NamenPlacila = config['Namen'].values[0],
                    KodaNamena =  config['Koda namena'].values[0],
                    RokPlacila = pd.to_datetime(config['Rok placila'].values[0]).strftime('%d.%m.%Y'),
                    RokPlacilaDni = "0",
                    Nujno = str((config['Nujno'].values[0].lower() == 'da')).lower(),
                    BrezZneska = str((config['Brez zneska'].values[0].lower() == 'da')).lower(),
                    BrezPlacnika = str((config['Brez placnika'].values[0].lower() == 'da')).lower(),
                    NatisniQR = str((config['QR'].values[0].lower() == 'da')).lower(),
                )
                f.write(content)
                
            template = environment.get_template("footer.txt")
            content = template.render()
            # Write footer
            f.write(content)
            return 0 
    except:
        print("Napaka pri izvozu. Struktura konfiguracijske ali vhodne datoteke ni pravilna.")
        os.remove(args.output_path)
        return -4