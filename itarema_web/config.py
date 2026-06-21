# =============================================================================
#  ARQUIVO DE CONFIGURAÇÃO DO CLIENTE
#  Para replicar para outro contrato/município, edite apenas este arquivo.
#  NÃO é necessário mexer no app.py
# =============================================================================

# ── Dados do Município ────────────────────────────────────────────────────────
MUNICIPIO_NOME    = "Itarema"
MUNICIPIO_UF      = "CE"
SECRETARIA_NOME   = "Secretaria Municipal de Saúde"
SISTEMA_SUBTITULO = "Controle de Exames Lab."

# ── Dados do Contrato ─────────────────────────────────────────────────────────
CONTRATO_NUM   = "004/2023-SMS-02"
CONTRATO_EMP   = "DIAGNOSIS / A B PACHECO ME"
CONTRATO_VALOR = 351247.00
CONTRATO_ANO   = 2023

# Vigência do contrato (assinatura original + aditivos de renovação).
# Atualize CONTRATO_VENCIMENTO sempre que houver um novo termo aditivo.
CONTRATO_INICIO     = "2024-02-01"
CONTRATO_VENCIMENTO = "2026-12-31"

# ── Opções de Justificativa ───────────────────────────────────────────────────
# Personalize as opções de justificativa para cada contrato/cliente
JUSTIFICATIVA_OPCOES = [
    ("DIABÉTICO",             "heart-pulse"),
    ("HIPERTENSO",            "activity"),
    ("GESTANTE",              "person-standing-dress"),
    ("GESTANTE DE ALTO RISCO","exclamation-triangle"),
    ("INTERNADO",             "hospital"),
    ("PÚBLICO GERAL",         "people"),
]

