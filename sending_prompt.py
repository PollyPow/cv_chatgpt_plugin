import openai
from flask import Flask, redirect, render_template, request, url_for


def openai_completion(cv, jd):
    if request.method == "POST":

        jd = request.form["job description"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(cv, jd),
            temperature=0.6
        )

        return redirect(url_for("get_request", result=response.choices[0].text))

    result = request.args.get("result")
    return result


def generate_prompt(cv, jd):
    return """Suggest an improvement for a CV so that it suits a JD.
            CV: {}
            JD: {}""".format(cv, jd)
