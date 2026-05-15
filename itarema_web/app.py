#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONTROLE DE EXAMES LABORATORIAIS – PREFEITURA MUNICIPAL DE ITAREMA
Sistema Web – Contrato Nº 004/2023-SMS-02
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
import sqlite3, os, io
from datetime import datetime, date
from functools import wraps

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "itarema-saude-2023")

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "itarema_web.db"))
CONTRATO_NUM   = "004/2023-SMS-02"
CONTRATO_EMP   = "DIAGNOSIS / A B PACHECO ME"
CONTRATO_VALOR = 351247.00
CONTRATO_ANO   = 2023

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

# ── Banco de dados ─────────────────────────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS exames (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            descricao TEXT NOT NULL,
            tipo TEXT DEFAULT '',
            valor_unitario REAL DEFAULT 0.0,
            quantidade_contratada INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS autorizacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_autorizacao TEXT,
            data_autorizacao TEXT NOT NULL,
            nome_paciente TEXT NOT NULL,
            cpf_cns TEXT,
            codigo_exame TEXT NOT NULL,
            descricao_exame TEXT,
            quantidade_liberada INTEGER DEFAULT 1,
            valor_unitario REAL DEFAULT 0.0,
            valor_total REAL DEFAULT 0.0,
            responsavel TEXT,
            status TEXT DEFAULT 'AUTORIZADO',
            observacoes TEXT,
            criado_em TEXT DEFAULT (datetime('now','localtime'))
        );
        CREATE TABLE IF NOT EXISTS orcamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ano INTEGER NOT NULL UNIQUE,
            valor REAL DEFAULT 0.0
        );
    """)
    if conn.execute("SELECT COUNT(*) FROM exames").fetchone()[0] == 0:
        conn.executemany(
            "INSERT OR IGNORE INTO exames(codigo,descricao,tipo,valor_unitario,quantidade_contratada) VALUES(?,?,?,?,?)",
            EXAMES_CONTRATO)
    conn.execute("INSERT OR IGNORE INTO orcamento(ano,valor) VALUES(?,?)", (CONTRATO_ANO, CONTRATO_VALOR))
    conn.commit(); conn.close()

# ── Utilitários ────────────────────────────────────────────────────────────────
def fmt_brl(v):
    try:
        s = f"{float(v):,.2f}"
        return "R$ " + s.replace(",","X").replace(".",",").replace("X",".")
    except: return "R$ 0,00"

def parse_data(s):
    try: return datetime.strptime(s.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
    except: return None

def fmt_data(s):
    try: return datetime.strptime(s.strip(), "%Y-%m-%d").strftime("%d/%m/%Y")
    except: return s or ""

app.jinja_env.globals.update(fmt_brl=fmt_brl, fmt_data=fmt_data,
                              CONTRATO_NUM=CONTRATO_NUM, CONTRATO_EMP=CONTRATO_EMP,
                              CONTRATO_VALOR=CONTRATO_VALOR, hoje=date.today)

# ── Rotas ──────────────────────────────────────────────────────────────────────
@app.route("/")
def dashboard():
    ano = CONTRATO_ANO
    db = get_db()
    orc = (db.execute("SELECT valor FROM orcamento WHERE ano=?", (ano,)).fetchone() or [CONTRATO_VALOR])[0]
    gasto = db.execute(
        "SELECT COALESCE(SUM(valor_total),0) FROM autorizacoes WHERE status!='CANCELADO' AND strftime('%Y',data_autorizacao)=?",
        (str(ano),)).fetchone()[0]
    saldo = orc - gasto
    pct   = (gasto/orc*100) if orc > 0 else 0
    total_aut = db.execute("SELECT COUNT(*) FROM autorizacoes WHERE strftime('%Y',data_autorizacao)=?", (str(ano),)).fetchone()[0]

    status_data = {}
    for st in ["AUTORIZADO","PENDENTE","REALIZADO","CANCELADO"]:
        r = db.execute("SELECT COUNT(*), COALESCE(SUM(valor_total),0) FROM autorizacoes WHERE status=? AND strftime('%Y',data_autorizacao)=?", (st, str(ano))).fetchone()
        status_data[st] = {"count": r[0], "valor": r[1]}

    ultimas = db.execute(
        "SELECT * FROM autorizacoes ORDER BY id DESC LIMIT 10").fetchall()

    # Dados para gráfico mensal
    meses_labels, meses_valores = [], []
    for m in range(1, 13):
        v = db.execute(
            "SELECT COALESCE(SUM(valor_total),0) FROM autorizacoes WHERE strftime('%Y',data_autorizacao)=? AND strftime('%m',data_autorizacao)=? AND status!='CANCELADO'",
            (str(ano), f"{m:02d}")).fetchone()[0]
        meses_labels.append(["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"][m-1])
        meses_valores.append(round(v, 2))
    db.close()
    return render_template("dashboard.html", orc=orc, gasto=gasto, saldo=saldo, pct=pct,
                           total_aut=total_aut, status_data=status_data, ultimas=ultimas,
                           ano=ano, meses_labels=meses_labels, meses_valores=meses_valores)

@app.route("/autorizacao", methods=["GET","POST"])
def autorizacao():
    db = get_db()
    exames = db.execute("SELECT codigo, descricao FROM exames ORDER BY descricao").fetchall()
    if request.method == "POST":
        data_db = parse_data(request.form.get("data_autorizacao",""))
        pac  = request.form.get("nome_paciente","").strip()
        cod  = request.form.get("codigo_exame","").strip().upper()
        resp = request.form.get("responsavel","").strip()
        if not data_db: flash("Data inválida. Use DD/MM/AAAA.","danger"); return redirect(url_for("autorizacao"))
        if not pac: flash("Informe o nome do paciente.","danger"); return redirect(url_for("autorizacao"))
        if not cod: flash("Selecione o exame.","danger"); return redirect(url_for("autorizacao"))
        if not resp: flash("Informe o responsável.","danger"); return redirect(url_for("autorizacao"))
        try:
            qtde  = int(request.form.get("quantidade_liberada", 1))
            vu    = float(request.form.get("valor_unitario", 0))
            total = qtde * vu
        except:
            flash("Quantidade ou valor inválido.","danger"); return redirect(url_for("autorizacao"))
        row_e = db.execute("SELECT descricao, quantidade_contratada FROM exames WHERE codigo=?", (cod,)).fetchone()
        desc  = row_e["descricao"] if row_e else ""
        db.execute("""INSERT INTO autorizacoes
            (numero_autorizacao,data_autorizacao,nome_paciente,cpf_cns,codigo_exame,
             descricao_exame,quantidade_liberada,valor_unitario,valor_total,
             responsavel,status,observacoes)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
            (request.form.get("numero_autorizacao","").strip() or None,
             data_db, pac, request.form.get("cpf_cns","").strip() or None,
             cod, desc, qtde, vu, total, resp,
             request.form.get("status","AUTORIZADO"),
             request.form.get("observacoes","").strip() or None))
        db.commit()
        flash(f"✅ Autorização salva! Paciente: {pac} | Exame: {desc} | Valor: {fmt_brl(total)}","success")
        return redirect(url_for("autorizacao"))
    # Saldo financeiro
    orc  = (db.execute("SELECT valor FROM orcamento WHERE ano=?", (CONTRATO_ANO,)).fetchone() or [CONTRATO_VALOR])[0]
    gasto = db.execute("SELECT COALESCE(SUM(valor_total),0) FROM autorizacoes WHERE status!='CANCELADO' AND strftime('%Y',data_autorizacao)=?", (str(CONTRATO_ANO),)).fetchone()[0]
    db.close()
    return render_template("autorizacao.html", exames=exames, orc=orc, gasto=gasto,
                           saldo=orc-gasto, hoje_str=date.today().strftime("%d/%m/%Y"))

