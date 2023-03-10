import os

#DATABASE
DB_CONFIG = {
    "EXPENSE_DB_NAME": os.environ.get("EXPENSE_DB_NAME", "expenses"),
    "EXPENSE_DB_USERNAME": os.environ.get("EXPENSE_DB_USERNAME", "root"),
    "EXPENSE_DB_PASSWORD": os.environ.get("EXPENSE_DB_USERNAME", "password")
}
