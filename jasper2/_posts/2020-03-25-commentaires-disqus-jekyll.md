---
layout: post
current: post
cover: assets/images/cms-265128_1280.jpg
navigation: True
title: Ajouter une section de commentaires à Jekyll avec Disqus
date: 2020-03-25 13:30:00
tags: coulisses
class: post-template
subclass: 'post tag-coulisses'
author: quentin
---

Rien de tel que des commentaires pour ajouter de l'interactivité dans un article.

[Disqus](https://disqus.com/) est un plug-in permettant d'ajouter une section de commentaires sur n'importe quelle page web.
Son implémentation est relativement simple et permet aux lecteurs de donner un feedback sur le contenu qu'ils viennent de lire.

## Création d'un compte
La première étape consiste à [créer un site](https://disqus.com/admin/create/) sur votre compte discus.
Pour l'exemple, nous l'appellerons `esnu`, créant ainsi une URL `esnu.disqus.com`.

## Ajout d'un domaine de confiance
Sur la page d'administration du site chez Disqus, il faut ajouter le domaine du site sur lequel sera intégré le module de commentaires, afin qu'il ne puisse pas être utilisé ailleurs.
Cette configuration se trouve dans `Settings > Advanced > Trusted Domains`.
Toujours dans l'exemple présent, j'ai ajouté `parastuffs.github.io`, racine du site sur lequel est hébergé ce portfolio.

## Configuration de Jekyll
La configuration de Jekyll se fait en deux étapes : l'ajout de variables dans le fichier de configuration général et l'ajout du code permettant d'afficher les commentaires.

### Nouvelles variables
Il faut ajouter les variables suivantes au fichier `_config.yml`

```yaml
disqus: True
disqus_shortname: esnu
```
où `disqus_shortname` est le nom de votre site chez disqus.

### Code de mise en page
Il faut à présent ajouter le code html permettant d'afficher le module en bas de chaque billet.
Pour ce faire, ajoutez les lignes suivantes à l'endroit approprié dans le fichier `_layouts/post.html`.
Dans mon cas, l'endroit en question se trouve entre la fin de la balise `</footer>` et la balise `</article>`.
```html
{% raw %}
{% if site.disqus or page.disqus %}
    <section class="post-full-comments">
        <div id="disqus_thread"></div>
        <script>
            var disqus_config = function () {
                this.page.url = '{{ site.production_url }}{{ page.url }}';
                this.page.identifier = '{{ page.url }}';
            };
            (function() {
                var d = document, s = d.createElement('script');
                s.src = 'https://{{ site.disqus_shortname }}.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
            })();
        </script>
        <noscript>Please enable JavaScript to view the
        <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a>
        </noscript>
    </section>
{% endif %}
{% endraw %}
```
où `site.production_url` devrait être une variable du fichier `_config.yml` qui ressemble à ceci : `production_url:  https://parastuffs.github.io/esnu`.

Les commentaires devraient à présent être activés sur l'instance locale de test ainsi que sur le site de production.