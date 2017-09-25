---
title: Resources
permalink: /resources/
---

Here are some links, blogs, books and other things that I have found to be useful or interesting for myself. Perhaps they may also be useful for you. Many of the things revolve around doing research, deep learning, or both.


## Some other good books
Some books that I strongly recommend to read.  For me, they have contained some valuable and often timeless lessons.
- [How to win friends and influence people](https://www.amazon.com/How-Win-Friends-Influence-People/dp/0671027034/) by Dale Carnegie. There is a reason why this book has a 4.7 rating on Amazon despite the 6700+ reviews. This book contains practicable and timeless advice on how to improve the relationship to the people in your surroundings. The advice is often deceptively simple, but it seems that many people have forgotten or never learned even these simple things.
- [The ego is the enemy](https://www.amazon.com/Ego-Enemy-Ryan-Holiday/dp/1591847818) by Ryan Holiday. In this book, Ryan Holiday brilliantly lays out how our own Ego betrays us and itself by preventing us from getting what Ego wants - success.  
- [If you want to write](https://www.amazon.com/You-Want-Write-Brenda-Ueland/dp/1614271356) by Brenda Ueland. For me, this book unlocked my joy in writing.
- [How to read a book](https://www.amazon.com/How-Read-Book-Intelligent-Touchstone/dp/0671212095) by Mortimer J. Adler. Reading seems to be such an obvious task that many people never consciously question what it actually means to read and how to become more proficient in it. This book taught me a whole lot about how to actually meaningfully read a book. In addition, by learning how to properly read it also increased my writing style.  
- [Presentation Zen](https://www.amazon.com/Presentation-Zen-Simple-Design-Delivery/dp/0321811984) by Garr Reynolds. The core message that got stuck in my head from this book was: "Impress by clarity". That, and countless other tips and considerations on how to improve presentations.

## Fun stuff I follow
- [XKCD](https://xkcd.com/)
- [PhD Comics](http://phdcomics.com/comics.php)
- [Explosm](http://explosm.net/)
- [Lego Grad Student](https://legogradstudent.tumblr.com/)
- [lol my thesis](http://lolmythesis.com/)
- Finally, if you want my respect, try to manage a publication in this [Journal](http://www.universalrejection.org/)


<!--
You can see live demo [here](https://aweekj.github.io/Kiko-plus). This theme is inspired by [Kiko](http://github.com/gfjaru/Kiko) theme.

## Features

- Disqus comment system
- Google analytics
- Pagination support
- Custom tags
- SEO support


## Installation

#### Method 1: new master's repository (The Best)

1. First [fork](https://github.com/AWEEKJ/Kiko-plus/fork) it.
2. Change your forked repository name _Kiko-plus_ to __USERNAME.github.io__ where __USERNAME__ is your github username.
3. Access your new blog via [https://username.github.io](https://username.github.io).
4. [See configuration](#configuration).

#### Method 2: gh-pages in existing repository

1. Create a new branch called _gh-pages_ in the repository where you want to add a template [managing branches](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/).
2. From command line run `git clone https://github.com/AWEEKJ/Kiko-plus.git` - this will clone _Kiko-plus_ template to your computer.
3. Create new branch `git checkout -b gh-pages` where _gh-pages_ will be your branch name.
4. Add remote, which is your repo from the first step, to your new branch `git remote add gh-pages https://github.com/<yourName>/<yourMaster>/gh-pages`. _yourName_ is your account name and _yourMaster_ is your repository.
5. Push new branch to remote `git push gh-pages`.
6. Update `_config.yml` file by changing `baseurl: "<branchName>"` _branchName_ is your branch name where _gh-pages_ resides. See [configuration](#configuration).

#### Method 3: Run it locally

1. Download [zip](https://github.com/AWEEKJ/Kiko-plus/archive/master.zip) or clone it `git clone https://github.com/AWEEKJ/Kiko-plus`.
2. Go inside folder and run `jekyll serve` or `rake preview`. This will build a website which you can access [https://localhost:4000](https://localhost:4000). You need to have [Jekyll](https://jekyllrb.com/docs/installation/) installed to do this.


## Configuration

All configuration is done via `_config.yml` file which you will find in your main repo folder. Change this `<something>` to yours.

### Basic

- Config your blog name.

```yml
name: <blog-name>
```

- These configuration in `author:` is for links to icons in footer. If you want to add more link icons, modify `_includes/footer.html` file.

```yml
author:
  facebook:         your-id
  twitter:          your-id
  github:           your-id
  linkedin:         your-id
  medium:           your-id
  tumblr:           your-id
  email:            your-id@your-email.com
```

- Change copyright year and name in footer.

```yml
copyright:
  year:             2017
  name:             Kiko
```

### Google analytics

- Change this to your Google Analytic ID.

```yml
google-analytics:
  id:               "your-id"
```

### Disqus

- Change this to your Disqus short name.

```yml
disqus:
  id:               "your-id"
```

### URL

- Config your domain.

```yml
url: "https://<your-name>.github.io"
```

- **NOTE** When if running locally, change url to

```yml
url: "https://localhost:4000"
```

- Change this to your branch name where _gh-pages_ resides.
- **NOTE** apply only if you used __Method 2__ for installation.

```yml
baseurl: "/<branch-name>"
```

## Rakefile Usage

```bash
# Create new post
$ rake post title="A Title" [date="2015-08-16"] [tags="[tag1, tag2]"]

# Create new draft post
$ rake draft title="A Title" [date="2015-08-16"] [tags="[tag1, tag2]"]

# Install Jekyll Plugins. Do before running in local.
$ rake geminstall

# Run in Local
$ rake preview
```

## License

This theme is released under MIT License.
-->
