---
layout: page
title: Lesson Plans
nav_order: 5
has_children: true
permalink: /lesson-plans
---

This aims to document all of the possible lesson plans, or curriculums that you
could run at a RustBridge event.

<ul class="mt4 f5">
{% for page in site.lesson_plans %}
  <li><a href="{{ page.url }}">{{ page.title }}</a></li>
{% endfor %}
</ul>
