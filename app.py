from flask import Flask, render_template, request, redirect, url_for
from models import db, Employee
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Create table if not exists
with app.app_context():
    db.create_all()

# 🏠 Home - List Employees
@app.route('/')
def list_employees():
    employees = Employee.query.all()
    return render_template('listemp.html', employees=employees)

# ➕ Create Employee
@app.route('/create', methods=['GET', 'POST'])
def create_employee():


    if request.method == 'POST':
        name = request.form['name']
        dept = request.form['department']
        salary = float(request.form['salary'])

        new_emp = Employee(name=name, department=dept, salary=salary)
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('list_employees'))

    return render_template('create.html')

# ✏️ Edit Employee
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.department = request.form['department']
        employee.salary = float(request.form['salary'])

        db.session.commit()
        return redirect(url_for('list_employees'))

    return render_template('edit.html', employee=employee)

# 🗑️ Delete Employee
@app.route('/delete/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('list_employees'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
