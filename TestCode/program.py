from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd


def autoMateFormFilling():
    try:
        template_path = input("[+] Enter template path: ")
        doc = DocxTemplate(template_path)

        my_name = "xyz"
        my_phone = "+358 10234534"
        my_email = "xyz.xyz@edu.xyz.uk"
        my_address = "xyz 8"
        today_date = datetime.today().strftime("%d %b, %Y")

        my_info = {
            "my_name": my_name,
            "my_phone": my_phone,
            "my_email": my_email,
            "my_address": my_address,
            "today_date": today_date,
        }
        print("[+] FILLING FORM ....")
        doc.render(my_info)
        doc.save("generated_doc.docx")
        print("[+] DONE..")
    except Exception as ex:
        print("[+] SOMETHING WENT WRONG ..", str(ex))

df = pd.read_csv("fake_data.csv")
for index,row in df.iterrows():
    context={
        "my_na"
    }


# autoMateFormFilling()
