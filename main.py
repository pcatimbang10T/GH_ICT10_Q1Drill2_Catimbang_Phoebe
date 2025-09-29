from pyscript import display, document

def sample_function(e):
    data1 = document.getElementById('input1').value
    data2 = document.getElementById('input2').value
    data3 = document.getElementById('input3').value

    document.querySelector("#output").innerText = ""

    message = f"""Student Profile
Name   : {data1}
Age    : {data2}
School : {data3}

Notes:
{data1} is {data2} years old and studies at {data3}. This information was gathered through input fields and displayed using a multiline string in Python via PyScript.
"""
    display(message, target="output")
