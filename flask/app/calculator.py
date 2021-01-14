from app import app
import os
import sys
from flask import Flask, render_template, url_for, request


# main route
@app.route('/')
def main():
    return render_template('simple_calculator.html')


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
        except:
            note = sys.exc_info()[0]
            color = 'alert-danger'
            return render_template('simple_calculator.html', note=note, color=color)


        return render_template('simple_calculator.html', note=note, color=color)

            