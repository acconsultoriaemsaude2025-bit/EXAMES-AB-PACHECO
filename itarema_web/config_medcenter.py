# =============================================================================
#  ARQUIVO DE CONFIGURAÇÃO DO CLIENTE — MEDCENTER SAÚDE E IMAGEM LTDA
#  Para usar em outro contrato, edite apenas este arquivo.
# =============================================================================

# ── Dados do Município ────────────────────────────────────────────────────────
MUNICIPIO_NOME    = "Itarema"
MUNICIPIO_UF      = "CE"
SECRETARIA_NOME   = "Secretaria Municipal de Saúde"
SISTEMA_SUBTITULO = "Controle de Exames e Consultas"

# ── Dados do Contrato ─────────────────────────────────────────────────────────
CONTRATO_NUM   = "005/2022-SMS"
CONTRATO_EMP   = "MEDCENTER SAÚDE E IMAGEM LTDA"
CONTRATO_VALOR = 2282604.00
CONTRATO_ANO   = 2022

# ── Opções de Justificativa ───────────────────────────────────────────────────
JUSTIFICATIVA_OPCOES = [
    ("DIABÉTICO",             "heart-pulse"),
    ("HIPERTENSO",            "activity"),
    ("GESTANTE",              "person-standing-dress"),
    ("GESTANTE DE ALTO RISCO","exclamation-triangle"),
    ("INTERNADO",             "hospital"),
    ("PÚBLICO GERAL",         "people"),
]

# ── Catálogo de Serviços do Contrato ──────────────────────────────────────────
# Formato: (codigo, descricao, tipo, valor_unitario, quantidade_contratada)
EXAMES_CONTRATO = [
    ("MED-001", "ANGIOTOMAGRAFIA DE ARTÉRIAS CEREBRAIS",        "Tomografia",    650.00,   18),
    ("MED-002", "CONSULTA CIRURGIÃO VASCULAR",                  "Consulta",      350.00,  360),
    ("MED-003", "COLONOSCOPIA",                                 "Endoscopia",    750.00,  240),
    ("MED-004", "DENSITOMETRIA ÓSSEA",                          "Imagem",        115.00,  180),
    ("MED-005", "ECOCARDIOGRAMA COM DOPPLER",                   "Ecocardiografia",260.00, 600),
    ("MED-006", "ELETROENCEFALOGRAMA",                          "Neurologia",    150.00,  240),
    ("MED-007", "ELETROENCEFALOGRAMA COM MAPEAMENTO CEREBRAL",  "Neurologia",    180.00,  120),
    ("MED-008", "CONSULTA ENDOCRINOLOGISTA",                    "Consulta",      350.00,  360),
    ("MED-009", "ENDOSCOPIA",                                   "Endoscopia",    300.00,  720),
    ("MED-010", "ESTUDO URODINÂMICO",                           "Urologia",      400.00,  120),
    ("MED-011", "LARINGOSCOPIA",                                "Otorrino",      270.00,  120),
    ("MED-012", "PAAF DE TIREOIDE GUIADA POR ULTRASSOM",        "Imagem",        350.00,   60),
    ("MED-013", "CONSULTA PNEUMOLOGISTA",                       "Consulta",      350.00,  360),
    ("MED-014", "CONSULTA PROCTOLOGISTA",                       "Consulta",      350.00,  180),
    ("MED-015", "RESSONÂNCIA MAGNÉTICA COM CONTRASTE",          "Ressonância",   550.00,  120),
    ("MED-016", "RESSONÂNCIA MAGNÉTICA SEM CONTRASTE",          "Ressonância",   480.00,  360),
    ("MED-017", "RETOSSIGMOIDOSCOPIA",                          "Endoscopia",    700.00,   36),
    ("MED-018", "CONSULTA REUMATOLOGISTA",                      "Consulta",      350.00,  180),
    ("MED-019", "TOMOGRAFIA COM CONTRASTE",                     "Tomografia",    300.00,  240),
    ("MED-020", "TOMOGRAFIA SEM CONTRASTE",                     "Tomografia",    256.00,  540),
    ("MED-021", "ULTRASSOM GERAL",                              "Ultrassom",      85.00, 3600),
    ("MED-022", "ULTRASSOM GERAL COM DOPPLER",                  "Ultrassom",     173.00,  300),
    ("MED-023", "ULTRASSOM MORFOLÓGICO COM DOPPLER",            "Ultrassom",     303.00,  240),
    ("MED-024", "ULTRASSOM OBSTÉTRICA COM DOPPLER",             "Ultrassom",     173.00,  120),
    ("MED-025", "ULTRASSOM OBSTÉTRICA GERAL",                   "Ultrassom",      85.00, 1200),
    ("MED-026", "UROFLUXOMETRIA",                               "Urologia",      316.00,   24),
]