@app.route("/api/exame/<codigo>")
def api_exame(codigo):
    db = get_db()
    row = db.execute("SELECT descricao,valor_unitario,quantidade_contratada FROM exames WHERE codigo=?", (codigo.upper(),)).fetchone()
    usado = db.execute("SELECT COALESCE(SUM(quantidade_liberada),0) FROM autorizacoes WHERE codigo_exame=? AND status!='CANCELADO'", (codigo.upper(),)).fetchone()[0]
    db.close()
    if not row: return jsonify({"erro": "Não encontrado"})
    return jsonify({"descricao": row["descricao"], "valor_unitario": row["valor_unitario"],
                    "qtd_contratada": row["quantidade_contratada"], "qtd_usada": int(usado),
                    "saldo": row["quantidade_contratada"] - int(usado)})

@app.route("/historico")
def historico():
    db  = get_db()
    pac = request.args.get("paciente","")
    st  = request.args.get("status","")
    mes = request.args.get("mes","")
    exame = request.args.get("exame","")
    q  = "SELECT * FROM autorizacoes WHERE 1=1"
    p  = []
    if pac:   q += " AND nome_paciente LIKE ?";   p.append(f"%{pac}%")
    if st:    q += " AND status=?";               p.append(st)
    if mes:   q += " AND strftime('%m',data_autorizacao)=?"; p.append(mes.zfill(2))
    if exame: q += " AND (descricao_exame LIKE ? OR codigo_exame LIKE ?)"; p += [f"%{exame}%"]*2
    q += " ORDER BY data_autorizacao DESC, id DESC"
    rows = db.execute(q, p).fetchall()
    total_v = sum(r["valor_total"] for r in rows if r["status"] != "CANCELADO")
    db.close()
    return render_template("historico.html", rows=rows, total_v=total_v,
                           filtros={"paciente":pac,"status":st,"mes":mes,"exame":exame})

