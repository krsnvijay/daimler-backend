import pandas as pd


def test(filename):
    xl = pd.read_excel(open("../Book1.xlsx", "rb"), sheet_name="Dataset")
# df = xl.parse("Dataset")

# parsed = pd.ExcelFile.parse(xl, "Dataset")

# print parsed.columns

<<<<<<< 10a05143c46cc61ca484db25d2d2865ee41a5417
print(handle_uploaded_file())
=======
>>>>>>> Added records to the db Manually
