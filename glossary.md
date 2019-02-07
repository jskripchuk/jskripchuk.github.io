---
layout: page
title: Glossary
permalink: /glossary
weight: 5
sitemap:
  priority: 0.9
glossary:
  - term: minicomp
    meaning: "a loose umbrella organization for minimal computing projects, workflows, tools, experiments, and more; inspired by the global outlook :: digital humanities minimal computing working group."
    references: "[DO::DH](http://go-dh.github.io/mincomp/), [Minicomp](https://github.com/minicomp)"
  - term: static site
    meaning: "websites comprised of flat, 'static' files (e.g. html, css, and js) that do not require any web programming or database design."
    references: "[Wikipedia](https://en.wikipedia.org/wiki/Static_web_page)"
  - term: git
    meaning:
    references:
  - term: github
    meaning:
    references:
  - term: github pages
    meaning:
    references:
  - term: travis
    meaning:
    references:
  - term: ruby gem
    meaning:
    references:

---
# Glossary
<br>

| term | use | reference |
|:-----|:--------|:--------|
{% for item in page.glossary %} | __{{ item.term }}__ | {{ item.meaning }} | {{ item.references }} |
{% endfor %}
