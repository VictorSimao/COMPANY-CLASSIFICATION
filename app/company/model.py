class CompanyModel:
    def __init__(self, id: int, name: str, invoice: int, debit: int, score: int):
        self.id = id
        self.name = name
        self.invoice = invoice
        self.debit = debit
        self.score = score

    def __str__(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'invoice': self.invoice,
            'debit': self.debit,
            'score': self.score
        }
