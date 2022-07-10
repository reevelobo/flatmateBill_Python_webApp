import webbrowser
import os
from fpdf import FPDF
from filestack import Client

class PdfReport:
    """ Creates a pdf file that contains data about the faltmates such as their names, their due amounts and the period of hte bill  """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt' , format='A4')
        pdf.add_page()

        """Adding Title To the PDF file"""
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        """ Adding Billing period"""
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0 )
        pdf.cell(w=150, h=20, txt=str(round(flatmate1.pays(bill, flatmate2),2)), border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0 )
        pdf.cell(w=150, h=20, txt=str(round(flatmate2.pays(bill, flatmate1),2)), border=0, ln=1)

        path=f'files/{self.filename}'
        pdf.output(path)
        #os.chdir('files')
        #webbrowser.open(self.filename)

        client = Client('AoiR0ZinVQz6zrkDEaCCtz')
        new_filelink = client.upload(filepath=path)
        pdf_url = new_filelink.url
        print(pdf_url)
