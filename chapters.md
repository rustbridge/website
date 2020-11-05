---
layout: page
title: RustBridge Chapters
nav_order: 2
permalink: /chapters
---

<ul class="mt4 lh-copy">
{% for chapter in site.data.chapters %}
  <li>
<h3 class="mb0 f4">{{ chapter.name }}</h3>
      <p class="mt0"><a href="{{ chapter.url }}">Website</a> | {{ chapter.location.city}}, {{ chapter.location.country}}</p>
      <p><strong>Organizers</strong><br> {% for person in chapter.contact %} {{ person}}<br> {% endfor %}</p>
      <p></p>
    </li>
{% endfor %}
</ul>


Interested in organizing your own local chapter? [Read more](/organizing/chapter)