# ── Catálogo de Exames do Contrato ────────────────────────────────────────────
# Formato: (codigo_sigtap, descricao, tipo, valor_unitario, quantidade_contratada)
EXAMES_CONTRATO = [
    ("020208001-3","ANTIBIOGRAMA","Microbiologia",35.00,175),
    ("020203096-2","ANTIGENO CARCINOEMBRIONARIO - CEA","Oncológico",32.00,50),
    ("020205002-5","CLEARANCE DE CREATININA","Bioquímica",24.00,30),
    ("020203001-6","CONTAGEM DE RETICULOCITOS","Hematologia",248.50,10),
    ("020203002-4","CONTAGEM DE LEUCOCITOS/ERITROCITOS","Hematologia",164.00,10),
    ("020203003-2","CONTAGEM DE LEUCOCITOS TOTAIS","Hematologia",164.00,10),
    ("020202003-7","CONTAGEM DE LEUCOCITOS","Hematologia",18.00,25),
    ("020208008-0","CULTURA DE BACTERIAS","Microbiologia",30.00,175),
    ("020201004-0","CURVA GLICEMICA (02 DOSAGENS)","Bioquímica",32.00,100),
    ("020206001-2","INDICE DE TIROXINA LIVRE (T4 LIVRE INDEX)","Hormonal",15.00,100),
    ("020206002-0","DOSAGEM DE SOMATOMEDINA (IGF-1)","Hormonal",119.00,50),
    ("020208003-9","DOSAGEM DE T3 REVERSO","Hormonal",150.00,100),
    ("020203121-7","DOSAGEM DE ANTIGENO CA 19-9","Oncológico",32.00,30),
    ("020206004-7","DOSAGEM DE 17-ALFA-HIDROXIPROGESTERONA","Hormonal",59.60,25),
    ("020201076-7","DOSAGEM DE 25-OXI VITAMINA D","Bioquímica",78.30,100),
    ("020207005-0","DOSAGEM DE ACIDO URICO (URINA)","Bioquímica",67.30,15),
    ("020203009-1","DOSAGEM DE ALFA-1 PROTEINA","Bioquímica",30.00,15),
    ("020203010-5","DOSAGEM DE ANTIGENO PROSTATICO ESPECIFICO (PSA)","Oncológico",32.00,500),
    ("020201022-8","DOSAGEM DE CALCIO IONIZAVEL","Bioquímica",13.00,25),
    ("020201026-0","DOSAGEM DE CLORETO","Bioquímica",15.00,15),
    ("020203012-1","DOSAGEM DE COMPLEMENTO C3","Imunologia",30.00,15),
    ("020203019-0","DOSAGEM DE COMPLEMENTO C4","Imunologia",32.00,15),
    ("020206013-6","DOSAGEM DE CORTISOL","Hormonal",30.00,50),
    ("020206016-0","DOSAGEM DE ESTRADIOL","Hormonal",23.00,30),
    ("020201038-4","DOSAGEM DE FERRITINA","Bioquímica",32.00,50),
    ("020201039-2","DOSAGEM DE FERRO","Bioquímica",17.00,50),
    ("020202026-0","DOSAGEM DE FIBRINOGENIO","Coagulação",35.30,25),
    ("020206021-7","DOSAGEM DE GONADOTROFINA CORIONICA HUMANA (BETA HCG)","Hormonal",42.30,15),
    ("020201050-3","DOSAGEM DE HEMOGLOBINA GLICOLISADA (HbA1c)","Bioquímica",25.00,2000),
    ("020206023-3","DOSAGEM DE HORMONIO FOLICULO-ESTIMULANTE (FSH)","Hormonal",21.80,140),
    ("020206024-4","DOSAGEM DE HORMONIO LUTEINIZANTE (LH)","Hormonal",21.80,100),
    ("020206025-0","DOSAGEM DE HORMONIO TIREOESTIMULANTE (TSH)","Hormonal",13.00,288),
    ("020203015-6","DOSAGEM DE IMUNOGLOBULINA A (IGA)","Imunologia",36.00,25),
    ("020203016-4","DOSAGEM DE IMUNOGLOBULINA E (IGE)","Imunologia",31.00,25),
    ("020203017-2","DOSAGEM DE IMUNOGLOBULINA G (IGG)","Imunologia",33.00,25),
    ("020203018-0","DOSAGEM DE IMUNOGLOBULINA M (IGM)","Imunologia",33.00,25),
    ("020206026-8","DOSAGEM DE INSULINA","Hormonal",45.00,25),
    ("020201053-8","DOSAGEM DE LACTATO","Bioquímica",30.00,25),
    ("020207025-5","DOSAGEM DE LITIO","Bioquímica",28.00,30),
    ("020201056-2","DOSAGEM DE MAGNESIO","Bioquímica",19.00,50),
    ("020205009-2","DOSAGEM DE MICROALBUMINA NA URINA","Urinálise",38.30,50),
    ("020206027-6","DOSAGEM DE PARATORMONIO (PTH)","Hormonal",53.60,25),
    ("020201060-0","DOSAGEM DE POTASSIO","Bioquímica",13.00,125),
    ("020206030-6","DOSAGEM DE PROLACTINA","Hormonal",23.00,50),
    ("020205011-4","DOSAGEM DE PROTEINAS URINA 24 HORAS","Urinálise",17.00,150),
    ("020201062-7","DOSAGEM DE PROTEINAS TOTAL E FRACOES","Bioquímica",27.00,35),
    ("020201063-5","DOSAGEM DE SODIO","Bioquímica",12.00,100),
    ("020206038-1","DOSAGEM DE TIROXINA T4 LIVRE","Hormonal",15.00,288),
    ("020206037-3","DOSAGEM DE TIROXINA T4 TOTAL","Hormonal",15.00,120),
    ("020201066-0","DOSAGEM DE TRANSFERRINA","Bioquímica",38.00,50),
    ("020206039-0","DOSAGEM DE TRIIODOTIRONINA T3","Hormonal",14.00,250),
    ("020201070-8","DOSAGEM DE VITAMINA B12","Bioquímica",59.60,100),
    ("020201071-6","ELETROFORESE DE HEMOGLOBINA","Hematologia",89.60,25),
    ("020201072-4","ELETROFORESE DE PROTEINAS","Bioquímica",52.00,25),
    ("020302003-0","EXAME ANATOMO-PATOLOGICO (BIOPSIA/CONGELAMENTO)","Anatomopatológico",175.00,150),
    ("020301001-9","PAPANICOLAU - CITOPATOLOGICO","Citopatológico",42.00,1500),
    ("020203097-0","PESQUISA DE HBSAG (HEPATITE B - ANTIGENO)","Sorologia",22.00,350),
    ("020203027-0","PESQUISA DE ANTICORPOS ANTIDNA","Imunologia",74.00,15),
    ("020203030-0","PESQUISA DE ANTICORPOS ANTI-HIV-1+HIV-2 (ELISA)","Sorologia",45.00,250),
    ("020203031-8","PESQUISA DE ANTICORPOS ANTI-HTLV-1+HTLV-2","Sorologia",90.00,250),
    ("020203059-8","PESQUISA DE ANTICORPOS ANTINUCLEO (FAN)","Imunologia",32.00,50),
    ("020203063-6","PESQUISA DE ANTI-HBS (HEPATITE B)","Sorologia",37.00,15),
    ("020203064-4","PESQUISA DE ANTI-HBE (HEPATITE B)","Sorologia",46.30,15),
    ("020203067-9","PESQUISA DE ANTI-HCV (HEPATITE C)","Sorologia",52.00,25),
    ("020203073-3","PESQUISA DE ANTICORPOS CONTRA VIRUS EPSTEIN-BARR","Sorologia",20.00,15),
    ("020203074-1","PESQUISA DE ANTICORPOS IGG ANTICITOMEGALOVIRUS","Sorologia",20.00,100),
    ("020203076-8","PESQUISA DE ANTICORPOS IGG ANTITOXOPLASMA","Sorologia",19.00,500),
    ("020203081-4","PESQUISA DE ANTICORPOS IGG CONTRA VIRUS DA RUBEOLA","Sorologia",19.00,250),
    ("020203078-4","PESQUISA DE ANTI-HBC TOTAL (HEPATITE B)","Sorologia",40.00,25),
    ("020203085-7","PESQUISA DE ANTICORPOS IGM ANTICITOMEGALOVIRUS","Sorologia",20.00,100),
    ("020203087-3","PESQUISA DE ANTICORPOS IGM ANTITOXOPLASMA","Sorologia",19.00,240),
    ("020203092-0","PESQUISA DE ANTICORPOS IGM CONTRA VIRUS DA RUBEOLA","Sorologia",23.00,250),
    ("020203102-0","PESQUISA DE HIV-1 POR IMUNOFLUORESCENCIA","Sorologia",60.00,25),
    ("020203103-9","PESQUISA DE IGE ALERGENO-ESPECIFICA","Imunologia",63.00,35),
    ("020204014-3","PESQUISA DE SANGUE OCULTO NAS FEZES","Parasitologia",25.00,25),
    ("020203112-8","TESTE FTA-ABS IGG (SIFILIS)","Sorologia",53.00,25),
    ("020203113-6","TESTE FTA-ABS IGM (SIFILIS)","Sorologia",45.00,25),
]