@app.route("/historico/excluir/<int:id>", methods=["POST"])
def excluir_aut(id):
    db = get_db(); db.execute("DELETE FROM autorizacoes WHERE id=?", (id,)); db.commit(); db.close()
    flash("Autorização excluída.","warning"); return redirect(url_for("historico"))

@app.route("/historico/editar/<int:id>", methods=["GET","POST"])
def editar_aut(id):
    db = get_db()
    if request.method == "POST":
        data_db = parse_data(request.form.get("data_autorizacao",""))
        if not data_db: flash("Data inválida.","danger"); return redirect(url_for("editar_aut", id=id))
        db.execute("""UPDATE autorizacoes SET numero_autorizacao=?,data_autorizacao=?,
                      nome_paciente=?,cpf_cns=?,responsavel=?,observacoes=?,status=? WHERE id=?""",
            (request.form.get("numero_autorizacao","").strip() or None, data_db,
             request.form.get("nome_paciente","").strip(),
             request.form.get("cpf_cns","").strip() or None,
             request.form.get("responsavel","").strip() or None,
             request.form.get("observacoes","").strip() or None,
             request.form.get("status","AUTORIZADO"), id))
        db.commit(); db.close()
        flash("✅ Autorização atualizada!","success"); return redirect(url_for("historico"))
    row = db.execute("SELECT * FROM autorizacoes WHERE id=?", (id,)).fetchone()
    db.close()
    return render_template("editar.html", row=row)

@app.route("/saldo")
def saldo_exames():
    db = get_db()
    rows = db.execute("""
        SELECT e.codigo, e.descricao, e.tipo, e.valor_unitario, e.quantidade_contratada,
               COALESCE(SUM(CASE WHEN a.status!='CANCELADO' THEN a.quantidade_liberada ELSE 0 END),0) AS usada
        FROM exames e LEFT JOIN autorizacoes a ON a.codigo_exame=e.codigo
        GROUP BY e.codigo ORDER BY e.descricao
    """).fetchall()
    db.close()
    return render_template("saldo.html", rows=rows)

@app.route("/exames", methods=["GET","POST"])
def exames():
    db = get_db()
    if request.method == "POST":
        acao = request.form.get("acao")
        cod  = request.form.get("codigo","").strip().upper()
        desc = request.form.get("descricao","").strip()
        tipo = request.form.get("tipo","").strip()
        try: val = float(request.form.get("valor_unitario","0").replace(",","."))
        except: val = 0.0
        try: qtd = int(request.form.get("quantidade_contratada","0"))
        except: qtd = 0
        if acao == "add":
            try:
                db.execute("INSERT INTO exames(codigo,descricao,tipo,valor_unitario,quantidade_contratada) VALUES(?,?,?,?,?)",(cod,desc,tipo,val,qtd))
                flash(f"✅ Exame '{cod}' adicionado.","success")
            except: flash(f"Código '{cod}' já existe.","danger")
        elif acao == "edit":
            cod_orig = request.form.get("codigo_original","")
            db.execute("UPDATE exames SET codigo=?,descricao=?,tipo=?,valor_unitario=?,quantidade_contratada=? WHERE codigo=?",
                       (cod,desc,tipo,val,qtd,cod_orig))
            flash(f"✅ Exame '{cod}' atualizado.","success")
        elif acao == "del":
            db.execute("DELETE FROM exames WHERE codigo=?", (cod,))
            flash(f"Exame '{cod}' excluído.","warning")
        db.commit()
        return redirect(url_for("exames"))
    rows = db.execute("SELECT * FROM exames ORDER BY codigo").fetchall()
    db.close()
    return render_template("exames.html", rows=rows)

