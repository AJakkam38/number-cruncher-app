from app import app
import sys
import time
from flask import Flask, render_template, url_for, request
import pymysql


# Connect to the database
connection = pymysql.connect(port=3306,
                             host='db',
                             user='jakkam',
                             password='password',
                             db='calculations',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# Recent 10 calculations from db
def get_calculations():
    data = ''
    with connection.cursor() as cursor:
        calculations = cursor.execute('SELECT * FROM executions ORDER BY id DESC LIMIT 10')
        if calculations > 0:
            data = cursor.fetchall()
        connection.close()
        return data

# main route
@app.route('/')
def main():
    while True:
        return render_template('simple_calculator.html', results=get_calculations())
        time.sleep(5)

# calculations route        
@app.route("/calculation_result", methods=['GET', 'POST'])
def calculation_result():
    if request.method == 'POST':
        details = request.form
        first_number = int(details['firstNumber'])
        operator = details['operation']
        second_number = int(details['secondNumber'])
        note = ''
        color = 'alert-success'

        try:
            if operator == 'addition':
                result = first_number + second_number
                note = f'{first_number} + {second_number} = {result}'
            elif operator == 'subtract':
                result = first_number - second_number
                note = f'{first_number} - {second_number} = {result}'
            elif operator == 'multiply':
                result = first_number * second_number
                note = f'{first_number} * {second_number} = {result}'
            elif operator == 'divide':
                result = first_number / second_number
                note = f'{first_number} / {second_number} = {result}'
            
            with connection.cursor() as cursor:
                sql_query = f'INSERT INTO executions(first_num, operator, second_num, result) VALUES ({first_number}, {operator}, {second_number}, {result})'
                cursor.execute(sql_query)
                connection.commit()
                connection.close()
        except:
            note = sys.exc_info()[0]
            color = 'alert-danger'
            return render_template('simple_calculator.html', note=note, color=color, results=get_calculations())

        while True:
            return render_template('simple_calculator.html', note=note, color=color, results=get_calculations())
            time.sleep(5)
            