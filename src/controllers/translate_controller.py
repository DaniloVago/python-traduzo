from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()

    if request.method == "GET":
        return render_template('index.html',
                               languages=languages,
                               text_to_translate="O que deseja traduzir?",
                               translate_from="pt",
                               translate_to="en",
                               translated="What do you want to translate?"
                               )

    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translated_text = GoogleTranslator(
            source=translate_from,
            target=translate_to
        ).translate(text=text_to_translate)

        history_save = HistoryModel({
            'text_to_translate': text_to_translate,
            'translate_from': translate_from,
            'translate_to': translate_to,
        })

        history_save.save()

        return render_template('index.html',
                               languages=languages,
                               text_to_translate=text_to_translate,
                               translate_from=translate_from,
                               translate_to=translate_to,
                               translated=translated_text,
                               )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()

    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated_text = GoogleTranslator(
        source=translate_from,
        target=translate_to
    ).translate(text=text_to_translate)

    return render_template('index.html',
                           languages=languages,
                           text_to_translate=translated_text,
                           translate_from=translate_to,
                           translate_to=translate_from,
                           translated=text_to_translate,
                           )