@app.route("/relatorio")
def relatorio():
    ano = int(request.args.get("ano", CONTRATO_ANO))
    db  = get_db()
    orc = (db.execute("SELECT valor FROM orcamento WHERE ano=?", (ano,)).fetchone() or [CONTRATO_VALOR])[0]
    meses_nomes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                   "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    dados = []
    acum = 0.0
    for m, nome in enumerate(meses_nomes, 1):
        q, v = db.execute("""SELECT COUNT(*), COALESCE(SUM(valor_total),0) FROM autorizacoes
            WHERE strftime('%Y',data_autorizacao)=? AND strftime('%m',data_autorizacao)=? AND status!='CANCELADO'""",
            (str(ano), f"{m:02d}")).fetchone()
        acum += v
        dados.append({"mes": nome, "qtd": q, "valor": v, "acumulado": acum,
                      "pct": (v/orc*100) if orc > 0 else 0})
    db.close()
    return render_template("relatorio.html", dados=dados, ano=ano, orc=orc,
                           anos=list(range(2022, 2031)))

@app.route("/orcamento", methods=["POST"])
def set_orcamento():
    try:
        ano = int(request.form.get("ano", CONTRATO_ANO))
        val = float(request.form.get("valor","0").replace(",","."))
        db  = get_db()
        db.execute("INSERT INTO orcamento(ano,valor) VALUES(?,?) ON CONFLICT(ano) DO UPDATE SET valor=excluded.valor", (ano,val))
        db.commit(); db.close()
        flash(f"✅ Orçamento {ano} definido: {fmt_brl(val)}","success")
    except: flash("Erro ao salvar orçamento.","danger")
    return redirect(url_for("dashboard"))

@app.route("/exportar/<int:ano>")
def exportar(ano):
    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill, Alignment
    except ImportError:
        flash("openpyxl não instalado.","danger"); return redirect(url_for("relatorio"))
    db   = get_db()
    rows = db.execute("""SELECT data_autorizacao,numero_autorizacao,nome_paciente,cpf_cns,
                                codigo_exame,descricao_exame,quantidade_liberada,valor_unitario,
                                valor_total,responsavel,status,observacoes
                         FROM autorizacoes WHERE strftime('%Y',data_autorizacao)=?
                         ORDER BY data_autorizacao,id""", (str(ano),)).fetchall()
    db.close()
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = f"Autorizações {ano}"
    hdrs = ["Data","Nº Aut.","Paciente","CPF/CNS","Código","Descrição Exame","Qtde","Val.Unit","Val.Total","Responsável","Status","Obs"]
    for c, h in enumerate(hdrs,1):
        cell = ws.cell(1,c,h)
        cell.font = Font(bold=True,color="FFFFFF",name="Arial")
        cell.fill = PatternFill("solid",fgColor="1F3864")
        cell.alignment = Alignment(horizontal="center")
    for ri, r in enumerate(rows,2):
        vals = [fmt_data(r[0]),r[1] or "",r[2],r[3] or "",r[4],r[5] or "",r[6],r[7],r[8],r[9] or "",r[10] or "",r[11] or ""]
        for ci, v in enumerate(vals,1):
            cell = ws.cell(ri,ci,v)
            if ci in (8,9): cell.number_format = 'R$ #,##0.00'
    buf = io.BytesIO(); wb.save(buf); buf.seek(0)
    return send_file(buf, download_name=f"Itarema_Exames_{ano}.xlsx",
                     as_attachment=True, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# Inicializa o banco sempre que o módulo for carregado (gunicorn ou direto)
init_db()

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
