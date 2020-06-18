import math
import os
from datetime import datetime

from app.company.model import CompanyModel
from database import Database

db = Database()


def get_all() -> tuple:
    db.cursor.execute("""SELECT * FROM companies""")
    company_list = db.cursor.fetchall()
    company_list.sort(reverse=True, key=function_for_ranking)
    return company_list


def get_by_id(id: int):
    db.cursor.execute("""SELECT * FROM companies WHERE id = ?""", (id,))
    return db.cursor.fetchone()


def update(id: int, filename: str) -> tuple:
    company: CompanyModel = get_by_id(id)
    file = open(f'archive/upload/{filename}', 'r')
    data: dict = {}
    for linha in file:
        lista = linha.split(";")
        data["invoice"] = int(lista[2])
        data["debit"] = int(lista[3])
    invoice: int = data['invoice'] + company[2]
    debit: int = data['debit'] + company[3]
    score: int = update_score(invoice, debit)
    update_log(company, invoice, debit, score)
    file.close()
    os.replace(f'archive/upload/{filename}', f'archive/upload/{company[1]}.txt')
    db.cursor.execute("""UPDATE companies SET invoice = ?, debit = ?, score = ? 
    WHERE id = ?""", (invoice, debit, score, id))
    db.conn.commit()
    return "Atualização feita com sucesso", 201


def update_score(invoice: int, debit: int) -> int:
    score = 50
    for i in range(invoice):
        score = math.floor(score * (1 + 0.02))
    for i in range(debit):
        score = math.ceil(score - (score * 0.04))

    if score > 100:
        score = 100
    elif score < 1:
        score = 1
    return score


def update_log(company: CompanyModel, invoice: int, debit: int, score: int) -> None:
    file = open('archive/upload/log.txt', 'a')
    current_date = datetime.now()
    file.write(f"{company[0]} ; {company[1]} ; {invoice} ; {debit} ; {score} ; "
               f"{current_date.day}/{current_date.month}/{current_date.year} ; {current_date.strftime('%X')}\n")


def function_for_ranking(company: list) -> int:
    return company[4]
