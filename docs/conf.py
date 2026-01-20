# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Інформатика та комп'ютерна техніка"
copyright = "2026, Мартинюк С.В., Мартинюк О.В., Ковдриш В.В."
author = "Мартинюк С.В., Мартинюк О.В., Ковдриш В.В."
release = "2007"
booktype = "Методичні рекомендації"  # або 'custom', якщо використовуєш свій клас
booktitle = project
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


master_doc = "index"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_design",
]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "uk_UA"

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_js_files = ["version-switcher.js"]

smv_current_version = "main"
smv_metadata_path = ""
smv_tag_whitelist = r"^v\d+\.\d+(\.\d+)?$"
smv_branch_whitelist = r"^(main)$"
smv_remote_whitelist = None

html_title = "Методичні рекомендації"
html_theme_options = {
    "icon_links": [
        {
            "name": "завантажити PDF",
            "url": "_static/index.pdf",
            "icon": "fa-solid fa-file-pdf",
        },
    ],
    "switcher": {
        "json_url": "https://volodymyr-kovdrysh.github.io/IKT/_static/switcher.json",
        "version_match": smv_current_version,
    },
    "navbar_end": ["version-switcher", "navbar-icon-links"],
    "primary_sidebar_end": ["version-switcher"],
}


myst_enable_extensions = [
    "deflist",
    "dollarmath",
    "amsmath",
    "colon_fence",
    "attrs_block",
    "attrs_inline",
    "fieldlist",
    "html_image",
]

# нумерація фігур/таблиць/лістингів
numfig = True
# глибина секцій у номері (0 = глобальна нумерація; 1 = усередині розділу і т.д.)
numfig_secnum_depth = 1
# україномовні підписи
numfig_format = {
    "figure": "Мал. %s",
    "table": "Таблиця %s",
    "code-block": "Лістинг %s",
    "section": "Розділ %s",
}


from pathlib import Path

_local = Path(__file__).with_name("conf_latex.py")
if _local.exists():
    exec(_local.read_text(encoding="utf-8"), globals())
