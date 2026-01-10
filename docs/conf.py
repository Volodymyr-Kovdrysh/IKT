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

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


master_doc = "index"
extensions = ["myst_parser", "sphinx.ext.autodoc"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "uk_UA"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

html_title = "Методичні рекомендації"

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
