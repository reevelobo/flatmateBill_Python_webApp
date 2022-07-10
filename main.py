from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flatmates_bill import flat

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

        return render_template('bill_form_page.html', result=True, billform=billform, name1=flatmate1.name, amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))


class ResultsPage(MethodView):

     def post(self):
         billform = BillForm(request.form)

         the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
         flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
         flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))


         return render_template('results.html' ,billform=billform ,name1= flatmate1.name, amount1=flatmate1.pays(the_bill,flatmate2),name2=flatmate2.name,amount2=flatmate2.pays(the_bill,flatmate1))

class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page'))
#app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))


app.run(debug=True)